# coding: utf-8

"""
    JOJ Horse

    Git version: e2e4bb0@2021-11-27T11:37:00Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ScoreBoard(object):
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
        'problem_ids': 'list[str]',
        'results': 'list[UserScore]'
    }

    attribute_map = {
        'problem_ids': 'problemIds',
        'results': 'results'
    }

    def __init__(self, problem_ids=None, results=None):  # noqa: E501
        """ScoreBoard - a model defined in Swagger"""  # noqa: E501
        self._problem_ids = None
        self._results = None
        self.discriminator = None
        self.problem_ids = problem_ids
        self.results = results

    @property
    def problem_ids(self):
        """Gets the problem_ids of this ScoreBoard.  # noqa: E501


        :return: The problem_ids of this ScoreBoard.  # noqa: E501
        :rtype: list[str]
        """
        return self._problem_ids

    @problem_ids.setter
    def problem_ids(self, problem_ids):
        """Sets the problem_ids of this ScoreBoard.


        :param problem_ids: The problem_ids of this ScoreBoard.  # noqa: E501
        :type: list[str]
        """
        if problem_ids is None:
            raise ValueError("Invalid value for `problem_ids`, must not be `None`")  # noqa: E501

        self._problem_ids = problem_ids

    @property
    def results(self):
        """Gets the results of this ScoreBoard.  # noqa: E501


        :return: The results of this ScoreBoard.  # noqa: E501
        :rtype: list[UserScore]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ScoreBoard.


        :param results: The results of this ScoreBoard.  # noqa: E501
        :type: list[UserScore]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if issubclass(ScoreBoard, dict):
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
        if not isinstance(other, ScoreBoard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
