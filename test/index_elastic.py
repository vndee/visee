import json
from glob import glob
from tqdm import tqdm
from common.metadat import parse_meta_data
from common.elastic import ElasticsearchWrapper

elastic = ElasticsearchWrapper()
elastic.create_index(index='test')


if __name__ == '__main__':
    list_file = glob('data/json/*.json')
    for fi in tqdm(list_file):
        with open(fi) as json_file:
            data = json.loads(json_file.read())
            d = parse_meta_data(data)
            elastic.add(index='test', body=d)
