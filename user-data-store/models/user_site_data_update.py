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


class UserSiteDataUpdate(object):
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
        'data_processing_consent_provided': 'bool',
        'data': 'object'
    }

    attribute_map = {
        'data_processing_consent_provided': 'data_processing_consent_provided',
        'data': 'data'
    }

    def __init__(self, data_processing_consent_provided=None, data=None):
        """
        UserSiteDataUpdate - a model defined in Swagger
        """

        self._data_processing_consent_provided = None
        self._data = None

        if data_processing_consent_provided is not None:
          self.data_processing_consent_provided = data_processing_consent_provided
        if data is not None:
          self.data = data

    @property
    def data_processing_consent_provided(self):
        """
        Gets the data_processing_consent_provided of this UserSiteDataUpdate.

        :return: The data_processing_consent_provided of this UserSiteDataUpdate.
        :rtype: bool
        """
        return self._data_processing_consent_provided

    @data_processing_consent_provided.setter
    def data_processing_consent_provided(self, data_processing_consent_provided):
        """
        Sets the data_processing_consent_provided of this UserSiteDataUpdate.

        :param data_processing_consent_provided: The data_processing_consent_provided of this UserSiteDataUpdate.
        :type: bool
        """

        self._data_processing_consent_provided = data_processing_consent_provided

    @property
    def data(self):
        """
        Gets the data of this UserSiteDataUpdate.

        :return: The data of this UserSiteDataUpdate.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this UserSiteDataUpdate.

        :param data: The data of this UserSiteDataUpdate.
        :type: object
        """

        self._data = data

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
        if not isinstance(other, UserSiteDataUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
