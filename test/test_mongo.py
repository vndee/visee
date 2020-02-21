import unittest
from common.mongo import MongoDBWrapper


class MongoDBTestCase(unittest.TestCase):
    def test_constructor(self):
        mongo = MongoDBWrapper()
        self.assertIsNotNone(mongo)


if __name__ == '__main__':
    unittest.main()