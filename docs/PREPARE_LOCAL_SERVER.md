### Project Install 

- clone project: 
```
git clone -b develop https://github.com/63phc/lks.git
```
- create env
```
python3 -m venv name
source name/bin/activate 
pip3 install -r backend/requirements/local.txt
```
- or through pipenv:
```
pip3 install pipenv
pipenv install
pipenv shell
```

- edit .env.example file with your params
```
cp .env.expamle .env
# or create .env with params
SECRET_KEY=YOUR_SECRET_KEY
POSTGRES_USER=user_db
POSTGRES_DB=test_db
POSTGRES_PASSWORD=pass_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
PGDATA=/var/lib/postgresql/data/pgdata

```
- OLD frontend
```
# inside frontend
yarn && yarn run start
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
