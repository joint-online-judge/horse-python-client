# coding: utf-8

"""
    JOJ Horse

    Git version: 193dff2@2021-12-02T15:06:55Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemPreviewWithRecordState(object):
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
        'title': 'str',
        'content': 'str',
        'hidden': 'bool',
        'owner_id': 'str',
        'record_id': 'str',
        'record_state': 'RecordState'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'title': 'title',
        'content': 'content',
        'hidden': 'hidden',
        'owner_id': 'ownerId',
        'record_id': 'recordId',
        'record_state': 'recordState'
    }

    def __init__(self, id=None, url='', title=None, content='', hidden=False, owner_id=None, record_id=None, record_state=None):  # noqa: E501
        """ProblemPreviewWithRecordState - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._title = None
        self._content = None
        self._hidden = None
        self._owner_id = None
        self._record_id = None
        self._record_state = None
        self.discriminator = None
        self.id = id
        if url is not None:
            self.url = url
        self.title = title
        if content is not None:
            self.content = content
        if hidden is not None:
            self.hidden = hidden
        if owner_id is not None:
            self.owner_id = owner_id
        if record_id is not None:
            self.record_id = record_id
        if record_state is not None:
            self.record_state = record_state

    @property
    def id(self):
        """Gets the id of this ProblemPreviewWithRecordState.  # noqa: E501


        :return: The id of this ProblemPreviewWithRecordState.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProblemPreviewWithRecordState.


        :param id: The id of this ProblemPreviewWithRecordState.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def url(self):
        """Gets the url of this ProblemPreviewWithRecordState.  # noqa: E501

        (unique) url of the domain  # noqa: E501

        :return: The url of this ProblemPreviewWithRecordState.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProblemPreviewWithRecordState.

        (unique) url of the domain  # noqa: E501

        :param url: The url of this ProblemPreviewWithRecordState.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def title(self):
        """Gets the title of this ProblemPreviewWithRecordState.  # noqa: E501

        title of the problem  # noqa: E501

        :return: The title of this ProblemPreviewWithRecordState.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemPreviewWithRecordState.

        title of the problem  # noqa: E501

        :param title: The title of this ProblemPreviewWithRecordState.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def content(self):
        """Gets the content of this ProblemPreviewWithRecordState.  # noqa: E501

        content of the problem  # noqa: E501

        :return: The content of this ProblemPreviewWithRecordState.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ProblemPreviewWithRecordState.

        content of the problem  # noqa: E501

        :param content: The content of this ProblemPreviewWithRecordState.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def hidden(self):
        """Gets the hidden of this ProblemPreviewWithRecordState.  # noqa: E501

        is the problem hidden  # noqa: E501

        :return: The hidden of this ProblemPreviewWithRecordState.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ProblemPreviewWithRecordState.

        is the problem hidden  # noqa: E501

        :param hidden: The hidden of this ProblemPreviewWithRecordState.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def owner_id(self):
        """Gets the owner_id of this ProblemPreviewWithRecordState.  # noqa: E501


        :return: The owner_id of this ProblemPreviewWithRecordState.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ProblemPreviewWithRecordState.


        :param owner_id: The owner_id of this ProblemPreviewWithRecordState.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def record_id(self):
        """Gets the record_id of this ProblemPreviewWithRecordState.  # noqa: E501


        :return: The record_id of this ProblemPreviewWithRecordState.  # noqa: E501
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this ProblemPreviewWithRecordState.


        :param record_id: The record_id of this ProblemPreviewWithRecordState.  # noqa: E501
        :type: str
        """

        self._record_id = record_id

    @property
    def record_state(self):
        """Gets the record_state of this ProblemPreviewWithRecordState.  # noqa: E501


        :return: The record_state of this ProblemPreviewWithRecordState.  # noqa: E501
        :rtype: RecordState
        """
        return self._record_state

    @record_state.setter
    def record_state(self, record_state):
        """Sets the record_state of this ProblemPreviewWithRecordState.


        :param record_state: The record_state of this ProblemPreviewWithRecordState.  # noqa: E501
        :type: RecordState
        """

        self._record_state = record_state

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
        if issubclass(ProblemPreviewWithRecordState, dict):
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
        if not isinstance(other, ProblemPreviewWithRecordState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
