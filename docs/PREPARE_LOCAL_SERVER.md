### Project Install 

- clone project: 
```
git clone -b develop https://github.com/63phc/lks.git
```
 
```
python3 -m venv name
source name/bin/activate 
pip3 install -r requirements.txt
```
- pipenv:
```
pipenv install
pipenv shell
```

- edit .env.example file with your params
```
cp .env.expamle .env
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
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
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
