FROM nethacker/ubuntu-18-04-nginx:1.17.1

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
  && rm -rf /var/lib/apt/lists/*

ADD ./bash/run_nginx.sh .