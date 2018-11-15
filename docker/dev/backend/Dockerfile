FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev

RUN apk add --no-cache jpeg-dev zlib-dev

#ADD backend/requirements/ /backend/

RUN apk add --update bash && rm -rf /var/cache/apk/*

#ADD ./backend/ /backend/
COPY ./backend/ /backend/
RUN pip3 install -r requirements/local.txt
