#!/bin/bash

if [ $1 == "up" ]; then
  docker-compose up $2
elif [ $1 == "down" ]; then
  docker-compose down --rmi all --volumes
elif [ $1 == "logs" ]; then
  docker-compose logs $2
fi