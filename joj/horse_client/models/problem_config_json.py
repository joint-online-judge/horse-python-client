# coding: utf-8

"""
    JOJ Horse

    Git version: 6a64ecc@2022-05-19T15:50:22Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemConfigJson(object):
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
        'languages': 'list[Language]',
        'language_default': 'LanguageDefault'
    }

    attribute_map = {
        'languages': 'languages',
        'language_default': 'languageDefault'
    }

    def __init__(self, languages=None, language_default=None):  # noqa: E501
        """ProblemConfigJson - a model defined in Swagger"""  # noqa: E501
        self._languages = None
        self._language_default = None
        self.discriminator = None
        self.languages = languages
        if language_default is not None:
            self.language_default = language_default

    @property
    def languages(self):
        """Gets the languages of this ProblemConfigJson.  # noqa: E501


        :return: The languages of this ProblemConfigJson.  # noqa: E501
        :rtype: list[Language]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this ProblemConfigJson.


        :param languages: The languages of this ProblemConfigJson.  # noqa: E501
        :type: list[Language]
        """
        if languages is None:
            raise ValueError("Invalid value for `languages`, must not be `None`")  # noqa: E501

        self._languages = languages

    @property
    def language_default(self):
        """Gets the language_default of this ProblemConfigJson.  # noqa: E501


        :return: The language_default of this ProblemConfigJson.  # noqa: E501
        :rtype: LanguageDefault
        """
        return self._language_default

    @language_default.setter
    def language_default(self, language_default):
        """Sets the language_default of this ProblemConfigJson.


        :param language_default: The language_default of this ProblemConfigJson.  # noqa: E501
        :type: LanguageDefault
        """

        self._language_default = language_default

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
        if issubclass(ProblemConfigJson, dict):
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
        if not isinstance(other, ProblemConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
