# coding: utf-8

"""
    JOJ Horse

    Git version: 0ae99f8@2023-02-03T06:54:51Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserCreate(object):
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
        'email': 'str',
        'oauth_name': 'str',
        'oauth_account_id': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'email': 'email',
        'oauth_name': 'oauth_name',
        'oauth_account_id': 'oauth_account_id'
    }

    def __init__(self, username=None, password=None, email=None, oauth_name=None, oauth_account_id=None):  # noqa: E501
        """UserCreate - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._password = None
        self._email = None
        self._oauth_name = None
        self._oauth_account_id = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
        if oauth_name is not None:
            self.oauth_name = oauth_name
        if oauth_account_id is not None:
            self.oauth_account_id = oauth_account_id

    @property
    def username(self):
        """Gets the username of this UserCreate.  # noqa: E501


        :return: The username of this UserCreate.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserCreate.


        :param username: The username of this UserCreate.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this UserCreate.  # noqa: E501


        :return: The password of this UserCreate.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserCreate.


        :param password: The password of this UserCreate.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def email(self):
        """Gets the email of this UserCreate.  # noqa: E501


        :return: The email of this UserCreate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserCreate.


        :param email: The email of this UserCreate.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def oauth_name(self):
        """Gets the oauth_name of this UserCreate.  # noqa: E501


        :return: The oauth_name of this UserCreate.  # noqa: E501
        :rtype: str
        """
        return self._oauth_name

    @oauth_name.setter
    def oauth_name(self, oauth_name):
        """Sets the oauth_name of this UserCreate.


        :param oauth_name: The oauth_name of this UserCreate.  # noqa: E501
        :type: str
        """

        self._oauth_name = oauth_name

    @property
    def oauth_account_id(self):
        """Gets the oauth_account_id of this UserCreate.  # noqa: E501


        :return: The oauth_account_id of this UserCreate.  # noqa: E501
        :rtype: str
        """
        return self._oauth_account_id

    @oauth_account_id.setter
    def oauth_account_id(self, oauth_account_id):
        """Sets the oauth_account_id of this UserCreate.


        :param oauth_account_id: The oauth_account_id of this UserCreate.  # noqa: E501
        :type: str
        """

        self._oauth_account_id = oauth_account_id

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
        if issubclass(UserCreate, dict):
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
        if not isinstance(other, UserCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
