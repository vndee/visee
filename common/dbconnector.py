from common.logger import get_logger
from redis import StrictRedis
from common.config import AppConf

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


class DualRedisConnector:
    def __init__(self):
        self.host = AppConf.redis_host
        self.port = AppConf.redis_port
        self.password = AppConf.redis_password
        self.first_db = AppConf.redis_db_idx_first
        self.second_db = AppConf.redis_db_idx_second
        self.first_cursor = StrictRedis(host=self.host, port=self.port, db=self.first_db, password=self.password)
        self.second_cursor = StrictRedis(host=self.host, port=self.port, db=self.second_db, password=self.password)

    def set(self, first, second):
        try:
            self.first_cursor.set(first, second)
            self.second_cursor.set(second, first)
        except Exception as ex:
            return False
        return True

    def get_by_id(self, id):
        try:
            return self.first_cursor.get(id)
        except Exception as ex:
            return None

    def get_by_pos(self, pos):
        try:
            return self.second_cursor.get(pos)
        except Exception as ex:
            return None

