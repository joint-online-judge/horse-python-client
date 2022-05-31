# coding: utf-8

"""
    JOJ Horse

    Git version: d3f6f67@2022-05-31T04:21:08Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Diff(object):
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
        'type': 'DiffTypeEnum',
        'path': 'str',
        'path_type': 'PathTypeEnum',
        'size_bytes': 'int'
    }

    attribute_map = {
        'type': 'type',
        'path': 'path',
        'path_type': 'path_type',
        'size_bytes': 'size_bytes'
    }

    def __init__(self, type=None, path=None, path_type=None, size_bytes=None):  # noqa: E501
        """Diff - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._path = None
        self._path_type = None
        self._size_bytes = None
        self.discriminator = None
        self.type = type
        self.path = path
        self.path_type = path_type
        if size_bytes is not None:
            self.size_bytes = size_bytes

    @property
    def type(self):
        """Gets the type of this Diff.  # noqa: E501


        :return: The type of this Diff.  # noqa: E501
        :rtype: DiffTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Diff.


        :param type: The type of this Diff.  # noqa: E501
        :type: DiffTypeEnum
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def path(self):
        """Gets the path of this Diff.  # noqa: E501


        :return: The path of this Diff.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Diff.


        :param path: The path of this Diff.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def path_type(self):
        """Gets the path_type of this Diff.  # noqa: E501


        :return: The path_type of this Diff.  # noqa: E501
        :rtype: PathTypeEnum
        """
        return self._path_type

    @path_type.setter
    def path_type(self, path_type):
        """Sets the path_type of this Diff.


        :param path_type: The path_type of this Diff.  # noqa: E501
        :type: PathTypeEnum
        """
        if path_type is None:
            raise ValueError("Invalid value for `path_type`, must not be `None`")  # noqa: E501

        self._path_type = path_type

    @property
    def size_bytes(self):
        """Gets the size_bytes of this Diff.  # noqa: E501


        :return: The size_bytes of this Diff.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this Diff.


        :param size_bytes: The size_bytes of this Diff.  # noqa: E501
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
        if issubclass(Diff, dict):
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
        if not isinstance(other, Diff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
