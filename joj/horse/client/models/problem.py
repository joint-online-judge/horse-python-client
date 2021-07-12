# coding: utf-8

"""
    JOJ Horse

    Git version: 1a21292@2021-07-12 11:04:16  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Problem(object):
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
        'domain': 'AnyOfProblemDomain',
        'owner': 'AnyOfProblemOwner',
        'problem_group': 'AnyOfProblemProblemGroup',
        'config': 'AllOfProblemConfig',
        'num_submit': 'int',
        'num_accept': 'int',
        'data': 'int',
        'total_score': 'int',
        'data_version': 'AllOfProblemDataVersion'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'title': 'title',
        'content': 'content',
        'domain': 'domain',
        'owner': 'owner',
        'problem_group': 'problem_group',
        'config': 'config',
        'num_submit': 'num_submit',
        'num_accept': 'num_accept',
        'data': 'data',
        'total_score': 'total_score',
        'data_version': 'data_version'
    }

    def __init__(self, id=None, url=None, title=None, content='', domain=None, owner=None, problem_group=None, config=None, num_submit=0, num_accept=0, data=None, total_score=0, data_version=None):  # noqa: E501
        """Problem - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._title = None
        self._content = None
        self._domain = None
        self._owner = None
        self._problem_group = None
        self._config = None
        self._num_submit = None
        self._num_accept = None
        self._data = None
        self._total_score = None
        self._data_version = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.url = url
        self.title = title
        if content is not None:
            self.content = content
        self.domain = domain
        self.owner = owner
        self.problem_group = problem_group
        if config is not None:
            self.config = config
        if num_submit is not None:
            self.num_submit = num_submit
        if num_accept is not None:
            self.num_accept = num_accept
        if data is not None:
            self.data = data
        if total_score is not None:
            self.total_score = total_score
        if data_version is not None:
            self.data_version = data_version

    @property
    def id(self):
        """Gets the id of this Problem.  # noqa: E501


        :return: The id of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Problem.


        :param id: The id of this Problem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this Problem.  # noqa: E501


        :return: The url of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Problem.


        :param url: The url of this Problem.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def title(self):
        """Gets the title of this Problem.  # noqa: E501

        title of the problem  # noqa: E501

        :return: The title of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Problem.

        title of the problem  # noqa: E501

        :param title: The title of this Problem.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def content(self):
        """Gets the content of this Problem.  # noqa: E501

        content of the problem  # noqa: E501

        :return: The content of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Problem.

        content of the problem  # noqa: E501

        :param content: The content of this Problem.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def domain(self):
        """Gets the domain of this Problem.  # noqa: E501


        :return: The domain of this Problem.  # noqa: E501
        :rtype: AnyOfProblemDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Problem.


        :param domain: The domain of this Problem.  # noqa: E501
        :type: AnyOfProblemDomain
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def owner(self):
        """Gets the owner of this Problem.  # noqa: E501


        :return: The owner of this Problem.  # noqa: E501
        :rtype: AnyOfProblemOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Problem.


        :param owner: The owner of this Problem.  # noqa: E501
        :type: AnyOfProblemOwner
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def problem_group(self):
        """Gets the problem_group of this Problem.  # noqa: E501


        :return: The problem_group of this Problem.  # noqa: E501
        :rtype: AnyOfProblemProblemGroup
        """
        return self._problem_group

    @problem_group.setter
    def problem_group(self, problem_group):
        """Sets the problem_group of this Problem.


        :param problem_group: The problem_group of this Problem.  # noqa: E501
        :type: AnyOfProblemProblemGroup
        """
        if problem_group is None:
            raise ValueError("Invalid value for `problem_group`, must not be `None`")  # noqa: E501

        self._problem_group = problem_group

    @property
    def config(self):
        """Gets the config of this Problem.  # noqa: E501


        :return: The config of this Problem.  # noqa: E501
        :rtype: AllOfProblemConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Problem.


        :param config: The config of this Problem.  # noqa: E501
        :type: AllOfProblemConfig
        """

        self._config = config

    @property
    def num_submit(self):
        """Gets the num_submit of this Problem.  # noqa: E501


        :return: The num_submit of this Problem.  # noqa: E501
        :rtype: int
        """
        return self._num_submit

    @num_submit.setter
    def num_submit(self, num_submit):
        """Sets the num_submit of this Problem.


        :param num_submit: The num_submit of this Problem.  # noqa: E501
        :type: int
        """

        self._num_submit = num_submit

    @property
    def num_accept(self):
        """Gets the num_accept of this Problem.  # noqa: E501


        :return: The num_accept of this Problem.  # noqa: E501
        :rtype: int
        """
        return self._num_accept

    @num_accept.setter
    def num_accept(self, num_accept):
        """Sets the num_accept of this Problem.


        :param num_accept: The num_accept of this Problem.  # noqa: E501
        :type: int
        """

        self._num_accept = num_accept

    @property
    def data(self):
        """Gets the data of this Problem.  # noqa: E501


        :return: The data of this Problem.  # noqa: E501
        :rtype: int
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Problem.


        :param data: The data of this Problem.  # noqa: E501
        :type: int
        """

        self._data = data

    @property
    def total_score(self):
        """Gets the total_score of this Problem.  # noqa: E501


        :return: The total_score of this Problem.  # noqa: E501
        :rtype: int
        """
        return self._total_score

    @total_score.setter
    def total_score(self, total_score):
        """Sets the total_score of this Problem.


        :param total_score: The total_score of this Problem.  # noqa: E501
        :type: int
        """

        self._total_score = total_score

    @property
    def data_version(self):
        """Gets the data_version of this Problem.  # noqa: E501


        :return: The data_version of this Problem.  # noqa: E501
        :rtype: AllOfProblemDataVersion
        """
        return self._data_version

    @data_version.setter
    def data_version(self, data_version):
        """Sets the data_version of this Problem.


        :param data_version: The data_version of this Problem.  # noqa: E501
        :type: AllOfProblemDataVersion
        """

        self._data_version = data_version

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
        if issubclass(Problem, dict):
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
        if not isinstance(other, Problem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
