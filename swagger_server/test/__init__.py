import logging

import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from sqlalchemy.exc import SQLAlchemyError

from swagger_server import exception_handlers
from swagger_server.encoder import JSONEncoder

from user_data_store import models

DB = SQLAlchemy()


class BaseTestCase(TestCase):

    def create_app(self):
        #logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.app.config = models.app.config
        app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        DB.init_app(app.app)
        app.add_error_handler(SQLAlchemyError, exception_handlers.db_exceptions)
        app.add_api('swagger.yaml', arguments={'title': 'Test User Data API'})
        return app.app
