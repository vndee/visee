from django.shortcuts import render
from django_visee import settings
import requests
import json
import time
import os
import base64
from io import BytesIO
from PIL import Image


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


def rbga_to_rbg(b64):
    buffered = BytesIO()
    user_img = Image.open(BytesIO(base64.b64decode(b64)))

    os.makedirs(os.path.join('static', 'usr_img'), exist_ok=True)
    user_img.save("static/usr_img/{}.png".format(str(time.time()).replace(".", "_")), format="PNG")
    if user_img.mode == "RGBA":
        background = Image.new("RGB", user_img.size, (255, 255, 255))
        background.paste(user_img, mask=user_img.split()[3])
        background.save(buffered, format="PNG")
        return str(base64.b64encode(buffered.getvalue()))[2:-1]
    user_img.save(buffered, format="PNG")
    return str(base64.b64encode(buffered.getvalue()))[2:-1]


def search(request):
    if request.method == 'POST':
        begin_time = time.time()
        client_query = dict(request.POST)

        query_text = (
            client_query['search_text'][0].strip() if
            client_query['engine'][0] == 'text' else
            rbga_to_rbg(client_query['base64_img'][0].strip()[22:])
        )

        server_query = json.dumps({
            'engine': client_query['engine'][0],
            'query': query_text
        })

        search_result = requests.post(
            settings.API_HOST,
            data=server_query,
            headers={
                'api_key': settings.API_KEY,
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
            ),
            'search_img_ret': query_text,
        }
        return render(request, 'result.html', res)
    return render(request, 'index.html')
