# coding: utf-8

"""
    JOJ Horse

    Git version: bd11f07@2021-11-03T11:20:31Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RecordPermission(object):
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
        'view': 'bool',
        'detail': 'bool',
        'code': 'bool',
        'judge': 'bool',
        'rejudge': 'bool'
    }

    attribute_map = {
        'view': 'view',
        'detail': 'detail',
        'code': 'code',
        'judge': 'judge',
        'rejudge': 'rejudge'
    }

    def __init__(self, view=True, detail=False, code=False, judge=False, rejudge=False):  # noqa: E501
        """RecordPermission - a model defined in Swagger"""  # noqa: E501
        self._view = None
        self._detail = None
        self._code = None
        self._judge = None
        self._rejudge = None
        self.discriminator = None
        if view is not None:
            self.view = view
        if detail is not None:
            self.detail = detail
        if code is not None:
            self.code = code
        if judge is not None:
            self.judge = judge
        if rejudge is not None:
            self.rejudge = rejudge

    @property
    def view(self):
        """Gets the view of this RecordPermission.  # noqa: E501


        :return: The view of this RecordPermission.  # noqa: E501
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this RecordPermission.


        :param view: The view of this RecordPermission.  # noqa: E501
        :type: bool
        """

        self._view = view

    @property
    def detail(self):
        """Gets the detail of this RecordPermission.  # noqa: E501


        :return: The detail of this RecordPermission.  # noqa: E501
        :rtype: bool
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this RecordPermission.


        :param detail: The detail of this RecordPermission.  # noqa: E501
        :type: bool
        """

        self._detail = detail

    @property
    def code(self):
        """Gets the code of this RecordPermission.  # noqa: E501


        :return: The code of this RecordPermission.  # noqa: E501
        :rtype: bool
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RecordPermission.


        :param code: The code of this RecordPermission.  # noqa: E501
        :type: bool
        """

        self._code = code

    @property
    def judge(self):
        """Gets the judge of this RecordPermission.  # noqa: E501


        :return: The judge of this RecordPermission.  # noqa: E501
        :rtype: bool
        """
        return self._judge

    @judge.setter
    def judge(self, judge):
        """Sets the judge of this RecordPermission.


        :param judge: The judge of this RecordPermission.  # noqa: E501
        :type: bool
        """

        self._judge = judge

    @property
    def rejudge(self):
        """Gets the rejudge of this RecordPermission.  # noqa: E501


        :return: The rejudge of this RecordPermission.  # noqa: E501
        :rtype: bool
        """
        return self._rejudge

    @rejudge.setter
    def rejudge(self, rejudge):
        """Sets the rejudge of this RecordPermission.


        :param rejudge: The rejudge of this RecordPermission.  # noqa: E501
        :type: bool
        """

        self._rejudge = rejudge

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
        if issubclass(RecordPermission, dict):
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
        if not isinstance(other, RecordPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
