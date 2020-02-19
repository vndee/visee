import redis
import kafka
import time
import json
import ssl
import os
from kafka import RoundRobinPartitioner, TopicPartition
from common.config import AppConf
from common.logger import get_logger
from crawler.application.scraper import BasicWebDriver

logger = get_logger(__name__)


class ItemLinkWebDriver(BasicWebDriver):
    def __init__(self, executable_path=None, timeout=15, wait=15):
        BasicWebDriver.__init__(
            self, executable_path=executable_path, timeout=timeout, wait=wait
        )


def create_redis_connection(_config):
    return redis.StrictRedis(
        host=_config.redis_host,
        port=_config.redis_port,
        db=_config.redis_link2scrape_db,
        password=_config.redis_password
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
        TopicPartition(topic=_config.kafka_link_topic, partition=i) for i in range(0, _config.kafka_num_partitions)
    ]

    return kafka.KafkaProducer(
        bootstrap_servers=_config.kafka_hosts,
        partitioner=RoundRobinPartitioner(partitions=partitions),
        value_serializer=lambda x: json.dumps(
            x, indent=4, sort_keys=True, default=str, ensure_ascii=False
        ).encode('utf-8'),
        compression_type='gzip'
    ) if _config.kafka_user is None else create_kafka_producer_connect_with_user(_config, partitions)


def scrape_links(_config):
    redis_connect = create_redis_connection(_config)
    links_producer = create_kafka_producer_connect(_config)
    while True:
        logger.info("Start/Restart get item's links")
        web_driver = ItemLinkWebDriver(
            executable_path=os.path.join(os.getcwd(), _config.chromedriver_path)
        )
        rules = json.loads(redis_connect.get("homepages"))
        for domain in rules:
            logger.info("Processing {}".format(domain))
            if domain in []:
                continue

            for category in rules[domain]['categories']:
                web_driver.get_html(rules[domain]['categories'][category])

                if rules[domain]['newest_script'] is not None:
                    time.sleep(3)
                    web_driver.execute_script(rules[domain]['newest_script'])

                link_counter = 0
                while True:
                    try:
                        time.sleep(1)
                        all_items = web_driver.driver.find_elements_by_class_name(rules[domain]['item_class'])
                        time.sleep(2)
                        for item in all_items:
                            web_driver.driver.execute_script("arguments[0].scrollIntoView();", item)
                            try:
                                link_counter += 1
                                if rules[domain]['css_query_link'] is not None:
                                    item_link = item.find_element_by_css_selector(rules[domain]['css_query_link'])
                                    item_link = item_link.get_attribute('href')
                                else:
                                    item_link = item.get_attribute('href')
                                payload = {
                                    'link': item_link,
                                    'domain': domain,
                                }
                                links_producer.send(_config.kafka_link_topic, payload)
                            except Exception as ex:
                                logger.exception(ex)
                                continue

                        logger.info("Pushed {} link(s) from {} to kafka".format(all_items.__len__(), domain))
                        time.sleep(1)
                        web_driver.execute_script(rules[domain]['next_page_script'])
                    except Exception as exception:
                        time.sleep(3)
                        logger.error((str(exception)))


if __name__ == '__main__':
    try:
        scrape_links(AppConf)
    except Exception as ex:
        logger.error("Some thing went wrong. Application will stop after 1200 seconds")
        logger.exception(str(ex))
        time.sleep(1)
