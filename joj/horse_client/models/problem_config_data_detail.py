# coding: utf-8

"""
    JOJ Horse

    Git version: 3deba0b@2022-06-02T14:50:42Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemConfigDataDetail(object):
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
        'commit_message': 'str',
        'data_version': 'int',
        'commit_id': 'str',
        'committer_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'data': 'ProblemConfigJson'
    }

    attribute_map = {
        'id': 'id',
        'commit_message': 'commitMessage',
        'data_version': 'dataVersion',
        'commit_id': 'commitId',
        'committer_id': 'committerId',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'data': 'data'
    }

    def __init__(self, id=None, commit_message='', data_version=2, commit_id='', committer_id=None, created_at=None, updated_at=None, data=None):  # noqa: E501
        """ProblemConfigDataDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._commit_message = None
        self._data_version = None
        self._commit_id = None
        self._committer_id = None
        self._created_at = None
        self._updated_at = None
        self._data = None
        self.discriminator = None
        self.id = id
        if commit_message is not None:
            self.commit_message = commit_message
        if data_version is not None:
            self.data_version = data_version
        if commit_id is not None:
            self.commit_id = commit_id
        if committer_id is not None:
            self.committer_id = committer_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.data = data

    @property
    def id(self):
        """Gets the id of this ProblemConfigDataDetail.  # noqa: E501


        :return: The id of this ProblemConfigDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProblemConfigDataDetail.


        :param id: The id of this ProblemConfigDataDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def commit_message(self):
        """Gets the commit_message of this ProblemConfigDataDetail.  # noqa: E501


        :return: The commit_message of this ProblemConfigDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this ProblemConfigDataDetail.


        :param commit_message: The commit_message of this ProblemConfigDataDetail.  # noqa: E501
        :type: str
        """

        self._commit_message = commit_message

    @property
    def data_version(self):
        """Gets the data_version of this ProblemConfigDataDetail.  # noqa: E501


        :return: The data_version of this ProblemConfigDataDetail.  # noqa: E501
        :rtype: int
        """
        return self._data_version

    @data_version.setter
    def data_version(self, data_version):
        """Sets the data_version of this ProblemConfigDataDetail.


        :param data_version: The data_version of this ProblemConfigDataDetail.  # noqa: E501
        :type: int
        """

        self._data_version = data_version

    @property
    def commit_id(self):
        """Gets the commit_id of this ProblemConfigDataDetail.  # noqa: E501


        :return: The commit_id of this ProblemConfigDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this ProblemConfigDataDetail.


        :param commit_id: The commit_id of this ProblemConfigDataDetail.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def committer_id(self):
        """Gets the committer_id of this ProblemConfigDataDetail.  # noqa: E501


        :return: The committer_id of this ProblemConfigDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._committer_id

    @committer_id.setter
    def committer_id(self, committer_id):
        """Sets the committer_id of this ProblemConfigDataDetail.


        :param committer_id: The committer_id of this ProblemConfigDataDetail.  # noqa: E501
        :type: str
        """

        self._committer_id = committer_id

    @property
    def created_at(self):
        """Gets the created_at of this ProblemConfigDataDetail.  # noqa: E501


        :return: The created_at of this ProblemConfigDataDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ProblemConfigDataDetail.


        :param created_at: The created_at of this ProblemConfigDataDetail.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ProblemConfigDataDetail.  # noqa: E501


        :return: The updated_at of this ProblemConfigDataDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ProblemConfigDataDetail.


        :param updated_at: The updated_at of this ProblemConfigDataDetail.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def data(self):
        """Gets the data of this ProblemConfigDataDetail.  # noqa: E501


        :return: The data of this ProblemConfigDataDetail.  # noqa: E501
        :rtype: ProblemConfigJson
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ProblemConfigDataDetail.


        :param data: The data of this ProblemConfigDataDetail.  # noqa: E501
        :type: ProblemConfigJson
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

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
        if issubclass(ProblemConfigDataDetail, dict):
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
        if not isinstance(other, ProblemConfigDataDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
