# coding: utf-8

"""
    JOJ Horse

    Git version: 9b73af8@2022-05-02T19:19:37Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RecordPreview(object):
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
        'state': 'RecordState',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, state=None, created_at=None):  # noqa: E501
        """RecordPreview - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._state = None
        self._created_at = None
        self.discriminator = None
        self.id = id
        self.state = state
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this RecordPreview.  # noqa: E501


        :return: The id of this RecordPreview.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecordPreview.


        :param id: The id of this RecordPreview.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def state(self):
        """Gets the state of this RecordPreview.  # noqa: E501


        :return: The state of this RecordPreview.  # noqa: E501
        :rtype: RecordState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RecordPreview.


        :param state: The state of this RecordPreview.  # noqa: E501
        :type: RecordState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this RecordPreview.  # noqa: E501


        :return: The created_at of this RecordPreview.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RecordPreview.


        :param created_at: The created_at of this RecordPreview.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if issubclass(RecordPreview, dict):
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
        if not isinstance(other, RecordPreview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
