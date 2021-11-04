# coding: utf-8

"""
    JOJ Horse

    Git version: 3474762@2021-11-04T11:53:49Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BodyLoginApiV1AuthLoginPost(object):
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
        'grant_type': 'str',
        'username': 'str',
        'password': 'str',
        'scope': 'str',
        'client_id': 'str',
        'client_secret': 'str'
    }

    attribute_map = {
        'grant_type': 'grant_type',
        'username': 'username',
        'password': 'password',
        'scope': 'scope',
        'client_id': 'client_id',
        'client_secret': 'client_secret'
    }

    def __init__(self, grant_type=None, username=None, password=None, scope='', client_id=None, client_secret=None):  # noqa: E501
        """BodyLoginApiV1AuthLoginPost - a model defined in Swagger"""  # noqa: E501
        self._grant_type = None
        self._username = None
        self._password = None
        self._scope = None
        self._client_id = None
        self._client_secret = None
        self.discriminator = None
        if grant_type is not None:
            self.grant_type = grant_type
        self.username = username
        self.password = password
        if scope is not None:
            self.scope = scope
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret

    @property
    def grant_type(self):
        """Gets the grant_type of this BodyLoginApiV1AuthLoginPost.  # noqa: E501


        :return: The grant_type of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this BodyLoginApiV1AuthLoginPost.


        :param grant_type: The grant_type of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :type: str
        """

        self._grant_type = grant_type

    @property
    def username(self):
        """Gets the username of this BodyLoginApiV1AuthLoginPost.  # noqa: E501


        :return: The username of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this BodyLoginApiV1AuthLoginPost.


        :param username: The username of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this BodyLoginApiV1AuthLoginPost.  # noqa: E501


        :return: The password of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this BodyLoginApiV1AuthLoginPost.


        :param password: The password of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def scope(self):
        """Gets the scope of this BodyLoginApiV1AuthLoginPost.  # noqa: E501


        :return: The scope of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this BodyLoginApiV1AuthLoginPost.


        :param scope: The scope of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def client_id(self):
        """Gets the client_id of this BodyLoginApiV1AuthLoginPost.  # noqa: E501


        :return: The client_id of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this BodyLoginApiV1AuthLoginPost.


        :param client_id: The client_id of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this BodyLoginApiV1AuthLoginPost.  # noqa: E501


        :return: The client_secret of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this BodyLoginApiV1AuthLoginPost.


        :param client_secret: The client_secret of this BodyLoginApiV1AuthLoginPost.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

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
        if issubclass(BodyLoginApiV1AuthLoginPost, dict):
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
        if not isinstance(other, BodyLoginApiV1AuthLoginPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
