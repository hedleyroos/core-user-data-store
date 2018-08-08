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
    schema = DB.Column(DB.JSON, default={}, nullable=False)
    created_at = DB.Column(DB.DateTime, default=utcnow(), nullable=False)
    updated_at = DB.Column(
        DB.DateTime, default=utcnow(), onupdate=utcnow(), nullable=False)


class UserSiteData(DB.Model):
    __tablename__ = "usersitedata"
    user_id = DB.Column(UUID, primary_key=True)
    site_id = DB.Column(DB.Integer, primary_key=True)
    data = DB.Column(DB.JSON, default={}, nullable=False)
    created_at = DB.Column(DB.DateTime, default=utcnow(), nullable=False)
    updated_at = DB.Column(
        DB.DateTime, default=utcnow(), onupdate=utcnow(), nullable=False)


class AdminNote(DB.Model):
    __tablename__ = "adminnote"
    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(UUID, nullable=False)
    creator_id = DB.Column(UUID, nullable=False)
    created_at = DB.Column(DB.DateTime, default=utcnow(), nullable=False)
    note = DB.Column(DB.Text, nullable=False)
    updated_at = DB.Column(
        DB.DateTime, default=utcnow(), onupdate=utcnow(), nullable=False)


class DeletedUser(DB.Model):
    __tablename__ = "deleteduser"
    id = DB.Column(UUID, primary_key=True)
    username = DB.Column(DB.VARCHAR(150), nullable=False)
    email = DB.Column(DB.VARCHAR(254))
    msisdn = DB.Column(DB.VARCHAR(16))
    reason = DB.Column(DB.Text, nullable=False)
    deleter_id = DB.Column(UUID, nullable=False)
    deleted_at = DB.Column(DB.DateTime)
    created_at = DB.Column(DB.DateTime, default=utcnow(), nullable=False)
    updated_at = DB.Column(
        DB.DateTime, default=utcnow(), onupdate=utcnow(), nullable=False)


class DeletedUserSite(DB.Model):
    __tablename__ = "deletedusersite"
    deleted_user_id = DB.Column(UUID, primary_key=True)
    site_id = DB.Column(DB.Integer, primary_key=True)
    deletion_requested_at = DB.Column(DB.DateTime)
    deletion_requested_via = DB.Column(DB.VARCHAR(255))
    deletion_confirmed_at = DB.Column(DB.DateTime)
    deletion_confirmed_via = DB.Column(DB.VARCHAR(255))
    created_at = DB.Column(DB.DateTime, default=utcnow(), nullable=False)
    updated_at = DB.Column(
        DB.DateTime, default=utcnow(), onupdate=utcnow(), nullable=False)
