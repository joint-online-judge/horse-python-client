# coding: utf-8

"""
    JOJ Horse

    Git version: 4e88176@2022-02-19T13:04:07Z  # noqa: E501

    OpenAPI spec version: 1
    
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
        'url': 'str',
        'title': 'str',
        'hidden': 'bool',
        'content': 'str'
    }

    attribute_map = {
        'url': 'url',
        'title': 'title',
        'hidden': 'hidden',
        'content': 'content'
    }

    def __init__(self, url='', title=None, hidden=False, content=''):  # noqa: E501
        """ProblemCreate - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._title = None
        self._hidden = None
        self._content = None
        self.discriminator = None
        if url is not None:
            self.url = url
        self.title = title
        if hidden is not None:
            self.hidden = hidden
        if content is not None:
            self.content = content

    @property
    def url(self):
        """Gets the url of this ProblemCreate.  # noqa: E501

        (unique) url of the domain  # noqa: E501

        :return: The url of this ProblemCreate.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProblemCreate.

        (unique) url of the domain  # noqa: E501

        :param url: The url of this ProblemCreate.  # noqa: E501
        :type: str
        """

        self._url = url

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
    def hidden(self):
        """Gets the hidden of this ProblemCreate.  # noqa: E501

        is the problem hidden  # noqa: E501

        :return: The hidden of this ProblemCreate.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ProblemCreate.

        is the problem hidden  # noqa: E501

        :param hidden: The hidden of this ProblemCreate.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

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
