# coding: utf-8

"""
    JOJ Horse

    Git version: 9a397f7@2022-05-24T21:29:56Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemDetail(object):
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
        'hidden': 'bool',
        'num_submit': 'int',
        'num_accept': 'int',
        'owner_id': 'str',
        'problem_group_id': 'str',
        'content': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'languages': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domainId',
        'url': 'url',
        'title': 'title',
        'hidden': 'hidden',
        'num_submit': 'numSubmit',
        'num_accept': 'numAccept',
        'owner_id': 'ownerId',
        'problem_group_id': 'problemGroupId',
        'content': 'content',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'languages': 'languages'
    }

    def __init__(self, id=None, domain_id=None, url='', title=None, hidden=False, num_submit=0, num_accept=0, owner_id=None, problem_group_id=None, content='', created_at=None, updated_at=None, languages=None):  # noqa: E501
        """ProblemDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._domain_id = None
        self._url = None
        self._title = None
        self._hidden = None
        self._num_submit = None
        self._num_accept = None
        self._owner_id = None
        self._problem_group_id = None
        self._content = None
        self._created_at = None
        self._updated_at = None
        self._languages = None
        self.discriminator = None
        self.id = id
        self.domain_id = domain_id
        if url is not None:
            self.url = url
        self.title = title
        if hidden is not None:
            self.hidden = hidden
        if num_submit is not None:
            self.num_submit = num_submit
        if num_accept is not None:
            self.num_accept = num_accept
        if owner_id is not None:
            self.owner_id = owner_id
        if problem_group_id is not None:
            self.problem_group_id = problem_group_id
        if content is not None:
            self.content = content
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if languages is not None:
            self.languages = languages

    @property
    def id(self):
        """Gets the id of this ProblemDetail.  # noqa: E501


        :return: The id of this ProblemDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProblemDetail.


        :param id: The id of this ProblemDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def domain_id(self):
        """Gets the domain_id of this ProblemDetail.  # noqa: E501


        :return: The domain_id of this ProblemDetail.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ProblemDetail.


        :param domain_id: The domain_id of this ProblemDetail.  # noqa: E501
        :type: str
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")  # noqa: E501

        self._domain_id = domain_id

    @property
    def url(self):
        """Gets the url of this ProblemDetail.  # noqa: E501

        (unique) url of the domain  # noqa: E501

        :return: The url of this ProblemDetail.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProblemDetail.

        (unique) url of the domain  # noqa: E501

        :param url: The url of this ProblemDetail.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def title(self):
        """Gets the title of this ProblemDetail.  # noqa: E501

        title of the problem  # noqa: E501

        :return: The title of this ProblemDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemDetail.

        title of the problem  # noqa: E501

        :param title: The title of this ProblemDetail.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def hidden(self):
        """Gets the hidden of this ProblemDetail.  # noqa: E501

        is the problem hidden  # noqa: E501

        :return: The hidden of this ProblemDetail.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ProblemDetail.

        is the problem hidden  # noqa: E501

        :param hidden: The hidden of this ProblemDetail.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def num_submit(self):
        """Gets the num_submit of this ProblemDetail.  # noqa: E501


        :return: The num_submit of this ProblemDetail.  # noqa: E501
        :rtype: int
        """
        return self._num_submit

    @num_submit.setter
    def num_submit(self, num_submit):
        """Sets the num_submit of this ProblemDetail.


        :param num_submit: The num_submit of this ProblemDetail.  # noqa: E501
        :type: int
        """

        self._num_submit = num_submit

    @property
    def num_accept(self):
        """Gets the num_accept of this ProblemDetail.  # noqa: E501


        :return: The num_accept of this ProblemDetail.  # noqa: E501
        :rtype: int
        """
        return self._num_accept

    @num_accept.setter
    def num_accept(self, num_accept):
        """Sets the num_accept of this ProblemDetail.


        :param num_accept: The num_accept of this ProblemDetail.  # noqa: E501
        :type: int
        """

        self._num_accept = num_accept

    @property
    def owner_id(self):
        """Gets the owner_id of this ProblemDetail.  # noqa: E501


        :return: The owner_id of this ProblemDetail.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ProblemDetail.


        :param owner_id: The owner_id of this ProblemDetail.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def problem_group_id(self):
        """Gets the problem_group_id of this ProblemDetail.  # noqa: E501


        :return: The problem_group_id of this ProblemDetail.  # noqa: E501
        :rtype: str
        """
        return self._problem_group_id

    @problem_group_id.setter
    def problem_group_id(self, problem_group_id):
        """Sets the problem_group_id of this ProblemDetail.


        :param problem_group_id: The problem_group_id of this ProblemDetail.  # noqa: E501
        :type: str
        """

        self._problem_group_id = problem_group_id

    @property
    def content(self):
        """Gets the content of this ProblemDetail.  # noqa: E501

        content of the problem  # noqa: E501

        :return: The content of this ProblemDetail.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ProblemDetail.

        content of the problem  # noqa: E501

        :param content: The content of this ProblemDetail.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this ProblemDetail.  # noqa: E501


        :return: The created_at of this ProblemDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ProblemDetail.


        :param created_at: The created_at of this ProblemDetail.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ProblemDetail.  # noqa: E501


        :return: The updated_at of this ProblemDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ProblemDetail.


        :param updated_at: The updated_at of this ProblemDetail.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def languages(self):
        """Gets the languages of this ProblemDetail.  # noqa: E501


        :return: The languages of this ProblemDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this ProblemDetail.


        :param languages: The languages of this ProblemDetail.  # noqa: E501
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
        if issubclass(ProblemDetail, dict):
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
        if not isinstance(other, ProblemDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
