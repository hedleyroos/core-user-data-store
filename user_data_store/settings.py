import os

from flask import Flask


DEFAULT_API_LIMIT = os.environ.get("DEFAULT_API_LIMIT", 50)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DB_URI", "postgresql+psycopg2://user_data_store:password@127.0.0.1:5432/user_data_store")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

API_KEY_HEADER = "X-API-KEY"
ALLOWED_API_KEYS = set(os.getenv("ALLOWED_API_KEYS").split(","))
