import kafka
import json
import redis
import ssl
import os
import re
import requests
import base64
from kafka import TopicPartition, RoundRobinPartitioner
from application.crawler.environments import create_environments
from application.crawler.scraper import BasicWebDriver
from application.helpers import logger
from application.crawler.elastic import ElasticsearchWrapper


config = create_environments()

def get_image_tiki(img_url):
    return re.sub(
        r'/\d+x\d+/',
        '/' + str(config['image_size']) + 'x' + str(config['image_size']) + '/',
        img_url
    )

def create_kafka_producer_connect_with_user(_config, partitions):
    sasl_mechanism = 'PLAIN'
    security_protocol = 'SASL_PLAINTEXT'
    context = ssl.create_default_context()
    context.options &= ssl.OP_NO_TLSv1
    context.options &= ssl.OP_NO_TLSv1_1

    return kafka.KafkaProducer(
        bootstrap_servers=_config.kafka_hosts,
        partitioner=RoundRobinPartitioner(partitions=partitions),
        compression_type='gzip',
        value_serializer=lambda x: json.dumps(
            x, indent=4, sort_keys=True, default=str, ensure_ascii=False
        ).encode('utf-8'),
        sasl_plain_username=_config.kafka_user,
        sasl_plain_password=_config.kafka_password,
        security_protocol=security_protocol,
        ssl_context=context,
        sasl_mechanism=sasl_mechanism
    )

def create_kafka_producer_connect(_config):
    partitions = [
        TopicPartition(topic=_config.kafka_index_topic, partition=i) for i in range(0, _config.kafka_num_partitions)
    ]

    return kafka.KafkaProducer(
        bootstrap_servers=_config.kafka_hosts,
        partitioner=RoundRobinPartitioner(partitions=partitions),
        value_serializer=lambda x: json.dumps(
            x, indent=4, sort_keys=True, default=str, ensure_ascii=False
        ).encode('utf-8'),
        compression_type='gzip'
    ) if _config.kafka_user is None else create_kafka_producer_connect_with_user(_config, partitions)


class ItemWebDriver(BasicWebDriver):
    def __init__(self, _config, timeout=15, wait=15):
        self.config = _config
        BasicWebDriver.__init__(
            self,
            executable_path=os.path.join(self.config.driver_path),
            timeout=timeout,
            wait=wait
        )

        self.elastic_cursor = ElasticsearchWrapper()
        self.redis_connection = self.create_redis_connection()
        self.redis_image_caching = redis.StrictRedis(
            host=self.config.redis_host,
            port=self.config.redis_port,
            db=self.config.redis_cache_db,
            password=self.config.redis_password
        )

        self.kafka_link_consumer = self.create_kafka_consummer()
        self.kafka_index_producer = create_kafka_producer_connect(config)
        self.rules = json.loads(self.redis_connection.get('pages_rule'))

    def update_rule(self):
        self.rules = json.loads(self.redis_connection.get('pages_rule'))

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
            dict_item['id'] = int(self.redis_connection.get('obj_current_id'))
            self.redis_connection.set('obj_current_id', int(dict_item['id']) + 1)
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
            response = self.elastic_cursor.add(index=config.elastic_index, body=item_scraped)
            self.kafka_index_producer.send(config.kafka_index_topic, {'item_id': response['_id']})
            self.redis_image_caching.set(response['_id'], item_scraped['images'])


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
