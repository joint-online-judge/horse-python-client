# coding: utf-8

"""
    JOJ Horse

    Git version: f04fcdd@2022-05-14T19:01:31Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class JudgerCredentials(object):
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
        'access_key_id': 'str',
        'secret_access_key': 'str',
        'problem_config_repo_name': 'str',
        'problem_config_commit_id': 'str',
        'record_repo_name': 'str',
        'record_commit_id': 'str'
    }

    attribute_map = {
        'access_key_id': 'accessKeyId',
        'secret_access_key': 'secretAccessKey',
        'problem_config_repo_name': 'problemConfigRepoName',
        'problem_config_commit_id': 'problemConfigCommitId',
        'record_repo_name': 'recordRepoName',
        'record_commit_id': 'recordCommitId'
    }

    def __init__(self, access_key_id=None, secret_access_key=None, problem_config_repo_name=None, problem_config_commit_id=None, record_repo_name=None, record_commit_id=None):  # noqa: E501
        """JudgerCredentials - a model defined in Swagger"""  # noqa: E501
        self._access_key_id = None
        self._secret_access_key = None
        self._problem_config_repo_name = None
        self._problem_config_commit_id = None
        self._record_repo_name = None
        self._record_commit_id = None
        self.discriminator = None
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.problem_config_repo_name = problem_config_repo_name
        self.problem_config_commit_id = problem_config_commit_id
        self.record_repo_name = record_repo_name
        self.record_commit_id = record_commit_id

    @property
    def access_key_id(self):
        """Gets the access_key_id of this JudgerCredentials.  # noqa: E501


        :return: The access_key_id of this JudgerCredentials.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this JudgerCredentials.


        :param access_key_id: The access_key_id of this JudgerCredentials.  # noqa: E501
        :type: str
        """
        if access_key_id is None:
            raise ValueError("Invalid value for `access_key_id`, must not be `None`")  # noqa: E501

        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this JudgerCredentials.  # noqa: E501


        :return: The secret_access_key of this JudgerCredentials.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this JudgerCredentials.


        :param secret_access_key: The secret_access_key of this JudgerCredentials.  # noqa: E501
        :type: str
        """
        if secret_access_key is None:
            raise ValueError("Invalid value for `secret_access_key`, must not be `None`")  # noqa: E501

        self._secret_access_key = secret_access_key

    @property
    def problem_config_repo_name(self):
        """Gets the problem_config_repo_name of this JudgerCredentials.  # noqa: E501


        :return: The problem_config_repo_name of this JudgerCredentials.  # noqa: E501
        :rtype: str
        """
        return self._problem_config_repo_name

    @problem_config_repo_name.setter
    def problem_config_repo_name(self, problem_config_repo_name):
        """Sets the problem_config_repo_name of this JudgerCredentials.


        :param problem_config_repo_name: The problem_config_repo_name of this JudgerCredentials.  # noqa: E501
        :type: str
        """
        if problem_config_repo_name is None:
            raise ValueError("Invalid value for `problem_config_repo_name`, must not be `None`")  # noqa: E501

        self._problem_config_repo_name = problem_config_repo_name

    @property
    def problem_config_commit_id(self):
        """Gets the problem_config_commit_id of this JudgerCredentials.  # noqa: E501


        :return: The problem_config_commit_id of this JudgerCredentials.  # noqa: E501
        :rtype: str
        """
        return self._problem_config_commit_id

    @problem_config_commit_id.setter
    def problem_config_commit_id(self, problem_config_commit_id):
        """Sets the problem_config_commit_id of this JudgerCredentials.


        :param problem_config_commit_id: The problem_config_commit_id of this JudgerCredentials.  # noqa: E501
        :type: str
        """
        if problem_config_commit_id is None:
            raise ValueError("Invalid value for `problem_config_commit_id`, must not be `None`")  # noqa: E501

        self._problem_config_commit_id = problem_config_commit_id

    @property
    def record_repo_name(self):
        """Gets the record_repo_name of this JudgerCredentials.  # noqa: E501


        :return: The record_repo_name of this JudgerCredentials.  # noqa: E501
        :rtype: str
        """
        return self._record_repo_name

    @record_repo_name.setter
    def record_repo_name(self, record_repo_name):
        """Sets the record_repo_name of this JudgerCredentials.


        :param record_repo_name: The record_repo_name of this JudgerCredentials.  # noqa: E501
        :type: str
        """
        if record_repo_name is None:
            raise ValueError("Invalid value for `record_repo_name`, must not be `None`")  # noqa: E501

        self._record_repo_name = record_repo_name

    @property
    def record_commit_id(self):
        """Gets the record_commit_id of this JudgerCredentials.  # noqa: E501


        :return: The record_commit_id of this JudgerCredentials.  # noqa: E501
        :rtype: str
        """
        return self._record_commit_id

    @record_commit_id.setter
    def record_commit_id(self, record_commit_id):
        """Sets the record_commit_id of this JudgerCredentials.


        :param record_commit_id: The record_commit_id of this JudgerCredentials.  # noqa: E501
        :type: str
        """
        if record_commit_id is None:
            raise ValueError("Invalid value for `record_commit_id`, must not be `None`")  # noqa: E501

        self._record_commit_id = record_commit_id

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
        if issubclass(JudgerCredentials, dict):
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
        if not isinstance(other, JudgerCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
