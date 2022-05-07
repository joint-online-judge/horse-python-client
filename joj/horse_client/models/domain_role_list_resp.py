# coding: utf-8

"""
    JOJ Horse

    Git version: a4439e0@2022-05-07T19:56:21Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainRoleListResp(object):
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
        'error_code': 'ErrorCode',
        'error_msg': 'str',
        'data': 'DomainRoleList'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_msg': 'errorMsg',
        'data': 'data'
    }

    def __init__(self, error_code=None, error_msg=None, data=None):  # noqa: E501
        """DomainRoleListResp - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._error_msg = None
        self._data = None
        self.discriminator = None
        self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if data is not None:
            self.data = data

    @property
    def error_code(self):
        """Gets the error_code of this DomainRoleListResp.  # noqa: E501


        :return: The error_code of this DomainRoleListResp.  # noqa: E501
        :rtype: ErrorCode
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this DomainRoleListResp.


        :param error_code: The error_code of this DomainRoleListResp.  # noqa: E501
        :type: ErrorCode
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this DomainRoleListResp.  # noqa: E501


        :return: The error_msg of this DomainRoleListResp.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this DomainRoleListResp.


        :param error_msg: The error_msg of this DomainRoleListResp.  # noqa: E501
        :type: str
        """

        self._error_msg = error_msg

    @property
    def data(self):
        """Gets the data of this DomainRoleListResp.  # noqa: E501


        :return: The data of this DomainRoleListResp.  # noqa: E501
        :rtype: DomainRoleList
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DomainRoleListResp.


        :param data: The data of this DomainRoleListResp.  # noqa: E501
        :type: DomainRoleList
        """

        self._data = data

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
        if issubclass(DomainRoleListResp, dict):
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
        if not isinstance(other, DomainRoleListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
