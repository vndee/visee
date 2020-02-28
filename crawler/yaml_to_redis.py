import redis
import yaml
import os
import glob
import json

from common.config import AppConf


def push_data_to_redis():
    redis_connect = redis.StrictRedis(
        host=AppConf.redis_host,
        port=AppConf.redis_port,
        db=AppConf.redis_categories_db,
        password=AppConf.redis_password
    )

    homepages_dict = dict()
    list_domain = list()
    with open('rules/homepages.yaml', mode='r', encoding='utf-8') as stream:
        yaml_data = yaml.safe_load(stream)
        for i in yaml_data['list_domain']:
            list_domain.append(i)

    redis_connect.set('list_domain', json.dumps(list_domain))

    for yaml_file in glob.glob('rules/homepages/*.yaml'):
        with open(yaml_file, 'r') as stream:
            yaml_data = yaml.safe_load(stream)
            key = os.path.basename(os.path.splitext(yaml_file)[0])
            homepages_dict[key] = yaml_data

    redis_connect.set("homepages", json.dumps(homepages_dict))
    redis_connect.close()

    redis_connect = redis.StrictRedis(
        host=AppConf.redis_host,
        port=AppConf.redis_port,
        db=AppConf.redis_link2scrape_db,
        password=AppConf.redis_password
    )

    pages_rule_dict = dict()
    for yaml_file in glob.glob('rules/pages/*.yaml'):
        with open(yaml_file, 'r') as stream:
            yaml_data = yaml.safe_load(stream)
            key = os.path.basename(os.path.splitext(yaml_file)[0])
            pages_rule_dict[key] = yaml_data

    redis_connect.set("pages_rule", json.dumps(pages_rule_dict))
    redis_connect.set("obj_current_id", 0)
    redis_connect.close()


if __name__ == "__main__":
    push_data_to_redis()
