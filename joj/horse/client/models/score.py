# coding: utf-8

"""
    JOJ Horse

    Git version: fb13909@2021-11-17T18:47:48Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Score(object):
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
        'score': 'int',
        'time': 'datetime',
        'full_score': 'int',
        'time_spent': 'float',
        'tried': 'bool'
    }

    attribute_map = {
        'score': 'score',
        'time': 'time',
        'full_score': 'fullScore',
        'time_spent': 'timeSpent',
        'tried': 'tried'
    }

    def __init__(self, score=None, time=None, full_score=None, time_spent=None, tried=None):  # noqa: E501
        """Score - a model defined in Swagger"""  # noqa: E501
        self._score = None
        self._time = None
        self._full_score = None
        self._time_spent = None
        self._tried = None
        self.discriminator = None
        self.score = score
        self.time = time
        self.full_score = full_score
        self.time_spent = time_spent
        self.tried = tried

    @property
    def score(self):
        """Gets the score of this Score.  # noqa: E501


        :return: The score of this Score.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Score.


        :param score: The score of this Score.  # noqa: E501
        :type: int
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def time(self):
        """Gets the time of this Score.  # noqa: E501


        :return: The time of this Score.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Score.


        :param time: The time of this Score.  # noqa: E501
        :type: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def full_score(self):
        """Gets the full_score of this Score.  # noqa: E501


        :return: The full_score of this Score.  # noqa: E501
        :rtype: int
        """
        return self._full_score

    @full_score.setter
    def full_score(self, full_score):
        """Sets the full_score of this Score.


        :param full_score: The full_score of this Score.  # noqa: E501
        :type: int
        """
        if full_score is None:
            raise ValueError("Invalid value for `full_score`, must not be `None`")  # noqa: E501

        self._full_score = full_score

    @property
    def time_spent(self):
        """Gets the time_spent of this Score.  # noqa: E501


        :return: The time_spent of this Score.  # noqa: E501
        :rtype: float
        """
        return self._time_spent

    @time_spent.setter
    def time_spent(self, time_spent):
        """Sets the time_spent of this Score.


        :param time_spent: The time_spent of this Score.  # noqa: E501
        :type: float
        """
        if time_spent is None:
            raise ValueError("Invalid value for `time_spent`, must not be `None`")  # noqa: E501

        self._time_spent = time_spent

    @property
    def tried(self):
        """Gets the tried of this Score.  # noqa: E501


        :return: The tried of this Score.  # noqa: E501
        :rtype: bool
        """
        return self._tried

    @tried.setter
    def tried(self, tried):
        """Sets the tried of this Score.


        :param tried: The tried of this Score.  # noqa: E501
        :type: bool
        """
        if tried is None:
            raise ValueError("Invalid value for `tried`, must not be `None`")  # noqa: E501

        self._tried = tried

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
        if issubclass(Score, dict):
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
        if not isinstance(other, Score):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
