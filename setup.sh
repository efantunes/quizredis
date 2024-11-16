#! /bin/bash
docker compose build --no-cache web-front
docker compose build --no-cache web-back
docker compose up -d --force-recreate 
