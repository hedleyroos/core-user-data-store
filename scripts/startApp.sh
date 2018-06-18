#!/bin/bash

python manage.py db upgrade -d user_data_store/migrations
uwsgi uwsgi.ini
