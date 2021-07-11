# coding: utf-8

"""
    JOJ Horse

    Git version: 55b1698@2021-07-11 05:05:35  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemEdit(object):
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
        'data': 'int',
        'data_version': 'DataVersion',
        'languages': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'content': 'content',
        'data': 'data',
        'data_version': 'data_version',
        'languages': 'languages'
    }

    def __init__(self, title=None, content=None, data=None, data_version=None, languages=None):  # noqa: E501
        """ProblemEdit - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._content = None
        self._data = None
        self._data_version = None
        self._languages = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        if data is not None:
            self.data = data
        if data_version is not None:
            self.data_version = data_version
        if languages is not None:
            self.languages = languages

    @property
    def title(self):
        """Gets the title of this ProblemEdit.  # noqa: E501


        :return: The title of this ProblemEdit.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemEdit.


        :param title: The title of this ProblemEdit.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def content(self):
        """Gets the content of this ProblemEdit.  # noqa: E501


        :return: The content of this ProblemEdit.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ProblemEdit.


        :param content: The content of this ProblemEdit.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def data(self):
        """Gets the data of this ProblemEdit.  # noqa: E501


        :return: The data of this ProblemEdit.  # noqa: E501
        :rtype: int
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ProblemEdit.


        :param data: The data of this ProblemEdit.  # noqa: E501
        :type: int
        """

        self._data = data

    @property
    def data_version(self):
        """Gets the data_version of this ProblemEdit.  # noqa: E501


        :return: The data_version of this ProblemEdit.  # noqa: E501
        :rtype: DataVersion
        """
        return self._data_version

    @data_version.setter
    def data_version(self, data_version):
        """Sets the data_version of this ProblemEdit.


        :param data_version: The data_version of this ProblemEdit.  # noqa: E501
        :type: DataVersion
        """

        self._data_version = data_version

    @property
    def languages(self):
        """Gets the languages of this ProblemEdit.  # noqa: E501


        :return: The languages of this ProblemEdit.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this ProblemEdit.


        :param languages: The languages of this ProblemEdit.  # noqa: E501
        :type: list[str]
        """

        self._languages = languages

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
        if issubclass(ProblemEdit, dict):
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
        if not isinstance(other, ProblemEdit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
