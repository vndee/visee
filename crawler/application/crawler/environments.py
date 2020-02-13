import os

DEPLOY = 'local'
DRIVER_PATH_DEFAULT = 'chromedriver'

if DEPLOY == 'local':
    '''
    *******************************************
    ** Environment variable for LOCAL deploy **
    *******************************************
    '''
    # Kafka default info
    KAFKA_HOSTS_DEFAULT = '172.24.0.4:9092'
    KAFKA_USER_DEFAULT = None
    KAFKA_PASSWORD_DEFAULT = None
    KAFKA_NUM_PARTITIONS_DEFAULT = '10'
    KAFKA_LINK_TOPIC_DEFAULT = 'links_item'
    KAFKA_OBJECT_TOPIC_DEFAULT = 'objects_item'
    KAFKA_CONSUMER_GROUP_DEFAULT = 'default'
    KAFKA_INDEX_TOPIC_DEFAULT = 'indexes'

    # Redis default info
    REDIS_HOST_DEFAULT = 'localhost'
    REDIS_PORT_DEFAULT = '6379'
    REDIS_DB_DEFAULT = '1'
    REDIS_DB_CACHE_DEFAULT = '0'
    REDIS_PASSWORD_DEFAULT = None

    # Other info
    DOWNLOAD_IMAGES_DEFAULT = 'True'
    IMAGE_SIZE_DEFAULT = 1000
    DEEP_CRAWL_DEFAULT = 'True'
    YAML_FOLDER_DEFAULT = 'rules/'
    DEFAULT_DOWNLOAD_DIR = 'downloads/'

    # Elasticsearch
    ELASTIC_HOST_DEFAULT = 'localhost'
    ELASTIC_PORT_DEFAULT = '9200'
    ELASTIC_USER_DEAFULT = 'elastic'
    ELASTIC_PASSWORD_DEFAULT = 'changeme'


elif DEPLOY == 'dps':
    '''
    *******************************************
    ** Environment variable for CLOUD deploy **
    *******************************************
    '''
    # Kafka default info
    KAFKA_HOSTS_DEFAULT = '192.168.1.5:9099'
    KAFKA_USER_DEFAULT = None
    KAFKA_PASSWORD_DEFAULT = None
    KAFKA_NUM_PARTITIONS_DEFAULT = '10'
    KAFKA_LINK_TOPIC_DEFAULT = 'links_product'
    KAFKA_OBJECT_TOPIC_DEFAULT = 'product'
    KAFKA_CONSUMER_GROUP_DEFAULT = 'default'
    KAFKA_INDEX_TOPIC_DEFAULT = 'indexes'

    # Redis default info
    REDIS_HOST_DEFAULT = '192.168.1.5'
    REDIS_PORT_DEFAULT = '6381'
    REDIS_DB_DEFAULT = '2'
    REDIS_PASSWORD_DEFAULT = None
    REDIS_DB_CACHE = '0'

    # Other info
    DOWNLOAD_IMAGES_DEFAULT = 'True'
    IMAGE_SIZE_DEFAULT = 1000
    DEEP_CRAWL_DEFAULT = 'True'
    YAML_FOLDER_DEFAULT = 'rules/'
    DEFAULT_DOWNLOAD_DIR = 'downloads/'

    # Elasticsearch
    ELASTIC_HOST_DEFAULT = 'localhost'
    ELASTIC_PORT_DEFAULT = '9200'
    ELASTIC_USER_DEAFULT = 'elastic'
    ELASTIC_PASSWORD_DEFAULT = 'changeme'


elif DEPLOY == 'cloud':
    '''
    *******************************************
    ** Environment variable for CLOUD deploy **
    *******************************************
    '''
    # Kafka default info
    KAFKA_HOSTS_DEFAULT = '35.186.148.118:9092'
    KAFKA_USER_DEFAULT = None
    KAFKA_PASSWORD_DEFAULT = None
    KAFKA_NUM_PARTITIONS_DEFAULT = '10'
    KAFKA_LINK_TOPIC_DEFAULT = 'links_product'
    KAFKA_OBJECT_TOPIC_DEFAULT = 'project_dict'
    KAFKA_CONSUMER_GROUP_DEFAULT = 'default'

    # Redis default info
    REDIS_HOST_DEFAULT = '35.186.148.118'
    REDIS_PORT_DEFAULT = '6379'
    REDIS_DB_DEFAULT = '9'
    REDIS_PASSWORD_DEFAULT = None

    # Other info
    DOWNLOAD_IMAGES_DEFAULT = 'True'
    IMAGE_SIZE_DEFAULT = 1000
    DEEP_CRAWL_DEFAULT = 'True'
    YAML_FOLDER_DEFAULT = 'rules/'
    DEFAULT_DOWNLOAD_DIR = 'downloads/'

    # Elasticsearch
    ELASTIC_HOST_DEFAULT = 'localhost'
    ELASTIC_PORT_DEFAULT = '9200'
    ELASTIC_USER_DEAFULT = 'elastic'
    ELASTIC_PASSWORD_DEFAULT = 'changeme'


class ConfigDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def create_environments():
    configs = dict()

    configs['driver_path'] = os.environ.get('DRIVER_PATH', DRIVER_PATH_DEFAULT)

    # kafka info
    configs['kafka_hosts'] = [x for x in os.environ.get('KAFKA_HOSTS', KAFKA_HOSTS_DEFAULT).split()]
    configs['kafka_user'] = os.environ.get('KAFKA_USER', KAFKA_USER_DEFAULT)
    configs['kafka_password'] = os.environ.get('KAFKA_PASSWORD', KAFKA_PASSWORD_DEFAULT)
    configs['kafka_num_partitions'] = int(os.environ.get('KAFKA_NUM_PARTITIONS', KAFKA_NUM_PARTITIONS_DEFAULT))
    configs['kafka_link_topic'] = os.environ.get('KAFKA_LINK_TOPIC', KAFKA_LINK_TOPIC_DEFAULT)
    configs['kafka_index_topic'] = os.environ.get('KAFKA_INDEX_TOPIC', KAFKA_INDEX_TOPIC_DEFAULT)
    configs['kafka_object_topic'] = os.environ.get('KAFKA_OBJECT_TOPIC', KAFKA_OBJECT_TOPIC_DEFAULT)
    configs['kafka_consumer_group'] = os.environ.get('KAFKA_CONSUMER_GROUP', KAFKA_CONSUMER_GROUP_DEFAULT)

    configs['redis_host'] = os.environ.get('REDIS_HOST', REDIS_HOST_DEFAULT)
    configs['redis_port'] = int(os.environ.get('REDIS_PORT', REDIS_PORT_DEFAULT))
    configs['redis_db'] = os.environ.get('REDIS_DB', REDIS_DB_DEFAULT)
    configs['redis_cache_db'] = os.environ.get('REDIS_CACHE_DB', REDIS_DB_CACHE_DEFAULT)
    configs['redis_password'] = os.environ.get('REDIS_PASSWORD', REDIS_PASSWORD_DEFAULT)

    # external info
    configs['yaml_folder'] = os.environ.get('YAML_FOLDER', YAML_FOLDER_DEFAULT)
    configs['download_images'] = bool(os.environ.get('DOWNLOAD_IMAGES', DOWNLOAD_IMAGES_DEFAULT))
    configs['image_size'] = int(os.environ.get('IMAGE_SIZE', IMAGE_SIZE_DEFAULT))
    configs['deep_crawl'] = bool(os.environ.get('DEEP_CRAWL', DEEP_CRAWL_DEFAULT))
    configs['download_dir'] = bool(os.environ.get('DOWNLOAD_DIR', DEFAULT_DOWNLOAD_DIR))

    configs['elastic_hosts'] = [x for x in os.environ.get('ELASTIC_HOSTS', ELASTIC_HOST_DEFAULT).split()]
    configs['elastic_port'] = os.environ.get('ELASTIC_PORT', ELASTIC_PORT_DEFAULT)
    configs['elastic_user'] = os.environ.get('ELASTIC_USER', ELASTIC_USER_DEAFULT)
    configs['elastic_password'] = os.environ.get('ELASTIC_PASSWORD', ELASTIC_PASSWORD_DEFAULT)

    return ConfigDict(configs)
