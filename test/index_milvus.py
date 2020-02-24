import json
import string
import random
from glob import glob
from tqdm import tqdm
from pprint import pprint
from indexer.mwrapper import MilvusWrapper
from PIL import Image
import base64
from io import BytesIO

milvus = MilvusWrapper()


def generate_random(x=16):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(x)])

cnt = 0

if __name__ == '__main__':
    list_file = glob('data/json/*.json')
    for idx, fi in enumerate(tqdm(list_file)):
        if idx > 10:
            break
        with open(fi) as json_file:
            data = json.loads(json_file.read())
            id = generate_random(x=16)
            for image in data['images']:
                img = bytes(image['base64_data'][2:-1], encoding='utf-8').decode()
                # _img = Image.open(BytesIO(base64.b64decode(img)))
                response = milvus.add(img, cnt)
                cnt = cnt + 1
                print(response)