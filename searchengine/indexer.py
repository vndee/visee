import ssl
import json
import redis
import kafka
import faiss

from searchengine.elastic.indexer import ElasticIndexer
from searchengine.elastic.seeker import ElasticSeeker
from searchengine.visual.indexer import FaissIndexer
from searchengine.visual.seeker import FaissSeeker
from common.dbconnector import DualRedisConnector
from common.config import AppConf


class Indexer:
    def __init__(self):
        self.kafka_index_consumer = kafka.KafkaConsumer(
            AppConf.kafka_index_topic,
            boostrap_servers=AppConf.kafka_hosts,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            group_id=AppConf.kafka_cosumer_group
        )

        self.redis_cache_connector = redis.StrictRedis(
            host=AppConf.redis_host,
            port=AppConf.redis_port,
            db=AppConf.redis_db_cache,
            password=AppConf.redis_password
        )

        self.dual_redis_connector = DualRedisConnector()
        self.faiss_index = FaissIndexer()

    def execute(self):
        for message in self.kafka_index_consumer:
            item_id = message['item_id']
            images = self.redis_cache_connector.get(item_id)
            for image in images:
                pos = self.faiss_index.add(value=image['base64_data'])
                self.dual_redis_connector.set(item_id, pos)

    def add(self, data):
        '''
        Add retrieved data from kafka queue to elasticsearch and faisslib indexes.
        data is in json format
        '''

        # retrieve product id from kafka queue

        # retrieve product meta data from redis caching db

        # add meta-data to elasticsearch

        # 
        return True

    def update(self, key, value):
        '''
        Update record
        '''
        return True
