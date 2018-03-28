#!/bin/bash

python manage.py db upgrade -d user_data_store/migrations
python3 -m swagger_server
