# coding: utf-8

"""
    JOJ Horse

    Git version: c5741c9@2023-02-03T15:02:34Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainInvitationEdit(object):
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
        'code': 'str',
        'expire_at': 'datetime',
        'role': 'str'
    }

    attribute_map = {
        'code': 'code',
        'expire_at': 'expireAt',
        'role': 'role'
    }

    def __init__(self, code=None, expire_at=None, role=None):  # noqa: E501
        """DomainInvitationEdit - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._expire_at = None
        self._role = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if expire_at is not None:
            self.expire_at = expire_at
        if role is not None:
            self.role = role

    @property
    def code(self):
        """Gets the code of this DomainInvitationEdit.  # noqa: E501

        invitation code  # noqa: E501

        :return: The code of this DomainInvitationEdit.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DomainInvitationEdit.

        invitation code  # noqa: E501

        :param code: The code of this DomainInvitationEdit.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def expire_at(self):
        """Gets the expire_at of this DomainInvitationEdit.  # noqa: E501

        expire time of invitation  # noqa: E501

        :return: The expire_at of this DomainInvitationEdit.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        """Sets the expire_at of this DomainInvitationEdit.

        expire time of invitation  # noqa: E501

        :param expire_at: The expire_at of this DomainInvitationEdit.  # noqa: E501
        :type: datetime
        """

        self._expire_at = expire_at

    @property
    def role(self):
        """Gets the role of this DomainInvitationEdit.  # noqa: E501

        domain role after invitation  # noqa: E501

        :return: The role of this DomainInvitationEdit.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DomainInvitationEdit.

        domain role after invitation  # noqa: E501

        :param role: The role of this DomainInvitationEdit.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if issubclass(DomainInvitationEdit, dict):
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
        if not isinstance(other, DomainInvitationEdit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
