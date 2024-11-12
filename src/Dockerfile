# syntax=docker/dockerfile:1
FROM python:slim-bullseye
WORKDIR /code
ENV FASTAPI_APP="quizmemory/app.py"
ENV FASTAPI_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["fastapi", "dev", "quizmemory/app.py" ,"--host", "0.0.0.0" ,"--port","5000"]