import kafka
import json
import redis
import ssl
import os
import re
import requests
import base64
from kafka import RoundRobinPartitioner
from common.logger import get_logger
from common.config import AppConf
from crawler.application.scraper import BasicWebDriver
from common.elastic import ElasticsearchWrapper
from indexer.mwrapper import MilvusWrapper
from common.metadat import parse_meta_data
from common.mongo import MongoDBWrapper

logger = get_logger('Product Scraper')


def get_image_tiki(img_url):
    return re.sub(
        r'/\d+x\d+/',
        '/' + str(AppConf.image_size) + 'x' + str(AppConf.image_size) + '/',
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
        kafka.TopicPartition(topic=_config.kafka_index_topic, partition=i)
        for i in
        range(0, _config.kafka_num_partitions)
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
            executable_path=os.path.join(os.getcwd(), self.config.chromedriver_path),
            timeout=timeout,
            wait=wait
        )

        self.elastic_cursor = ElasticsearchWrapper()
        self.mongo_cursor = MongoDBWrapper()
        self.redis_connection = self.create_redis_connection()
        self.kafka_link_consumer = self.create_kafka_consummer()
        self.milvus_indexer = MilvusWrapper()
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
            db=self.config.redis_link2scrape_db,
            password=self.config.redis_password
        )

    def scrap_link(self, _domain, _link):
        logger.info("Processing {}".format(_link))
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
                logger.error((str(exception)))
                dict_item[key] = None

        if AppConf.download_image:
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
        logger.info('Waiting for links.')
        for msg in self.kafka_link_consumer:
            try:
                item_scraped = self.scrap_link(msg.value['domain'], msg.value['link'])
                meta_data = parse_meta_data(item_scraped)

                response = self.elastic_cursor.add(index=AppConf.elastic_index, body=meta_data)
                item_scraped['_id'] = response['_id']

                self.mongo_cursor.insert(collection=AppConf.mongodb_collection, doc=item_scraped)

                for image in item_scraped['images']:
                    self.milvus_indexer.add(image, response['_id'])

                logger.info('Index {} completely.'.format(response['_id']))
            except Exception as ex:
                logger.exception(ex)


if __name__ == "__main__":
    # create webdriver
    scraper = ItemWebDriver(AppConf)
    scraper.run_scrap()
