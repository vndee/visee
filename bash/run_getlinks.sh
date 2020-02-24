#!/bin/sh
export PYTHONPATH=/visee
cd /visee/crawler/
python yaml_to_redis.py
python get_item_links.py