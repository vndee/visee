import unittest
import datetime
from application.crawler.elastic import ElasticsearchWrapper


class ElasticTestCase(unittest.TestCase):
    def test_contructor(self):
        self.es = ElasticsearchWrapper()
        self.assertIsNotNone(self.es)

    def test_create_index(self):
        self.es = ElasticsearchWrapper()
        self.es.create_index('test_index')

    def test_index(self):
        doc = {
            'author': 'Duy Huynh',
            'text': 'Lorem ipsum dolor sit amet',
            'timestamp': datetime.datetime.now(),
        }
        self.es = ElasticsearchWrapper()
        self.assertIsInstance(self.es, ElasticsearchWrapper)
        self.assertIsNotNone(self.es.add(index='test_index', body=doc))

    def test_get(self):
        self.es = ElasticsearchWrapper()
        self.assertIsNotNone(self.es.get('test_index', id='04rqMnABT2Z0L2Ghnhml'))

    def test_search(self):
        self.es = ElasticsearchWrapper()
        self.es.search(index='test_index')

if __name__ == '__main__':
    unittest.main()
