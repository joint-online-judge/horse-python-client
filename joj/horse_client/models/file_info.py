# coding: utf-8

"""
    JOJ Horse

    Git version: 1ba9201@2022-03-06T09:39:13Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FileInfo(object):
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
        'is_dir': 'bool',
        'checksum': 'str',
        'mtime': 'AnyOfFileInfoMtime',
        'size_bytes': 'int'
    }

    attribute_map = {
        'path': 'path',
        'is_dir': 'is_dir',
        'checksum': 'checksum',
        'mtime': 'mtime',
        'size_bytes': 'size_bytes'
    }

    def __init__(self, path=None, is_dir=None, checksum=None, mtime=None, size_bytes=0):  # noqa: E501
        """FileInfo - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._is_dir = None
        self._checksum = None
        self._mtime = None
        self._size_bytes = None
        self.discriminator = None
        self.path = path
        self.is_dir = is_dir
        if checksum is not None:
            self.checksum = checksum
        if mtime is not None:
            self.mtime = mtime
        if size_bytes is not None:
            self.size_bytes = size_bytes

    @property
    def path(self):
        """Gets the path of this FileInfo.  # noqa: E501


        :return: The path of this FileInfo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileInfo.


        :param path: The path of this FileInfo.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def is_dir(self):
        """Gets the is_dir of this FileInfo.  # noqa: E501


        :return: The is_dir of this FileInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_dir

    @is_dir.setter
    def is_dir(self, is_dir):
        """Sets the is_dir of this FileInfo.


        :param is_dir: The is_dir of this FileInfo.  # noqa: E501
        :type: bool
        """
        if is_dir is None:
            raise ValueError("Invalid value for `is_dir`, must not be `None`")  # noqa: E501

        self._is_dir = is_dir

    @property
    def checksum(self):
        """Gets the checksum of this FileInfo.  # noqa: E501


        :return: The checksum of this FileInfo.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this FileInfo.


        :param checksum: The checksum of this FileInfo.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def mtime(self):
        """Gets the mtime of this FileInfo.  # noqa: E501


        :return: The mtime of this FileInfo.  # noqa: E501
        :rtype: AnyOfFileInfoMtime
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """Sets the mtime of this FileInfo.


        :param mtime: The mtime of this FileInfo.  # noqa: E501
        :type: AnyOfFileInfoMtime
        """

        self._mtime = mtime

    @property
    def size_bytes(self):
        """Gets the size_bytes of this FileInfo.  # noqa: E501


        :return: The size_bytes of this FileInfo.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this FileInfo.


        :param size_bytes: The size_bytes of this FileInfo.  # noqa: E501
        :type: int
        """

        self._size_bytes = size_bytes

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
        if issubclass(FileInfo, dict):
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
        if not isinstance(other, FileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
