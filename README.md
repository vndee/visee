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

### Configuration

List of environment variables can be use to config VISEE. All variables define in `.env`.

| Variable | Description | Deafult value |
|----------|-------------|---------------|
|`API_KEY`| Authorization key for REST API|`h$+wt&%3BtH*6rA^KfPzMKDm**GdH_wQaQebd&X9!h=nNVjrt+pn8GNB5%-_ug-U`|
|`API_HOST`| REST API host binding (docker internal network)|`0.0.0.0`|
|`API_PORT`| REST API port binding (docker internal network)|`7070`|
|`KAFKA_HOSTS`| Kafka hosts | `[visee_kafka:9092]`|
|`KAFKA_USER`| Kafka user| `None`|

### Libraries and framework

- **Crawler:** Selenium, BeatifulSoup, Apache Kafka, Redis.
- **Indexer:** PyTorch, Apache Kafka, Redis.
- **Search Engine:** Elasticsearch, Milvus.
- **RESTful Services:** Flask, Nginx, Gunicorn.
- **User Interface:** NodeJS, Nginx, HTML + CSS + JS.
- **Logging System:** ELK+ Stack (Elasticsearch, Beats, Logtash, Kibana).
 
<p align="center">
  <img src="https://raw.githubusercontent.com/vndee/visee/master/imgs/visee.png?token=AGXWHAGPQ5HJLX5WGY5ZC326QTSKE">
  <p align="center">System Architecture and Technical Stack</p>
</p>

Contributor: [**Duy V. Huynh**](https://github.com/vndee), [**Hoang N. Truong**](https://github.com/hoangperry/), [**Linh Q. Tran**](https://github.com/tql247/)
