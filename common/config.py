import os
from yaml import load
from collections import namedtuple


def get_env():
    conf = dict()
    # conf['api_key'] = os.getenv('API_KEY')
    conf['api_key'] = 'h$+wt&%3BtH*6rA^KfPzMKDm**GdH_wQaQebd&X9!h=nNVjrt+pn8GNB5%-_ug-U'
    
    # redis configuration
    conf['redis_host'] = 'localhost' if not os.getenv('REDIS_HOST') else os.getenv('REDIS_HOST')
    conf['redis_port'] = 6379 if not os.getenv('REDIS_PORT') else int(os.getenv('REDIS_PORT'))
    conf['redis_password'] = '' if not os.getenv('REDIS_PASSWORD') else os.getenv('REDIS_PASSWORD')
    conf['redis_db_cache'] = 0 if not os.getenv('REDIS_DB_CACHE') else int(os.getenv('REDIS_DB_CACHE'))
    conf['redis_db_idx'] = 1 if not os.getenv('REDIS_DB_IDX') else int(os.getenv('REDIS_DB_IDX'))

    return env


env = get_env()
AppConf = namedtuple('AppConf', env.keys())(*env.values())
