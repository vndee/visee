import os
import faiss

from searchengine.visual.model.extractor import FeatureExtractor


class FaissIndexer:
    def __init__(self):
        self.feature_dim = 128 if not os.getenv('FAISS_FEATURE_DIM') else int(os.getenv('FAISS_FEATURE_DIM'))
        self.feature_extractor = FeatureExtractor()
        self.faiss_index = faiss.IndexFlatL2(self.feature_dim)

    def add(self, key, value):
        '''
        Add retrieved data from kafka queue to elasticsearch and faisslib indexes.
        data is in json format
        '''
        feature = self.feature_extractor.extract(value)
        
        return True

    def update(self, key, value):
        '''
        Update record
        '''
        return True
