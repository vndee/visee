import unittest
from indexer.mwrapper import MilvusWrapper


class MilvusTestCase(unittest.TestCase):
    def test_constructor(self):
        self.milvus = MilvusWrapper()
        self.assertIsNotNone(self.milvus)


if __name__ == '__main__':
    unittest.main()
