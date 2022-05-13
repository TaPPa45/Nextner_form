#!/bin/bash


python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input
exec gunicorn Nextner.wsgi:application -b 0.0.0.0:8000 --reload --timeout 120 --workers 10

