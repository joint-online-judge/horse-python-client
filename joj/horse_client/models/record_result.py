# coding: utf-8

"""
    JOJ Horse

    Git version: ece3890@2022-01-07T15:40:26Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RecordResult(object):
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
        'state': 'RecordState',
        'score': 'int',
        'time_ms': 'int',
        'memory_kb': 'int',
        'judge_at': 'datetime'
    }

    attribute_map = {
        'state': 'state',
        'score': 'score',
        'time_ms': 'timeMs',
        'memory_kb': 'memoryKb',
        'judge_at': 'judgeAt'
    }

    def __init__(self, state=None, score=None, time_ms=None, memory_kb=None, judge_at=None):  # noqa: E501
        """RecordResult - a model defined in Swagger"""  # noqa: E501
        self._state = None
        self._score = None
        self._time_ms = None
        self._memory_kb = None
        self._judge_at = None
        self.discriminator = None
        self.state = state
        self.score = score
        self.time_ms = time_ms
        self.memory_kb = memory_kb
        self.judge_at = judge_at

    @property
    def state(self):
        """Gets the state of this RecordResult.  # noqa: E501


        :return: The state of this RecordResult.  # noqa: E501
        :rtype: RecordState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RecordResult.


        :param state: The state of this RecordResult.  # noqa: E501
        :type: RecordState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def score(self):
        """Gets the score of this RecordResult.  # noqa: E501


        :return: The score of this RecordResult.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this RecordResult.


        :param score: The score of this RecordResult.  # noqa: E501
        :type: int
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def time_ms(self):
        """Gets the time_ms of this RecordResult.  # noqa: E501


        :return: The time_ms of this RecordResult.  # noqa: E501
        :rtype: int
        """
        return self._time_ms

    @time_ms.setter
    def time_ms(self, time_ms):
        """Sets the time_ms of this RecordResult.


        :param time_ms: The time_ms of this RecordResult.  # noqa: E501
        :type: int
        """
        if time_ms is None:
            raise ValueError("Invalid value for `time_ms`, must not be `None`")  # noqa: E501

        self._time_ms = time_ms

    @property
    def memory_kb(self):
        """Gets the memory_kb of this RecordResult.  # noqa: E501


        :return: The memory_kb of this RecordResult.  # noqa: E501
        :rtype: int
        """
        return self._memory_kb

    @memory_kb.setter
    def memory_kb(self, memory_kb):
        """Sets the memory_kb of this RecordResult.


        :param memory_kb: The memory_kb of this RecordResult.  # noqa: E501
        :type: int
        """
        if memory_kb is None:
            raise ValueError("Invalid value for `memory_kb`, must not be `None`")  # noqa: E501

        self._memory_kb = memory_kb

    @property
    def judge_at(self):
        """Gets the judge_at of this RecordResult.  # noqa: E501


        :return: The judge_at of this RecordResult.  # noqa: E501
        :rtype: datetime
        """
        return self._judge_at

    @judge_at.setter
    def judge_at(self, judge_at):
        """Sets the judge_at of this RecordResult.


        :param judge_at: The judge_at of this RecordResult.  # noqa: E501
        :type: datetime
        """
        if judge_at is None:
            raise ValueError("Invalid value for `judge_at`, must not be `None`")  # noqa: E501

        self._judge_at = judge_at

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
        if issubclass(RecordResult, dict):
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
        if not isinstance(other, RecordResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
