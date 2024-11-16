#! /bin/bash
cd quizmemory-backend
docker compose up -d 
py -m quizmemory.scripts.rankings_queries