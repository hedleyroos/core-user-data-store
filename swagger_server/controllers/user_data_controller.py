import datetime
import socket

import connexion
import six
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.app import DB
from user_data_store import __version__
from swagger_server.models.admin_note import AdminNote  # noqa: E501
from swagger_server.models.admin_note_create import AdminNoteCreate  # noqa: E501
from swagger_server.models.admin_note_update import AdminNoteUpdate  # noqa: E501
from swagger_server.models.deleted_user import DeletedUser  # noqa: E501
from swagger_server.models.deleted_user_create import DeletedUserCreate  # noqa: E501
from swagger_server.models.deleted_user_site import DeletedUserSite  # noqa: E501
from swagger_server.models.deleted_user_site_create import DeletedUserSiteCreate  # noqa: E501
from swagger_server.models.deleted_user_site_update import DeletedUserSiteUpdate  # noqa: E501
from swagger_server.models.deleted_user_update import DeletedUserUpdate  # noqa: E501
from swagger_server.models.health_info import HealthInfo  # noqa: E501
from swagger_server.models.site_data_schema import SiteDataSchema  # noqa: E501
from swagger_server.models.site_data_schema_create import SiteDataSchemaCreate  # noqa: E501
from swagger_server.models.site_data_schema_update import SiteDataSchemaUpdate  # noqa: E501
from swagger_server.models.user_site_data import UserSiteData  # noqa: E501
from swagger_server.models.user_site_data_create import UserSiteDataCreate  # noqa: E501
from swagger_server.models.user_site_data_update import UserSiteDataUpdate  # noqa: E501
from swagger_server import util
from ge_core_shared import db_actions, decorators

from user_data_store.models import AdminNote as SQLA_AdminNote


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

    :param admin_note_id: A unique integer value identifying the admin note.
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


@decorators.list_response
def adminnote_list(offset=None, limit=None, user_id=None, creator_id=None, admin_note_ids=None):  # noqa: E501
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
    :param admin_note_ids: An optional list of adminnote ids
    :type admin_note_ids: List[int]

    :rtype: List[AdminNote]
    """
    query = {
        "order_by": ["id"]
    }
    if admin_note_ids is not None:
        query["ids"] = admin_note_ids
    if offset is not None:
        query["offset"] = offset
    if limit is not None:
        query["limit"] = limit
    if user_id is not None:
        query["user_id"] = user_id
    if creator_id is not None:
        query["creator_id"] = creator_id

    return db_actions.crud(
        model="AdminNote",
        api_model=AdminNote,
        action="list",
        query=query
    )


def adminnote_read(admin_note_id):  # noqa: E501
    """adminnote_read

     # noqa: E501

    :param admin_note_id: A unique integer value identifying the admin note.
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

    :param admin_note_id: A unique integer value identifying the admin note.
    :type admin_note_id: int
    :param data:
    :type data: dict | bytes

    :rtype: AdminNote
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="AdminNote",
        api_model=AdminNote,
        action="update",
        data=data,
        query={"id": admin_note_id},
    )


def deleteduser_create(data=None):  # noqa: E501
    """deleteduser_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: DeletedUser
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="DeletedUser",
        api_model=DeletedUserCreate,
        action="create",
        data=data,
    )


def deleteduser_delete(user_id):  # noqa: E501
    """deleteduser_delete

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes

    :rtype: None
    """
    return db_actions.crud(
        model="DeletedUser",
        api_model=DeletedUser,
        action="delete",
        query={
            "id": user_id
        }
    )


def deleteduser_list(offset=None, limit=None):  # noqa: E501
    """deleteduser_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int

    :rtype: List[DeletedUser]
    """
    return 'do some magic!'


def deleteduser_read(user_id):  # noqa: E501
    """deleteduser_read

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes

    :rtype: DeletedUser
    """
    if connexion.request.is_json:
        user_id = DeletedUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def deleteduser_update(user_id, data=None):  # noqa: E501
    """deleteduser_update

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param data: 
    :type data: dict | bytes

    :rtype: DeletedUser
    """
    if connexion.request.is_json:
        user_id = DeletedUser.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        data = DeletedUserUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def deletedusersite_create(data=None):  # noqa: E501
    """deletedusersite_create

     # noqa: E501

    :param data: 
    :type data: dict | bytes

    :rtype: DeletedUserSite
    """
    if connexion.request.is_json:
        data = DeletedUserSiteCreate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def deletedusersite_delete(user_id, site_id):  # noqa: E501
    """deletedusersite_delete

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        user_id = DeletedUserSite.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def deletedusersite_list(offset=None, limit=None):  # noqa: E501
    """deletedusersite_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int

    :rtype: List[DeletedUserSite]
    """
    return 'do some magic!'


def deletedusersite_read(user_id, site_id):  # noqa: E501
    """deletedusersite_read

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: DeletedUserSite
    """
    if connexion.request.is_json:
        user_id = DeletedUserSite.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def deletedusersite_update(user_id, site_id, data=None):  # noqa: E501
    """deletedusersite_update

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param data: 
    :type data: dict | bytes

    :rtype: DeletedUserSite
    """
    if connexion.request.is_json:
        user_id = DeletedUserSite.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        data = DeletedUserSiteUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def healthcheck():  # noqa: E501
    """healthcheck

    Get the status of the service. # noqa: E501


    :rtype: HealthInfo
    """
    result = DB.engine.execute("SELECT LOCALTIMESTAMP")
    db_timestamp = result.fetchone()[0]

    result = HealthInfo(
        host=socket.getfqdn(),
        server_timestamp=datetime.datetime.now(),
        version=__version__,
        db_timestamp=db_timestamp
    )
    return result


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



@decorators.list_response
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
    if connexion.request.is_json:
        data = connexion.request.get_json()

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

    # Get site data schema
    schema = sitedataschema_read(data["site_id"]).schema

    # Check data schema first
    util.validate_schema(data["data"], schema)

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


@decorators.list_response
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
    return db_actions.crud(
        model="UserSiteData",
        api_model=UserSiteData,
        action="list",
        query={
            "offset": offset,
            "limit": limit,
            "ids": {
                "user_id": user_id,
                "site_id": site_id
            },
            "order_by": ["user_id", "site_id"]
        }
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
    if connexion.request.is_json:
        data = connexion.request.get_json()

    # Get site data schema
    schema = sitedataschema_read(site_id).schema

    # Check data schema first
    util.validate_schema(data["data"], schema)

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
