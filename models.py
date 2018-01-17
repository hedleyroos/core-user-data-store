from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "postgresql+psycopg2://postgres@/user_data_store"
db = SQLAlchemy(app)


class SiteDataSchema(db.Model):
    __tablename__ = "sitedataschema"
    site_id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.JSON)
