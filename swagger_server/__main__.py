#!/usr/bin/env python3

import connexion

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from ge_core_shared import exception_handlers, middleware, handlers

import project.app
from swagger_server import encoder

DB = SQLAlchemy()


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'User Data API'})
    app.app.config = project.app.APP.config
    DB.init_app(app.app)
    app.add_error_handler(SQLAlchemyError, exception_handlers.db_exceptions)
    app.app.wsgi_app = middleware.AuthMiddleware(app.app.wsgi_app)
    app.app.after_request(handlers.add_total_count)
    app.run(port=8080)


if __name__ == '__main__':
    main()
