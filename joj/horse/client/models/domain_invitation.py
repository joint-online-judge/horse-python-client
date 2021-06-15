# coding: utf-8

"""
    JOJ Horse

    Git version: 5c38b66@2021-06-15 12:19:18  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainInvitation(object):
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
        'id': 'str',
        'code': 'str',
        'expire_at': 'datetime',
        'role': 'str',
        'domain': 'AnyOfDomainInvitationDomain'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'expire_at': 'expire_at',
        'role': 'role',
        'domain': 'domain'
    }

    def __init__(self, id=None, code='', expire_at=None, role='user', domain=None):  # noqa: E501
        """DomainInvitation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._code = None
        self._expire_at = None
        self._role = None
        self._domain = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if expire_at is not None:
            self.expire_at = expire_at
        if role is not None:
            self.role = role
        self.domain = domain

    @property
    def id(self):
        """Gets the id of this DomainInvitation.  # noqa: E501


        :return: The id of this DomainInvitation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainInvitation.


        :param id: The id of this DomainInvitation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this DomainInvitation.  # noqa: E501

        invitation code  # noqa: E501

        :return: The code of this DomainInvitation.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DomainInvitation.

        invitation code  # noqa: E501

        :param code: The code of this DomainInvitation.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def expire_at(self):
        """Gets the expire_at of this DomainInvitation.  # noqa: E501

        expire time of invitation  # noqa: E501

        :return: The expire_at of this DomainInvitation.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        """Sets the expire_at of this DomainInvitation.

        expire time of invitation  # noqa: E501

        :param expire_at: The expire_at of this DomainInvitation.  # noqa: E501
        :type: datetime
        """

        self._expire_at = expire_at

    @property
    def role(self):
        """Gets the role of this DomainInvitation.  # noqa: E501

        domain role after invitation  # noqa: E501

        :return: The role of this DomainInvitation.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DomainInvitation.

        domain role after invitation  # noqa: E501

        :param role: The role of this DomainInvitation.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def domain(self):
        """Gets the domain of this DomainInvitation.  # noqa: E501


        :return: The domain of this DomainInvitation.  # noqa: E501
        :rtype: AnyOfDomainInvitationDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DomainInvitation.


        :param domain: The domain of this DomainInvitation.  # noqa: E501
        :type: AnyOfDomainInvitationDomain
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

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
        if issubclass(DomainInvitation, dict):
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
        if not isinstance(other, DomainInvitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other