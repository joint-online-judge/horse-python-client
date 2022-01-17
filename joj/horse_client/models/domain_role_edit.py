# coding: utf-8

"""
    JOJ Horse

    Git version: eaa141a@2022-01-17T16:33:07Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainRoleEdit(object):
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
        'permission': 'object'
    }

    attribute_map = {
        'role': 'role',
        'permission': 'permission'
    }

    def __init__(self, role=None, permission=None):  # noqa: E501
        """DomainRoleEdit - a model defined in Swagger"""  # noqa: E501
        self._role = None
        self._permission = None
        self.discriminator = None
        if role is not None:
            self.role = role
        if permission is not None:
            self.permission = permission

    @property
    def role(self):
        """Gets the role of this DomainRoleEdit.  # noqa: E501

        New role name  # noqa: E501

        :return: The role of this DomainRoleEdit.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DomainRoleEdit.

        New role name  # noqa: E501

        :param role: The role of this DomainRoleEdit.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def permission(self):
        """Gets the permission of this DomainRoleEdit.  # noqa: E501

        The permission which needs to be updated  # noqa: E501

        :return: The permission of this DomainRoleEdit.  # noqa: E501
        :rtype: object
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this DomainRoleEdit.

        The permission which needs to be updated  # noqa: E501

        :param permission: The permission of this DomainRoleEdit.  # noqa: E501
        :type: object
        """

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
        if issubclass(DomainRoleEdit, dict):
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
        if not isinstance(other, DomainRoleEdit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
