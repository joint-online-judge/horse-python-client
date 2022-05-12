# coding: utf-8

"""
    JOJ Horse

    Git version: c31343f@2022-05-12T02:05:27Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LanguageDefault(object):
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
        'compile_files': 'list[str]',
        'compile_args': 'list[str]',
        'lint_files': 'list[str]',
        'lint_args': 'list[str]',
        'case_default': 'Case',
        'cases': 'list[Case]'
    }

    attribute_map = {
        'compile_files': 'compileFiles',
        'compile_args': 'compileArgs',
        'lint_files': 'lintFiles',
        'lint_args': 'lintArgs',
        'case_default': 'caseDefault',
        'cases': 'cases'
    }

    def __init__(self, compile_files=None, compile_args=None, lint_files=None, lint_args=None, case_default=None, cases=None):  # noqa: E501
        """LanguageDefault - a model defined in Swagger"""  # noqa: E501
        self._compile_files = None
        self._compile_args = None
        self._lint_files = None
        self._lint_args = None
        self._case_default = None
        self._cases = None
        self.discriminator = None
        if compile_files is not None:
            self.compile_files = compile_files
        if compile_args is not None:
            self.compile_args = compile_args
        if lint_files is not None:
            self.lint_files = lint_files
        if lint_args is not None:
            self.lint_args = lint_args
        if case_default is not None:
            self.case_default = case_default
        if cases is not None:
            self.cases = cases

    @property
    def compile_files(self):
        """Gets the compile_files of this LanguageDefault.  # noqa: E501


        :return: The compile_files of this LanguageDefault.  # noqa: E501
        :rtype: list[str]
        """
        return self._compile_files

    @compile_files.setter
    def compile_files(self, compile_files):
        """Sets the compile_files of this LanguageDefault.


        :param compile_files: The compile_files of this LanguageDefault.  # noqa: E501
        :type: list[str]
        """

        self._compile_files = compile_files

    @property
    def compile_args(self):
        """Gets the compile_args of this LanguageDefault.  # noqa: E501


        :return: The compile_args of this LanguageDefault.  # noqa: E501
        :rtype: list[str]
        """
        return self._compile_args

    @compile_args.setter
    def compile_args(self, compile_args):
        """Sets the compile_args of this LanguageDefault.


        :param compile_args: The compile_args of this LanguageDefault.  # noqa: E501
        :type: list[str]
        """

        self._compile_args = compile_args

    @property
    def lint_files(self):
        """Gets the lint_files of this LanguageDefault.  # noqa: E501


        :return: The lint_files of this LanguageDefault.  # noqa: E501
        :rtype: list[str]
        """
        return self._lint_files

    @lint_files.setter
    def lint_files(self, lint_files):
        """Sets the lint_files of this LanguageDefault.


        :param lint_files: The lint_files of this LanguageDefault.  # noqa: E501
        :type: list[str]
        """

        self._lint_files = lint_files

    @property
    def lint_args(self):
        """Gets the lint_args of this LanguageDefault.  # noqa: E501


        :return: The lint_args of this LanguageDefault.  # noqa: E501
        :rtype: list[str]
        """
        return self._lint_args

    @lint_args.setter
    def lint_args(self, lint_args):
        """Sets the lint_args of this LanguageDefault.


        :param lint_args: The lint_args of this LanguageDefault.  # noqa: E501
        :type: list[str]
        """

        self._lint_args = lint_args

    @property
    def case_default(self):
        """Gets the case_default of this LanguageDefault.  # noqa: E501


        :return: The case_default of this LanguageDefault.  # noqa: E501
        :rtype: Case
        """
        return self._case_default

    @case_default.setter
    def case_default(self, case_default):
        """Sets the case_default of this LanguageDefault.


        :param case_default: The case_default of this LanguageDefault.  # noqa: E501
        :type: Case
        """

        self._case_default = case_default

    @property
    def cases(self):
        """Gets the cases of this LanguageDefault.  # noqa: E501


        :return: The cases of this LanguageDefault.  # noqa: E501
        :rtype: list[Case]
        """
        return self._cases

    @cases.setter
    def cases(self, cases):
        """Sets the cases of this LanguageDefault.


        :param cases: The cases of this LanguageDefault.  # noqa: E501
        :type: list[Case]
        """

        self._cases = cases

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
        if issubclass(LanguageDefault, dict):
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
        if not isinstance(other, LanguageDefault):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other