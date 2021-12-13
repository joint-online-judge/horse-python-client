# coding: utf-8

"""
    JOJ Horse

    Git version: adca461@2021-12-13T17:05:38Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemSetAddProblem(object):
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
        'position': 'int',
        'problem': 'str'
    }

    attribute_map = {
        'position': 'position',
        'problem': 'problem'
    }

    def __init__(self, position=None, problem=None):  # noqa: E501
        """ProblemSetAddProblem - a model defined in Swagger"""  # noqa: E501
        self._position = None
        self._problem = None
        self.discriminator = None
        if position is not None:
            self.position = position
        self.problem = problem

    @property
    def position(self):
        """Gets the position of this ProblemSetAddProblem.  # noqa: E501

        the position of the problem in the problem set. if None, append to the end of the problems list.  # noqa: E501

        :return: The position of this ProblemSetAddProblem.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ProblemSetAddProblem.

        the position of the problem in the problem set. if None, append to the end of the problems list.  # noqa: E501

        :param position: The position of this ProblemSetAddProblem.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def problem(self):
        """Gets the problem of this ProblemSetAddProblem.  # noqa: E501

        url or id of the problem  # noqa: E501

        :return: The problem of this ProblemSetAddProblem.  # noqa: E501
        :rtype: str
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this ProblemSetAddProblem.

        url or id of the problem  # noqa: E501

        :param problem: The problem of this ProblemSetAddProblem.  # noqa: E501
        :type: str
        """
        if problem is None:
            raise ValueError("Invalid value for `problem`, must not be `None`")  # noqa: E501

        self._problem = problem

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
        if issubclass(ProblemSetAddProblem, dict):
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
        if not isinstance(other, ProblemSetAddProblem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
