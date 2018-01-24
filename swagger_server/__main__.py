#!/usr/bin/env python3

import connexion
import os
from flask_sqlalchemy import SQLAlchemy

from swagger_server import encoder

DB = SQLAlchemy()


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'User Data API'})
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DB_URI",
        "postgresql+psycopg2://user_data_store:password@127.0.0.1:5432/user_data_store"
    )
    DB.init_app(app.app)
    app.run(port=8080)


if __name__ == '__main__':
    main()
