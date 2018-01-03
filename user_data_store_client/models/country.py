# coding: utf-8

"""
    User Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Country(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, code=None, name=None, created_at=None, updated_at=None):
        """
        Country - a model defined in Swagger
        """

        self._code = None
        self._name = None
        self._created_at = None
        self._updated_at = None

        self.code = code
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def code(self):
        """
        Gets the code of this Country.

        :return: The code of this Country.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Country.

        :param code: The code of this Country.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")
        if code is not None and len(code) > 2:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `2`")
        if code is not None and len(code) < 2:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `2`")

        self._code = code

    @property
    def name(self):
        """
        Gets the name of this Country.

        :return: The name of this Country.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Country.

        :param name: The name of this Country.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")

        self._name = name

    @property
    def created_at(self):
        """
        Gets the created_at of this Country.

        :return: The created_at of this Country.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Country.

        :param created_at: The created_at of this Country.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Country.

        :return: The updated_at of this Country.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Country.

        :param updated_at: The updated_at of this Country.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Country):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
