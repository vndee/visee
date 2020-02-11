import os
import faiss

from common.logger import get_logger
from common.config import AppConf
from common.dbconnector import RedisConnector
from searchengine.visual.model.extractor import FeatureExtractor

logger = get_logger(logger_name=__name__)


class FaissIndexer:
    def __init__(self):
        self.feature_dim = 1280 if not os.getenv('FAISS_FEATURE_DIM') else int(os.getenv('FAISS_FEATURE_DIM'))

        try:
            self.feature_extractor = FeatureExtractor()
        except Exception as ex:
            logger.error('An error occured while init feature extractor')
            logger.exception(ex)
            self.feature_extractor = None
        finally:
            logger.info('Init feature extractor success')

        try:
            self.faiss_index = faiss.IndexFlatL2(self.feature_dim)
        except Exception as ex:
            logger.error('An error occured while init faiss indexer')
            logger.exception(ex)
        finally:
            logger.info('Init faiss indexer success')

        # try:
        #     self.redis_cursor = RedisConnector(host=AppConf.redis_host,
        #                                        port=AppConf.redis_port,
        #                                        password=AppConf.redis_password,
        #                                        db=AppConf.redis_db_idx)
        # except Exception as ex:
        #     logger.error('An error occured while init redis cursor %d' % AppConf.redis_db_idx)
        #     logger.exception(ex)
        # finally:
        #     logger.info('Init redis cursor success on db %d' % AppConf.redis_db_idx)

    def add(self, value):
        '''
        Add retrieved data from kafka queue to elasticsearch and faisslib indexes.
        data is in json format
        '''

        feature = self.feature_extractor.extract(value)
        self.faiss_index.add(feature)
        return True

    def update(self, key, value):
        '''
        Update record
        '''
        return True

    def search(self, key, k):
        '''
        Search vector
        @param key: vector
        @param k: number of return items
        @return: top k-item with the highest score of similarity
        '''
