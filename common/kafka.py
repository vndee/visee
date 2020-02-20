import ssl
import kafka
import json
from kafka import RoundRobinPartitioner, TopicPartition
from common.logger import get_logger

logger = get_logger(logger_name=__name__)


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
