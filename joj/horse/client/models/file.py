# coding: utf-8

"""
    JOJ Horse

    Git version: f94044f@2021-07-13 06:06:59  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class File(object):
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
        'type': 'FileType',
        'path': 'str',
        'digest': 'str'
    }

    attribute_map = {
        'type': 'type',
        'path': 'path',
        'digest': 'digest'
    }

    def __init__(self, type=None, path=None, digest=None):  # noqa: E501
        """File - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._path = None
        self._digest = None
        self.discriminator = None
        self.type = type
        self.path = path
        self.digest = digest

    @property
    def type(self):
        """Gets the type of this File.  # noqa: E501


        :return: The type of this File.  # noqa: E501
        :rtype: FileType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this File.


        :param type: The type of this File.  # noqa: E501
        :type: FileType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def path(self):
        """Gets the path of this File.  # noqa: E501


        :return: The path of this File.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this File.


        :param path: The path of this File.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def digest(self):
        """Gets the digest of this File.  # noqa: E501


        :return: The digest of this File.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this File.


        :param digest: The digest of this File.  # noqa: E501
        :type: str
        """
        if digest is None:
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest

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
        if issubclass(File, dict):
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
        if not isinstance(other, File):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
