import os
from yaml import load
from collections import namedtuple


def get_devenv():
    conf = dict()

    # api configuration
    conf['api_key'] = os.environ.get('API_KEY', 'h$+wt&%3BtH*6rA^KfPzMKDm**GdH_wQaQebd&X9!h=nNVjrt+pn8GNB5%-_ug-U')
    conf['api_host'] = os.environ.get('API_HOST', '0.0.0.0')
    conf['api_port'] = os.environ.get('API_PORT', 7070)
    conf['api_text_mode'] = 'text'
    conf['api_visual_mode'] = 'visual'

    # kafka configuration
    conf['kafka_hosts'] = [x for x in os.environ.get('KAFKA_HOSTS', 'localhost:9094').split()]
    conf['kafka_user'] = os.environ.get('KAFKA_USER', None)
    conf['kafka_password'] = os.environ.get('KAFKA_PASSWORD', None)
    conf['kafka_num_partitions'] = int(os.environ.get('KAFKA_NUM_PARTITIONS', 10))
    conf['kafka_link_topic'] = os.environ.get('KAFKA_LINK_TOPIC', 'links_item')
    conf['kafka_consumer_group'] = os.environ.get('KAFKA_CONSUMER_GROUP', 'default')

    # redis configuration
    conf['redis_host'] = os.environ.get('REDIS_HOST', 'localhost')
    conf['redis_port'] = os.environ.get('REDIS_PORT', 6379)
    conf['redis_password'] = os.environ.get('REDIS_PASSWORD', '')
    conf['redis_categories_db'] = os.environ.get('REDIS_CATEGORIES_DB', 0)
    conf['redis_link2scrape_db'] = os.environ.get('REDIS_LINK2SCRAPE_DB', 1)

    # milvus configuration
    conf['milvus_host'] = os.environ.get('MILVUS_HOST', 'localhost')
    conf['milvus_port'] = os.environ.get('MILVUS_PORT', 19530)
    conf['milvus_table_name'] = os.environ.get('MILVUS_TABLE_NAME', 'visee')

    # elastic configuration
    conf['elastic_hosts'] = [x for x in os.environ.get('ELASTIC_HOSTS', 'localhost').split()]
    conf['elastic_port'] = os.environ.get('ELASTIC_PORT', 9200)
    conf['elastic_user'] = os.environ.get('ELASTIC_USER', 'elastic')
    conf['elastic_password'] = os.environ.get('ELASTIC_PASSWORD', 'changeme')
    conf['elastic_index'] = os.environ.get('ELASTIC_INDEX', 'visee')

    # other
    conf['chromedriver_path'] = os.environ.get('CHROMEDRIVER_PATH', 'static/chromedriver')
    conf['image_size'] = os.environ.get('IMAGE_SIZE', 1000)
    conf['download_image'] = os.environ.get('DOWNLOAD_IMAGE', True)

    return conf


def get_prodenv():
    conf = dict()

    # api configuration
    conf['api_key'] = os.environ.get('API_KEY', 'h$+wt&%3BtH*6rA^KfPzMKDm**GdH_wQaQebd&X9!h=nNVjrt+pn8GNB5%-_ug-U')
    conf['api_host'] = os.environ.get('API_HOST', '0.0.0.0')
    conf['api_port'] = os.environ.get('API_PORT', 7070)
    conf['api_text_mode'] = 'text'
    conf['api_visual_mode'] = 'visual'

    # kafka configuration
    conf['kafka_hosts'] = [x for x in os.environ.get('KAFKA_HOSTS', 'visee_kafka:9092').split()]
    conf['kafka_user'] = os.environ.get('KAFKA_USER', None)
    conf['kafka_password'] = os.environ.get('KAFKA_PASSWORD', None)
    conf['kafka_num_partitions'] = int(os.environ.get('KAFKA_NUM_PARTITIONS', 10))
    conf['kafka_link_topic'] = os.environ.get('KAFKA_LINK_TOPIC', 'links_item')
    conf['kafka_consumer_group'] = os.environ.get('KAFKA_CONSUMER_GROUP', 'default')

    # redis configuration
    conf['redis_host'] = os.environ.get('REDIS_HOST', 'visee_redis')
    conf['redis_port'] = os.environ.get('REDIS_PORT', 6379)
    conf['redis_password'] = os.environ.get('REDIS_PASSWORD', '')
    conf['redis_categories_db'] = os.environ.get('REDIS_CATEGORIES_DB', 0)
    conf['redis_link2scrape_db'] = os.environ.get('REDIS_LINK2SCRAPE_DB', 1)

    # milvus configuration
    conf['milvus_host'] = os.environ.get('MILVUS_HOST', 'visee_milvus')
    conf['milvus_port'] = os.environ.get('MILVUS_PORT', 19530)
    conf['milvus_table_name'] = os.environ.get('MILVUS_TABLE_NAME', 'visee')

    # elastic configuration
    conf['elastic_hosts'] = [x for x in os.environ.get('ELASTIC_HOSTS', 'visee_elasticsearch').split()]
    conf['elastic_port'] = os.environ.get('ELASTIC_PORT', 9200)
    conf['elastic_user'] = os.environ.get('ELASTIC_USER', 'elastic')
    conf['elastic_password'] = os.environ.get('ELASTIC_PASSWORD', 'changeme')
    conf['elastic_index'] = os.environ.get('ELASTIC_INDEX', 'visee')

    # other
    conf['chromedriver_path'] = os.environ.get('CHROMEDRIVER_PATH', '/visee/static/chromedriver')
    conf['image_size'] = os.environ.get('IMAGE_SIZE', 1000)
    conf['download_image'] = os.environ.get('DOWNLOAD_IMAGE', True)

    return conf


env = get_devenv()
AppConf = namedtuple('AppConf', env.keys())(*env.values())
