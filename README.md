[![tests](https://github.com/63phc/lks/workflows/tests/badge.svg)](https://github.com/63phc/lks/actions?query=workflow%3Atests)
[![build](https://github.com/63phc/lks/workflows/build/badge.svg)](https://github.com/63phc/lks/actions?query=workflow%3Abuild)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/63phc/lks/LICENCE)
<div align="center">
<h1>LITTLE KNITS STORY</h1>  
    
[![swagger](https://validator.swagger.io/validator?url=http://dev.backend.littleknitsstory.com/)](http://dev.backend.littleknitsstory.com/) 
[![graphql](https://badgen.net/badge/icon/graphql.beta?icon=graphql&label)](http://dev.backend.littleknitsstory.com/api/v2/)
</div>
  - This is project with the most modern technologies, also for testing new version of python and django. <br>
  - This is just a pet project backend, this is not a boxed solution, this is just an API for my project. <br>
  - The project that underlies this repository is coming out of deep beta and the production version of the product 1.0.0 is being prepared. <br>
  - So the master branch can be used however you like. <br>
  - There is a lot of experimental stuff in the development branch.

### Project Contents

- [Project Structure](#project-structure)
- [Project Features](#project-features)
- [Project Install](#project-install)
- [Project Issues](#project-issues)

### Project Code

[![CodeFactor](https://www.codefactor.io/repository/github/63phc/lks/badge?s=20b5db5dea700723ad3e05f5a2e0e6bb500fda65)](https://www.codefactor.io/repository/github/63phc/lks)
[![codebeat badge](https://codebeat.co/badges/8b6af8ba-2ad4-45bf-a07e-210829951461)](https://codebeat.co/projects/github-com-63phc-lks-develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/79d402edf48b4b8886a47f22cc7e9212)](https://app.codacy.com/manual/pavel.burns/lks)
[![BCH compliance](https://bettercodehub.com/edge/badge/63phc/lks?branch=develop)](https://bettercodehub.com/)
[![codecov](https://codecov.io/gh/63phc/lks/branch/develop/graph/badge.svg)](https://codecov.io/gh/63phc/lks)
[![CodeScene System Mastery](https://codescene.io/projects/9132/status-badges/system-mastery)](https://codescene.io/projects/9132)

### Project Structure
    applications:
        account       + 
        api           + 
        blog          +
          comments    +
          reactions   + 
        contacts      + 
        courses       - 
        dashboard     - 
        feed          -
        menu          + 
        reviews       + 
        shop          +
          order       +
          product     +
          delivery    -
        shorter       -
        slider        + 
        subscribe     + 
        notification  - 
          in app      - 
          email       -

### Project Technology
[![GitHub](https://badgen.net/badge/python/3.10.4/blue)](https://github.com/63phc/lks/blob/develop/.docker/Dockerfile#L1)
[![GitHub](https://badgen.net/badge/django/4.1.2/blue)](https://github.com/63phc/lks/blob/develop/src/requirements/base.txt#L3)
[![GitHub](https://img.shields.io/badge/code%20style-black-ffffff.svg)](https://github.com/psf/black)

* Python ([docs](https://www.python.org/doc/), [hub.docker](https://hub.docker.com/_/python))
* Django ([docs](https://docs.djangoproject.com/en/3.1/))
* DRF ([docs](https://www.django-rest-framework.org))
* Celery ([docs](http://www.celeryproject.org/))
* Swagger ([docs](https://swagger.io/docs/specification/about/))
* Redis ([docs](https://redis.io/documentation), [hub.docker](https://hub.docker.com/_/redis/))
* PostgreSQL ([docs](https://www.postgresql.org/docs/), [hub.docker](https://hub.docker.com/_/postgres/))
* Nginx ([hub.docker](https://docs.nginx.com/), [hub.docker](https://hub.docker.com/_/nginx/))
* Docker ([docs](https://docs.docker.com/))
* Docker compose ([docs](https://docs.docker.com/compose/reference/overview/))
* GraphQL ([docs](https://graphql.org/))

### Project Features
 - Support multilingual
 - CI/CD with github actions
 - Auto posting FB, INST, VK
 - Watermarks photo
 - Async views for graphQL
 - ... be sure to add features ...
 
 
### Project Install
- Clone project:
```
        git clone -b develop https://github.com/63phc/lks.git
```
- There are two ways to start a project, all in docker or only pg, redis in docker
- You can not use docker, then you should have pg and redis in local
 
### Start for developing locale with postgres, redis in docker

```
   cp .env.example .env
   # all 
   docker-compose -f .docker/docker-compose.local.yml up --build --quiet-pull
   # postgresql redis
   docker-compose -f .docker/docker-compose.local.yml up postgresql redis
```
- Create virtual env:
```
    python3 -m venv Venv
    source Venv/bin/activate
    pip3 install -r src/requirements/development.txt
```

- Prepare project:
```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py loaddata src/fixtures/*.json
    python manage.py runserver

```
```
    gunicorn src.core.wsgi:application -w 2 -b 0.0.0.0:8000
    gunicorn src.core.asgi:application -k uvicorn.workers.UvicornWorker
```


#### Parameters

- .env file:

| Environment                | Default                        | Description                                     |
| -------------------------- | ------------------------------ | ----------------------------------------------- |
| SECRET_KEY                 |                                |                                                 |
| ENVIRONMENT                | test                           |   test using sqlite                             |
| NGINX_PORT                 | 26363                          |                                                 |
| POSTGRES_NAME              | lks_pg_name                    |                                                 |
| POSTGRES_USER              | lks_pg_user                    |                                                 |
| POSTGRES_DB                | lks_pg_db                      |                                                 |
| POSTGRES_PASSWORD          | lks_pg_pass                    |                                                 |
| PGDATA                     | /var/lib/postgresql/data/pgdata|                                                 |
| POSTGRES_HOST              | localhost                      |                                                 |
| POSTGRES_PORT              | 5432                           |                                                 |
| REDIS_HOST                 | localhost                      |                                                 |
| REDIS_PASSWORD             | pswd123                        |                                                 |
| REDIS_PORT                 | 6379                           |                                                 |
| FLOWER_PORT                | 9876                           |                                                 |
| FLOWER_USER                | admin                          |                                                 |
| FLOWER_PASSWORD            | admin                          |                                                 |
| PROVIDER_EMAIL             |                                |                                                 |
| EMAIL_HOST                 |                                |                                                 |
| EMAIL_PORT                 | 587                            |                                                 |
| EMAIL_HOST_USER            |                                |                                                 |
| EMAIL_HOST_PASSWORD        |                                |                                                 |
| SENDGRID_API_KEY           |                                |                                                 |
| MAILGUN_API_KEY            |                                |                                                 |
| SENTRY_DNS                 |                                |                                                 |


### Start in Docker

- Install Docker: [instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/#supported-storage-drivers)
- edit .docker/dev/.env file with your params:
```
        cp .env.example .docker/.env
        docker-compose -f .docker/docker-compose.yml build
        docker-compose -f .docker/docker-compose.yml up
        #
        docker-compose -f .docker/docker-compose.yml run backend python manage.py makemigrations
        docker-compose -f .docker/docker-compose.yml run backend python manage.py migrate
        docker-compose -f .docker/docker-compose.yml run backend python manage.py loaddata src/fixtures/*.json
```
- Pycharm Setup: https://www.jetbrains.com/help/pycharm/docker.html


## Project Issues [![TODOs](https://badgen.net/https/api.tickgit.com/badgen/github.com/63phc/lks)](https://www.tickgit.com/browse?repo=github.com/63phc/lks)
 - If you find any bugs, feel free to file an issue on the github issue tracker.