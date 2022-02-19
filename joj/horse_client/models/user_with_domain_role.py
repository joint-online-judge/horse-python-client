# coding: utf-8

"""
    JOJ Horse

    Git version: abfa91b@2022-02-19T13:35:45Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserWithDomainRole(object):
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
        'username': 'str',
        'gravatar': 'str',
        'domain_id': 'str',
        'domain_role': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'gravatar': 'gravatar',
        'domain_id': 'domainId',
        'domain_role': 'domainRole'
    }

    def __init__(self, id=None, username=None, gravatar='', domain_id=None, domain_role=None):  # noqa: E501
        """UserWithDomainRole - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._gravatar = None
        self._domain_id = None
        self._domain_role = None
        self.discriminator = None
        self.id = id
        self.username = username
        if gravatar is not None:
            self.gravatar = gravatar
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_role is not None:
            self.domain_role = domain_role

    @property
    def id(self):
        """Gets the id of this UserWithDomainRole.  # noqa: E501


        :return: The id of this UserWithDomainRole.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserWithDomainRole.


        :param id: The id of this UserWithDomainRole.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this UserWithDomainRole.  # noqa: E501


        :return: The username of this UserWithDomainRole.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserWithDomainRole.


        :param username: The username of this UserWithDomainRole.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def gravatar(self):
        """Gets the gravatar of this UserWithDomainRole.  # noqa: E501


        :return: The gravatar of this UserWithDomainRole.  # noqa: E501
        :rtype: str
        """
        return self._gravatar

    @gravatar.setter
    def gravatar(self, gravatar):
        """Sets the gravatar of this UserWithDomainRole.


        :param gravatar: The gravatar of this UserWithDomainRole.  # noqa: E501
        :type: str
        """

        self._gravatar = gravatar

    @property
    def domain_id(self):
        """Gets the domain_id of this UserWithDomainRole.  # noqa: E501


        :return: The domain_id of this UserWithDomainRole.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this UserWithDomainRole.


        :param domain_id: The domain_id of this UserWithDomainRole.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def domain_role(self):
        """Gets the domain_role of this UserWithDomainRole.  # noqa: E501


        :return: The domain_role of this UserWithDomainRole.  # noqa: E501
        :rtype: str
        """
        return self._domain_role

    @domain_role.setter
    def domain_role(self, domain_role):
        """Sets the domain_role of this UserWithDomainRole.


        :param domain_role: The domain_role of this UserWithDomainRole.  # noqa: E501
        :type: str
        """

        self._domain_role = domain_role

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
        if issubclass(UserWithDomainRole, dict):
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
        if not isinstance(other, UserWithDomainRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
