FROM python:3.10.4
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/requirements && mkdir -p /app/log/gunicorn
WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y postgresql-client libpq-dev gettext && \
    apt-get install --no-install-recommends -y gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY src/requirements /app/requirements

ARG ENVIRONMENT
RUN pip install -r requirements/${ENVIRONMENT}.txt

COPY . /app

ENTRYPOINT [".docker/entrypoint.sh"]
