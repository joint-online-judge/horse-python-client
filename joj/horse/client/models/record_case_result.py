# coding: utf-8

"""
    JOJ Horse

    Git version: 335bcde@2021-07-15 17:24:35  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RecordCaseResult(object):
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
        'index': 'int',
        'result': 'RecordCase'
    }

    attribute_map = {
        'index': 'index',
        'result': 'result'
    }

    def __init__(self, index=None, result=None):  # noqa: E501
        """RecordCaseResult - a model defined in Swagger"""  # noqa: E501
        self._index = None
        self._result = None
        self.discriminator = None
        self.index = index
        self.result = result

    @property
    def index(self):
        """Gets the index of this RecordCaseResult.  # noqa: E501


        :return: The index of this RecordCaseResult.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this RecordCaseResult.


        :param index: The index of this RecordCaseResult.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def result(self):
        """Gets the result of this RecordCaseResult.  # noqa: E501


        :return: The result of this RecordCaseResult.  # noqa: E501
        :rtype: RecordCase
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RecordCaseResult.


        :param result: The result of this RecordCaseResult.  # noqa: E501
        :type: RecordCase
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

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
        if issubclass(RecordCaseResult, dict):
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
        if not isinstance(other, RecordCaseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
