import redis
import yaml
import os
import glob
import json
from crawler.application.crawler.environments import create_environments

if __name__ == "__main__":
    config = create_environments()

    redis_connect = redis.StrictRedis(
        host=config.redis_host, port=config.redis_port, db=config.redis_db, password=config.redis_password
    )
    homepages_dict = dict()
    for yaml_file in glob.glob('rules/homepages/*.yaml'):
        with open(yaml_file, 'r') as stream:
            yaml_data = yaml.safe_load(stream)
            key = os.path.basename(os.path.splitext(yaml_file)[0])
            homepages_dict[key] = yaml_data

    redis_connect.set("homepages", json.dumps(homepages_dict))

    pages_rule_dict = dict()
    for yaml_file in glob.glob('rules/pages/*.yaml'):
        with open(yaml_file, 'r') as stream:
            yaml_data = yaml.safe_load(stream)
            key = os.path.basename(os.path.splitext(yaml_file)[0])
            pages_rule_dict[key] = yaml_data

    redis_connect.set("pages_rule", json.dumps(pages_rule_dict))
