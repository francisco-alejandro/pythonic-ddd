#!/usr/bin/env bash

set -a

developmentNet=$(docker network ls -f name=development -q)

if [[ -z $developmentNet ]]; then
  printf "\nCreating development network"
  docker network create development
fi

printf "\nLaunching Postgres container..."
docker-compose -f ./db/docker-compose.yml up -d --build
docker container exec -u postgres -i postgres psql < ./db/db.sql

docker container exec -u postgres -i postgres psql user_domain < ./db/tables/wallet.sql
docker container exec -u postgres -i postgres psql user_domain < ./db/tables/user.sql

docker container exec -u postgres -i postgres psql user_domain < ./db/populate.sql
