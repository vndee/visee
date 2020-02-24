import json
import unittest
from glob import glob
from common.elastic import ElasticsearchWrapper


class ElasticsearchTestCase(unittest.TestCase):
    def test_constructor(self):
        elastic = ElasticsearchWrapper()
        self.assertIsNotNone(elastic)

    # def test_add_method(self):
    #     elastic = ElasticsearchWrapper()
    #     json_file = glob('data/json/*.json')
    #     for fi in json_file:
    #         data = json.loads(json_file)


if __name__ == '__main__':
    unittest.main()
