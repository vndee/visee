from django.shortcuts import render
import requests
import json
import time
import os
import base64


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def handle_uploaded_file(f):
    section_dir = "static/user_upload/{}/".format(str(time.time()).replace(".", "_"))
    ensure_dir(section_dir)
    with open(section_dir + 'img.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return section_dir


def search(request):
    if request.method == 'POST':
        begin_time = time.time()
        client_query = dict(request.POST)

        query_text = (
            client_query['search_text'][0].strip() if
            client_query['engine'][0] == 'text' else
            client_query['base64_img'][0].strip()[22:]
        )

        server_query = json.dumps({
            'engine': client_query['engine'][0],
            'query': query_text
        })

        search_result = requests.post(
            'http://192.168.191.235:8001/api/rest/search/',
            data=server_query,
            headers={
                'api_key': 'h$+wt&%3BtH*6rA^KfPzMKDm**GdH_wQaQebd&X9!h=nNVjrt+pn8GNB5%-_ug-U',
                'Content-Type': 'application/json',
                'Accept': 'text/plain',
            }
        )
        _result = search_result.json()
        res = {
            'res_text': json.dumps(_result),
            'search_text': client_query['search_text'][0] if client_query['engine'] == 'text' else '',
            'time_process': str(time.time() - begin_time)[0:4],
            'num_result': "{} result{}".format(
                len(_result['hits']),
                's' if len(_result['hits']) > 1 else '',
            )
        }
        return render(request, 'result.html', res)
    return render(request, 'index.html')
