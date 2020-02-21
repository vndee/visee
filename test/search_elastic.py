from pprint import pprint
from common.elastic import ElasticsearchWrapper


if __name__ == '__main__':
    elastic = ElasticsearchWrapper()
    query = {
        'query': {
            'query_string': {
                'query': 'bot cam',
                # 'fuzziness': 4
            }
        }
    }
    response = elastic.search('test', query)
    print(response)
    pprint(response['hits']['hits'][0])