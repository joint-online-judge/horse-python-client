# coding: utf-8

"""
    JOJ Horse

    Git version: 16b8c55@2021-11-30T10:39:35Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemClone(object):
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
        'problems': 'list[str]',
        'problem_set': 'str',
        'new_group': 'bool'
    }

    attribute_map = {
        'problems': 'problems',
        'problem_set': 'problemSet',
        'new_group': 'newGroup'
    }

    def __init__(self, problems=None, problem_set=None, new_group=False):  # noqa: E501
        """ProblemClone - a model defined in Swagger"""  # noqa: E501
        self._problems = None
        self._problem_set = None
        self._new_group = None
        self.discriminator = None
        self.problems = problems
        self.problem_set = problem_set
        if new_group is not None:
            self.new_group = new_group

    @property
    def problems(self):
        """Gets the problems of this ProblemClone.  # noqa: E501


        :return: The problems of this ProblemClone.  # noqa: E501
        :rtype: list[str]
        """
        return self._problems

    @problems.setter
    def problems(self, problems):
        """Sets the problems of this ProblemClone.


        :param problems: The problems of this ProblemClone.  # noqa: E501
        :type: list[str]
        """
        if problems is None:
            raise ValueError("Invalid value for `problems`, must not be `None`")  # noqa: E501

        self._problems = problems

    @property
    def problem_set(self):
        """Gets the problem_set of this ProblemClone.  # noqa: E501

        url or id of the problem set  # noqa: E501

        :return: The problem_set of this ProblemClone.  # noqa: E501
        :rtype: str
        """
        return self._problem_set

    @problem_set.setter
    def problem_set(self, problem_set):
        """Sets the problem_set of this ProblemClone.

        url or id of the problem set  # noqa: E501

        :param problem_set: The problem_set of this ProblemClone.  # noqa: E501
        :type: str
        """
        if problem_set is None:
            raise ValueError("Invalid value for `problem_set`, must not be `None`")  # noqa: E501

        self._problem_set = problem_set

    @property
    def new_group(self):
        """Gets the new_group of this ProblemClone.  # noqa: E501

        whether to create new problem group  # noqa: E501

        :return: The new_group of this ProblemClone.  # noqa: E501
        :rtype: bool
        """
        return self._new_group

    @new_group.setter
    def new_group(self, new_group):
        """Sets the new_group of this ProblemClone.

        whether to create new problem group  # noqa: E501

        :param new_group: The new_group of this ProblemClone.  # noqa: E501
        :type: bool
        """

        self._new_group = new_group

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
        if issubclass(ProblemClone, dict):
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
        if not isinstance(other, ProblemClone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
