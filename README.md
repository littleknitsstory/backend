

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/63phc/lks.git)


* main development in the [development](https://github.com/63phc/lks/tree/develop) branch
* project releases in the master branch

### Descriptions
 This is my pet-project for my wife, Blog and shop with the most modern technologies, also for testing new versions of python and django

#### versions 

project:
* develop - v.0.1 - **_`COMPLETE`_**
* develop - v.0.2
* develop - v.0.3
* develop - v.0.4
* release - v.0.5-beta 

backend:
* Python 3.7 
* Django 2.1
* DRF 3.8.2
* redis 5.0 [hub.docker](https://hub.docker.com/_/redis/)

frontend:
* React [16.5](https://reactjs.org/versions)
* Webpack 4.21.0

other:
* Docker 18.06.0-ce
* Docker compose 1.22.0
* nginx 1.15 [hub.docker](https://hub.docker.com/_/nginx/)
* postgres 11 [hub.docker](https://hub.docker.com/_/postgres/)

### start project 
```
>>> python3 -m venv name
>>> source name/bin/activate 
>>> pip3 install -r requirements.txt
>>> OR pipenv install && pipenv shell
>>> manage.py migrate
>>> yarn && yarn run start
```

```
    docker-compose -f docker/docker-compose.dev.yml up 
```

#### feature


|  1 |  2 | 3  |  4 | 5  |
|----|----|----|----|----|
|  1 | 2  |  3 | 4  | 5  |
|  1 |  2 |  3 |   4| 5  |
