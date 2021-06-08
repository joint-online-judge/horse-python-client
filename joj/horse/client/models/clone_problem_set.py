# coding: utf-8

"""
    JOJ Horse

    Git version: dad896a@2021-06-08 19:53:00  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CloneProblemSet(object):
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
        'problem_set': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'url': 'url',
        'problem_set': 'problem_set',
        'domain': 'domain'
    }

    def __init__(self, url=None, problem_set=None, domain=None):  # noqa: E501
        """CloneProblemSet - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._problem_set = None
        self._domain = None
        self.discriminator = None
        if url is not None:
            self.url = url
        self.problem_set = problem_set
        self.domain = domain

    @property
    def url(self):
        """Gets the url of this CloneProblemSet.  # noqa: E501

        url of the cloned problem set  # noqa: E501

        :return: The url of this CloneProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CloneProblemSet.

        url of the cloned problem set  # noqa: E501

        :param url: The url of this CloneProblemSet.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def problem_set(self):
        """Gets the problem_set of this CloneProblemSet.  # noqa: E501

        url or ObjectId of the problem set  # noqa: E501

        :return: The problem_set of this CloneProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._problem_set

    @problem_set.setter
    def problem_set(self, problem_set):
        """Sets the problem_set of this CloneProblemSet.

        url or ObjectId of the problem set  # noqa: E501

        :param problem_set: The problem_set of this CloneProblemSet.  # noqa: E501
        :type: str
        """
        if problem_set is None:
            raise ValueError("Invalid value for `problem_set`, must not be `None`")  # noqa: E501

        self._problem_set = problem_set

    @property
    def domain(self):
        """Gets the domain of this CloneProblemSet.  # noqa: E501

        url or ObjectId of the domain  # noqa: E501

        :return: The domain of this CloneProblemSet.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CloneProblemSet.

        url or ObjectId of the domain  # noqa: E501

        :param domain: The domain of this CloneProblemSet.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

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
        if issubclass(CloneProblemSet, dict):
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
        if not isinstance(other, CloneProblemSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
