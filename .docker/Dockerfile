FROM python:3.9-rc-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/requirements && mkdir -p /app/log/gunicorn
WORKDIR /app

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev && \
    apk add postgresql-dev postgresql-client jpeg-dev zlib-dev && \
    python -m pip install --upgrade pip && \
    apk add --update bash && rm -rf /var/cache/apk/*

COPY src/requirements /app/requirements

ARG REQUIREMENT
RUN pip install -r requirements/${REQUIREMENT}.txt
#--no-cache-dir

COPY . /app

ENTRYPOINT [".docker/entrypoint.sh"]
