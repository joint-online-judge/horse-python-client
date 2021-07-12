# coding: utf-8

"""
    JOJ Horse

    Git version: d47939f@2021-07-12 17:53:41  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainUser(object):
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
        'domain': 'AnyOfDomainUserDomain',
        'user': 'AnyOfDomainUserUser',
        'role': 'str',
        'join_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'domain': 'domain',
        'user': 'user',
        'role': 'role',
        'join_at': 'join_at'
    }

    def __init__(self, id=None, domain=None, user=None, role=None, join_at=None):  # noqa: E501
        """DomainUser - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._domain = None
        self._user = None
        self._role = None
        self._join_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.domain = domain
        self.user = user
        self.role = role
        if join_at is not None:
            self.join_at = join_at

    @property
    def id(self):
        """Gets the id of this DomainUser.  # noqa: E501


        :return: The id of this DomainUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainUser.


        :param id: The id of this DomainUser.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def domain(self):
        """Gets the domain of this DomainUser.  # noqa: E501


        :return: The domain of this DomainUser.  # noqa: E501
        :rtype: AnyOfDomainUserDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DomainUser.


        :param domain: The domain of this DomainUser.  # noqa: E501
        :type: AnyOfDomainUserDomain
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def user(self):
        """Gets the user of this DomainUser.  # noqa: E501


        :return: The user of this DomainUser.  # noqa: E501
        :rtype: AnyOfDomainUserUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DomainUser.


        :param user: The user of this DomainUser.  # noqa: E501
        :type: AnyOfDomainUserUser
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def role(self):
        """Gets the role of this DomainUser.  # noqa: E501


        :return: The role of this DomainUser.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DomainUser.


        :param role: The role of this DomainUser.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def join_at(self):
        """Gets the join_at of this DomainUser.  # noqa: E501


        :return: The join_at of this DomainUser.  # noqa: E501
        :rtype: datetime
        """
        return self._join_at

    @join_at.setter
    def join_at(self, join_at):
        """Sets the join_at of this DomainUser.


        :param join_at: The join_at of this DomainUser.  # noqa: E501
        :type: datetime
        """

        self._join_at = join_at

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
        if issubclass(DomainUser, dict):
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
        if not isinstance(other, DomainUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
