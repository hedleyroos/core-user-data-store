# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DeletedUserSite(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, deleted_user_id: str=None, site_id: int=None, created_at: datetime=None, updated_at: datetime=None, deletion_requested_at: datetime=None, deletion_requested_via: str=None, deletion_confirmed_at: datetime=None, deletion_confirmed_via: str=None):  # noqa: E501
        """DeletedUserSite - a model defined in Swagger

        :param deleted_user_id: The deleted_user_id of this DeletedUserSite.  # noqa: E501
        :type deleted_user_id: str
        :param site_id: The site_id of this DeletedUserSite.  # noqa: E501
        :type site_id: int
        :param created_at: The created_at of this DeletedUserSite.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this DeletedUserSite.  # noqa: E501
        :type updated_at: datetime
        :param deletion_requested_at: The deletion_requested_at of this DeletedUserSite.  # noqa: E501
        :type deletion_requested_at: datetime
        :param deletion_requested_via: The deletion_requested_via of this DeletedUserSite.  # noqa: E501
        :type deletion_requested_via: str
        :param deletion_confirmed_at: The deletion_confirmed_at of this DeletedUserSite.  # noqa: E501
        :type deletion_confirmed_at: datetime
        :param deletion_confirmed_via: The deletion_confirmed_via of this DeletedUserSite.  # noqa: E501
        :type deletion_confirmed_via: str
        """
        self.swagger_types = {
            'deleted_user_id': str,
            'site_id': int,
            'created_at': datetime,
            'updated_at': datetime,
            'deletion_requested_at': datetime,
            'deletion_requested_via': str,
            'deletion_confirmed_at': datetime,
            'deletion_confirmed_via': str
        }

        self.attribute_map = {
            'deleted_user_id': 'deleted_user_id',
            'site_id': 'site_id',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'deletion_requested_at': 'deletion_requested_at',
            'deletion_requested_via': 'deletion_requested_via',
            'deletion_confirmed_at': 'deletion_confirmed_at',
            'deletion_confirmed_via': 'deletion_confirmed_via'
        }

        self._deleted_user_id = deleted_user_id
        self._site_id = site_id
        self._created_at = created_at
        self._updated_at = updated_at
        self._deletion_requested_at = deletion_requested_at
        self._deletion_requested_via = deletion_requested_via
        self._deletion_confirmed_at = deletion_confirmed_at
        self._deletion_confirmed_via = deletion_confirmed_via

    @classmethod
    def from_dict(cls, dikt) -> 'DeletedUserSite':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The deleted_user_site of this DeletedUserSite.  # noqa: E501
        :rtype: DeletedUserSite
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deleted_user_id(self) -> str:
        """Gets the deleted_user_id of this DeletedUserSite.


        :return: The deleted_user_id of this DeletedUserSite.
        :rtype: str
        """
        return self._deleted_user_id

    @deleted_user_id.setter
    def deleted_user_id(self, deleted_user_id: str):
        """Sets the deleted_user_id of this DeletedUserSite.


        :param deleted_user_id: The deleted_user_id of this DeletedUserSite.
        :type deleted_user_id: str
        """
        if deleted_user_id is None:
            raise ValueError("Invalid value for `deleted_user_id`, must not be `None`")  # noqa: E501

        self._deleted_user_id = deleted_user_id

    @property
    def site_id(self) -> int:
        """Gets the site_id of this DeletedUserSite.


        :return: The site_id of this DeletedUserSite.
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id: int):
        """Sets the site_id of this DeletedUserSite.


        :param site_id: The site_id of this DeletedUserSite.
        :type site_id: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this DeletedUserSite.


        :return: The created_at of this DeletedUserSite.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this DeletedUserSite.


        :param created_at: The created_at of this DeletedUserSite.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self) -> datetime:
        """Gets the updated_at of this DeletedUserSite.


        :return: The updated_at of this DeletedUserSite.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        """Sets the updated_at of this DeletedUserSite.


        :param updated_at: The updated_at of this DeletedUserSite.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def deletion_requested_at(self) -> datetime:
        """Gets the deletion_requested_at of this DeletedUserSite.


        :return: The deletion_requested_at of this DeletedUserSite.
        :rtype: datetime
        """
        return self._deletion_requested_at

    @deletion_requested_at.setter
    def deletion_requested_at(self, deletion_requested_at: datetime):
        """Sets the deletion_requested_at of this DeletedUserSite.


        :param deletion_requested_at: The deletion_requested_at of this DeletedUserSite.
        :type deletion_requested_at: datetime
        """

        self._deletion_requested_at = deletion_requested_at

    @property
    def deletion_requested_via(self) -> str:
        """Gets the deletion_requested_via of this DeletedUserSite.


        :return: The deletion_requested_via of this DeletedUserSite.
        :rtype: str
        """
        return self._deletion_requested_via

    @deletion_requested_via.setter
    def deletion_requested_via(self, deletion_requested_via: str):
        """Sets the deletion_requested_via of this DeletedUserSite.


        :param deletion_requested_via: The deletion_requested_via of this DeletedUserSite.
        :type deletion_requested_via: str
        """

        self._deletion_requested_via = deletion_requested_via

    @property
    def deletion_confirmed_at(self) -> datetime:
        """Gets the deletion_confirmed_at of this DeletedUserSite.


        :return: The deletion_confirmed_at of this DeletedUserSite.
        :rtype: datetime
        """
        return self._deletion_confirmed_at

    @deletion_confirmed_at.setter
    def deletion_confirmed_at(self, deletion_confirmed_at: datetime):
        """Sets the deletion_confirmed_at of this DeletedUserSite.


        :param deletion_confirmed_at: The deletion_confirmed_at of this DeletedUserSite.
        :type deletion_confirmed_at: datetime
        """

        self._deletion_confirmed_at = deletion_confirmed_at

    @property
    def deletion_confirmed_via(self) -> str:
        """Gets the deletion_confirmed_via of this DeletedUserSite.


        :return: The deletion_confirmed_via of this DeletedUserSite.
        :rtype: str
        """
        return self._deletion_confirmed_via

    @deletion_confirmed_via.setter
    def deletion_confirmed_via(self, deletion_confirmed_via: str):
        """Sets the deletion_confirmed_via of this DeletedUserSite.


        :param deletion_confirmed_via: The deletion_confirmed_via of this DeletedUserSite.
        :type deletion_confirmed_via: str
        """

        self._deletion_confirmed_via = deletion_confirmed_via
