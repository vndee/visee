FROM python:3.6-alpine3.7

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers gcc g++ musl-dev
RUN apk add libxml2-dev libxslt-dev python3-dev
RUN pip install cython

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium

WORKDIR /crawler
COPY . /crawler
RUN pip install -r requirements.txt

CMD ["python", "get_item_links.py"]