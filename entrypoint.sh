#!/bin/bash

python manage.py migrate --settings $DJANGO_SETTINGS
python manage.py runserver 0.0.0.0:8000 --settings $DJANGO_SETTINGS