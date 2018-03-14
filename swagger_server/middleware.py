import os

from werkzeug.wrappers import Request, Response


class AuthMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        key = request.headers.get("X-Api-Key", None)
        if key:
            if key in os.environ.get("ALLOWED_KEYS"):
                return self.app(environ, start_response)
            response = Response(status="403 Forbidden")
            return response(environ, start_response)
        response = Response(status="401 Unauthorized")
        return response(environ, start_response)
