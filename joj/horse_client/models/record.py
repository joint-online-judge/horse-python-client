# coding: utf-8

"""
    JOJ Horse

    Git version: c5741c9@2023-02-03T15:02:34Z  # noqa: E501

    OpenAPI spec version: 1
    
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'str',
        'domain_id': 'str',
        'state': 'AllOfRecordState',
        'language': 'str',
        'score': 'int',
        'time_ms': 'int',
        'memory_kb': 'int',
        'judged_at': 'datetime'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'domain_id': 'domainId',
        'state': 'state',
        'language': 'language',
        'score': 'score',
        'time_ms': 'timeMs',
        'memory_kb': 'memoryKb',
        'judged_at': 'judgedAt'
    }

    def __init__(self, created_at=None, updated_at=None, id=None, domain_id=None, state=None, language=None, score=0, time_ms=0, memory_kb=0, judged_at=None):  # noqa: E501
        """Record - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._domain_id = None
        self._state = None
        self._language = None
        self._score = None
        self._time_ms = None
        self._memory_kb = None
        self._judged_at = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.id = id
        self.domain_id = domain_id
        if state is not None:
            self.state = state
        self.language = language
        if score is not None:
            self.score = score
        if time_ms is not None:
            self.time_ms = time_ms
        if memory_kb is not None:
            self.memory_kb = memory_kb
        if judged_at is not None:
            self.judged_at = judged_at

    @property
    def created_at(self):
        """Gets the created_at of this Record.  # noqa: E501


        :return: The created_at of this Record.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Record.


        :param created_at: The created_at of this Record.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Record.  # noqa: E501


        :return: The updated_at of this Record.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Record.


        :param updated_at: The updated_at of this Record.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
    def domain_id(self):
        """Gets the domain_id of this Record.  # noqa: E501


        :return: The domain_id of this Record.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Record.


        :param domain_id: The domain_id of this Record.  # noqa: E501
        :type: str
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")  # noqa: E501

        self._domain_id = domain_id

    @property
    def state(self):
        """Gets the state of this Record.  # noqa: E501


        :return: The state of this Record.  # noqa: E501
        :rtype: AllOfRecordState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Record.


        :param state: The state of this Record.  # noqa: E501
        :type: AllOfRecordState
        """

        self._state = state

    @property
    def language(self):
        """Gets the language of this Record.  # noqa: E501


        :return: The language of this Record.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Record.


        :param language: The language of this Record.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

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
    def judged_at(self):
        """Gets the judged_at of this Record.  # noqa: E501


        :return: The judged_at of this Record.  # noqa: E501
        :rtype: datetime
        """
        return self._judged_at

    @judged_at.setter
    def judged_at(self, judged_at):
        """Sets the judged_at of this Record.


        :param judged_at: The judged_at of this Record.  # noqa: E501
        :type: datetime
        """

        self._judged_at = judged_at

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
