FROM python:3.9.0b3-alpine3.12
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/requirements && mkdir -p /app/log/gunicorn
WORKDIR /app

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev && \
    apk add postgresql-dev postgresql-client jpeg-dev zlib-dev && \
    python -m pip install --upgrade pip
RUN apk add --update bash && rm -rf /var/cache/apk/*

COPY requirements /app/requirements
#--no-cache-dir
RUN pip install -r requirements/dev.txt

ARG DEV
RUN echo ${DEV}

COPY . /app

ENTRYPOINT [".docker/entrypoint.sh"]
