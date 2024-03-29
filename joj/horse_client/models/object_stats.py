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

class ObjectStats(object):
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
        'path': 'str',
        'path_type': 'PathTypeEnum',
        'checksum': 'str',
        'size_bytes': 'int',
        'mtime': 'int',
        'content_type': 'str'
    }

    attribute_map = {
        'path': 'path',
        'path_type': 'path_type',
        'checksum': 'checksum',
        'size_bytes': 'size_bytes',
        'mtime': 'mtime',
        'content_type': 'content_type'
    }

    def __init__(self, path=None, path_type=None, checksum=None, size_bytes=None, mtime=None, content_type=None):  # noqa: E501
        """ObjectStats - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._path_type = None
        self._checksum = None
        self._size_bytes = None
        self._mtime = None
        self._content_type = None
        self.discriminator = None
        self.path = path
        self.path_type = path_type
        self.checksum = checksum
        if size_bytes is not None:
            self.size_bytes = size_bytes
        self.mtime = mtime
        if content_type is not None:
            self.content_type = content_type

    @property
    def path(self):
        """Gets the path of this ObjectStats.  # noqa: E501


        :return: The path of this ObjectStats.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ObjectStats.


        :param path: The path of this ObjectStats.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def path_type(self):
        """Gets the path_type of this ObjectStats.  # noqa: E501


        :return: The path_type of this ObjectStats.  # noqa: E501
        :rtype: PathTypeEnum
        """
        return self._path_type

    @path_type.setter
    def path_type(self, path_type):
        """Sets the path_type of this ObjectStats.


        :param path_type: The path_type of this ObjectStats.  # noqa: E501
        :type: PathTypeEnum
        """
        if path_type is None:
            raise ValueError("Invalid value for `path_type`, must not be `None`")  # noqa: E501

        self._path_type = path_type

    @property
    def checksum(self):
        """Gets the checksum of this ObjectStats.  # noqa: E501


        :return: The checksum of this ObjectStats.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this ObjectStats.


        :param checksum: The checksum of this ObjectStats.  # noqa: E501
        :type: str
        """
        if checksum is None:
            raise ValueError("Invalid value for `checksum`, must not be `None`")  # noqa: E501

        self._checksum = checksum

    @property
    def size_bytes(self):
        """Gets the size_bytes of this ObjectStats.  # noqa: E501


        :return: The size_bytes of this ObjectStats.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this ObjectStats.


        :param size_bytes: The size_bytes of this ObjectStats.  # noqa: E501
        :type: int
        """

        self._size_bytes = size_bytes

    @property
    def mtime(self):
        """Gets the mtime of this ObjectStats.  # noqa: E501


        :return: The mtime of this ObjectStats.  # noqa: E501
        :rtype: int
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """Sets the mtime of this ObjectStats.


        :param mtime: The mtime of this ObjectStats.  # noqa: E501
        :type: int
        """
        if mtime is None:
            raise ValueError("Invalid value for `mtime`, must not be `None`")  # noqa: E501

        self._mtime = mtime

    @property
    def content_type(self):
        """Gets the content_type of this ObjectStats.  # noqa: E501


        :return: The content_type of this ObjectStats.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ObjectStats.


        :param content_type: The content_type of this ObjectStats.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

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
        if issubclass(ObjectStats, dict):
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
        if not isinstance(other, ObjectStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
