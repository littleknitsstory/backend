FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
ARG DEV=dev

RUN mkdir -p /app
WORKDIR /app

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev postgresql-client jpeg-dev zlib-dev
RUN apk add --update bash && rm -rf /var/cache/apk/*

COPY requirements /app/requirements
RUN pip install -r requirements/${DEV}.txt

COPY . /app
RUN mkdir -p /app/log/gunicorn

ENTRYPOINT ["entrypoint.sh"]

