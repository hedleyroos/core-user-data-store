import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

from project import settings

APP = Flask(__name__)
SENTRY = Sentry(dsn=settings.SENTRY_DSN)

# Grab URI from env here, instead of getting it from settings. Original setting
# implementation caused circular import issues for certain envs. Tox test env
# for example.
DB_URI = os.environ.get(
    "DB_URI",
    "postgresql+psycopg2://user_data_store:password@127.0.0.1:5432/user_data_store"
)
APP.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialise sentry
SENTRY.init_app(APP, level=settings.SENTRY_LOG_LEVEL)

DB = SQLAlchemy(APP)
