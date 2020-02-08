FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
	tk-dev apt-utils python3-pip tzdata locales

RUN cd /usr/bin \
  && ln -sf python3 python \
  && ln -sf pip3 pip

ENV LANG C.UTF-8

RUN locale-gen en_US.UTF-8

# set locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TZ=Asia/Ho_Chi_Minh

RUN apt-get update && apt-get install -y --no-install-recommends

COPY . .
WORKDIR .
RUN pip3 install -r requirements.txt

CMD ["python3", "get_item_links.py"]