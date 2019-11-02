FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
WORKDIR /app

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev postgresql-client jpeg-dev zlib-dev
RUN apk add --update bash && rm -rf /var/cache/apk/*

COPY requirements/development.txt /app
RUN pip install -r ./requirements/development.txt  #--no-cache-dir

COPY . /app
#ADD ./docker/dev/backend/entrypoint.sh /

#RUN chmod +x /entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]
ENTRYPOINT [".docker/entrypoint.sh"]

