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
    apps:
        login
        store
        blogs
        dashboard
        contact
        notification
        delivery
        order

### Project structure
 - /backend 		- Django backend
 - /docker			- Deploy configs and scripts
 ~~- /docs 			- Documentation~~ (need to transfer)

### Project Documentation
[Read here](docs/README.md)

#### Project versions 

backend (fresh versions):
* Python 3.7 
* Django 2.2.2
* DRF 3.9.4 ([docs](https://www.django-rest-framework.org))
* redis 5.0 ([hub.docker](https://hub.docker.com/_/redis/))
* PostgreSQL 11.1 ([hub.docker](https://hub.docker.com/_/postgres/))
* Celery 
* Swagger 


~~frontend: [REPO](https://github.com/63phc/lks_frontend)
* React [16.5](https://reactjs.org/versions)
* Webpack 4.21.0
* Node 11.6.0 ([hub.docker](https://hub.docker.com/_/node/))~~
(outdated, need to transfer)

other:
* Docker 18.06.0-ce
* Docker compose 1.22.0
* nginx 1.15 ([hub.docker](https://hub.docker.com/_/nginx/))
* postgres 11 ([hub.docker](https://hub.docker.com/_/postgres/))



