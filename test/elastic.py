import unittest
from searchengine.elastic.indexer import ElasticIndexer
from searchengine.elastic.seeker import ElasticSeeker


class ElasticsearchTestCase(unittest.TestCase):
    def test_constructor(self):
        elastic_index = ElasticIndexer()
        elastic_seeker = ElasticSeeker()
        self.assertIsNotNone(elastic_index)
        self.assertIsNotNone(elastic_seeker)


if __name__ == '__main__':
    unittest.main()
