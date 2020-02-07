from common.logger import get_logger
from redis import StrictRedis

logger = get_logger(__name__)


class RedisConnector:
    def __init__(self, host='localhost', port=6379, password='', db=0):
        self.cursor = None
        self.host = host
        self.port = port
        self.password = password
        self.db = db

        try:
            self.cursor = StrictRedis(host=self.host, port=self.port, password=self.password, db=self.db)
        except Exception as ex:
            logger.error('Create redis connection failed on db_index: %d' % (db))
            logger.exception(ex)
        finally:
            logger.info('Create redis connection on db_index: %d' % (db))

    def get(self, key):
        try:
            self.cursor.get(key)
        except Exception as ex:
            logger.error('An error occured while getting data from redis db: %d' % (self.db))
            logger.exception(ex)
        finally:
            return True

    def set(self, key, value):
        try:
            self.cursor.set(key, value)
        except Exception as ex:
            logger.error('An error occured while adding data to redis db: %d' % (self.db))
            logger.exception(ex)
            return False
        finally:
            return True
