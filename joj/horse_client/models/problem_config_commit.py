# coding: utf-8

"""
    JOJ Horse

    Git version: b343911@2022-05-10T10:42:09Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemConfigCommit(object):
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
        'message': 'str',
        'data_version': 'int'
    }

    attribute_map = {
        'message': 'message',
        'data_version': 'dataVersion'
    }

    def __init__(self, message='', data_version=2):  # noqa: E501
        """ProblemConfigCommit - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._data_version = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if data_version is not None:
            self.data_version = data_version

    @property
    def message(self):
        """Gets the message of this ProblemConfigCommit.  # noqa: E501


        :return: The message of this ProblemConfigCommit.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ProblemConfigCommit.


        :param message: The message of this ProblemConfigCommit.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def data_version(self):
        """Gets the data_version of this ProblemConfigCommit.  # noqa: E501


        :return: The data_version of this ProblemConfigCommit.  # noqa: E501
        :rtype: int
        """
        return self._data_version

    @data_version.setter
    def data_version(self, data_version):
        """Sets the data_version of this ProblemConfigCommit.


        :param data_version: The data_version of this ProblemConfigCommit.  # noqa: E501
        :type: int
        """

        self._data_version = data_version

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
        if issubclass(ProblemConfigCommit, dict):
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
        if not isinstance(other, ProblemConfigCommit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
