# coding: utf-8

"""
    JOJ Horse

    Git version: 6c53391@2022-05-07T19:36:22Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class JudgerCreate(object):
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
        'username': 'str',
        'password': 'str',
        'email': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'email': 'email'
    }

    def __init__(self, username=None, password=None, email=None):  # noqa: E501
        """JudgerCreate - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._password = None
        self._email = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if email is not None:
            self.email = email

    @property
    def username(self):
        """Gets the username of this JudgerCreate.  # noqa: E501


        :return: The username of this JudgerCreate.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this JudgerCreate.


        :param username: The username of this JudgerCreate.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this JudgerCreate.  # noqa: E501


        :return: The password of this JudgerCreate.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this JudgerCreate.


        :param password: The password of this JudgerCreate.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def email(self):
        """Gets the email of this JudgerCreate.  # noqa: E501


        :return: The email of this JudgerCreate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this JudgerCreate.


        :param email: The email of this JudgerCreate.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(JudgerCreate, dict):
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
        if not isinstance(other, JudgerCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
