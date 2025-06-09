#!/bin/bash

# Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input
python3 manage.py create_default_superuser
python3 manage.py runserver 0.0.0.0:8000