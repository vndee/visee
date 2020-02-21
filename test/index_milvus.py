import json
from glob import glob
from tqdm import tqdm
from pprint import pprint
from indexer.mwrapper import MilvusWrapper

milvus = MilvusWrapper()


if __name__ == '__main__':
    list_file = glob('data/json/*.json')
    for fi in tqdm(list_file):
        with open(fi) as json_file:
            data = json.loads(json_file.read())
            pprint(data)