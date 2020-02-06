from config import *
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/rest/verify/')
def verify():
    headers = request.headers
    auth = headers.get('api_key')

    if auth == APIConf.api_key:
        return jsonify({'Message': 'OK: Authorized'}), 200
    else:
        return jsonify({'Message': 'ERROR: Unauthorized'}), 401

@app.route('/api/rest/index/')
def index():
    headers = request.headers
    auth = headers.get('api_key')

    if auth != APIConf.api_key:
        return jsonify({'Message': 'ERROR: Unauthorized'}), 401


if __name__ == '__main__':
    app.run()
