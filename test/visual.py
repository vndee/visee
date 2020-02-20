import unittest
from indexer.mwrapper import FaissIndexer


class VisualTestCase(unittest.TestCase):
    def test_constructor(self):
        faiss = FaissIndexer()
        self.assertIsNotNone(faiss)


if __name__ == '__main__':
    unittest.main()
