#!/bin/bash

sql/create_database.sh $(DB_NAME) $(DB_USER) | -u postgres psql -f -
FLASK_APP=user_data_store/models.py flask db upgrade -d user_data_store/migrations
python3 -m swagger_server
