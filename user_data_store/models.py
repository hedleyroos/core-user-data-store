from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import types
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression

from user_data_store.settings import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# func.utc_timestamp() is only supports MySQL out of the box.
# http://docs.sqlalchemy.org/en/latest/core/compiler.html#utc-timestamp-function
class utcnow(expression.FunctionElement):
    type = types.DateTime()

@compiles(utcnow, "postgresql")
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


class SiteDataSchema(db.Model):
    __tablename__ = "sitedataschema"
    site_id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=utcnow())
    updated_at = db.Column(
        db.DateTime, default=utcnow(), onupdate=utcnow())


class UserSiteData(db.Model):
    __tablename__ = "usersitedata"
    user_id = db.Column(UUID, primary_key=True)
    site_id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)
    consented_at = db.Column(db.DateTime)
    blocked = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=utcnow())
    updated_at = db.Column(
        db.DateTime, default=utcnow(), onupdate=utcnow())


class AdminNote(db.Model):
    __tablename__ = "adminnote"
    user_id = db.Column(UUID, primary_key=True)
    creator_id = db.Column(UUID, primary_key=True)
    created_at = db.Column(db.DateTime, primary_key=True, default=utcnow())
    note = db.Column(db.Text)
    updated_at = db.Column(
        db.DateTime, default=utcnow(), onupdate=utcnow())
