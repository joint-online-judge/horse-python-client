# coding: utf-8

"""
    JOJ Horse

    Git version: f3b5abe@2022-01-23T23:30:52Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from joj.horse_client.models.general_permission import GeneralPermission  # noqa: F401,E501

class AllOfDomainPermissionGeneral(GeneralPermission):
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
    }
    if hasattr(GeneralPermission, "swagger_types"):
        swagger_types.update(GeneralPermission.swagger_types)

    attribute_map = {
    }
    if hasattr(GeneralPermission, "attribute_map"):
        attribute_map.update(GeneralPermission.attribute_map)

    def __init__(self, *args, **kwargs):  # noqa: E501
        """AllOfDomainPermissionGeneral - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None
        GeneralPermission.__init__(self, *args, **kwargs)

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
        if issubclass(AllOfDomainPermissionGeneral, dict):
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
        if not isinstance(other, AllOfDomainPermissionGeneral):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
