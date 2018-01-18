from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "postgresql+psycopg2://postgres@/user_data_store"
db = SQLAlchemy(app)


class SiteDataSchema(db.Model):
    __tablename__ = "sitedataschema"
    site_id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.JSON)


class UserSiteData(db.Model):
    __tablename__ = "usersitedata"
    user_id = db.Column(UUID, primary_key=True)
    site_id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)
    consented_at = db.Column(db.DateTime)
    blocked = db.Column(db.Boolean)


class AdminNote(db.Model):
    __tablename__ = "adminnote"
    user_id = db.Column(UUID, primary_key=True)
    creator_id = db.Column(UUID, primary_key=True)
    created_at = db.Column(db.DateTime, primary_key=True)
    note = db.Column(db.Text)
    updated_at = db.Column(db.DateTime)
