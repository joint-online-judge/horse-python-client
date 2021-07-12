# coding: utf-8

"""
    JOJ Horse

    Git version: a2191d6@2021-07-12 14:52:30  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Domain(object):
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
        'id': 'str',
        'url': 'str',
        'name': 'str',
        'bulletin': 'str',
        'gravatar': 'str',
        'owner': 'AnyOfDomainOwner'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'name': 'name',
        'bulletin': 'bulletin',
        'gravatar': 'gravatar',
        'owner': 'owner'
    }

    def __init__(self, id=None, url=None, name=None, bulletin='', gravatar='', owner=None):  # noqa: E501
        """Domain - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._name = None
        self._bulletin = None
        self._gravatar = None
        self._owner = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.url = url
        self.name = name
        if bulletin is not None:
            self.bulletin = bulletin
        if gravatar is not None:
            self.gravatar = gravatar
        self.owner = owner

    @property
    def id(self):
        """Gets the id of this Domain.  # noqa: E501


        :return: The id of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Domain.


        :param id: The id of this Domain.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this Domain.  # noqa: E501


        :return: The url of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Domain.


        :param url: The url of this Domain.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def name(self):
        """Gets the name of this Domain.  # noqa: E501

        displayed name of the domain  # noqa: E501

        :return: The name of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Domain.

        displayed name of the domain  # noqa: E501

        :param name: The name of this Domain.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def bulletin(self):
        """Gets the bulletin of this Domain.  # noqa: E501

        bulletin of the domain  # noqa: E501

        :return: The bulletin of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._bulletin

    @bulletin.setter
    def bulletin(self, bulletin):
        """Sets the bulletin of this Domain.

        bulletin of the domain  # noqa: E501

        :param bulletin: The bulletin of this Domain.  # noqa: E501
        :type: str
        """

        self._bulletin = bulletin

    @property
    def gravatar(self):
        """Gets the gravatar of this Domain.  # noqa: E501

        gravatar url of the domain  # noqa: E501

        :return: The gravatar of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._gravatar

    @gravatar.setter
    def gravatar(self, gravatar):
        """Sets the gravatar of this Domain.

        gravatar url of the domain  # noqa: E501

        :param gravatar: The gravatar of this Domain.  # noqa: E501
        :type: str
        """

        self._gravatar = gravatar

    @property
    def owner(self):
        """Gets the owner of this Domain.  # noqa: E501


        :return: The owner of this Domain.  # noqa: E501
        :rtype: AnyOfDomainOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Domain.


        :param owner: The owner of this Domain.  # noqa: E501
        :type: AnyOfDomainOwner
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

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
        if issubclass(Domain, dict):
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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
