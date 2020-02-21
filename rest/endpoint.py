from flask import Flask, request, jsonify
from common.config import AppConf
from common.elastic import ElasticsearchWrapper
from indexer.mwrapper import MilvusWrapper
from common.logger import get_logger


app = Flask('ViSee - Visual Search Engine RESTful API Server')
logger = get_logger('REST Server')
elastic_cursor = ElasticsearchWrapper()
milvus_cursor = MilvusWrapper()


@app.route('/api/rest/verify/')
def verify():
    headers = request.headers
    auth = headers.get('api_key')

    if auth == AppConf.api_key:
        return jsonify(message='OK: Authorized'), 200
    else:
        return jsonify(message='ERROR: Unauthorized'), 401


@app.route('/api/rest/search/')
def search():
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
                    'from': 0, 'size': 10,
                    'query_string': {
                        'query': request.json['query'],
                    }
                }
            }

            response = elastic_cursor.search(index=AppConf.elastic_index, body=query)

            return jsonify(response), 200
        elif request.json['engine'] == AppConf.api_visual_mode:
            query = request.json['query']
            response = milvus_cursor.search(key=query, k=10)
            return jsonify(response), 200
    except Exception as ex:
        logger.exception(ex)
        return jsonify(message='Unspecific error'), 500


if __name__ == '__main__':
    app.run(host=AppConf.api_host, port=AppConf.api_port)
