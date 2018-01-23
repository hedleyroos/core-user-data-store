# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AdminNoteCreate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, user_id: str=None, creator_id: str=None, note: str=None):  # noqa: E501
        """AdminNoteCreate - a model defined in Swagger

        :param user_id: The user_id of this AdminNoteCreate.  # noqa: E501
        :type user_id: str
        :param creator_id: The creator_id of this AdminNoteCreate.  # noqa: E501
        :type creator_id: str
        :param note: The note of this AdminNoteCreate.  # noqa: E501
        :type note: str
        """
        self.swagger_types = {
            'user_id': str,
            'creator_id': str,
            'note': str
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'creator_id': 'creator_id',
            'note': 'note'
        }

        self._user_id = user_id
        self._creator_id = creator_id
        self._note = note

    @classmethod
    def from_dict(cls, dikt) -> 'AdminNoteCreate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The admin_note_create of this AdminNoteCreate.  # noqa: E501
        :rtype: AdminNoteCreate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> str:
        """Gets the user_id of this AdminNoteCreate.


        :return: The user_id of this AdminNoteCreate.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this AdminNoteCreate.


        :param user_id: The user_id of this AdminNoteCreate.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def creator_id(self) -> str:
        """Gets the creator_id of this AdminNoteCreate.


        :return: The creator_id of this AdminNoteCreate.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id: str):
        """Sets the creator_id of this AdminNoteCreate.


        :param creator_id: The creator_id of this AdminNoteCreate.
        :type creator_id: str
        """
        if creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def note(self) -> str:
        """Gets the note of this AdminNoteCreate.


        :return: The note of this AdminNoteCreate.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note: str):
        """Sets the note of this AdminNoteCreate.


        :param note: The note of this AdminNoteCreate.
        :type note: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note