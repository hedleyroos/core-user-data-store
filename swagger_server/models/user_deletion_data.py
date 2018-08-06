# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserDeletionData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, amount: int=None):  # noqa: E501
        """UserDeletionData - a model defined in Swagger

        :param amount: The amount of this UserDeletionData.  # noqa: E501
        :type amount: int
        """
        self.swagger_types = {
            'amount': int
        }

        self.attribute_map = {
            'amount': 'amount'
        }

        self._amount = amount

    @classmethod
    def from_dict(cls, dikt) -> 'UserDeletionData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_deletion_data of this UserDeletionData.  # noqa: E501
        :rtype: UserDeletionData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self) -> int:
        """Gets the amount of this UserDeletionData.


        :return: The amount of this UserDeletionData.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this UserDeletionData.


        :param amount: The amount of this UserDeletionData.
        :type amount: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount