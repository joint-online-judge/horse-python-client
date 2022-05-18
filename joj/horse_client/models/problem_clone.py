# coding: utf-8

"""
    JOJ Horse

    Git version: c41bfc4@2022-05-18T21:45:42Z  # noqa: E501

    OpenAPI spec version: 1
    
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
        'from_domain': 'str',
        'problems': 'list[str]',
        'new_group': 'bool'
    }

    attribute_map = {
        'from_domain': 'fromDomain',
        'problems': 'problems',
        'new_group': 'newGroup'
    }

    def __init__(self, from_domain=None, problems=None, new_group=False):  # noqa: E501
        """ProblemClone - a model defined in Swagger"""  # noqa: E501
        self._from_domain = None
        self._problems = None
        self._new_group = None
        self.discriminator = None
        self.from_domain = from_domain
        self.problems = problems
        if new_group is not None:
            self.new_group = new_group

    @property
    def from_domain(self):
        """Gets the from_domain of this ProblemClone.  # noqa: E501

        url or id of the domain to clone from  # noqa: E501

        :return: The from_domain of this ProblemClone.  # noqa: E501
        :rtype: str
        """
        return self._from_domain

    @from_domain.setter
    def from_domain(self, from_domain):
        """Sets the from_domain of this ProblemClone.

        url or id of the domain to clone from  # noqa: E501

        :param from_domain: The from_domain of this ProblemClone.  # noqa: E501
        :type: str
        """
        if from_domain is None:
            raise ValueError("Invalid value for `from_domain`, must not be `None`")  # noqa: E501

        self._from_domain = from_domain

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
