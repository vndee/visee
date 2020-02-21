import pymongo
from common.logger import get_logger
from common.config import AppConf

logger = get_logger(__name__)


class MongoDBWrapper:
    def __init__(self,
                 mongdb_host=AppConf.mongodb_host,
                 mongdb_port=AppConf.mongodb_port,
                 mongodb_user=AppConf.mongodb_user,
                 mongodb_password=AppConf.mongodb_password):
        try:
            self.mongo_instace = pymongo.MongoClient(f'mongodb://{mongodb_user}:{mongodb_password}@{mongdb_host}:{mongdb_port}/')
            self.mongodb = self.mongo_instace[AppConf.mongodb_collection]
            logger.info(f'Connect to MongoDB successful at {mongdb_host}:{mongdb_port}.')
        except Exception as ex:
            logger.exception(ex)
            self.mongo_instace = None
            self.mongodb = None

    def insert(self, collection, doc):
        try:
            inserted = self.mongodb.insert_one(doc)
            logger.info(f'Insert one document to {collection}:{inserted.inserted_ids}')
        except Exception as ex:
            logger.exception(ex)

    def get_by_id(self, collection, id):
        try:
            response = self.mongodb.find({}, {'_id': id})
            return response
        except Exception as ex:
            logger.error(f'Can not find document {id} in MongoDB')
            logger.exception(ex)
            return None