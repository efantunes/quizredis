#! /bin/bash
docker compose up -d 
cd quizmemory-backend
py -m quizmemory.scripts.rankings_queries