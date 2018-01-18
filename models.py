from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

from settings import app

db = SQLAlchemy(app)


class SiteDataSchema(db.Model):
    __tablename__ = "sitedataschema"
    site_id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    db.ForeignKeyConstraint(["site_id"], ["site.id"])

class UserSiteData(db.Model):
    __tablename__ = "usersitedata"
    user_id = db.Column(UUID, primary_key=True)
    site_id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)
    consented_at = db.Column(db.DateTime)
    blocked = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    db.ForeignKeyConstraint(["user_id", "site_id"], ["user.id", "site.id"])


class AdminNote(db.Model):
    __tablename__ = "adminnote"
    user_id = db.Column(UUID, primary_key=True)
    creator_id = db.Column(UUID, primary_key=True)
    created_at = db.Column(db.DateTime, primary_key=True, default=datetime.now)
    note = db.Column(db.Text)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    db.ForeignKeyConstraint(["user_id", "creator_id"], ["user.id", "user.id"])

# Create tables when executed
print("Creating tables...")
db.create_all()
db.session.commit()
