FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev

RUN apk add --no-cache jpeg-dev zlib-dev
RUN rm -rf /var/cache/apk/*

ADD ./backend/ ./

RUN pip3 install -r requirements/production.txt

ADD ./docker/prod/backend/entrypoint.sh ./entrypoint.sh

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
