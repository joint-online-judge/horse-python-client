# coding: utf-8

"""
    JOJ Horse

    Git version: ed0122c@2022-05-12T03:18:43Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AuthTokens(object):
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
        'access_token': 'str',
        'refresh_token': 'str',
        'token_type': 'str'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'refresh_token': 'refreshToken',
        'token_type': 'tokenType'
    }

    def __init__(self, access_token=None, refresh_token=None, token_type=None):  # noqa: E501
        """AuthTokens - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._refresh_token = None
        self._token_type = None
        self.discriminator = None
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_type = token_type

    @property
    def access_token(self):
        """Gets the access_token of this AuthTokens.  # noqa: E501


        :return: The access_token of this AuthTokens.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this AuthTokens.


        :param access_token: The access_token of this AuthTokens.  # noqa: E501
        :type: str
        """
        if access_token is None:
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this AuthTokens.  # noqa: E501


        :return: The refresh_token of this AuthTokens.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this AuthTokens.


        :param refresh_token: The refresh_token of this AuthTokens.  # noqa: E501
        :type: str
        """
        if refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")  # noqa: E501

        self._refresh_token = refresh_token

    @property
    def token_type(self):
        """Gets the token_type of this AuthTokens.  # noqa: E501


        :return: The token_type of this AuthTokens.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this AuthTokens.


        :param token_type: The token_type of this AuthTokens.  # noqa: E501
        :type: str
        """
        if token_type is None:
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501

        self._token_type = token_type

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
        if issubclass(AuthTokens, dict):
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
        if not isinstance(other, AuthTokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
