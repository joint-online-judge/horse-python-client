# coding: utf-8

"""
    JOJ Horse

    Git version: 9e94d56@2021-07-16 06:38:54  # noqa: E501

    OpenAPI spec version: 0.0.0
    
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
        'url': 'str',
        'title': 'str',
        'content': 'str',
        'hidden': 'bool',
        'scoreboard_hidden': 'bool',
        'available_time': 'datetime',
        'due_time': 'datetime',
        'domain': 'AnyOfProblemSetDomain',
        'owner': 'AnyOfProblemSetOwner',
        'num_submit': 'int',
        'num_accept': 'int',
        'problems': 'list[AnyOfProblemSetProblemsItems]'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'title': 'title',
        'content': 'content',
        'hidden': 'hidden',
        'scoreboard_hidden': 'scoreboard_hidden',
        'available_time': 'available_time',
        'due_time': 'due_time',
        'domain': 'domain',
        'owner': 'owner',
        'num_submit': 'num_submit',
        'num_accept': 'num_accept',
        'problems': 'problems'
    }

    def __init__(self, id=None, url=None, title=None, content='', hidden=False, scoreboard_hidden=False, available_time=None, due_time=None, domain=None, owner=None, num_submit=0, num_accept=0, problems=None):  # noqa: E501
        """ProblemSet - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._title = None
        self._content = None
        self._hidden = None
        self._scoreboard_hidden = None
        self._available_time = None
        self._due_time = None
        self._domain = None
        self._owner = None
        self._num_submit = None
        self._num_accept = None
        self._problems = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.url = url
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
        self.domain = domain
        self.owner = owner
        if num_submit is not None:
            self.num_submit = num_submit
        if num_accept is not None:
            self.num_accept = num_accept
        if problems is not None:
            self.problems = problems

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

        self._id = id

    @property
    def url(self):
        """Gets the url of this ProblemSet.  # noqa: E501


        :return: The url of this ProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProblemSet.


        :param url: The url of this ProblemSet.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

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
    def available_time(self):
        """Gets the available_time of this ProblemSet.  # noqa: E501

        the problem set is available from  # noqa: E501

        :return: The available_time of this ProblemSet.  # noqa: E501
        :rtype: datetime
        """
        return self._available_time

    @available_time.setter
    def available_time(self, available_time):
        """Sets the available_time of this ProblemSet.

        the problem set is available from  # noqa: E501

        :param available_time: The available_time of this ProblemSet.  # noqa: E501
        :type: datetime
        """

        self._available_time = available_time

    @property
    def due_time(self):
        """Gets the due_time of this ProblemSet.  # noqa: E501

        the problem set is due at  # noqa: E501

        :return: The due_time of this ProblemSet.  # noqa: E501
        :rtype: datetime
        """
        return self._due_time

    @due_time.setter
    def due_time(self, due_time):
        """Sets the due_time of this ProblemSet.

        the problem set is due at  # noqa: E501

        :param due_time: The due_time of this ProblemSet.  # noqa: E501
        :type: datetime
        """

        self._due_time = due_time

    @property
    def domain(self):
        """Gets the domain of this ProblemSet.  # noqa: E501


        :return: The domain of this ProblemSet.  # noqa: E501
        :rtype: AnyOfProblemSetDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ProblemSet.


        :param domain: The domain of this ProblemSet.  # noqa: E501
        :type: AnyOfProblemSetDomain
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def owner(self):
        """Gets the owner of this ProblemSet.  # noqa: E501


        :return: The owner of this ProblemSet.  # noqa: E501
        :rtype: AnyOfProblemSetOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ProblemSet.


        :param owner: The owner of this ProblemSet.  # noqa: E501
        :type: AnyOfProblemSetOwner
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

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
    def problems(self):
        """Gets the problems of this ProblemSet.  # noqa: E501


        :return: The problems of this ProblemSet.  # noqa: E501
        :rtype: list[AnyOfProblemSetProblemsItems]
        """
        return self._problems

    @problems.setter
    def problems(self, problems):
        """Sets the problems of this ProblemSet.


        :param problems: The problems of this ProblemSet.  # noqa: E501
        :type: list[AnyOfProblemSetProblemsItems]
        """

        self._problems = problems

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
