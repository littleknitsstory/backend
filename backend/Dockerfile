FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /project
WORKDIR /project

RUN apk update && \
apk add --virtual build-deps gcc python3-dev musl-dev && \
apk add postgresql-dev

ADD requirements.txt /project/
RUN pip3 install -r requirements.txt

RUN apk add --update bash && rm -rf /var/cache/apk/*
ADD . /project/

WORKDIR /project/src