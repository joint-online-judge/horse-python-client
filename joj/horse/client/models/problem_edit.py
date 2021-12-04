# coding: utf-8

"""
    JOJ Horse

    Git version: 2b6cbca@2021-12-04T18:50:49Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
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
        'url': 'str',
        'title': 'str',
        'content': 'str',
        'hidden': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'title': 'title',
        'content': 'content',
        'hidden': 'hidden'
    }

    def __init__(self, url=None, title=None, content=None, hidden=None):  # noqa: E501
        """ProblemEdit - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._title = None
        self._content = None
        self._hidden = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        if hidden is not None:
            self.hidden = hidden

    @property
    def url(self):
        """Gets the url of this ProblemEdit.  # noqa: E501


        :return: The url of this ProblemEdit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProblemEdit.


        :param url: The url of this ProblemEdit.  # noqa: E501
        :type: str
        """

        self._url = url

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
    def hidden(self):
        """Gets the hidden of this ProblemEdit.  # noqa: E501


        :return: The hidden of this ProblemEdit.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ProblemEdit.


        :param hidden: The hidden of this ProblemEdit.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

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
