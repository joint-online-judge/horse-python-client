# coding: utf-8

"""
    JOJ Horse

    Git version: b5e6a46@2022-01-03T17:48:56Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemSetCreate(object):
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
        'due_at': 'datetime',
        'lock_at': 'datetime',
        'unlock_at': 'datetime'
    }

    attribute_map = {
        'url': 'url',
        'title': 'title',
        'content': 'content',
        'hidden': 'hidden',
        'scoreboard_hidden': 'scoreboardHidden',
        'due_at': 'dueAt',
        'lock_at': 'lockAt',
        'unlock_at': 'unlockAt'
    }

    def __init__(self, url='', title=None, content='', hidden=False, scoreboard_hidden=False, due_at=None, lock_at=None, unlock_at=None):  # noqa: E501
        """ProblemSetCreate - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._title = None
        self._content = None
        self._hidden = None
        self._scoreboard_hidden = None
        self._due_at = None
        self._lock_at = None
        self._unlock_at = None
        self.discriminator = None
        if url is not None:
            self.url = url
        self.title = title
        if content is not None:
            self.content = content
        if hidden is not None:
            self.hidden = hidden
        if scoreboard_hidden is not None:
            self.scoreboard_hidden = scoreboard_hidden
        if due_at is not None:
            self.due_at = due_at
        if lock_at is not None:
            self.lock_at = lock_at
        if unlock_at is not None:
            self.unlock_at = unlock_at

    @property
    def url(self):
        """Gets the url of this ProblemSetCreate.  # noqa: E501

        (unique) url of the domain  # noqa: E501

        :return: The url of this ProblemSetCreate.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProblemSetCreate.

        (unique) url of the domain  # noqa: E501

        :param url: The url of this ProblemSetCreate.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def title(self):
        """Gets the title of this ProblemSetCreate.  # noqa: E501

        title of the problem set  # noqa: E501

        :return: The title of this ProblemSetCreate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemSetCreate.

        title of the problem set  # noqa: E501

        :param title: The title of this ProblemSetCreate.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def content(self):
        """Gets the content of this ProblemSetCreate.  # noqa: E501

        content of the problem set  # noqa: E501

        :return: The content of this ProblemSetCreate.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ProblemSetCreate.

        content of the problem set  # noqa: E501

        :param content: The content of this ProblemSetCreate.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def hidden(self):
        """Gets the hidden of this ProblemSetCreate.  # noqa: E501

        whether the problem set is hidden  # noqa: E501

        :return: The hidden of this ProblemSetCreate.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ProblemSetCreate.

        whether the problem set is hidden  # noqa: E501

        :param hidden: The hidden of this ProblemSetCreate.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def scoreboard_hidden(self):
        """Gets the scoreboard_hidden of this ProblemSetCreate.  # noqa: E501

        whether the scoreboard of the problem set is hidden  # noqa: E501

        :return: The scoreboard_hidden of this ProblemSetCreate.  # noqa: E501
        :rtype: bool
        """
        return self._scoreboard_hidden

    @scoreboard_hidden.setter
    def scoreboard_hidden(self, scoreboard_hidden):
        """Sets the scoreboard_hidden of this ProblemSetCreate.

        whether the scoreboard of the problem set is hidden  # noqa: E501

        :param scoreboard_hidden: The scoreboard_hidden of this ProblemSetCreate.  # noqa: E501
        :type: bool
        """

        self._scoreboard_hidden = scoreboard_hidden

    @property
    def due_at(self):
        """Gets the due_at of this ProblemSetCreate.  # noqa: E501


        :return: The due_at of this ProblemSetCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._due_at

    @due_at.setter
    def due_at(self, due_at):
        """Sets the due_at of this ProblemSetCreate.


        :param due_at: The due_at of this ProblemSetCreate.  # noqa: E501
        :type: datetime
        """

        self._due_at = due_at

    @property
    def lock_at(self):
        """Gets the lock_at of this ProblemSetCreate.  # noqa: E501


        :return: The lock_at of this ProblemSetCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._lock_at

    @lock_at.setter
    def lock_at(self, lock_at):
        """Sets the lock_at of this ProblemSetCreate.


        :param lock_at: The lock_at of this ProblemSetCreate.  # noqa: E501
        :type: datetime
        """

        self._lock_at = lock_at

    @property
    def unlock_at(self):
        """Gets the unlock_at of this ProblemSetCreate.  # noqa: E501


        :return: The unlock_at of this ProblemSetCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, unlock_at):
        """Sets the unlock_at of this ProblemSetCreate.


        :param unlock_at: The unlock_at of this ProblemSetCreate.  # noqa: E501
        :type: datetime
        """

        self._unlock_at = unlock_at

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
        if issubclass(ProblemSetCreate, dict):
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
        if not isinstance(other, ProblemSetCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
