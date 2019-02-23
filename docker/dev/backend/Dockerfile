FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev postgresql-client

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --update bash && rm -rf /var/cache/apk/*

ADD ./backend/ ./

RUN pip3 install -r ./requirements/development.txt

ADD ./docker/dev/backend/entrypoint.sh /

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
