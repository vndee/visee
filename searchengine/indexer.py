import faiss

from searchengine.elastic.indexer import ElasticIndexer
from searchengine.elastic.seeker import ElasticSeeker
from searchengine.visual.indexer import FaissIndexer
from searchengine.visual.seeker import FaissSeeker


class Indexer:
    def __init__(self):
        self.kafka_consumer = None
        self.redis_connector = None

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
