import ssl
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context
from application.crawler.environments import create_environments

configs = create_environments()


class ElasticsearchWrapper:
    def __init__(self):
        self.elastic_instance = Elasticsearch(
            configs.elastic_hosts,
            http_auth=(configs.elastic_user, configs.elastic_password),
            scheme='http',
            port=configs.elastic_port,
            http_compress=True,
            verify_certs=False
        )

    def add(self, index, body):
        response = self.elastic_instance.index(index=index, body=body)
        return response

    def get(self, index, id):
        response = self.elastic_instance.get(index=index, id=id)
        return response

    def search(self, index):
        response = self.elastic_instance.search(index=index, body={'query': {'match_all': {}}})
        return response

    def create_index(self, index):
        try:
            response = self.elastic_instance.indices.create(index=index)
            return response
        except Exception as ex:
            return

 