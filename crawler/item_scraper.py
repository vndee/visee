import kafka
import json
import redis
import os
import re
import requests
import base64
from application.crawler.environments import create_environments
from application.crawler.scraper import BasicWebDriver
from application.helpers import logger

config = create_environments()


def get_image_tiki(img_url):
    return re.sub(
        r'/\d+x\d+/',
        '/' + str(config['image_size']) + 'x' + str(config['image_size']) + '/',
        img_url
    )


class ItemWebDriver(BasicWebDriver):
    def __init__(self, _config, timeout=15, wait=15):
        self.config = _config
        BasicWebDriver.__init__(
            self,
            executable_path=os.path.join(self.config.driver_path),
            timeout=timeout,
            wait=wait
        )
        self.redis_connecttion = self.create_redis_connection()
        self.kafka_link_consumer = self.create_kafka_consummer()
        self.rules = json.loads(self.redis_connecttion.get('pages_rule'))

    def update_rule(self):
        self.rules = json.loads(self.redis_connecttion.get('pages_rule'))

    def create_kafka_consummer(self):
        return kafka.KafkaConsumer(
            self.config.kafka_link_topic,
            bootstrap_servers=self.config.kafka_hosts,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            group_id=self.config.kafka_consumer_group
        )

    def create_redis_connection(self):
        return redis.StrictRedis(
            host=self.config.redis_host,
            port=self.config.redis_port,
            db=self.config.redis_db,
            password=self.config.redis_password
        )

    def scrap_link(self, _domain, _link):
        logger.info_log.info("Processing {}".format(_link))
        self.get_html(_link)

        dict_item = {
            'domain': _domain,
            'link': _link
        }

        ignore_key = ['domain', 'image_holder']
        for key in self.rules[_domain]:
            if key in ignore_key:
                continue
            try:
                if key == 'rating_point':
                    if _domain == 'tiki.vn':
                        dict_item[key] = re.findall(
                            r'\d+',
                            self.driver.find_element_by_css_selector(
                                self.rules[_domain][key]
                            ).get_attribute('style')
                        )[0]

                    else:
                        dict_item[key] = self.driver.find_element_by_css_selector(self.rules[_domain][key]).text
                else:
                    dict_item[key] = self.driver.find_element_by_css_selector(self.rules[_domain][key]).text

            except Exception as exception:
                logger.error_log.error((str(exception)))
                dict_item[key] = None

        if config['download_images']:
            image_holder = self.driver.find_element_by_css_selector(self.rules[_domain]['image_holder'])
            dict_item['images'] = list()
            dict_item['id'] = int(self.redis_connecttion.get('obj_current_id'))
            self.redis_connecttion.set('obj_current_id', int(dict_item['id']) + 1)
            for img_tag in image_holder.find_elements_by_tag_name('img'):

                if _domain == 'tiki.vn':
                    image_url = get_image_tiki(img_tag.get_attribute('src'))
                else:
                    image_url = img_tag.get_attribute('src')

                img_base64 = base64.b64encode(requests.get(image_url).content)
                dict_item['images'].append({
                    'base64_data': img_base64,
                    'img_link': image_url
                })

        return dict_item

    def run_scrap(self):
        for msg in self.kafka_link_consumer:
            item_scraped = self.scrap_link(msg.value['domain'], msg.value['link'])
            print(item_scraped)
            # push item_scraped to elastic search


if __name__ == "__main__":

    # time.sleep(60)
    # item_producer = kafka.KafkaProducer(
    #     bootstrap_servers=config.kafka_hosts,
    #     value_serializer=lambda x: json.dumps(
    #         x, indent=4, sort_keys=True, default=str, ensure_ascii=False
    #     ).encode('utf-8')
    # )

    # create webdriver
    scraper = ItemWebDriver(config)
    scraper.run_scrap()
