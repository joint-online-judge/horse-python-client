# coding: utf-8

"""
    JOJ Horse

    Git version: f6a791e@2021-11-27T07:58:36Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserAccessKey(object):
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
        'service': 'str',
        'access_key_id': 'str',
        'secret_access_key': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'service': 'service',
        'access_key_id': 'accessKeyId',
        'secret_access_key': 'secretAccessKey',
        'user_id': 'userId'
    }

    def __init__(self, id=None, service=None, access_key_id=None, secret_access_key=None, user_id=None):  # noqa: E501
        """UserAccessKey - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._service = None
        self._access_key_id = None
        self._secret_access_key = None
        self._user_id = None
        self.discriminator = None
        self.id = id
        self.service = service
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.user_id = user_id

    @property
    def id(self):
        """Gets the id of this UserAccessKey.  # noqa: E501


        :return: The id of this UserAccessKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAccessKey.


        :param id: The id of this UserAccessKey.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def service(self):
        """Gets the service of this UserAccessKey.  # noqa: E501


        :return: The service of this UserAccessKey.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this UserAccessKey.


        :param service: The service of this UserAccessKey.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def access_key_id(self):
        """Gets the access_key_id of this UserAccessKey.  # noqa: E501


        :return: The access_key_id of this UserAccessKey.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this UserAccessKey.


        :param access_key_id: The access_key_id of this UserAccessKey.  # noqa: E501
        :type: str
        """
        if access_key_id is None:
            raise ValueError("Invalid value for `access_key_id`, must not be `None`")  # noqa: E501

        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this UserAccessKey.  # noqa: E501


        :return: The secret_access_key of this UserAccessKey.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this UserAccessKey.


        :param secret_access_key: The secret_access_key of this UserAccessKey.  # noqa: E501
        :type: str
        """
        if secret_access_key is None:
            raise ValueError("Invalid value for `secret_access_key`, must not be `None`")  # noqa: E501

        self._secret_access_key = secret_access_key

    @property
    def user_id(self):
        """Gets the user_id of this UserAccessKey.  # noqa: E501


        :return: The user_id of this UserAccessKey.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserAccessKey.


        :param user_id: The user_id of this UserAccessKey.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if issubclass(UserAccessKey, dict):
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
        if not isinstance(other, UserAccessKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
