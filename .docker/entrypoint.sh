#!/bin/bash

set -x
echo "Starting backend ..."

if [[ ${POSTGRES_HOST} ]]; then
    export PGPASSWORD=${POSTGRES_PASSWORD}
    until psql -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_DB -c '\l'; do
      >&2 echo "Postgres is unavailable - sleeping 63 sec"
      sleep 63
    done
    >&2 echo "Postgres is up - continuing"
    psql -h $POSTGRES_HOST -U $POSTGRES_USER -d template1 -c 'CREATE EXTENSION IF NOT EXISTS hstore;'
    unset PGPASSWORD
fi


echo "Run migrate collectstatic and compilemessages"
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compilemessages

exec "$@"
