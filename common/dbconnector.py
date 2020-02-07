from logger import app_logging
from common.config import AppConf
from redis import StrictRedis


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
            app_logging.error('Create redis connection failed on db_index: %d' % (db))
            app_logging.exception(ex)
        finally:
            app_logging.error('Create redis connection on db_index: %d' % (db))

    def get(self, key):
        try:
            self.cursor.get(key)
        except Exception as ex:
            app_logging.error('An error occured while getting data from redis db: %d' % (self.db))
            app_logging.exception(ex)
        finally:
            return True

    def set(self, key, value):
        try:
            self.cursor.set(key, value)
        except Exception as ex:
            app_logging.error('An error occured while adding data to redis db: %d' % (self.db))
            app_logging.exception(ex)
            return False
        finally:
            return True
