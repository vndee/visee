from pprint import pprint
from common.elastic import ElasticsearchWrapper


if __name__ == '__main__':
    elastic = ElasticsearchWrapper()
    query = {
        'query': {
            'query_string': {
                'query': 'Bot cam',
            },
        }
    }

    response = elastic.search(index='test', body=query)
    print(response)