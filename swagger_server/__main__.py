#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from flask_sqlalchemy import SQLAlchemy

from user_data_store import models

DB = SQLAlchemy()


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'User Data API'})
    app.app.config = models.app.config
    DB.init_app(app.app)
    app.run(port=8080)


if __name__ == '__main__':
    main()
