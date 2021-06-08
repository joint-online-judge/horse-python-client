# coding: utf-8

"""
    JOJ Horse

    Git version: dad896a@2021-06-08 19:53:00  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ListDomainUsers(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'results': 'list[DomainUser]'
    }

    attribute_map = {
        'results': 'results'
    }

    def __init__(self, results=None):  # noqa: E501
        """ListDomainUsers - a model defined in Swagger"""  # noqa: E501
        self._results = None
        self.discriminator = None
        self.results = results

    @property
    def results(self):
        """Gets the results of this ListDomainUsers.  # noqa: E501


        :return: The results of this ListDomainUsers.  # noqa: E501
        :rtype: list[DomainUser]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ListDomainUsers.


        :param results: The results of this ListDomainUsers.  # noqa: E501
        :type: list[DomainUser]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ListDomainUsers, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDomainUsers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
