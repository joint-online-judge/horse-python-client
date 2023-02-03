# coding: utf-8

"""
    JOJ Horse

    Git version: c5741c9@2023-02-03T15:02:34Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OAuth2Client(object):
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
        'oauth_name': 'str',
        'display_name': 'str',
        'icon': 'str'
    }

    attribute_map = {
        'oauth_name': 'oauthName',
        'display_name': 'displayName',
        'icon': 'icon'
    }

    def __init__(self, oauth_name=None, display_name=None, icon=None):  # noqa: E501
        """OAuth2Client - a model defined in Swagger"""  # noqa: E501
        self._oauth_name = None
        self._display_name = None
        self._icon = None
        self.discriminator = None
        self.oauth_name = oauth_name
        self.display_name = display_name
        self.icon = icon

    @property
    def oauth_name(self):
        """Gets the oauth_name of this OAuth2Client.  # noqa: E501


        :return: The oauth_name of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._oauth_name

    @oauth_name.setter
    def oauth_name(self, oauth_name):
        """Sets the oauth_name of this OAuth2Client.


        :param oauth_name: The oauth_name of this OAuth2Client.  # noqa: E501
        :type: str
        """
        if oauth_name is None:
            raise ValueError("Invalid value for `oauth_name`, must not be `None`")  # noqa: E501

        self._oauth_name = oauth_name

    @property
    def display_name(self):
        """Gets the display_name of this OAuth2Client.  # noqa: E501


        :return: The display_name of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this OAuth2Client.


        :param display_name: The display_name of this OAuth2Client.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def icon(self):
        """Gets the icon of this OAuth2Client.  # noqa: E501


        :return: The icon of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this OAuth2Client.


        :param icon: The icon of this OAuth2Client.  # noqa: E501
        :type: str
        """
        if icon is None:
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501

        self._icon = icon

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
        if issubclass(OAuth2Client, dict):
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
        if not isinstance(other, OAuth2Client):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
