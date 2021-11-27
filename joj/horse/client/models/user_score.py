# coding: utf-8

"""
    JOJ Horse

    Git version: 13e2edd@2021-11-27T17:58:14Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserScore(object):
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
        'user': 'User',
        'total_score': 'int',
        'total_time_spent': 'float',
        'scores': 'list[Score]'
    }

    attribute_map = {
        'user': 'user',
        'total_score': 'totalScore',
        'total_time_spent': 'totalTimeSpent',
        'scores': 'scores'
    }

    def __init__(self, user=None, total_score=None, total_time_spent=None, scores=None):  # noqa: E501
        """UserScore - a model defined in Swagger"""  # noqa: E501
        self._user = None
        self._total_score = None
        self._total_time_spent = None
        self._scores = None
        self.discriminator = None
        self.user = user
        self.total_score = total_score
        self.total_time_spent = total_time_spent
        self.scores = scores

    @property
    def user(self):
        """Gets the user of this UserScore.  # noqa: E501


        :return: The user of this UserScore.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserScore.


        :param user: The user of this UserScore.  # noqa: E501
        :type: User
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def total_score(self):
        """Gets the total_score of this UserScore.  # noqa: E501


        :return: The total_score of this UserScore.  # noqa: E501
        :rtype: int
        """
        return self._total_score

    @total_score.setter
    def total_score(self, total_score):
        """Sets the total_score of this UserScore.


        :param total_score: The total_score of this UserScore.  # noqa: E501
        :type: int
        """
        if total_score is None:
            raise ValueError("Invalid value for `total_score`, must not be `None`")  # noqa: E501

        self._total_score = total_score

    @property
    def total_time_spent(self):
        """Gets the total_time_spent of this UserScore.  # noqa: E501


        :return: The total_time_spent of this UserScore.  # noqa: E501
        :rtype: float
        """
        return self._total_time_spent

    @total_time_spent.setter
    def total_time_spent(self, total_time_spent):
        """Sets the total_time_spent of this UserScore.


        :param total_time_spent: The total_time_spent of this UserScore.  # noqa: E501
        :type: float
        """
        if total_time_spent is None:
            raise ValueError("Invalid value for `total_time_spent`, must not be `None`")  # noqa: E501

        self._total_time_spent = total_time_spent

    @property
    def scores(self):
        """Gets the scores of this UserScore.  # noqa: E501


        :return: The scores of this UserScore.  # noqa: E501
        :rtype: list[Score]
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        """Sets the scores of this UserScore.


        :param scores: The scores of this UserScore.  # noqa: E501
        :type: list[Score]
        """
        if scores is None:
            raise ValueError("Invalid value for `scores`, must not be `None`")  # noqa: E501

        self._scores = scores

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
        if issubclass(UserScore, dict):
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
        if not isinstance(other, UserScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
