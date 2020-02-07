import os
import faiss


class FaissIndexer:
    def __init__(self):
        self.feature_dim = 128 if not os.getenv('FAISS_FEATURE_DIM') else int(os.getenv('FAISS_FEATURE_DIM'))
        self.faiss_index = faiss.IndexFlatL2(self.feature_dim)

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
