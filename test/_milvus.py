from milvus import Milvus


if __name__ == '__main__':
    milvus = Milvus()
    param = {'host': '127.0.0.1', 'port': '19530'}
    status = milvus.connect(**param)
    status, result = milvus.count_collection('visee')
    print(result)