#!/bin/bash
python manage.py makemigrations
python manage.py migrate
#python manage.py runserver 0.0.0.0:8000
exec gunicorn --workers 4 --bind 0.0.0.0:8000 trombongos_api.wsgi:application