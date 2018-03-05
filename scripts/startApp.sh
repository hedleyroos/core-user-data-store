#!/bin/bash

FLASK_APP=user_data_store/models.py flask db upgrade -d user_data_store/migrations
python3 -m swagger_server
