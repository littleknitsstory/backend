[![version](https://img.shields.io/badge/version-0.1.93b-green.svg)]()
[![tests](https://github.com/63phc/lks/workflows/tests/badge.svg)](https://github.com/63phc/lks/actions?query=workflow%3Atests)
[![build](https://github.com/63phc/lks/workflows/build/badge.svg)](https://github.com/63phc/lks/actions?query=workflow%3Abuild)
[![Documentation Status](https://readthedocs.org/projects/lks/badge/?version=develop)](https://lks.readthedocs.io/en/develop/?badge=develop)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/63phc/lks/LICENCE)
<div align="center">
    <h1>LITTLE KNITS STORY</h1>  
    
[![swagger](https://validator.swagger.io/validator?url=http://dev.backend.littleknitsstory.com/)](http://dev.backend.littleknitsstory.com/) 
[![graphql](https://badgen.net/badge/icon/graphql.beta?icon=graphql&label)](http://dev.backend.littleknitsstory.com/api/v2/)
</div>
  - This is project, blog and shop with the most modern technologies, also for testing new version of python and django. <br>
  - This is just a pet project backend, this is not a boxed solution, this is just an API for my project. <br>
  - The project that underlies this repository is coming out of deep beta and the production version of the product 1.0.0 is being prepared. <br>
  - So the master branch can be used however you like. <br>
  - There is a lot of experimental stuff in the development branch.

### Project Deploying 
[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/63phc/lks)

### Project Contents

- [Project Code](#project-code)
- [Project Documentation](#project-documentation)
- [Project Structure](#project-structure)
- [Project Features](#project-features)
- [Project Technology](#project-technology)
- [Project Guides](#project-guides)

### Project Code

[![CodeFactor](https://www.codefactor.io/repository/github/63phc/lks/badge?s=20b5db5dea700723ad3e05f5a2e0e6bb500fda65)](https://www.codefactor.io/repository/github/63phc/lks)
[![codebeat badge](https://codebeat.co/badges/8b6af8ba-2ad4-45bf-a07e-210829951461)](https://codebeat.co/projects/github-com-63phc-lks-develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/79d402edf48b4b8886a47f22cc7e9212)](https://app.codacy.com/manual/pavel.burns/lks)
[![BCH compliance](https://bettercodehub.com/edge/badge/63phc/lks?branch=develop)](https://bettercodehub.com/)
[![codecov](https://codecov.io/gh/63phc/lks/branch/develop/graph/badge.svg)](https://codecov.io/gh/63phc/lks)
[![CodeScene System Mastery](https://codescene.io/projects/9132/status-badges/system-mastery)](https://codescene.io/projects/9132)

### Project Documentation
[Read here](https://63phc.github.io/lks/)

### Project Structure
    applications:
        account       + 
        api           + 
        blog          +
          comments    -
           remark     -
        contacts      + 
        menu          + 
        reviews       + 
        shop          +
          order       +
          product     +
          delivery    -
        shorter       -
        slider        + 
        subscribe     + 
        dashboard     - 
        notification  - 
          web push - 
          email    -

### Project Technology
[![GitHub](https://badgen.net/badge/python/3.9/blue)](https://github.com/63phc/lks/blob/develop/.docker/Dockerfile#L1)
[![GitHub](https://badgen.net/badge/django/3.1/blue)](https://github.com/63phc/lks/blob/develop/src/requirements/base.txt#L3)
[![GitHub](https://img.shields.io/badge/code%20style-black-ffffff.svg)](https://github.com/psf/black)

* Python ([docs](https://www.python.org/doc/), [hub.docker](https://hub.docker.com/_/python))
* Django ([docs](https://docs.djangoproject.com/en/3.1/))
* DRF ([docs](https://www.django-rest-framework.org))
* Celery ([docs](http://www.celeryproject.org/))
* Swagger ([docs](htps://swagger.io/docs/specification/about/))
* Redis ([docs](https://redis.io/documentation), [hub.docker](https://hub.docker.com/_/redis/))
* PostgreSQL ([docs](https://www.postgresql.org/docs/), [hub.docker](https://hub.docker.com/_/postgres/))
* Nginx ([hub.docker](https://docs.nginx.com/), [hub.docker](https://hub.docker.com/_/nginx/))
* Docker ([docs](https://docs.docker.com/))
* Docker compose ([docs](https://docs.docker.com/compose/reference/overview/))
* Flower
* Redis-commander
* GraphQL


## Project Issues [![TODOs](https://badgen.net/https/api.tickgit.com/badgen/github.com/63phc/lks)](https://www.tickgit.com/browse?repo=github.com/63phc/lks)
 - If you find any bugs, feel free to file an issue on the github issue tracker.

### Project Features
 - Support multilingual
 - CI/CD with github actions
 - Auto posting FB, INST, VK
 - Watermarks photo
 - Async views for graphQL
 - ... be sure to add features ...
 
### Project Guides
- guides will be collected here, for example:
 - How to do versioning?
 - How to make multilingual api?
 - How to write reusable apps?
 - How to use CI/CD with github actions?
 
### Project Contributing
pass
