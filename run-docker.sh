#!/usr/bin/env bash

set -a
source services.envar

if [[ -z $developmentNet ]]; then
  echo "Creating development network"
  docker network create development
fi

if [[ ${PYTHON_ENV} == 'production' ]]; then
  echo "Launching user_domain API Rest mode PRODUCTION..."
  export TARGET=release
else
  echo "Launching user_domain API Rest mode DEVELOPMENT..."
  export TARGET=development
fi

bash ./db/run-docker.sh

docker-compose up -d --build
