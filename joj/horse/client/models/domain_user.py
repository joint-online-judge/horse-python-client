# coding: utf-8

"""
    JOJ Horse

    Git version: baceace@2021-11-05T20:56:21Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'role': 'str',
        'domain_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'role': 'role',
        'domain_id': 'domainId',
        'user_id': 'userId'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, role=None, domain_id=None, user_id=None):  # noqa: E501
        """DomainUser - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._role = None
        self._domain_id = None
        self._user_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.role = role
        self.domain_id = domain_id
        self.user_id = user_id

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
    def created_at(self):
        """Gets the created_at of this DomainUser.  # noqa: E501


        :return: The created_at of this DomainUser.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DomainUser.


        :param created_at: The created_at of this DomainUser.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DomainUser.  # noqa: E501


        :return: The updated_at of this DomainUser.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DomainUser.


        :param updated_at: The updated_at of this DomainUser.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
    def domain_id(self):
        """Gets the domain_id of this DomainUser.  # noqa: E501


        :return: The domain_id of this DomainUser.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DomainUser.


        :param domain_id: The domain_id of this DomainUser.  # noqa: E501
        :type: str
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")  # noqa: E501

        self._domain_id = domain_id

    @property
    def user_id(self):
        """Gets the user_id of this DomainUser.  # noqa: E501


        :return: The user_id of this DomainUser.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DomainUser.


        :param user_id: The user_id of this DomainUser.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
