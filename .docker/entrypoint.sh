#!/bin/bash

#set -e
#
#while ! pg_isready -h $DB_HOST -p $DB_PORT > /dev/null 2> /dev/null; do
#    echo "Waiting for postgres..."
#    sleep 3
#done
#echo "PostgreSQL started"

#source /app/venv/bin/activate

if [ "$1" = "test" ]; then
    flake8 src
    python manage.py makemigrations --check --dry-run
    PROFILE='test'
    DJANGO_SETTINGS_MODULE='src.settings.test_settings'
    if [ "$2" = "full" ]; then
      pytest -n=4 --disable-warnings src/apps
    else
      pytest -n=4 --disable-warnings src/apps --ignore-glob=*_long.py
    fi
    exit 0
fi

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compilemessages

exec "$@"
