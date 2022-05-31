# coding: utf-8

"""
    JOJ Horse

    Git version: c4a9464@2022-05-31T05:05:16Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DiffList(object):
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
        'pagination': 'Pagination',
        'results': 'list[Diff]'
    }

    attribute_map = {
        'pagination': 'pagination',
        'results': 'results'
    }

    def __init__(self, pagination=None, results=None):  # noqa: E501
        """DiffList - a model defined in Swagger"""  # noqa: E501
        self._pagination = None
        self._results = None
        self.discriminator = None
        self.pagination = pagination
        self.results = results

    @property
    def pagination(self):
        """Gets the pagination of this DiffList.  # noqa: E501


        :return: The pagination of this DiffList.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this DiffList.


        :param pagination: The pagination of this DiffList.  # noqa: E501
        :type: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")  # noqa: E501

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this DiffList.  # noqa: E501


        :return: The results of this DiffList.  # noqa: E501
        :rtype: list[Diff]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DiffList.


        :param results: The results of this DiffList.  # noqa: E501
        :type: list[Diff]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if issubclass(DiffList, dict):
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
        if not isinstance(other, DiffList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
