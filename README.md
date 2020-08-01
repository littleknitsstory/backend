[![version](https://badgen.net/badge/version/v0.0.2b/black/)]()
[![tests](https://github.com/63phc/lks/workflows/tests/badge.svg)](https://github.com/63phc/lks/actions?query=workflow%3Atests)
[![develop](https://github.com/63phc/lks/workflows/develop/badge.svg?branch=develop)](https://github.com/63phc/lks/actions?query=workflow%3Adevelop)
[![CodeFactor](https://www.codefactor.io/repository/github/63phc/lks/badge?s=20b5db5dea700723ad3e05f5a2e0e6bb500fda65)](https://www.codefactor.io/repository/github/63phc/lks)
[![BCH compliance](https://bettercodehub.com/edge/badge/63phc/lks?branch=develop)](https://bettercodehub.com/)
[![codecov](https://codecov.io/gh/63phc/lks/branch/develop/graph/badge.svg)](https://codecov.io/gh/63phc/lks)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/63phc/lks/LICENCE)
### Project Descriptions
 This is project, blog and shop with the most modern technologies, also for testing new v of python and django

### Project Resource
* main development in the [development](https://github.com/63phc/lks/tree/develop) branch
* project releases in the [master](https://github.com/63phc/lks/tree/master) branch
* frontend-vue [REPO](https://github.com/63phc/lks-frontend-vue)

### Project Documentation
[Read here](docs/README.md)

### Project Structure
    applications:
        account       + 
        api           + 
        blog          +
          comments    - remark -
        contacts      + 
        menu          + 
        reviews       + 
        shop          +
          order       +
          product     +
          delivery    -
        slider        + 
        subscribe     + 
        dashboard     - 
        notification  - 
        

### Project Technology
[![GitHub](https://badgen.net/badge/python/3.9/blue)](https://github.com/63phc/lks/blob/develop/.docker/Dockerfile#L1)
[![GitHub](https://badgen.net/badge/django/3.0.7/blue)](https://github.com/63phc/lks/blob/develop/requirements/base.txt#L3)

* Python ([docs](https://www.python.org/doc/), [hub.docker](https://hub.docker.com/_/python))
* Django ([docs](https://docs.djangoproject.com/en/3.0/))
* DRF ([docs](https://www.django-rest-framework.org))
* Celery ([docs](http://www.celeryproject.org/))
* Swagger ([docs](https://swagger.io/docs/specification/about/))
* Redis ([hub.docker](https://hub.docker.com/_/redis/))
* PostgreSQL ([hub.docker](https://hub.docker.com/_/postgres/))
* Nginx ([hub.docker](https://hub.docker.com/_/nginx/))
* Docker 
* Docker compose 


###### 
 uvicorn src.core.asgi:application
