# coding: utf-8

"""
    JOJ Horse

    Git version: 3deba0b@2022-06-02T14:50:42Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class JudgerDetail(object):
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
        'role': 'str',
        'is_active': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'is_alive': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'gravatar': 'gravatar',
        'role': 'role',
        'is_active': 'isActive',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'is_alive': 'isAlive'
    }

    def __init__(self, id=None, username=None, gravatar='', role='user', is_active=False, created_at=None, updated_at=None, is_alive=None):  # noqa: E501
        """JudgerDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._gravatar = None
        self._role = None
        self._is_active = None
        self._created_at = None
        self._updated_at = None
        self._is_alive = None
        self.discriminator = None
        self.id = id
        self.username = username
        if gravatar is not None:
            self.gravatar = gravatar
        if role is not None:
            self.role = role
        if is_active is not None:
            self.is_active = is_active
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.is_alive = is_alive

    @property
    def id(self):
        """Gets the id of this JudgerDetail.  # noqa: E501


        :return: The id of this JudgerDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JudgerDetail.


        :param id: The id of this JudgerDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this JudgerDetail.  # noqa: E501


        :return: The username of this JudgerDetail.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this JudgerDetail.


        :param username: The username of this JudgerDetail.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def gravatar(self):
        """Gets the gravatar of this JudgerDetail.  # noqa: E501


        :return: The gravatar of this JudgerDetail.  # noqa: E501
        :rtype: str
        """
        return self._gravatar

    @gravatar.setter
    def gravatar(self, gravatar):
        """Sets the gravatar of this JudgerDetail.


        :param gravatar: The gravatar of this JudgerDetail.  # noqa: E501
        :type: str
        """

        self._gravatar = gravatar

    @property
    def role(self):
        """Gets the role of this JudgerDetail.  # noqa: E501


        :return: The role of this JudgerDetail.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this JudgerDetail.


        :param role: The role of this JudgerDetail.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def is_active(self):
        """Gets the is_active of this JudgerDetail.  # noqa: E501


        :return: The is_active of this JudgerDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this JudgerDetail.


        :param is_active: The is_active of this JudgerDetail.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def created_at(self):
        """Gets the created_at of this JudgerDetail.  # noqa: E501


        :return: The created_at of this JudgerDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this JudgerDetail.


        :param created_at: The created_at of this JudgerDetail.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this JudgerDetail.  # noqa: E501


        :return: The updated_at of this JudgerDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this JudgerDetail.


        :param updated_at: The updated_at of this JudgerDetail.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def is_alive(self):
        """Gets the is_alive of this JudgerDetail.  # noqa: E501


        :return: The is_alive of this JudgerDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        """Sets the is_alive of this JudgerDetail.


        :param is_alive: The is_alive of this JudgerDetail.  # noqa: E501
        :type: bool
        """
        if is_alive is None:
            raise ValueError("Invalid value for `is_alive`, must not be `None`")  # noqa: E501

        self._is_alive = is_alive

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
        if issubclass(JudgerDetail, dict):
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
        if not isinstance(other, JudgerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
