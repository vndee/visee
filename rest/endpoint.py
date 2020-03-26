from flask import Flask, request, jsonify
from common.config import AppConf
from common.elastic import ElasticsearchWrapper
from common.dbconnector import DualRedisConnector
from indexer.mwrapper import MilvusWrapper
from common.logger import get_logger


app = Flask('ViSee - Visual Search Engine RESTful API Server')
logger = get_logger('REST Server')
elastic_cursor = ElasticsearchWrapper()
milvus_cursor = MilvusWrapper()
dual_redis_cursor = DualRedisConnector()


@app.route('/api/rest/verify/', methods=['GET'])
def verify():
    headers = request.headers
    auth = headers.get('api_key')
    if auth == AppConf.api_key:
        return jsonify(message='OK: Authorized'), 200
    else:
        return jsonify(message='ERROR: Unauthorized'), 401


@app.route('/api/rest/search/', methods=['POST'])
def search():
    """
    response: top k=10 document with meta-data.
    """
    try:
        headers = request.headers
        auth = headers.get('api_key')

        if auth != AppConf.api_key:
            return jsonify(message='ERROR: Unauthorized'), 401

        if 'engine' not in request.json or 'query' not in request.json:
            return jsonify(message='ERROR: Request format is invalid.'), 200

        if request.json['engine'] == AppConf.api_text_mode:
            query = {
                'query': {
                    'query_string': {
                        'query': request.json['query'],
                    }
                }
            }

            response = elastic_cursor.search(index='visee', body=query)
            print(response)
            if 'hits' not in response['hits']:
                logger.info('Empty response')
                return jsonify(message='No hits in search response'), 500
            else:
                logger.info('Healthy response')
                return jsonify(hits=response['hits']['hits']), 200
        elif request.json['engine'] == AppConf.api_visual_mode:
            query = request.json['query']
            response = milvus_cursor.search(key=query, k=10)

            if response.__len__() <= 0:
                logger.info('Empty response from Milvus')
                return jsonify(message='No hits in search response'), 500

            d = list()
            for pos in response.id_array[0]:
                _id = dual_redis_cursor.get_by_pos(pos)
                if _id is None:
                    continue
                d.append(elastic_cursor.get(index='visee', id=_id))

            logger.info('Healthy response')
            return jsonify(hits=d), 200
    except Exception as ex:
        logger.exception(ex)
        return jsonify(message=ex), 500


if __name__ == '__main__':
    app.run(host=AppConf.api_host, port=AppConf.api_port)
