[![version](https://img.shields.io/badge/version-0.3.313b-green.svg)]()
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

### Project Deploying 
[![Deploy to DO](https://www.deploytodo.com/do-btn-white.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/63phc/lks/tree/develop)

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
          comments    -
          like        - 
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
* GraphQL ([docs](https://graphql.org/)

### Project Features
 - Versioning
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
| FIXER_ACCESS_KEY           |                                |                                                 |
| OPEN_EXCHANGE_RATES_APP_ID |                                |                                                 |
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

## doker instructions




pr_How_to_install_Doker_on_Windows_en-US.docx


The program is downloaded from the official site following all the instructions - there should be no problems.
https://www.docker.com/ If the Doker works correctly, go down to the installation of Vistulstudio.
You may get a notification on that Doker is not connected because virtualization is not running on the computer.
To check that this is really the problem. Go to the Task Manager to select "Performance". 
If it doesn't show the visualization enabled as in the picture. Run it as shown below
Go to the control panel. You can do this in several ways.
The easiest way is to type a query in the search box.Under Preview, select Large Icons, then click Programs and Components.
Then choose Turn Windows Components On or Off -> HuperV-> OK.
Enabling or disabling Windows components Wait for Windows to install the component and restart the computer.Next, click the Close button and restart your computer.
If the Doker works correctly, move down to the installation of Vistulstudio.

If this does not help and Doker shows the same visualization error, fix it as described below:
From experience, the problem was solved as follows:- Turn off the computer (and be sure to wait 5 minutes after a complete shutdown!!!!!!) 
- press the "turn on the computer" button and immediately start pressing F2 every second. !!!! 
If the BIOS does not start:press DEL or F2 when the computer boots. Brand-name PCs and all-in-one PCs may have other keys.
To enter the BIOS on a desktop computer, you need to press the DEL key at startup. 
This is the key most often used, but in some cases there may be others (especially on monoblocks and branded computers). 
The exact keys are determined by the manufacturer, for example, ASRock specifies DEL or F2 for its motherboards. 
Monoblocks and desktop PCs from Lenovo monoblocks use the F1 key.enter the BIOS on the laptopIn short: 
Press F2, DEL, ESC or one of the function keys (mostly F1, F8, F9, F10, F11, F12) while booting. Also try combinations Fn c F1 - F12.
In contrast to desktop computers, on laptops there can be a lot more differences between different manufacturers. 
The most common way to enter the BIOS is to use the F2 key (sometimes combined with the Fn) but there are also other keys and their combinations. 
In particular, there can be such less common combinations: Ctrl + Alt + Ins, Ctrl + Alt + F3, Ctrl + Alt + S and others.Now you have to go to the "Advanced" item. 
It can also be called "Integrated Peripherals". In it you need to go to "CPU Configuration". 
There you need to find the item "Intel Virtualization Technology" (the route and the name of the item may vary slightly). 
Switch it to "Enabled". If it does not, it means that your computer does not support virtualization.It would roughly look like this

INSTALLING Visualstudio
https://code.visualstudio.com
Install with an extension for Doker!!!
Go to your Github.
Download the archive with Backend, unzip it into a convenient folder.
In the . Docker you need to replace the existing Dockerfile and docker-compose.yml files with the necessary ones (they are available in our team).

In addition, it is necessary to replace the name of the . env to env
Go to VisualStudioCode, use the built-in explorer to navigate to the folder with the unpacked Backend. Go to the folder .
Docker.
Run compose up the replaced docker-compose.yml file either by command or from the menu:
Waiting for the images to be built and the containers to run. Voila.


