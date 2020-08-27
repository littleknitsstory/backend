## Welcome to LKS Project Docs 

### Project Install 

#### Clone project: 
```
git clone -b develop https://github.com/63phc/lks.git
```
#### Docker setup
 - Install Docker: [instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/#supported-storage-drivers) 
 - edit docker/dev/.env file with your params

```
cp docker/dev/.env.example .env
docker-compose -f docker/docker-compose.dev.yml build
docker-compose -f docker/docker-compose.dev.yml run backend python manage.py makemigrations
docker-compose -f docker/docker-compose.dev.yml run backend python manage.py migrate
docker-compose -f docker/docker-compose.dev.yml up
```
 - Pycharm Setup: [instruction](https://www.jetbrains.com/help/pycharm/docker.html)

* only postgres

```
docker-compose -f docker/docker-compose.local.yml up postgresql
# in .env:6
POSTGRES_HOST=localhost
# AND GO Local setup
```


### Local setup
#### Create env
- VirtualEnv
```
python3 -m venv name
source name/bin/activate 
pip3 install -r backend/requirements/local.txt
```
- Or through pipenv:
```
pip3 install pipenv
pipenv install
pipenv shell
```

#### Env File

- edit .env.example file with your params

```
cp .env.expamle .env
```

- or create .env with params

```
    DJANGO_ENV=development
    SECRET_KEY=YOUR_SECRET_KEY
    # POSTGRES_USER=user_db
    # POSTGRES_DB=test_db
    # POSTGRES_PASSWORD=pass_db
    # POSTGRES_HOST=postgresql # for docker
    # POSTGRES_HOST=localhost  # for local
    # POSTGRES_PORT=5432
    # PGDATA=/var/lib/postgresql/data/pgdata

```

- Prepare project:

```
    python manage.py makemigration
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py loaddata src/fixtures/*.json
    python manage.py runserver
```

#### Git flow

- Easy git flow

```
    git checkout develop
    git pull develop
    git checkout -b <your branch>
    # when complete task
    git add .
    git commit -m '#<number task> commit messages' 
    git push origin <your branch>
```

- Git flow healthy person
[git-flow-cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)

 - Settings flake + pre-commit hook
 
``` 
    sudo pip3 install flake8
    #(OUTPUT FILTERS -> $FILE_PATH$\:$LINE$\:$COLUMN$\:.*)
    flake8 --install-hook git
    git config --global --bool flake8.strict true
    # Easy start -> ctrl + shift + a -> flake -> enter
```

