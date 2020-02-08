import kafka
import json
import redis
import os
import re
import requests
import base64
from pymongo import MongoClient
from crawler.application.crawler.environments import create_environments
from crawler.application.crawler.scraper import BasicWebDriver
from crawler.application.helpers import logger
config = create_environments()


def get_image_tiki(img_url):
    return re.sub(
        r'/\d+x\d+/',
        '/' + str(config['image_size']) + 'x' + str(config['image_size']) + '/',
        img_url
    )


class ItemWebDriver(BasicWebDriver):
    def __init__(self, redis_connecttion, kafka_link_consumer, kafka_object_producer,
                 executable_path=None, timeout=15, wait=15):
        BasicWebDriver.__init__(
            self, executable_path=executable_path, timeout=timeout, wait=wait
        )
        # self.client_mongo_db = MongoClient(
        #     config.mongo_host,
        #     config.mongo_port,
        #     username=config.mongo_user,
        #     password=config.mongo_password
        # )
        # self.item_db = self.client_mongo_db[config.mongo_db]
        # self.item_db.add_user('hoang', '4983', roles=[{'role': 'readWrite', 'db': 'testdb'}])

        self.redis_connecttion = redis_connecttion
        self.kafka_link_consumer = kafka_link_consumer
        self.kafka_object_producer = kafka_object_producer
        self.rules = json.loads(redis_connecttion.get('pages_rule'))

    def update_rule(self):
        self.rules = json.loads(self.redis_connecttion.get('pages_rule'))

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
        count_file = 0
        for msg in self.kafka_link_consumer:
            item_scraped = self.scrap_link(msg.value['domain'], msg.value['link'])

            # self.item_db.reviews.insert_one(item_scraped)
            count_file += 1


if __name__ == "__main__":
    # time.sleep(60)

    # connect kafka and create consumers
    # link consumer
    link_consumer = kafka.KafkaConsumer(
        config.kafka_link_topic,
        bootstrap_servers=config.kafka_hosts,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        group_id=config.kafka_consumer_group
    )
    # link_consumer.subscribe([config.kafka_link_topic])
    # and object producer for another process
    item_producer = kafka.KafkaProducer(
        bootstrap_servers=config.kafka_hosts,
        value_serializer=lambda x: json.dumps(
            x, indent=4, sort_keys=True, default=str, ensure_ascii=False
        ).encode('utf-8')
    )
    # connect redis
    # load rule from path
    redis_connect = redis.StrictRedis(
        host=config.redis_host,
        port=config.redis_port,
        db=config.redis_db,
        password=config.redis_password
    )

    # create webdriver
    scraper = ItemWebDriver(
        redis_connecttion=redis_connect,
        kafka_link_consumer=link_consumer,
        kafka_object_producer=item_producer,
        executable_path=os.getcwd() + config.driver_path,
    )
    scraper.run_scrap()
