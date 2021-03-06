import os
import sys
import milvus
from common.logger import get_logger
from common.config import AppConf
from indexer.feature_extractor.extractor import FeatureExtractor

logger = get_logger(logger_name=__name__)


class MilvusWrapper:
    def __init__(self):
        self.feature_dim = 2560 if not os.getenv('FEATURE_DIM') else int(os.getenv('FEATURE_DIM'))
        self.milvus_host = AppConf.milvus_host
        self.milvus_port = AppConf.milvus_port

        try:
            self.feature_extractor = FeatureExtractor()
        except Exception as ex:
            logger.error('An error occurred while init feature extractor')
            logger.exception(ex)
            self.feature_extractor = None
        finally:
            logger.info('Init feature extractor success')

        try:
            self.milvus_instace = milvus.Milvus()
            self.milvus_instace.connect(host=self.milvus_host, port=self.milvus_port)
            logger.info('Init milvus instance success')

        except Exception as ex:
            logger.error("An error occurred while init milvus instance")
            logger.exception(ex)
            self.milvus_instace = None

        self.create_table()
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

    def create_table(self):
        try:
            param = {'table_name': AppConf.milvus_table_name, 'dimension': self.feature_dim,
                     'index_file_size': 1024, 'metric_type': milvus.MetricType.L2}
            response = self.milvus_instace.create_table(param)
            logger.info(response.message)
        except Exception as ex:
            logger.error(f'Can not create table {AppConf.milvus_table_name}')
            logger.exception(ex)

    def add(self, value, id):
        '''
        Add retrieved data from kafka queue to elasticsearch and milvus indexes.
        data is in json format
        '''

        feature = self.feature_extractor.extract(value)
        try:
            self.milvus_instace.add_vectors(table_name=AppConf.milvus_table_name, records=[feature.tolist()], ids=[id])
            return True
        except Exception as ex:
            logger.exception(ex)
            try:
                _, _, lineno = sys.exc_info()
                logger.error('Line error: {} - Error: {}'.format(lineno.tb_lineno, ex))
            except:
                logger.error('Cannot get line error - Error{}'.format(ex))

            return False

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
        feauture = self.feature_extractor.extract(key)
        status, results = self.milvus_instace.search_vectors(table_name=AppConf.milvus_table_name, query_records=[feauture.tolist()], top_k=k, nprobe=16)

        if status.code != 0:
            logger.error('Error when query vector')
            print(status)
            print(results)
            return []
        else:
            return results
