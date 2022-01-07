# coding: utf-8

"""
    JOJ Horse

    Git version: ece3890@2022-01-07T15:40:26Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemPreviewWithLatestRecord(object):
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
        'hidden': 'bool',
        'owner_id': 'str',
        'latest_record': 'RecordPreview'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'title': 'title',
        'hidden': 'hidden',
        'owner_id': 'ownerId',
        'latest_record': 'latestRecord'
    }

    def __init__(self, id=None, url='', title=None, hidden=False, owner_id=None, latest_record=None):  # noqa: E501
        """ProblemPreviewWithLatestRecord - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._title = None
        self._hidden = None
        self._owner_id = None
        self._latest_record = None
        self.discriminator = None
        self.id = id
        if url is not None:
            self.url = url
        self.title = title
        if hidden is not None:
            self.hidden = hidden
        if owner_id is not None:
            self.owner_id = owner_id
        if latest_record is not None:
            self.latest_record = latest_record

    @property
    def id(self):
        """Gets the id of this ProblemPreviewWithLatestRecord.  # noqa: E501


        :return: The id of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProblemPreviewWithLatestRecord.


        :param id: The id of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def url(self):
        """Gets the url of this ProblemPreviewWithLatestRecord.  # noqa: E501

        (unique) url of the domain  # noqa: E501

        :return: The url of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProblemPreviewWithLatestRecord.

        (unique) url of the domain  # noqa: E501

        :param url: The url of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def title(self):
        """Gets the title of this ProblemPreviewWithLatestRecord.  # noqa: E501

        title of the problem  # noqa: E501

        :return: The title of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemPreviewWithLatestRecord.

        title of the problem  # noqa: E501

        :param title: The title of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def hidden(self):
        """Gets the hidden of this ProblemPreviewWithLatestRecord.  # noqa: E501

        is the problem hidden  # noqa: E501

        :return: The hidden of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ProblemPreviewWithLatestRecord.

        is the problem hidden  # noqa: E501

        :param hidden: The hidden of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def owner_id(self):
        """Gets the owner_id of this ProblemPreviewWithLatestRecord.  # noqa: E501


        :return: The owner_id of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ProblemPreviewWithLatestRecord.


        :param owner_id: The owner_id of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def latest_record(self):
        """Gets the latest_record of this ProblemPreviewWithLatestRecord.  # noqa: E501


        :return: The latest_record of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :rtype: RecordPreview
        """
        return self._latest_record

    @latest_record.setter
    def latest_record(self, latest_record):
        """Sets the latest_record of this ProblemPreviewWithLatestRecord.


        :param latest_record: The latest_record of this ProblemPreviewWithLatestRecord.  # noqa: E501
        :type: RecordPreview
        """

        self._latest_record = latest_record

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
        if issubclass(ProblemPreviewWithLatestRecord, dict):
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
        if not isinstance(other, ProblemPreviewWithLatestRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
