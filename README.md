[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/63phc/lks.git)
[![TravisCI](https://travis-ci.com/63phc/lks.svg?branch=develop)]()
[![BCH compliance](https://bettercodehub.com/edge/badge/63phc/lks?branch=develop)](https://bettercodehub.com/)
[![Requirements Status](https://requires.io/github/63phc/lks/requirements.svg?branch=develop)](https://requires.io/github/63phc/lks/requirements/?branch=develop)
[![codecov](https://codecov.io/gh/63phc/lks/branch/develop/graph/badge.svg)](https://codecov.io/gh/63phc/lks)

* main development in the [development](https://github.com/63phc/lks/tree/develop) branch
* project releases in the master branch

### Project Descriptions
 This is project, blog and shop with the most modern technologies, also for testing new versions of python and django

### Project structure
 - /backend 		- Django backend
 - /frontend        - Frontend Sources
 - /docker			- Deploy configs and scripts
 - /docs 			- Documentation 
 - /storage         - Storage files

### Project Documentation
[Read here](docs/README.md)

#### Project versions 

backend:
* Python 3.7 
* Django 2.1.6
* DRF 3.8.2
* redis 5.0 ([hub.docker](https://hub.docker.com/_/redis/))
* PostgreSQL 11.1 ([hub.docker](https://hub.docker.com/_/postgres/))
* Celery 
* Swagger 

frontend:
* React [16.5](https://reactjs.org/versions)
* Webpack 4.21.0
* Node 11.6.0 ([hub.docker](https://hub.docker.com/_/node/))

other:
* Docker 18.06.0-ce
* Docker compose 1.22.0
* nginx 1.15 ([hub.docker](https://hub.docker.com/_/nginx/))
* postgres 11 ([hub.docker](https://hub.docker.com/_/postgres/))
