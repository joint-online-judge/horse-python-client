# coding: utf-8

"""
    JOJ Horse

    Git version: 1b6d8ac@2021-12-10T21:16:20Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainDetail(object):
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
        'gravatar': 'str',
        'bulletin': 'str',
        'hidden': 'bool',
        'tag': 'str',
        'owner_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'name': 'name',
        'gravatar': 'gravatar',
        'bulletin': 'bulletin',
        'hidden': 'hidden',
        'tag': 'tag',
        'owner_id': 'ownerId',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, url='', name=None, gravatar='', bulletin='', hidden=True, tag='', owner_id=None, created_at=None, updated_at=None):  # noqa: E501
        """DomainDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._name = None
        self._gravatar = None
        self._bulletin = None
        self._hidden = None
        self._tag = None
        self._owner_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.id = id
        if url is not None:
            self.url = url
        self.name = name
        if gravatar is not None:
            self.gravatar = gravatar
        if bulletin is not None:
            self.bulletin = bulletin
        if hidden is not None:
            self.hidden = hidden
        if tag is not None:
            self.tag = tag
        if owner_id is not None:
            self.owner_id = owner_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this DomainDetail.  # noqa: E501


        :return: The id of this DomainDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainDetail.


        :param id: The id of this DomainDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def url(self):
        """Gets the url of this DomainDetail.  # noqa: E501

        (unique) url of the domain  # noqa: E501

        :return: The url of this DomainDetail.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DomainDetail.

        (unique) url of the domain  # noqa: E501

        :param url: The url of this DomainDetail.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this DomainDetail.  # noqa: E501

        displayed name of the domain  # noqa: E501

        :return: The name of this DomainDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainDetail.

        displayed name of the domain  # noqa: E501

        :param name: The name of this DomainDetail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def gravatar(self):
        """Gets the gravatar of this DomainDetail.  # noqa: E501

        gravatar url of the domain  # noqa: E501

        :return: The gravatar of this DomainDetail.  # noqa: E501
        :rtype: str
        """
        return self._gravatar

    @gravatar.setter
    def gravatar(self, gravatar):
        """Sets the gravatar of this DomainDetail.

        gravatar url of the domain  # noqa: E501

        :param gravatar: The gravatar of this DomainDetail.  # noqa: E501
        :type: str
        """

        self._gravatar = gravatar

    @property
    def bulletin(self):
        """Gets the bulletin of this DomainDetail.  # noqa: E501

        bulletin of the domain  # noqa: E501

        :return: The bulletin of this DomainDetail.  # noqa: E501
        :rtype: str
        """
        return self._bulletin

    @bulletin.setter
    def bulletin(self, bulletin):
        """Sets the bulletin of this DomainDetail.

        bulletin of the domain  # noqa: E501

        :param bulletin: The bulletin of this DomainDetail.  # noqa: E501
        :type: str
        """

        self._bulletin = bulletin

    @property
    def hidden(self):
        """Gets the hidden of this DomainDetail.  # noqa: E501

        is the domain hidden  # noqa: E501

        :return: The hidden of this DomainDetail.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this DomainDetail.

        is the domain hidden  # noqa: E501

        :param hidden: The hidden of this DomainDetail.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def tag(self):
        """Gets the tag of this DomainDetail.  # noqa: E501

        tag of the domain  # noqa: E501

        :return: The tag of this DomainDetail.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this DomainDetail.

        tag of the domain  # noqa: E501

        :param tag: The tag of this DomainDetail.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def owner_id(self):
        """Gets the owner_id of this DomainDetail.  # noqa: E501


        :return: The owner_id of this DomainDetail.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this DomainDetail.


        :param owner_id: The owner_id of this DomainDetail.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def created_at(self):
        """Gets the created_at of this DomainDetail.  # noqa: E501


        :return: The created_at of this DomainDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DomainDetail.


        :param created_at: The created_at of this DomainDetail.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DomainDetail.  # noqa: E501


        :return: The updated_at of this DomainDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DomainDetail.


        :param updated_at: The updated_at of this DomainDetail.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if issubclass(DomainDetail, dict):
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
        if not isinstance(other, DomainDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
