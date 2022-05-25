# coding: utf-8

"""
    JOJ Horse

    Git version: 2d4bf09@2022-05-25T04:20:17Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Pagination(object):
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
        'has_more': 'bool',
        'next_offset': 'str',
        'results': 'int',
        'max_per_page': 'int'
    }

    attribute_map = {
        'has_more': 'has_more',
        'next_offset': 'next_offset',
        'results': 'results',
        'max_per_page': 'max_per_page'
    }

    def __init__(self, has_more=None, next_offset=None, results=None, max_per_page=None):  # noqa: E501
        """Pagination - a model defined in Swagger"""  # noqa: E501
        self._has_more = None
        self._next_offset = None
        self._results = None
        self._max_per_page = None
        self.discriminator = None
        self.has_more = has_more
        self.next_offset = next_offset
        self.results = results
        self.max_per_page = max_per_page

    @property
    def has_more(self):
        """Gets the has_more of this Pagination.  # noqa: E501


        :return: The has_more of this Pagination.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this Pagination.


        :param has_more: The has_more of this Pagination.  # noqa: E501
        :type: bool
        """
        if has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")  # noqa: E501

        self._has_more = has_more

    @property
    def next_offset(self):
        """Gets the next_offset of this Pagination.  # noqa: E501


        :return: The next_offset of this Pagination.  # noqa: E501
        :rtype: str
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this Pagination.


        :param next_offset: The next_offset of this Pagination.  # noqa: E501
        :type: str
        """
        if next_offset is None:
            raise ValueError("Invalid value for `next_offset`, must not be `None`")  # noqa: E501

        self._next_offset = next_offset

    @property
    def results(self):
        """Gets the results of this Pagination.  # noqa: E501


        :return: The results of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this Pagination.


        :param results: The results of this Pagination.  # noqa: E501
        :type: int
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def max_per_page(self):
        """Gets the max_per_page of this Pagination.  # noqa: E501


        :return: The max_per_page of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._max_per_page

    @max_per_page.setter
    def max_per_page(self, max_per_page):
        """Sets the max_per_page of this Pagination.


        :param max_per_page: The max_per_page of this Pagination.  # noqa: E501
        :type: int
        """
        if max_per_page is None:
            raise ValueError("Invalid value for `max_per_page`, must not be `None`")  # noqa: E501

        self._max_per_page = max_per_page

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
        if issubclass(Pagination, dict):
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
        if not isinstance(other, Pagination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
