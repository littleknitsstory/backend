#!/usr/bin/env bash

until cd /data/www/src/
do
    echo "Waiting for django volume..."
    sleep 1
done

sleep 1

python manage.py collectstatic --noinput
python manage.py compilemessages
python manage.py migrate --noinput

echo "Running project..."
uwsgi -l 10 --ini /data/www/conf/uwsgi.ini
