#!/bin/sh

set -e

#Migrate
python manage.py migrate

#Start server
python manage.py runserver 0.0.0.0:8000