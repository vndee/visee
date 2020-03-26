![CI](https://github.com/vndee/visee/workflows/CI/badge.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/vndee/visee/badge?s=9f1351e9a1c480decd19a6bbb7e8b19b447d8474)](https://www.codefactor.io/repository/github/vndee/visee)
![](https://www.code-inspector.com/project/5387/score/svg)
![](https://www.code-inspector.com/project/5387/status/svg)
[![DepShield Badge](https://depshield.sonatype.org/badges/vndee/visee/depshield.svg)](https://depshield.github.io)
<p align="center">
  <img width="200" height="100" src="https://raw.githubusercontent.com/vndee/visee/master/imgs/logo.png?token=AGXWHAHFKIENLEQPVIJOZZK6QTQRQ">
</p>

**VISEE** is a system that combine both full-text search and visual search (base on image) together. Our system focus on 
Vietnam e-commerce product, which was collected from [**Tiki**](https://tiki.vn/), [**Lazada**](https://www.lazada.vn/), [**Shopee**](https://shopee.vn/),
[**Sendo**](https://www.sendo.vn/). **VISEE** is completely dockerization.

## Installation

### Requirements

- docker, docker-dompose, nvidia-docker

### Quickstart

To run all containers and services: 

    ./dev.sh up

Stop all services:

    ./dev.sh down
    
You can use `docker-compose` command alternatively. Especially when a service is running, its code were mount directly
from host machine to docker container. So just edit your code and restart container, you will see your changes.

### Configurations

List of environment variables can be use to config VISEE. All variables define in `.env`.

| Variable | Description | Deafult value |
|----------|-------------|---------------|
|`API_KEY`| Authorization key for REST API|`h$+wt&%3BtH*6rA^KfPzMKDm**GdH_wQaQebd&X9!h=nNVjrt+pn8GNB5%-_ug-U`|
|`API_HOST`| REST API host binding (docker internal network)|`0.0.0.0`|
|`API_PORT`| REST API port binding (docker internal network)|`7070`|
|`KAFKA_HOSTS`| Kafka hosts | `[visee_kafka:9092]`|
|`KAFKA_USER`| Kafka user| `None`|
|`KAFKA_PASSWORD`| Kafka password| `None`|
|`KAFKA_NUM_PARTITION`| Kafka number of partitions| `10`|
|`KAFKA_LINK_TOPIC`| Kafka topic for links scraper| `Link item`|
|`KAFKA_CONSUMER_GROUP`| Kafka consumer group| `default`|
|`REDIS_HOST`| Redis host (docker internal network)| `visee_redis`|
|`REDIS_PASSWORD`| Redis password| `None`|
|`REDIS_CATEGORIES_DB`| Redis database for website categories| `0`|
|`REDIS_LINK2SCRAPE_DB`| Redis database for link to scraper|`1`|
|`REDIS_DB_IDX_FIRST`| Redis first database for `DualRedisConnector`|`2`|
|`REDIS_DB_IDX_SECOND`| Redis second database for `DualRedisConnector`|`3`|
|`MILVUS_HOST`| Milvus host (docker internal network)| `visee_milvus`|
|`MILVUS_PORT`| Milvus port| `19530`|
|`MILVUS_TABLE_NAME`| Milvus table name|`visee`|
|`ELASTIC_HOSTS`| Elasticearch hosts (docker internal network)|`[visee_elasticsearch]`|
|`ELASTIC_PORT`| Elasticsearch port| `9200`|
|`ELASTIC_USER`| Elasticsearch username| `elastic`|
|`ELASTIC_PASSWORD`| Elasticsearch password|`changeme`|
|`ELASTIC_INDEX`| Elasticsearch index|`visee`|
|`EFFNET_WEIGHT`| EfficientNet weights path (in container)| `/visee/static/eff_b7.pth`|
|`CHROME_DRIVER_PATH`| Path to chrome driver (in container)| `/visee/static/chromedriver`|
|`IMAGE_SIZE`| Image downloaded size| `1000`|
|`DOWNLOAD_IMAGE`| Download image or not| `True`|

### Libraries and frameworks

- **Crawler:** Selenium, BeatifulSoup, Apache Kafka, Redis.
- **Indexer:** PyTorch, Apache Kafka, Redis.
- **Search Engine:** Elasticsearch, Milvus.
- **RESTful Services:** Flask, Nginx, Gunicorn.
- **User Interface:** NodeJS, Nginx, HTML + CSS + JS.
- **Logging System:** ELK+ Stack (Elasticsearch, Logtash, Kibana, Beats).
 
<p align="center">
  <img src="https://raw.githubusercontent.com/vndee/visee/master/imgs/visee.png?token=AGXWHAGPQ5HJLX5WGY5ZC326QTSKE">
  <p align="center">System Architecture and Technical Stack</p>
</p>

Developers: [**Duy V. Huynh**](https://github.com/vndee), [**Hoang N. Truong**](https://github.com/hoangperry/), [**Linh Q. Tran**](https://github.com/tql247/)
