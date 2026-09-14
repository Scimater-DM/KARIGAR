#!/bin/sh
python manage.py migrate --noinput
exec gunicorn --bind :$PORT --workers 2 --threads 4 --timeout 120 config.wsgi:application
