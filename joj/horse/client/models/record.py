# coding: utf-8

"""
    JOJ Horse

    Git version: ae9905f@2021-11-20T17:34:51Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Record(object):
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
        'status': 'AllOfRecordStatus',
        'score': 'int',
        'time_ms': 'int',
        'memory_kb': 'int',
        'commit_id': 'str',
        'problem_set_id': 'str',
        'problem_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'score': 'score',
        'time_ms': 'timeMs',
        'memory_kb': 'memoryKb',
        'commit_id': 'commitId',
        'problem_set_id': 'problemSetId',
        'problem_id': 'problemId',
        'user_id': 'userId'
    }

    def __init__(self, id=None, status=None, score=0, time_ms=0, memory_kb=0, commit_id=None, problem_set_id=None, problem_id=None, user_id=None):  # noqa: E501
        """Record - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._score = None
        self._time_ms = None
        self._memory_kb = None
        self._commit_id = None
        self._problem_set_id = None
        self._problem_id = None
        self._user_id = None
        self.discriminator = None
        self.id = id
        if status is not None:
            self.status = status
        if score is not None:
            self.score = score
        if time_ms is not None:
            self.time_ms = time_ms
        if memory_kb is not None:
            self.memory_kb = memory_kb
        if commit_id is not None:
            self.commit_id = commit_id
        if problem_set_id is not None:
            self.problem_set_id = problem_set_id
        if problem_id is not None:
            self.problem_id = problem_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def id(self):
        """Gets the id of this Record.  # noqa: E501


        :return: The id of this Record.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Record.


        :param id: The id of this Record.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this Record.  # noqa: E501


        :return: The status of this Record.  # noqa: E501
        :rtype: AllOfRecordStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Record.


        :param status: The status of this Record.  # noqa: E501
        :type: AllOfRecordStatus
        """

        self._status = status

    @property
    def score(self):
        """Gets the score of this Record.  # noqa: E501


        :return: The score of this Record.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Record.


        :param score: The score of this Record.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def time_ms(self):
        """Gets the time_ms of this Record.  # noqa: E501


        :return: The time_ms of this Record.  # noqa: E501
        :rtype: int
        """
        return self._time_ms

    @time_ms.setter
    def time_ms(self, time_ms):
        """Sets the time_ms of this Record.


        :param time_ms: The time_ms of this Record.  # noqa: E501
        :type: int
        """

        self._time_ms = time_ms

    @property
    def memory_kb(self):
        """Gets the memory_kb of this Record.  # noqa: E501


        :return: The memory_kb of this Record.  # noqa: E501
        :rtype: int
        """
        return self._memory_kb

    @memory_kb.setter
    def memory_kb(self, memory_kb):
        """Sets the memory_kb of this Record.


        :param memory_kb: The memory_kb of this Record.  # noqa: E501
        :type: int
        """

        self._memory_kb = memory_kb

    @property
    def commit_id(self):
        """Gets the commit_id of this Record.  # noqa: E501


        :return: The commit_id of this Record.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this Record.


        :param commit_id: The commit_id of this Record.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def problem_set_id(self):
        """Gets the problem_set_id of this Record.  # noqa: E501


        :return: The problem_set_id of this Record.  # noqa: E501
        :rtype: str
        """
        return self._problem_set_id

    @problem_set_id.setter
    def problem_set_id(self, problem_set_id):
        """Sets the problem_set_id of this Record.


        :param problem_set_id: The problem_set_id of this Record.  # noqa: E501
        :type: str
        """

        self._problem_set_id = problem_set_id

    @property
    def problem_id(self):
        """Gets the problem_id of this Record.  # noqa: E501


        :return: The problem_id of this Record.  # noqa: E501
        :rtype: str
        """
        return self._problem_id

    @problem_id.setter
    def problem_id(self, problem_id):
        """Sets the problem_id of this Record.


        :param problem_id: The problem_id of this Record.  # noqa: E501
        :type: str
        """

        self._problem_id = problem_id

    @property
    def user_id(self):
        """Gets the user_id of this Record.  # noqa: E501


        :return: The user_id of this Record.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Record.


        :param user_id: The user_id of this Record.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(Record, dict):
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
        if not isinstance(other, Record):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
