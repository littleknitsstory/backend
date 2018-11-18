### Project Install 

#### Clone project: 
```
git clone -b develop https://github.com/63phc/lks.git
```
### Docker setup
 - Install Docker: [instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/#supported-storage-drivers) 
 - edit docker/dev/.env file with your params

```
cp docker/dev/.env.example .env
docker-compose -f docker/docker-compose.dev.yml build
docker-compose -f docker/docker-compose.dev.yml run backend python manage.py makemigrations
docker-compose -f docker/docker-compose.dev.yml run backend python manage.py migrate
docker-compose -f docker/docker-compose.dev.yml up
```

* only postgres

```
docker-compose -f docker/docker-compose.dev.yml up postgresql
# in .env:6
POSTGRES_HOST=localhost
./manage.py runserver
```
 - Pycharm Setup: [instruction](https://www.jetbrains.com/help/pycharm/docker.html)


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

### Prepare project
 - Prepare project:

```
# inside backend
python manage.py makemigration
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py createsuperuser
python manage.py loaddata _backups/*.json
```

### Running
 - Run developer server:

```
# inside backend
python manage.py runserver
```

### Docker setup
 - Install Docker: [instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/#supported-storage-drivers) 
 - edit docker/dev/.env file with your params

```
cp docker/dev/.env.example .env
docker-compose -f docker/docker-compose.dev.yml build
docker-compose -f docker/docker-compose.dev.yml up
```
 - Pycharm Setup: [instruction](https://www.jetbrains.com/help/pycharm/docker.html)


#### OLD frontend
```
# inside frontend
yarn && yarn run start
```
