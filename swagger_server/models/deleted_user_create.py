# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DeletedUserCreate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, username: str=None, email: str=None, msisdn: str=None, reason: str=None, deleter_id: str=None):  # noqa: E501
        """DeletedUserCreate - a model defined in Swagger

        :param id: The id of this DeletedUserCreate.  # noqa: E501
        :type id: str
        :param username: The username of this DeletedUserCreate.  # noqa: E501
        :type username: str
        :param email: The email of this DeletedUserCreate.  # noqa: E501
        :type email: str
        :param msisdn: The msisdn of this DeletedUserCreate.  # noqa: E501
        :type msisdn: str
        :param reason: The reason of this DeletedUserCreate.  # noqa: E501
        :type reason: str
        :param deleter_id: The deleter_id of this DeletedUserCreate.  # noqa: E501
        :type deleter_id: str
        """
        self.swagger_types = {
            'id': str,
            'username': str,
            'email': str,
            'msisdn': str,
            'reason': str,
            'deleter_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'email': 'email',
            'msisdn': 'msisdn',
            'reason': 'reason',
            'deleter_id': 'deleter_id'
        }

        self._id = id
        self._username = username
        self._email = email
        self._msisdn = msisdn
        self._reason = reason
        self._deleter_id = deleter_id

    @classmethod
    def from_dict(cls, dikt) -> 'DeletedUserCreate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The deleted_user_create of this DeletedUserCreate.  # noqa: E501
        :rtype: DeletedUserCreate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this DeletedUserCreate.


        :return: The id of this DeletedUserCreate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this DeletedUserCreate.


        :param id: The id of this DeletedUserCreate.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this DeletedUserCreate.


        :return: The username of this DeletedUserCreate.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this DeletedUserCreate.


        :param username: The username of this DeletedUserCreate.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email(self) -> str:
        """Gets the email of this DeletedUserCreate.


        :return: The email of this DeletedUserCreate.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this DeletedUserCreate.


        :param email: The email of this DeletedUserCreate.
        :type email: str
        """

        self._email = email

    @property
    def msisdn(self) -> str:
        """Gets the msisdn of this DeletedUserCreate.


        :return: The msisdn of this DeletedUserCreate.
        :rtype: str
        """
        return self._msisdn

    @msisdn.setter
    def msisdn(self, msisdn: str):
        """Sets the msisdn of this DeletedUserCreate.


        :param msisdn: The msisdn of this DeletedUserCreate.
        :type msisdn: str
        """

        self._msisdn = msisdn

    @property
    def reason(self) -> str:
        """Gets the reason of this DeletedUserCreate.


        :return: The reason of this DeletedUserCreate.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this DeletedUserCreate.


        :param reason: The reason of this DeletedUserCreate.
        :type reason: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def deleter_id(self) -> str:
        """Gets the deleter_id of this DeletedUserCreate.


        :return: The deleter_id of this DeletedUserCreate.
        :rtype: str
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id: str):
        """Sets the deleter_id of this DeletedUserCreate.


        :param deleter_id: The deleter_id of this DeletedUserCreate.
        :type deleter_id: str
        """
        if deleter_id is None:
            raise ValueError("Invalid value for `deleter_id`, must not be `None`")  # noqa: E501

        self._deleter_id = deleter_id