from elasticsearch import Elasticsearch
from common.config import AppConf


class ElasticsearchWrapper:
    def __init__(self):
        self.elastic_instance = Elasticsearch(
            AppConf.elastic_hosts,
            http_auth=(AppConf.elastic_user, AppConf.elastic_password),
            scheme='http',
            port=AppConf.elastic_port,
            http_compress=True,
            verify_certs=False
        )

    def add(self, index, body):
        response = self.elastic_instance.index(index=index, body=body)
        return response

    def get(self, index, id):
        response = self.elastic_instance.get(index=index, id=id)
        return response

    def search(self, index, body):
        response = self.elastic_instance.search(index=index, body=body)
        return response

    def delete(self, index, id):
        response = self.elastic_instance.delete(index=index, id=id)
        return response

    def delete_index(self, index):
        response = self.elastic_instance.delete(index=index, ignore=[404, 404])
        return response

    def create_index(self, index):
        try:
            response = self.elastic_instance.indices.create(index=index)
            return response
        except:
            return
