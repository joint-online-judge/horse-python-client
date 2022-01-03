# coding: utf-8

"""
    JOJ Horse

    Git version: 3bf3d9e@2022-01-03T17:46:04Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemSolutionSubmit(object):
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
        'code_type': 'RecordCodeType',
        'file': 'str'
    }

    attribute_map = {
        'code_type': 'codeType',
        'file': 'file'
    }

    def __init__(self, code_type=None, file=None):  # noqa: E501
        """ProblemSolutionSubmit - a model defined in Swagger"""  # noqa: E501
        self._code_type = None
        self._file = None
        self.discriminator = None
        self.code_type = code_type
        if file is not None:
            self.file = file

    @property
    def code_type(self):
        """Gets the code_type of this ProblemSolutionSubmit.  # noqa: E501


        :return: The code_type of this ProblemSolutionSubmit.  # noqa: E501
        :rtype: RecordCodeType
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this ProblemSolutionSubmit.


        :param code_type: The code_type of this ProblemSolutionSubmit.  # noqa: E501
        :type: RecordCodeType
        """
        if code_type is None:
            raise ValueError("Invalid value for `code_type`, must not be `None`")  # noqa: E501

        self._code_type = code_type

    @property
    def file(self):
        """Gets the file of this ProblemSolutionSubmit.  # noqa: E501


        :return: The file of this ProblemSolutionSubmit.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ProblemSolutionSubmit.


        :param file: The file of this ProblemSolutionSubmit.  # noqa: E501
        :type: str
        """

        self._file = file

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
        if issubclass(ProblemSolutionSubmit, dict):
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
        if not isinstance(other, ProblemSolutionSubmit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
