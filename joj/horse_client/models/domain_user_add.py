# coding: utf-8

"""
    JOJ Horse

    Git version: 9a6ad1c@2022-02-19T11:02:02Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainUserAdd(object):
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
        'role': 'str',
        'user': 'str'
    }

    attribute_map = {
        'role': 'role',
        'user': 'user'
    }

    def __init__(self, role='user', user=None):  # noqa: E501
        """DomainUserAdd - a model defined in Swagger"""  # noqa: E501
        self._role = None
        self._user = None
        self.discriminator = None
        if role is not None:
            self.role = role
        self.user = user

    @property
    def role(self):
        """Gets the role of this DomainUserAdd.  # noqa: E501


        :return: The role of this DomainUserAdd.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DomainUserAdd.


        :param role: The role of this DomainUserAdd.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def user(self):
        """Gets the user of this DomainUserAdd.  # noqa: E501

        'me' or id of the user  # noqa: E501

        :return: The user of this DomainUserAdd.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DomainUserAdd.

        'me' or id of the user  # noqa: E501

        :param user: The user of this DomainUserAdd.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if issubclass(DomainUserAdd, dict):
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
        if not isinstance(other, DomainUserAdd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
