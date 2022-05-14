# coding: utf-8

"""
    JOJ Horse

    Git version: b3db0dc@2022-05-14T18:00:18Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Version(object):
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
        'version': 'str',
        'git': 'str'
    }

    attribute_map = {
        'version': 'version',
        'git': 'git'
    }

    def __init__(self, version=None, git=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._git = None
        self.discriminator = None
        self.version = version
        self.git = git

    @property
    def version(self):
        """Gets the version of this Version.  # noqa: E501


        :return: The version of this Version.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Version.


        :param version: The version of this Version.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def git(self):
        """Gets the git of this Version.  # noqa: E501


        :return: The git of this Version.  # noqa: E501
        :rtype: str
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this Version.


        :param git: The git of this Version.  # noqa: E501
        :type: str
        """
        if git is None:
            raise ValueError("Invalid value for `git`, must not be `None`")  # noqa: E501

        self._git = git

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
        if issubclass(Version, dict):
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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
