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

from user_data_store.settings import app

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


def adminnote_delete(admin_note_id):  # noqa: E501
    """adminnote_delete

     # noqa: E501

    :param admin_note_id: Parameter to filter by id
    :type admin_note_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="AdminNote",
        api_model=AdminNote,
        action="delete",
        query={
            "id": admin_note_id
        }
    )


def adminnote_list(offset=None, limit=None, admin_note_ids=None):  # noqa: E501
    """adminnote_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param admin_note_ids: An optional list of adminnote ids
    :type admin_note_ids: List[int]

    :rtype: List[AdminNote]
    """
    query = {
        "ids": admin_note_ids,
        "order_by": ["id"]
    }
    if offset:
        query["offset"] = offset
    if limit:
        query["limit"] = limit

    return db_actions.crud(
        model="AdminNote",
        api_model=AdminNote,
        action="list",
        query=query
    )


def adminnote_read(admin_note_id):  # noqa: E501
    """adminnote_read

     # noqa: E501

    :param admin_note_id: A unique integer value identifying the adminnote.
    :type admin_note_id: int

    :rtype: AdminNote
    """
    return db_actions.crud(
        model="AdminNote",
        api_model=AdminNote,
        action="read",
        query={"id": admin_note_id}
)


def adminnote_update(admin_note_id, data=None):  # noqa: E501
    """adminnote_update

     # noqa: E501

    :param admin_note_id: A unique integer value identifying the adminote.
    :type admin_note_id: int
    :param data:
    :type data: dict | bytes

    :rtype: AdminNote
    """
    return db_actions.crud(
        model="AdminNote",
        api_model=AdminNote,
        action="update",
        data=data,
        query={"id": admin_note_id},
    )


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
    return db_actions.crud(
        model="SiteDataSchema",
        api_model=SiteDataSchema,
        action="delete",
        query={
            "site_id": site_id
        }
    )



def sitedataschema_list(offset=None, limit=None):  # noqa: E501
    """sitedataschema_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int

    :rtype: List[SiteDataSchema]
    """
    query = {
        "order_by": ["site_id"]
    }
    if limit:
        query["limit"] = limit
    if offset:
        query["offset"] = offset

    return db_actions.crud(
        model="SiteDataSchema",
        api_model=SiteDataSchema,
        action="list",
        query=query
    )


def sitedataschema_read(site_id):  # noqa: E501
    """sitedataschema_read

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: SiteDataSchema
    """
    return db_actions.crud(
        model="SiteDataSchema",
        api_model=SiteDataSchema,
        action="read",
        query={"site_id": site_id}
    )

def sitedataschema_update(site_id, data=None):  # noqa: E501
    """sitedataschema_update

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param data:
    :type data: dict | bytes

    :rtype: SiteDataSchema
    """
    return db_actions.crud(
        model="SiteDataSchema",
        api_model=SiteDataSchema,
        action="update",
        data=data,
        query={"site_id": site_id},
    )


def usersitedata_create(data=None):  # noqa: E501
    """usersitedata_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: UserSiteData
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="UserSiteData",
        api_model=UserSiteData,
        action="create",
        data=data,
    )


def usersitedata_delete(user_id, site_id):  # noqa: E501
    """usersitedata_delete

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="UserSiteData",
        api_model=UserSiteData,
        action="delete",
        query={
            "user_id": user_id,
            "site_id": site_id
        }
    )


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

    query = {
        "order_by": ["site_id", "user_id"],
    }

    if offset:
        query["offset"] = offset
    if limit:
        query["limit"] = limit
    if user_id:
        query["ids"] = user_id
    if site_id:
        query["ids"] = site_id

    return db_actions.crud(
        model="UserSiteData",
        api_model=UserSiteData,
        action="list",
        query=query
    )


def usersitedata_read(user_id, site_id):  # noqa: E501
    """usersitedata_read

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: UserSiteData
    """
    return db_actions.crud(
        model="UserSiteData",
        api_model=UserSiteData,
        action="read",
        query={
            "user_id": user_id,
            "site_id": site_id
        }
    )


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
    return db_actions.crud(
        model="UserSiteData",
        api_model=UserSiteData,
        action="update",
        data=data,
        query={
            "user_id": user_id,
            "site_id": site_id
        },
    )