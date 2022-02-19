# coding: utf-8

"""
    JOJ Horse

    Git version: a34c3a9@2022-02-19T10:17:25Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemSet(object):
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
        'id': 'str',
        'domain_id': 'str',
        'url': 'str',
        'title': 'str',
        'content': 'str',
        'hidden': 'bool',
        'scoreboard_hidden': 'bool',
        'due_at': 'datetime',
        'lock_at': 'datetime',
        'unlock_at': 'datetime',
        'num_submit': 'int',
        'num_accept': 'int',
        'owner_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domainId',
        'url': 'url',
        'title': 'title',
        'content': 'content',
        'hidden': 'hidden',
        'scoreboard_hidden': 'scoreboardHidden',
        'due_at': 'dueAt',
        'lock_at': 'lockAt',
        'unlock_at': 'unlockAt',
        'num_submit': 'numSubmit',
        'num_accept': 'numAccept',
        'owner_id': 'ownerId'
    }

    def __init__(self, id=None, domain_id=None, url='', title=None, content='', hidden=False, scoreboard_hidden=False, due_at=None, lock_at=None, unlock_at=None, num_submit=0, num_accept=0, owner_id=None):  # noqa: E501
        """ProblemSet - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._domain_id = None
        self._url = None
        self._title = None
        self._content = None
        self._hidden = None
        self._scoreboard_hidden = None
        self._due_at = None
        self._lock_at = None
        self._unlock_at = None
        self._num_submit = None
        self._num_accept = None
        self._owner_id = None
        self.discriminator = None
        self.id = id
        self.domain_id = domain_id
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
        if num_submit is not None:
            self.num_submit = num_submit
        if num_accept is not None:
            self.num_accept = num_accept
        if owner_id is not None:
            self.owner_id = owner_id

    @property
    def id(self):
        """Gets the id of this ProblemSet.  # noqa: E501


        :return: The id of this ProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProblemSet.


        :param id: The id of this ProblemSet.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def domain_id(self):
        """Gets the domain_id of this ProblemSet.  # noqa: E501


        :return: The domain_id of this ProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ProblemSet.


        :param domain_id: The domain_id of this ProblemSet.  # noqa: E501
        :type: str
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")  # noqa: E501

        self._domain_id = domain_id

    @property
    def url(self):
        """Gets the url of this ProblemSet.  # noqa: E501

        (unique) url of the domain  # noqa: E501

        :return: The url of this ProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProblemSet.

        (unique) url of the domain  # noqa: E501

        :param url: The url of this ProblemSet.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def title(self):
        """Gets the title of this ProblemSet.  # noqa: E501

        title of the problem set  # noqa: E501

        :return: The title of this ProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemSet.

        title of the problem set  # noqa: E501

        :param title: The title of this ProblemSet.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def content(self):
        """Gets the content of this ProblemSet.  # noqa: E501

        content of the problem set  # noqa: E501

        :return: The content of this ProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ProblemSet.

        content of the problem set  # noqa: E501

        :param content: The content of this ProblemSet.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def hidden(self):
        """Gets the hidden of this ProblemSet.  # noqa: E501

        whether the problem set is hidden  # noqa: E501

        :return: The hidden of this ProblemSet.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ProblemSet.

        whether the problem set is hidden  # noqa: E501

        :param hidden: The hidden of this ProblemSet.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def scoreboard_hidden(self):
        """Gets the scoreboard_hidden of this ProblemSet.  # noqa: E501

        whether the scoreboard of the problem set is hidden  # noqa: E501

        :return: The scoreboard_hidden of this ProblemSet.  # noqa: E501
        :rtype: bool
        """
        return self._scoreboard_hidden

    @scoreboard_hidden.setter
    def scoreboard_hidden(self, scoreboard_hidden):
        """Sets the scoreboard_hidden of this ProblemSet.

        whether the scoreboard of the problem set is hidden  # noqa: E501

        :param scoreboard_hidden: The scoreboard_hidden of this ProblemSet.  # noqa: E501
        :type: bool
        """

        self._scoreboard_hidden = scoreboard_hidden

    @property
    def due_at(self):
        """Gets the due_at of this ProblemSet.  # noqa: E501

        the problem set is due at this date  # noqa: E501

        :return: The due_at of this ProblemSet.  # noqa: E501
        :rtype: datetime
        """
        return self._due_at

    @due_at.setter
    def due_at(self, due_at):
        """Sets the due_at of this ProblemSet.

        the problem set is due at this date  # noqa: E501

        :param due_at: The due_at of this ProblemSet.  # noqa: E501
        :type: datetime
        """

        self._due_at = due_at

    @property
    def lock_at(self):
        """Gets the lock_at of this ProblemSet.  # noqa: E501

        the problem set is locked after this date  # noqa: E501

        :return: The lock_at of this ProblemSet.  # noqa: E501
        :rtype: datetime
        """
        return self._lock_at

    @lock_at.setter
    def lock_at(self, lock_at):
        """Sets the lock_at of this ProblemSet.

        the problem set is locked after this date  # noqa: E501

        :param lock_at: The lock_at of this ProblemSet.  # noqa: E501
        :type: datetime
        """

        self._lock_at = lock_at

    @property
    def unlock_at(self):
        """Gets the unlock_at of this ProblemSet.  # noqa: E501

        the problem set is unlocked after this date  # noqa: E501

        :return: The unlock_at of this ProblemSet.  # noqa: E501
        :rtype: datetime
        """
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, unlock_at):
        """Sets the unlock_at of this ProblemSet.

        the problem set is unlocked after this date  # noqa: E501

        :param unlock_at: The unlock_at of this ProblemSet.  # noqa: E501
        :type: datetime
        """

        self._unlock_at = unlock_at

    @property
    def num_submit(self):
        """Gets the num_submit of this ProblemSet.  # noqa: E501


        :return: The num_submit of this ProblemSet.  # noqa: E501
        :rtype: int
        """
        return self._num_submit

    @num_submit.setter
    def num_submit(self, num_submit):
        """Sets the num_submit of this ProblemSet.


        :param num_submit: The num_submit of this ProblemSet.  # noqa: E501
        :type: int
        """

        self._num_submit = num_submit

    @property
    def num_accept(self):
        """Gets the num_accept of this ProblemSet.  # noqa: E501


        :return: The num_accept of this ProblemSet.  # noqa: E501
        :rtype: int
        """
        return self._num_accept

    @num_accept.setter
    def num_accept(self, num_accept):
        """Sets the num_accept of this ProblemSet.


        :param num_accept: The num_accept of this ProblemSet.  # noqa: E501
        :type: int
        """

        self._num_accept = num_accept

    @property
    def owner_id(self):
        """Gets the owner_id of this ProblemSet.  # noqa: E501


        :return: The owner_id of this ProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ProblemSet.


        :param owner_id: The owner_id of this ProblemSet.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

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
        if issubclass(ProblemSet, dict):
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
        if not isinstance(other, ProblemSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
