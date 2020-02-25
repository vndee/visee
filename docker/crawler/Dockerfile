FROM python:3.6

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y tzdata tk-dev apt-utils locales


RUN locale-gen en_US.UTF-8

# set locale
ENV LANG C.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TZ=Asia/Ho_Chi_Minh

ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

RUN apt-get update && apt-get install -y --no-install-recommends

RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" >> /etc/locale.conf

RUN locale-gen en_US.UTF-8

# install chromedriver
RUN apt-get install -y chromium
RUN apt-get install -y xvfb
RUN apt-get install -y clang make libc-dev
RUN apt-get install -y build-essential software-properties-common gcc g++ musl-dev
RUN apt-get install -y libxml2-dev libxslt-dev python-dev cmake

# upgrade pip
RUN pip install --upgrade pip
RUN pip install cython
RUN pip install cmake

# install selenium
RUN pip install selenium

RUN Xvfb :0 -ac -screen 0 1024x768x24 &

ADD ./requirements.txt .
ADD ./bash/run_scraper.sh .
ADD ./bash/run_getlinks.sh .

RUN chmod +x run_scraper.sh
RUN chmod +x run_getlinks.sh
RUN pip install -r requirements.txt