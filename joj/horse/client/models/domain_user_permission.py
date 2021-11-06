# coding: utf-8

"""
    JOJ Horse

    Git version: 6e9f2ca@2021-11-06T09:28:18Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainUserPermission(object):
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
        'domain_user': 'DomainUser',
        'permission': 'DomainPermission'
    }

    attribute_map = {
        'domain_user': 'domainUser',
        'permission': 'permission'
    }

    def __init__(self, domain_user=None, permission=None):  # noqa: E501
        """DomainUserPermission - a model defined in Swagger"""  # noqa: E501
        self._domain_user = None
        self._permission = None
        self.discriminator = None
        self.domain_user = domain_user
        self.permission = permission

    @property
    def domain_user(self):
        """Gets the domain_user of this DomainUserPermission.  # noqa: E501


        :return: The domain_user of this DomainUserPermission.  # noqa: E501
        :rtype: DomainUser
        """
        return self._domain_user

    @domain_user.setter
    def domain_user(self, domain_user):
        """Sets the domain_user of this DomainUserPermission.


        :param domain_user: The domain_user of this DomainUserPermission.  # noqa: E501
        :type: DomainUser
        """
        if domain_user is None:
            raise ValueError("Invalid value for `domain_user`, must not be `None`")  # noqa: E501

        self._domain_user = domain_user

    @property
    def permission(self):
        """Gets the permission of this DomainUserPermission.  # noqa: E501


        :return: The permission of this DomainUserPermission.  # noqa: E501
        :rtype: DomainPermission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this DomainUserPermission.


        :param permission: The permission of this DomainUserPermission.  # noqa: E501
        :type: DomainPermission
        """
        if permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501

        self._permission = permission

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
        if issubclass(DomainUserPermission, dict):
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
        if not isinstance(other, DomainUserPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
