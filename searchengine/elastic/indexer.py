from datetime import datetime
from elasticsearch import Elasticsearch


class ElasticIndexer:
    def __init__(self):
        self.elastic = Elasticsearch()

    def add(self, data):
        '''
        Add retrieved data from kafka queue to elasticsearch and faisslib indexes.
        data is in json format
        '''
        return True

    def update(self, key, value):
        '''
        Update record
        '''
        return True
