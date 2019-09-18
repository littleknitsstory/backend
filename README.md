[![TravisCI](https://travis-ci.com/63phc/lks.svg?branch=develop)]()
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/63phc/lks.git)
[![BCH compliance](https://bettercodehub.com/edge/badge/63phc/lks?branch=develop)](https://bettercodehub.com/)
[![CodeFactor](https://www.codefactor.io/repository/github/63phc/lks/badge)](https://www.codefactor.io/repository/github/63phc/lks)
[![codecov](https://codecov.io/gh/63phc/lks/branch/develop/graph/badge.svg)](https://codecov.io/gh/63phc/lks)
[![workflows](https://github.com/actions/production/workflows/Production/badge.svg)](/)


* main development in the [development](https://github.com/63phc/lks/tree/develop) branch
* project releases in the master branch
* new front - react [REPO](https://github.com/63phc/lks_frontend)

### Project Descriptions
 This is project, blog and shop with the most modern technologies, also for testing new versions of python and django

###  Structure
    services:
        login         - 
        store         -
          order
          bucket
          delivery
        blogs         - 
          comments    - remark

        dashboard     - 
        contact       - 
        notification  - 
        

### Project Documentation
[Read here](docs/README.md)

#### Technology

#### Project versions 

backend (fresh versions):
* Python 3.7.4 ([docs](https://www.python.org/doc/))
* Django 3.0 ([docs](https://docs.djangoproject.com/en/3.0/))
* DRF 3.9.4 ([docs](https://www.django-rest-framework.org))
* redis 5.0 ([hub.docker](https://hub.docker.com/_/redis/))
* PostgreSQL 11.1 ([hub.docker](https://hub.docker.com/_/postgres/))
* Celery 4.3 ([docs](http://www.celeryproject.org/))
* Swagger ([docs](https://swagger.io/docs/specification/about/))

frontend: [REPO](https://github.com/63phc/lks_frontend)
* Vue(?)
* React [16.5](https://reactjs.org/versions)
* Webpack 4.40.2 ([docs](https://webpack.js.org/concepts/))
* Node 11.6.0 ([hub.docker](https://hub.docker.com/_/node/))

other:
* Docker 19.03.2
* Docker compose 1.24.1
* nginx 1.15 ([hub.docker](https://hub.docker.com/_/nginx/))
* postgres 11 ([hub.docker](https://hub.docker.com/_/postgres/))
