#!/bin/bash

echo "RUN migrate collectstatic compilemessages"
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compilemessages

exec "$@"
docker tag dev docker.pkg.github.com/63phc/lks/test_dev:0.1
docker push docker.pkg.github.com/63phc/lks/test_dev:0.1