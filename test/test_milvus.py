import unittest
from searchengine.visual.indexer import MilvusIndexer


class MilvusTestCase(unittest.TestCase):
    def test_constructor(self):
        self.milvus = MilvusIndexer()
        self.assertIsNotNone(self.milvus)


if __name__ == '__main__':
    unittest.main()
