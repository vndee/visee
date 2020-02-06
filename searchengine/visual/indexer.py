import faiss


class Indexer:
    def __init__(self):
        self.kafka_consumer = None
        self.redis_connector = None

    def add(self, data):
        '''
        Add retrieved data from kafka queue to elasticsearch and faiss indexes.
        data is in json format
        '''
        return True

    def update(self, key, value):
        '''
        Update record
        '''
        return True


class ElasticIndexer(Indexer):
    def __init__(self):
        super().__init__()
        self.elastic_connector = None

    def add(self, data):
        '''
        Add data to elasticsearch engine
        '''
        return True

    def update(self, key, value):
        '''
        Update elasticsearch indexes
        '''
        return True


class FaissIndexer(Indexer):
    def __init__(self):
        super().__init__()
        self.faiss_connector = None

    def add(self, data):
        '''
        Add data to faiss index
        '''
        return True

    def update(self, key, value):
        '''
        Update faiss index
        '''
        return True