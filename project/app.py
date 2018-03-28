import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)

# Grab URI from env here, instead of getting it from settings. Original setting
# implementation caused circular import issues for certain envs. Tox test env
# for example.
DB_URI = os.environ.get(
    "DB_URI",
    "postgresql+psycopg2://user_data_store:password@127.0.0.1:5432/user_data_store"
)
APP.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

DB = SQLAlchemy(APP)
