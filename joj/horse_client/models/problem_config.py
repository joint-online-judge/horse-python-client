# coding: utf-8

"""
    JOJ Horse

    Git version: 07316f1@2022-02-19T10:40:47Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemConfig(object):
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
        'languages': 'list[str]',
        'commit_id': 'str',
        'committer_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'commit_message': 'commitMessage',
        'data_version': 'dataVersion',
        'languages': 'languages',
        'commit_id': 'commitId',
        'committer_id': 'committerId'
    }

    def __init__(self, id=None, commit_message='', data_version=2, languages=None, commit_id='', committer_id=None):  # noqa: E501
        """ProblemConfig - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._commit_message = None
        self._data_version = None
        self._languages = None
        self._commit_id = None
        self._committer_id = None
        self.discriminator = None
        self.id = id
        if commit_message is not None:
            self.commit_message = commit_message
        if data_version is not None:
            self.data_version = data_version
        if languages is not None:
            self.languages = languages
        if commit_id is not None:
            self.commit_id = commit_id
        if committer_id is not None:
            self.committer_id = committer_id

    @property
    def id(self):
        """Gets the id of this ProblemConfig.  # noqa: E501


        :return: The id of this ProblemConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProblemConfig.


        :param id: The id of this ProblemConfig.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def commit_message(self):
        """Gets the commit_message of this ProblemConfig.  # noqa: E501


        :return: The commit_message of this ProblemConfig.  # noqa: E501
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this ProblemConfig.


        :param commit_message: The commit_message of this ProblemConfig.  # noqa: E501
        :type: str
        """

        self._commit_message = commit_message

    @property
    def data_version(self):
        """Gets the data_version of this ProblemConfig.  # noqa: E501


        :return: The data_version of this ProblemConfig.  # noqa: E501
        :rtype: int
        """
        return self._data_version

    @data_version.setter
    def data_version(self, data_version):
        """Sets the data_version of this ProblemConfig.


        :param data_version: The data_version of this ProblemConfig.  # noqa: E501
        :type: int
        """

        self._data_version = data_version

    @property
    def languages(self):
        """Gets the languages of this ProblemConfig.  # noqa: E501


        :return: The languages of this ProblemConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this ProblemConfig.


        :param languages: The languages of this ProblemConfig.  # noqa: E501
        :type: list[str]
        """

        self._languages = languages

    @property
    def commit_id(self):
        """Gets the commit_id of this ProblemConfig.  # noqa: E501


        :return: The commit_id of this ProblemConfig.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this ProblemConfig.


        :param commit_id: The commit_id of this ProblemConfig.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def committer_id(self):
        """Gets the committer_id of this ProblemConfig.  # noqa: E501


        :return: The committer_id of this ProblemConfig.  # noqa: E501
        :rtype: str
        """
        return self._committer_id

    @committer_id.setter
    def committer_id(self, committer_id):
        """Sets the committer_id of this ProblemConfig.


        :param committer_id: The committer_id of this ProblemConfig.  # noqa: E501
        :type: str
        """

        self._committer_id = committer_id

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
        if issubclass(ProblemConfig, dict):
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
        if not isinstance(other, ProblemConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
