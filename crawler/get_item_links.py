import redis
import kafka
import time
import json
import ssl
import os
from common.config import AppConf
from common.logger import get_logger
from crawler.application.scraper import BasicWebDriver

logger = get_logger('Link Scraper')


class GetLink:
    class ItemLinkWebDriver(BasicWebDriver):
        def __init__(self, executable_path=None, timeout=15, wait=15):
            BasicWebDriver.__init__(
                self, executable_path=executable_path, timeout=timeout, wait=wait
            )

    def __init__(self, _config):
        self.config = _config
        self.rules = list()
        self.web_driver = dict()
        self.visited = dict()
        self.redis_connection = self.create_redis_connection()
        self.links_producer = self.create_kafka_producer_connect()

    def create_redis_connection(self):
        return redis.StrictRedis(
            host=self.config.redis_host,
            port=self.config.redis_port,
            db=self.config.redis_categories_db,
            password=self.config.redis_password
        )

    def create_kafka_producer_connect_with_user(self):
        sasl_mechanism = 'PLAIN'
        security_protocol = 'SASL_PLAINTEXT'
        context = ssl.create_default_context()
        context.options &= ssl.OP_NO_TLSv1
        context.options &= ssl.OP_NO_TLSv1_1

        return kafka.KafkaProducer(
            bootstrap_servers=self.config.kafka_hosts,
            compression_type='gzip',
            value_serializer=lambda x: json.dumps(
                x, indent=4, sort_keys=True, default=str, ensure_ascii=False
            ).encode('utf-8'),
            sasl_plain_username=self.config.kafka_user,
            sasl_plain_password=self.config.kafka_password,
            security_protocol=security_protocol,
            ssl_context=context,
            sasl_mechanism=sasl_mechanism
        )

    def create_kafka_producer_connect(self):
        return kafka.KafkaProducer(
            bootstrap_servers=self.config.kafka_hosts,
            value_serializer=lambda x: json.dumps(
                x, indent=4, sort_keys=True, default=str, ensure_ascii=False
            ).encode('utf-8'),
            compression_type='gzip'
        ) if self.config.kafka_user is None else self.create_kafka_producer_connect_with_user()

    def run(self):
        print(self.redis_connection.get("list_domain"))
        list_domain = json.loads(self.redis_connection.get("list_domain"))
        print(list_domain)
        while True:
            logger.info("Start/Restart get item's links")

            self.rules = json.loads(self.redis_connection.get("homepages"))

            for domain in list_domain:
                logger.info("Processing {}".format(domain))
                self.web_driver[domain] = self.ItemLinkWebDriver(
                    executable_path=os.path.join(
                        self.config.chromedriver_path
                    )
                )
                if domain in []:
                    continue
                if domain not in self.visited:
                    self.visited[domain] = list()
                for category in self.rules[domain]['categories']:
                    if category not in self.visited[domain]:
                        self.web_driver[domain].get_html(self.rules[domain]['categories'][category])
                        self.visited[domain].append(category)
                    else:
                        continue

                    if self.rules[domain]['newest_script'] is not None:
                        time.sleep(3)
                        self.web_driver[domain].execute_script(self.rules[domain]['newest_script'])

                    link_counter, loop_counter = 0, 0
                    while True:
                        try:
                            if link_counter > 10:
                                continue
                            time.sleep(1)
                            all_items = self.web_driver[domain].driver.find_elements_by_class_name(
                                self.rules[domain]['item_class']
                            )
                            time.sleep(2)
                            for item in all_items:
                                self.web_driver[domain].driver.execute_script("arguments[0].scrollIntoView();", item)
                                try:
                                    link_counter += 1
                                    if self.rules[domain]['css_query_link'] is not None:
                                        item_link = item.find_element_by_css_selector(
                                            self.rules[domain]['css_query_link']
                                        )
                                        item_link = item_link.get_attribute('href')
                                    else:
                                        item_link = item.get_attribute('href')
                                    payload = {
                                        'link': item_link,
                                        'domain': domain,
                                    }
                                    self.links_producer.send(self.config.kafka_link_topic, payload)
                                except:
                                    continue

                            logger.info(
                                "Pushed {} link(s) from {} to kafka".format(all_items.__len__(), domain)
                            )
                            time.sleep(1)
                            self.web_driver[domain].execute_script(self.rules[domain]['next_page_script'])
                            link_counter += 1
                        except Exception as exception:
                            time.sleep(3)
                            logger.error((str(exception)))


if __name__ == '__main__':
    try:
        getlink = GetLink(AppConf)
        getlink.run()
    except Exception as ex:
        logger.error("Some thing went wrong. Application will stop after 1200 seconds")
        logger.exception(str(ex))
        time.sleep(1)
