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

class DomainRole(object):
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
        'role': 'str',
        'permission': 'object',
        'updated_at': 'datetime',
        'domain': 'AnyOfDomainRoleDomain'
    }

    attribute_map = {
        'id': 'id',
        'role': 'role',
        'permission': 'permission',
        'updated_at': 'updated_at',
        'domain': 'domain'
    }

    def __init__(self, id=None, role=None, permission=None, updated_at=None, domain=None):  # noqa: E501
        """DomainRole - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._role = None
        self._permission = None
        self._updated_at = None
        self._domain = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.role = role
        if permission is not None:
            self.permission = permission
        if updated_at is not None:
            self.updated_at = updated_at
        self.domain = domain

    @property
    def id(self):
        """Gets the id of this DomainRole.  # noqa: E501


        :return: The id of this DomainRole.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainRole.


        :param id: The id of this DomainRole.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def role(self):
        """Gets the role of this DomainRole.  # noqa: E501


        :return: The role of this DomainRole.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DomainRole.


        :param role: The role of this DomainRole.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def permission(self):
        """Gets the permission of this DomainRole.  # noqa: E501


        :return: The permission of this DomainRole.  # noqa: E501
        :rtype: object
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this DomainRole.


        :param permission: The permission of this DomainRole.  # noqa: E501
        :type: object
        """

        self._permission = permission

    @property
    def updated_at(self):
        """Gets the updated_at of this DomainRole.  # noqa: E501


        :return: The updated_at of this DomainRole.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DomainRole.


        :param updated_at: The updated_at of this DomainRole.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def domain(self):
        """Gets the domain of this DomainRole.  # noqa: E501


        :return: The domain of this DomainRole.  # noqa: E501
        :rtype: AnyOfDomainRoleDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DomainRole.


        :param domain: The domain of this DomainRole.  # noqa: E501
        :type: AnyOfDomainRoleDomain
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
        if issubclass(DomainRole, dict):
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
        if not isinstance(other, DomainRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
