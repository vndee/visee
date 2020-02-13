### Visee Crawler

2020 @ VISE Technologies

#### Install requirements
python3:
    ```
    pip3 install -r requirements.txt 
    ```

python2:
    ```
    pip install -r requirements.txt 
    ```

#### Configuration environment
```bash
vi crawler/application/crawler/environments.py
```

#### Push data rule file to redis
```bash
python3 yaml_to_redis.py
```

#### Run getlink
```bash
python3 get_item_links.py
```

#### Run product scraper
```bash
python3 item_scraper.py
```
