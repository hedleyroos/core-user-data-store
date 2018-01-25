import connexion
import six
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from swagger_server.models.admin_note import AdminNote  # noqa: E501
from swagger_server.models.admin_note_create import AdminNoteCreate  # noqa: E501
from swagger_server.models.admin_note_update import AdminNoteUpdate  # noqa: E501
from swagger_server.models.site_data_schema import SiteDataSchema  # noqa: E501
from swagger_server.models.site_data_schema_create import SiteDataSchemaCreate  # noqa: E501
from swagger_server.models.site_data_schema_update import SiteDataSchemaUpdate  # noqa: E501
from swagger_server.models.user_site_data import UserSiteData  # noqa: E501
from swagger_server.models.user_site_data_create import UserSiteDataCreate  # noqa: E501
from swagger_server.models.user_site_data_update import UserSiteDataUpdate  # noqa: E501
from swagger_server import util
from user_data_store import db_actions

from user_data_store.models import AdminNote as SQLA_AdminNote

from user_data_store.site_config import app

db = SQLAlchemy(app)


def adminnote_create(data=None):
    """adminnote_create
    :param data:
    :type data: dict | bytes

    :rtype: AdminNote
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="AdminNote",
        api_model=AdminNote,
        action="create",
        data=data,
    )


def adminnote_delete(user_id, creator_id, created_at):  # noqa: E501
    """adminnote_delete

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param creator_id: The creator_id
    :type creator_id: dict | bytes
    :param created_at: The created_at value
    :type created_at: str

    :rtype: None
    """
    return 'do some magic!'


def adminnote_list(offset=None, limit=None, user_id=None, creator_id=None):  # noqa: E501
    """adminnote_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param user_id: An optional query parameter to filter by user_id
    :type user_id: dict | bytes
    :param creator_id: An optional query parameter to filter by creator (a user_id)
    :type creator_id: dict | bytes

    :rtype: List[AdminNote]
    """
    return 'do some magic!'


def adminnote_read(user_id, creator_id, created_at):  # noqa: E501
    """adminnote_read

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param creator_id: The creator_id
    :type creator_id: dict | bytes
    :param created_at: The created_at value
    :type created_at: str

    :rtype: AdminNote
    """
    return 'do some magic!'


def adminnote_update(user_id, creator_id, created_at, data=None):  # noqa: E501
    """adminnote_update

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param creator_id: The creator_id
    :type creator_id: dict | bytes
    :param created_at: The created_at value
    :type created_at: str
    :param data:
    :type data: dict | bytes

    :rtype: AdminNote
    """
    return 'do some magic!'


def sitedataschema_create(data=None):  # noqa: E501
    """sitedataschema_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: SiteDataSchema
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="SiteDataSchema",
        api_model=SiteDataSchema,
        action="create",
        data=data,
    )


def sitedataschema_delete(site_id):  # noqa: E501
    """sitedataschema_delete

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """



def sitedataschema_list(offset=None, limit=None):  # noqa: E501
    """sitedataschema_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int

    :rtype: List[SiteDataSchema]
    """
    return 'do some magic!'


def sitedataschema_read(site_id):  # noqa: E501
    """sitedataschema_read

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: SiteDataSchema
    """
    return 'do some magic!'


def sitedataschema_update(site_id, data=None):  # noqa: E501
    """sitedataschema_update

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param data:
    :type data: dict | bytes

    :rtype: SiteDataSchema
    """
    if connexion.request.is_json:
        data = SiteDataSchemaUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usersitedata_create(data=None):  # noqa: E501
    """usersitedata_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: UserSiteData
    """
    if connexion.request.is_json:
        data = UserSiteDataCreate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usersitedata_delete(user_id, site_id):  # noqa: E501
    """usersitedata_delete

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return 'do some magic!'


def usersitedata_list(offset=None, limit=None, user_id=None, site_id=None):  # noqa: E501
    """usersitedata_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param user_id: An optional query parameter to filter by user_id
    :type user_id: dict | bytes
    :param site_id: An optional query parameter to filter by site_id
    :type site_id: int

    :rtype: List[UserSiteData]
    """
    return 'do some magic!'


def usersitedata_read(user_id, site_id):  # noqa: E501
    """usersitedata_read

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: UserSiteData
    """
    return 'do some magic!'


def usersitedata_update(user_id, site_id, data=None):  # noqa: E501
    """usersitedata_update

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param data:
    :type data: dict | bytes

    :rtype: UserSiteData
    """
    return 'do some magic!'
