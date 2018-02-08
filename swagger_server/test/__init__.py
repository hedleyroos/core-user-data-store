import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase

from user_data_store import models
from swagger_server.encoder import JSONEncoder

DB = SQLAlchemy()


class BaseTestCase(TestCase):

    def create_app(self):
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.app.config = models.app.config
        app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        DB.init_app(app.app)
        app.add_api('swagger.yaml',
                    arguments={'title': 'Test User Data Store'})
        return app.app
