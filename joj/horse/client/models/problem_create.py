# coding: utf-8

"""
    JOJ Horse

    Git version: dad896a@2021-06-08 19:53:00  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemCreate(object):
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
        'title': 'str',
        'content': 'str',
        'data_version': 'AllOfProblemCreateDataVersion',
        'languages': 'list[str]',
        'problem_set': 'str'
    }

    attribute_map = {
        'title': 'title',
        'content': 'content',
        'data_version': 'data_version',
        'languages': 'languages',
        'problem_set': 'problem_set'
    }

    def __init__(self, title=None, content='', data_version=None, languages=None, problem_set=None):  # noqa: E501
        """ProblemCreate - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._content = None
        self._data_version = None
        self._languages = None
        self._problem_set = None
        self.discriminator = None
        self.title = title
        if content is not None:
            self.content = content
        if data_version is not None:
            self.data_version = data_version
        if languages is not None:
            self.languages = languages
        self.problem_set = problem_set

    @property
    def title(self):
        """Gets the title of this ProblemCreate.  # noqa: E501

        title of the problem  # noqa: E501

        :return: The title of this ProblemCreate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemCreate.

        title of the problem  # noqa: E501

        :param title: The title of this ProblemCreate.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def content(self):
        """Gets the content of this ProblemCreate.  # noqa: E501

        content of the problem  # noqa: E501

        :return: The content of this ProblemCreate.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ProblemCreate.

        content of the problem  # noqa: E501

        :param content: The content of this ProblemCreate.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def data_version(self):
        """Gets the data_version of this ProblemCreate.  # noqa: E501


        :return: The data_version of this ProblemCreate.  # noqa: E501
        :rtype: AllOfProblemCreateDataVersion
        """
        return self._data_version

    @data_version.setter
    def data_version(self, data_version):
        """Sets the data_version of this ProblemCreate.


        :param data_version: The data_version of this ProblemCreate.  # noqa: E501
        :type: AllOfProblemCreateDataVersion
        """

        self._data_version = data_version

    @property
    def languages(self):
        """Gets the languages of this ProblemCreate.  # noqa: E501

        acceptable language of the problem  # noqa: E501

        :return: The languages of this ProblemCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this ProblemCreate.

        acceptable language of the problem  # noqa: E501

        :param languages: The languages of this ProblemCreate.  # noqa: E501
        :type: list[str]
        """

        self._languages = languages

    @property
    def problem_set(self):
        """Gets the problem_set of this ProblemCreate.  # noqa: E501

        problem set it belongs to  # noqa: E501

        :return: The problem_set of this ProblemCreate.  # noqa: E501
        :rtype: str
        """
        return self._problem_set

    @problem_set.setter
    def problem_set(self, problem_set):
        """Sets the problem_set of this ProblemCreate.

        problem set it belongs to  # noqa: E501

        :param problem_set: The problem_set of this ProblemCreate.  # noqa: E501
        :type: str
        """
        if problem_set is None:
            raise ValueError("Invalid value for `problem_set`, must not be `None`")  # noqa: E501

        self._problem_set = problem_set

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
        if issubclass(ProblemCreate, dict):
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
        if not isinstance(other, ProblemCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
