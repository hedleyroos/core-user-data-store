import os

from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DB_URI", "postgresql+psycopg2://postgres@127.0.0.1:5432/user_data_store")
