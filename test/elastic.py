import unittest
from indexer.elastic.indexer import ElasticIndexer
from indexer.elastic.seeker import ElasticSeeker


class ElasticsearchTestCase(unittest.TestCase):
    def test_constructor(self):
        elastic_index = ElasticIndexer()
        elastic_seeker = ElasticSeeker()
        self.assertIsNotNone(elastic_index)
        self.assertIsNotNone(elastic_seeker)


if __name__ == '__main__':
    unittest.main()
