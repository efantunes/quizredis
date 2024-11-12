#! /bin/bash
cd src
docker compose build --no-cache web
docker compose up -d --force-recreate 
py -m quizmemory.scripts.carga_inicial
py -m quizmemory.scripts.carga_respostas_aleatorias