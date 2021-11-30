# coding: utf-8

"""
    JOJ Horse

    Git version: e1ec5a4@2021-11-30T12:04:58Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainInvitationCreate(object):
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
        'url': 'str',
        'code': 'str',
        'expire_at': 'datetime',
        'role': 'str'
    }

    attribute_map = {
        'url': 'url',
        'code': 'code',
        'expire_at': 'expireAt',
        'role': 'role'
    }

    def __init__(self, url='', code=None, expire_at=None, role='user'):  # noqa: E501
        """DomainInvitationCreate - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._code = None
        self._expire_at = None
        self._role = None
        self.discriminator = None
        if url is not None:
            self.url = url
        self.code = code
        if expire_at is not None:
            self.expire_at = expire_at
        if role is not None:
            self.role = role

    @property
    def url(self):
        """Gets the url of this DomainInvitationCreate.  # noqa: E501

        (unique) url of the domain  # noqa: E501

        :return: The url of this DomainInvitationCreate.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DomainInvitationCreate.

        (unique) url of the domain  # noqa: E501

        :param url: The url of this DomainInvitationCreate.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def code(self):
        """Gets the code of this DomainInvitationCreate.  # noqa: E501

        invitation code  # noqa: E501

        :return: The code of this DomainInvitationCreate.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DomainInvitationCreate.

        invitation code  # noqa: E501

        :param code: The code of this DomainInvitationCreate.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def expire_at(self):
        """Gets the expire_at of this DomainInvitationCreate.  # noqa: E501


        :return: The expire_at of this DomainInvitationCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        """Sets the expire_at of this DomainInvitationCreate.


        :param expire_at: The expire_at of this DomainInvitationCreate.  # noqa: E501
        :type: datetime
        """

        self._expire_at = expire_at

    @property
    def role(self):
        """Gets the role of this DomainInvitationCreate.  # noqa: E501

        domain role after invitation  # noqa: E501

        :return: The role of this DomainInvitationCreate.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DomainInvitationCreate.

        domain role after invitation  # noqa: E501

        :param role: The role of this DomainInvitationCreate.  # noqa: E501
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
        if issubclass(DomainInvitationCreate, dict):
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
        if not isinstance(other, DomainInvitationCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
