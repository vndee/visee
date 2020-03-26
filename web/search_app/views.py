from django.shortcuts import render
import requests
import json
import time


def search(request):
    if request.method == 'POST':
        begin_time = time.time()
        querry = dict(request.POST)
        search_result = requests.post(
            'http://192.168.191.235:8001/api/rest/search/',
            data=json.dumps({
                "engine": querry['engine'][0],
                "query": querry['search_text'][0],
            }),
            headers={
                'api_key': 'h$+wt&%3BtH*6rA^KfPzMKDm**GdH_wQaQebd&X9!h=nNVjrt+pn8GNB5%-_ug-U',
                'Content-Type': 'application/json',
                'Accept': 'text/plain',
            }
        )

        res = {
            'res_text': json.dumps(search_result.json()),
            'search_text': querry['search_text'][0],
            'time_process': str(time.time() - begin_time)[0:4],
        }
        return render(request, 'result.html', res)
    return render(request, 'index.html')
