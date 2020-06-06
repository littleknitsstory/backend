#!/bin/bash

set -x
echo "Starting backend ..."

if [[ ${POSTGRES_HOST} ]]; then
    export PGPASSWORD=${POSTGRES_PASSWORD}
    until psql -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_NAME -c '\l'; do
      >&2 echo "Postgres is unavailable - sleeping"
      sleep 5
    done
    >&2 echo "Postgres is up - continuing"
    psql -h $POSTGRES_HOST -U $POSTGRES_USER -d template1 -c 'create extension hstore;'
    unset PGPASSWORD
fi


echo "Run migrate collectstatic and compilemessages"
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compilemessages
python manage.py update_rates

echo "++++++++++++++++++++++++++++++++++++++++++"
echo "$*"
echo "++++++++++++++++++++++++++++++++++++++++++"

exec "$@"
