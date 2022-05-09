# coding: utf-8

"""
    JOJ Horse

    Git version: dc3c2e1@2022-05-09T06:18:32Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainTransfer(object):
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
        'target_user': 'str'
    }

    attribute_map = {
        'target_user': 'targetUser'
    }

    def __init__(self, target_user=None):  # noqa: E501
        """DomainTransfer - a model defined in Swagger"""  # noqa: E501
        self._target_user = None
        self.discriminator = None
        self.target_user = target_user

    @property
    def target_user(self):
        """Gets the target_user of this DomainTransfer.  # noqa: E501

        'me' or id of the user  # noqa: E501

        :return: The target_user of this DomainTransfer.  # noqa: E501
        :rtype: str
        """
        return self._target_user

    @target_user.setter
    def target_user(self, target_user):
        """Sets the target_user of this DomainTransfer.

        'me' or id of the user  # noqa: E501

        :param target_user: The target_user of this DomainTransfer.  # noqa: E501
        :type: str
        """
        if target_user is None:
            raise ValueError("Invalid value for `target_user`, must not be `None`")  # noqa: E501

        self._target_user = target_user

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
        if issubclass(DomainTransfer, dict):
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
        if not isinstance(other, DomainTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
