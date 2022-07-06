# coding: utf-8

"""
    JOJ Horse

    Git version: f4a351d@2022-07-06T03:30:14Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainPermission(object):
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
        'general': 'AllOfDomainPermissionGeneral',
        'problem': 'AllOfDomainPermissionProblem',
        'problem_set': 'AllOfDomainPermissionProblemSet',
        'record': 'AllOfDomainPermissionRecord'
    }

    attribute_map = {
        'general': 'general',
        'problem': 'problem',
        'problem_set': 'problemSet',
        'record': 'record'
    }

    def __init__(self, general=None, problem=None, problem_set=None, record=None):  # noqa: E501
        """DomainPermission - a model defined in Swagger"""  # noqa: E501
        self._general = None
        self._problem = None
        self._problem_set = None
        self._record = None
        self.discriminator = None
        if general is not None:
            self.general = general
        if problem is not None:
            self.problem = problem
        if problem_set is not None:
            self.problem_set = problem_set
        if record is not None:
            self.record = record

    @property
    def general(self):
        """Gets the general of this DomainPermission.  # noqa: E501


        :return: The general of this DomainPermission.  # noqa: E501
        :rtype: AllOfDomainPermissionGeneral
        """
        return self._general

    @general.setter
    def general(self, general):
        """Sets the general of this DomainPermission.


        :param general: The general of this DomainPermission.  # noqa: E501
        :type: AllOfDomainPermissionGeneral
        """

        self._general = general

    @property
    def problem(self):
        """Gets the problem of this DomainPermission.  # noqa: E501


        :return: The problem of this DomainPermission.  # noqa: E501
        :rtype: AllOfDomainPermissionProblem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this DomainPermission.


        :param problem: The problem of this DomainPermission.  # noqa: E501
        :type: AllOfDomainPermissionProblem
        """

        self._problem = problem

    @property
    def problem_set(self):
        """Gets the problem_set of this DomainPermission.  # noqa: E501


        :return: The problem_set of this DomainPermission.  # noqa: E501
        :rtype: AllOfDomainPermissionProblemSet
        """
        return self._problem_set

    @problem_set.setter
    def problem_set(self, problem_set):
        """Sets the problem_set of this DomainPermission.


        :param problem_set: The problem_set of this DomainPermission.  # noqa: E501
        :type: AllOfDomainPermissionProblemSet
        """

        self._problem_set = problem_set

    @property
    def record(self):
        """Gets the record of this DomainPermission.  # noqa: E501


        :return: The record of this DomainPermission.  # noqa: E501
        :rtype: AllOfDomainPermissionRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this DomainPermission.


        :param record: The record of this DomainPermission.  # noqa: E501
        :type: AllOfDomainPermissionRecord
        """

        self._record = record

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
        if issubclass(DomainPermission, dict):
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
        if not isinstance(other, DomainPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
