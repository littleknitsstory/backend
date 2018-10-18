#!/usr/bin/env bash

until cd /backend
do
    echo "Waiting for django volume..."
done

sleep 3

echo "Running project..."
python manage.py runserver 0.0.0.0:8000

exec $cmd

