# coding: utf-8

"""
    JOJ Horse

    Git version: 307ba8d@2021-11-11T16:39:45Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemSetEdit(object):
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
        'hidden': 'bool',
        'scoreboard_hidden': 'bool',
        'available_time': 'datetime',
        'due_time': 'datetime'
    }

    attribute_map = {
        'url': 'url',
        'title': 'title',
        'content': 'content',
        'hidden': 'hidden',
        'scoreboard_hidden': 'scoreboardHidden',
        'available_time': 'availableTime',
        'due_time': 'dueTime'
    }

    def __init__(self, url=None, title=None, content=None, hidden=None, scoreboard_hidden=None, available_time=None, due_time=None):  # noqa: E501
        """ProblemSetEdit - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._title = None
        self._content = None
        self._hidden = None
        self._scoreboard_hidden = None
        self._available_time = None
        self._due_time = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        if hidden is not None:
            self.hidden = hidden
        if scoreboard_hidden is not None:
            self.scoreboard_hidden = scoreboard_hidden
        if available_time is not None:
            self.available_time = available_time
        if due_time is not None:
            self.due_time = due_time

    @property
    def url(self):
        """Gets the url of this ProblemSetEdit.  # noqa: E501


        :return: The url of this ProblemSetEdit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProblemSetEdit.


        :param url: The url of this ProblemSetEdit.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def title(self):
        """Gets the title of this ProblemSetEdit.  # noqa: E501


        :return: The title of this ProblemSetEdit.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemSetEdit.


        :param title: The title of this ProblemSetEdit.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def content(self):
        """Gets the content of this ProblemSetEdit.  # noqa: E501


        :return: The content of this ProblemSetEdit.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ProblemSetEdit.


        :param content: The content of this ProblemSetEdit.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def hidden(self):
        """Gets the hidden of this ProblemSetEdit.  # noqa: E501


        :return: The hidden of this ProblemSetEdit.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ProblemSetEdit.


        :param hidden: The hidden of this ProblemSetEdit.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def scoreboard_hidden(self):
        """Gets the scoreboard_hidden of this ProblemSetEdit.  # noqa: E501


        :return: The scoreboard_hidden of this ProblemSetEdit.  # noqa: E501
        :rtype: bool
        """
        return self._scoreboard_hidden

    @scoreboard_hidden.setter
    def scoreboard_hidden(self, scoreboard_hidden):
        """Sets the scoreboard_hidden of this ProblemSetEdit.


        :param scoreboard_hidden: The scoreboard_hidden of this ProblemSetEdit.  # noqa: E501
        :type: bool
        """

        self._scoreboard_hidden = scoreboard_hidden

    @property
    def available_time(self):
        """Gets the available_time of this ProblemSetEdit.  # noqa: E501


        :return: The available_time of this ProblemSetEdit.  # noqa: E501
        :rtype: datetime
        """
        return self._available_time

    @available_time.setter
    def available_time(self, available_time):
        """Sets the available_time of this ProblemSetEdit.


        :param available_time: The available_time of this ProblemSetEdit.  # noqa: E501
        :type: datetime
        """

        self._available_time = available_time

    @property
    def due_time(self):
        """Gets the due_time of this ProblemSetEdit.  # noqa: E501


        :return: The due_time of this ProblemSetEdit.  # noqa: E501
        :rtype: datetime
        """
        return self._due_time

    @due_time.setter
    def due_time(self, due_time):
        """Sets the due_time of this ProblemSetEdit.


        :param due_time: The due_time of this ProblemSetEdit.  # noqa: E501
        :type: datetime
        """

        self._due_time = due_time

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
        if issubclass(ProblemSetEdit, dict):
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
        if not isinstance(other, ProblemSetEdit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
