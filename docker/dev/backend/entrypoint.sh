#!/bin/bash
set -x

echo "Starting backend ..."

python manage.py collectstatic --noinput
python manage.py compilemessages
python manage.py migrate --noinput
gunicorn -b 0:8000 core.wsgi:application

echo "End"
