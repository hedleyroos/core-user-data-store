from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import types
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression

import project.app

DB = project.app.DB


# func.utc_timestamp() is only supports MySQL out of the box.
# http://docs.sqlalchemy.org/en/latest/core/compiler.html#utc-timestamp-function
class utcnow(expression.FunctionElement):
    type = types.DateTime()


@compiles(utcnow, "postgresql")
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


class SiteDataSchema(DB.Model):
    __tablename__ = "sitedataschema"
    site_id = DB.Column(DB.Integer, primary_key=True)
    schema = DB.Column(DB.JSON)
    created_at = DB.Column(DB.DateTime, default=utcnow())
    updated_at = DB.Column(
        DB.DateTime, default=utcnow(), onupdate=utcnow())


class UserSiteData(DB.Model):
    __tablename__ = "usersitedata"
    user_id = DB.Column(UUID, primary_key=True)
    site_id = DB.Column(DB.Integer, primary_key=True)
    data = DB.Column(DB.JSON)
    consented_at = DB.Column(DB.DateTime)
    blocked = DB.Column(DB.Boolean)
    created_at = DB.Column(DB.DateTime, default=utcnow())
    updated_at = DB.Column(
        DB.DateTime, default=utcnow(), onupdate=utcnow())


class AdminNote(DB.Model):
    __tablename__ = "adminnote"
    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(UUID)
    creator_id = DB.Column(UUID)
    created_at = DB.Column(DB.DateTime, default=utcnow())
    note = DB.Column(DB.Text)
    updated_at = DB.Column(
        DB.DateTime, default=utcnow(), onupdate=utcnow())
