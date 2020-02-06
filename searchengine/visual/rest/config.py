import os
from yaml import load
from collections import namedtuple


def get_env():
    conf = dict()
    # conf['api_key'] = os.getenv('API_KEY')
    conf['api_key'] = 'h$+wt&%3BtH*6rA^KfPzMKDm**GdH_wQaQebd&X9!h=nNVjrt+pn8GNB5%-_ug-U'
    return conf


conf = get_env()
APIConf = namedtuple('APIConf', conf.keys())(*conf.values())
