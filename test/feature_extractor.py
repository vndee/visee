import unittest
from indexer.feature_extractor.extractor import FeatureExtractor


class FeatureExtractorTestCase(unittest.TestCase):
    def test_constructor(self):
        feature_extractor = FeatureExtractor()
        self.assertIsNotNone(feature_extractor)
        self.assertIsInstance(feature_extractor, FeatureExtractor)


if __name__ == '__main__':
    unittest.main()
