import json
from searchengine.visual.indexer import FaissIndexer

if __name__ == '__main__':
    faiss_index = FaissIndexer()
    data = json.loads(open('data/json/0.json').read())
    print(data.keys())
    for image in data['images']:
        print(image)