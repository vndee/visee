import json
import base64
from PIL import Image
from io import BytesIO
from indexer.mwrapper import MilvusWrapper

milvus = MilvusWrapper()

if __name__ == '__main__':
    data = json.loads(open('data/json/0.json').read())
    b64img = data['images'][0]['base64_data']
    img = bytes(b64img[2:-1], encoding='utf-8').decode()
    # img = Image.open(BytesIO(base64.b64decode(img)))
    r = milvus.search(key=img, k=10)
    print(r.id_array[0])
