#!/bin/sh
cd crawler/
python yaml_to_redis.py
python get_item_links.py