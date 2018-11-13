FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend

## for pgsql
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev
# for Pillow
RUN apk add --no-cache jpeg-dev zlib-dev


#ADD backend/requirements/ /backend/

## bash for dev mode
RUN apk add --update bash && rm -rf /var/cache/apk/*

ADD ./backend /backend/
RUN pip3 install -r requirements/local.txt


#WORKDIR /backend
EXPOSE 8000
