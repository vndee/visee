import redis
from application.crawler.environments import create_environments
from application.helpers.get_chromedriver import download_chrome_driver

config = create_environments()


def check_redis():
    redis_connect = redis.StrictRedis(
        host=config.redis_host, port=config.redis_port, db=config.redis_db, password=config.redis_password
    )
    response = redis_connect.client_list()
    print(response)


if __name__ == '__main__':
    # check_redis()
    download_chrome_driver()
