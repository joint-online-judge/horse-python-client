# coding: utf-8

"""
    JOJ Horse

    Git version: d436ddf@2021-11-06T09:32:11Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
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
        'url': 'str',
        'name': 'str',
        'gravatar': 'str',
        'bulletin': 'str',
        'hidden': 'bool',
        'id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'owner_id': 'str'
    }

    attribute_map = {
        'url': 'url',
        'name': 'name',
        'gravatar': 'gravatar',
        'bulletin': 'bulletin',
        'hidden': 'hidden',
        'id': 'id',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'owner_id': 'ownerId'
    }

    def __init__(self, url=None, name=None, gravatar='', bulletin='', hidden=True, id=None, created_at=None, updated_at=None, owner_id=None):  # noqa: E501
        """Domain - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._name = None
        self._gravatar = None
        self._bulletin = None
        self._hidden = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._owner_id = None
        self.discriminator = None
        self.url = url
        self.name = name
        if gravatar is not None:
            self.gravatar = gravatar
        if bulletin is not None:
            self.bulletin = bulletin
        if hidden is not None:
            self.hidden = hidden
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.owner_id = owner_id

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
    def hidden(self):
        """Gets the hidden of this Domain.  # noqa: E501

        is the domain hidden  # noqa: E501

        :return: The hidden of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Domain.

        is the domain hidden  # noqa: E501

        :param hidden: The hidden of this Domain.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

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
    def created_at(self):
        """Gets the created_at of this Domain.  # noqa: E501


        :return: The created_at of this Domain.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Domain.


        :param created_at: The created_at of this Domain.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Domain.  # noqa: E501


        :return: The updated_at of this Domain.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Domain.


        :param updated_at: The updated_at of this Domain.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def owner_id(self):
        """Gets the owner_id of this Domain.  # noqa: E501


        :return: The owner_id of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Domain.


        :param owner_id: The owner_id of this Domain.  # noqa: E501
        :type: str
        """
        if owner_id is None:
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

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
