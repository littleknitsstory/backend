FROM python:3.9.0a6-alpine3.11
ENV PYTHONUNBUFFERED 1
ARG DEV=dev

RUN mkdir -p /app/requirements
WORKDIR /app

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev postgresql-client jpeg-dev zlib-dev
RUN apk add --update bash && rm -rf /var/cache/apk/*

COPY requirements /app/requirements
#--no-cache-dir
RUN pip install -r requirements/dev.txt

COPY . /app
RUN mkdir -p /app/log/gunicorn

ENTRYPOINT [".docker/entrypoint.sh"]
