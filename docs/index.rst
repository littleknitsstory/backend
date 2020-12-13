### Welcome to LKS Project Docs
  - This is project, blog and shop with the most modern technologies, also for testing new version of python and django.
  - This is just a pet project backend, this is not a boxed solution, this is just an API for my project.


Project Install from repo for developing
------

Clone project::

        git clone -b develop https://github.com/63phc/lks.git

 - There are two ways to start a project, all in docker or only pg, redis in docker
 - You can not use docker, then you should have pg and redis in local
 
Start in Docker all
------

 - Install Docker: [instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/#supported-storage-drivers) 
 - edit docker/dev/.env file with your params::

        cp .env.example .env
        docker-compose -f .docker/docker-compose.dev.yml build
        docker-compose -f .docker/docker-compose.dev.yml run backend python manage.py makemigrations
        docker-compose -f .docker/docker-compose.dev.yml run backend python manage.py migrate
        docker-compose -f .docker/docker-compose.dev.yml up


 - Pycharm Setup: [instruction](https://www.jetbrains.com/help/pycharm/docker.html)

Start only postgres, redis
------

-  in file .env:6 need update `POSTGRES_HOST=localhost`::

    docker-compose -f .docker/docker-compose.local.yml up postgresql redis

Create virtual env
------

- VirtualEnv::

        python3 -m venv Venv
        source Venv/bin/activate
        pip3 install -r src/requirements/development.txt

- Or through pipenv::

        pip3 install pipenv
        pipenv install
        pipenv shell

- Env File

- edit .env.example file with your params::

        cp .env.example .env

- or create .env with params::


 DJANGO_ENV - ENUM: develop, test, production
 SECRET_KEY - random sting
 PROFILE 
 NGINX_PORT 
 POSTGRES_NAME 
 POSTGRES_USER 
 POSTGRES_DB 
 POSTGRES_PASSWORD 
 PGDATA 
 POSTGRES_HOST 
 POSTGRES_PORT 
 REDIS_HOST 
 REDIS_PASSWORD 
 REDIS_PORT 
 FLOWER_PORT 
 FLOWER_USER 
 FLOWER_PASSWORD 
 PROVIDER_EMAIL 
 EMAIL_HOST 
 EMAIL_PORT 
 EMAIL_HOST_USER 
 EMAIL_HOST_PASSWORD 
 SENDGRID_API_KEY 
 MAILGUN_API_KEY 
 FIXER_ACCESS_KEY 
 OPEN_EXCHANGE_RATES_APP_ID 
 SENTRY_DNS 

- Prepare project::

    python manage.py makemigration
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py loaddata src/fixtures/*.json
    python manage.py runserver

Git flow
------

- Easy git flow::

    git checkout develop
    git pull develop
    git checkout -b <your branch>
    # when complete task
    git add .
    git commit -m '#<number task> commit messages' 
    git push origin <your branch>

- Git flow healthy person
[git-flow-cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)

 - Settings flake + pre-commit hook::

    sudo pip3 install flake8
    #(OUTPUT FILTERS -> $FILE_PATH$\:$LINE$\:$COLUMN$\:.*)
    flake8 --install-hook git
    git config --global --bool flake8.strict true
    # Easy start -> ctrl + shift + a -> flake -> enter

