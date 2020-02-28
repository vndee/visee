import redis
from common.config import AppConf
from crawler.application.utils import download_chrome_driver
from common.logger import get_logger
from kafka.errors import TopicAlreadyExistsError
from kafka.admin import KafkaAdminClient, NewTopic

config = AppConf
logger = get_logger('Check system')


def create_kafka_topic(_config):
    if _config.kafka_user is None or _config.kafka_user == '':
        logger.info("Create kafka topic without sasl")
        admin_client = KafkaAdminClient(
            bootstrap_servers=_config.kafka_hosts,
            client_id=_config.kafka_user
        )
    else:
        logger.info("Create kafka topic with sasl")
        admin_client = KafkaAdminClient(
            bootstrap_servers=_config.kafka_hosts,
            client_id=_config.kafka_user,
            sasl_mechanism='PLAIN',
            sasl_plain_username=_config.kafka_user,
            sasl_plain_password=_config.kafka_password
        )

    topic_list = {
        _config.kafka_link_topic: NewTopic(
            name=_config.kafka_link_topic,
            num_partitions=_config.kafka_num_partitions,
            replication_factor=1
        ),
        _config.kafka_object_topic: NewTopic(
            name=_config.kafka_object_topic,
            num_partitions=_config.kafka_num_partitions,
            replication_factor=1
        )
    }

    for topic in topic_list:
        try:
            logger.info('Creating topic: {}'.format(topic))
            admin_client.create_topics(new_topics=[topic_list[topic]], validate_only=False)
        except TopicAlreadyExistsError:
            logger.error('Topic {} is exist --- skip'.format(topic))
            continue

    logger.info('FINISH\n')
    admin_client.close()


def check_redis(_config):
    logger.info('Check redis connection')
    redis_connect = redis.StrictRedis(
        host=_config.redis_host,
        port=_config.redis_port,
        db=_config.redis_db,
        password=_config.redis_password
    )
    try:
        response = redis_connect.client_list()
        logger.info('Redis is ready')
    except redis.exceptions.ConnectionError:
        logger.info('Redis is not available')
    logger.info('FINISH\n')


if __name__ == '__main__':
    check_redis(config)
    create_kafka_topic(config)
    download_chrome_driver()
