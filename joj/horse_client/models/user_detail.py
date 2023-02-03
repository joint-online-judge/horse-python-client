# coding: utf-8

"""
    JOJ Horse

    Git version: c2626d3@2023-02-03T07:14:12Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserDetail(object):
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
        'username': 'str',
        'gravatar': 'str',
        'role': 'str',
        'is_active': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'email': 'str',
        'student_id': 'str',
        'real_name': 'str',
        'register_ip': 'str',
        'login_at': 'datetime',
        'login_ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'gravatar': 'gravatar',
        'role': 'role',
        'is_active': 'isActive',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'email': 'email',
        'student_id': 'studentId',
        'real_name': 'realName',
        'register_ip': 'registerIp',
        'login_at': 'loginAt',
        'login_ip': 'loginIp'
    }

    def __init__(self, id=None, username=None, gravatar='', role='user', is_active=False, created_at=None, updated_at=None, email=None, student_id='', real_name='', register_ip=None, login_at=None, login_ip=None):  # noqa: E501
        """UserDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._gravatar = None
        self._role = None
        self._is_active = None
        self._created_at = None
        self._updated_at = None
        self._email = None
        self._student_id = None
        self._real_name = None
        self._register_ip = None
        self._login_at = None
        self._login_ip = None
        self.discriminator = None
        self.id = id
        self.username = username
        if gravatar is not None:
            self.gravatar = gravatar
        if role is not None:
            self.role = role
        if is_active is not None:
            self.is_active = is_active
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.email = email
        if student_id is not None:
            self.student_id = student_id
        if real_name is not None:
            self.real_name = real_name
        self.register_ip = register_ip
        self.login_at = login_at
        self.login_ip = login_ip

    @property
    def id(self):
        """Gets the id of this UserDetail.  # noqa: E501


        :return: The id of this UserDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDetail.


        :param id: The id of this UserDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this UserDetail.  # noqa: E501


        :return: The username of this UserDetail.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserDetail.


        :param username: The username of this UserDetail.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def gravatar(self):
        """Gets the gravatar of this UserDetail.  # noqa: E501


        :return: The gravatar of this UserDetail.  # noqa: E501
        :rtype: str
        """
        return self._gravatar

    @gravatar.setter
    def gravatar(self, gravatar):
        """Sets the gravatar of this UserDetail.


        :param gravatar: The gravatar of this UserDetail.  # noqa: E501
        :type: str
        """

        self._gravatar = gravatar

    @property
    def role(self):
        """Gets the role of this UserDetail.  # noqa: E501


        :return: The role of this UserDetail.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserDetail.


        :param role: The role of this UserDetail.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def is_active(self):
        """Gets the is_active of this UserDetail.  # noqa: E501


        :return: The is_active of this UserDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this UserDetail.


        :param is_active: The is_active of this UserDetail.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def created_at(self):
        """Gets the created_at of this UserDetail.  # noqa: E501


        :return: The created_at of this UserDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserDetail.


        :param created_at: The created_at of this UserDetail.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UserDetail.  # noqa: E501


        :return: The updated_at of this UserDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserDetail.


        :param updated_at: The updated_at of this UserDetail.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def email(self):
        """Gets the email of this UserDetail.  # noqa: E501


        :return: The email of this UserDetail.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserDetail.


        :param email: The email of this UserDetail.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def student_id(self):
        """Gets the student_id of this UserDetail.  # noqa: E501


        :return: The student_id of this UserDetail.  # noqa: E501
        :rtype: str
        """
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        """Sets the student_id of this UserDetail.


        :param student_id: The student_id of this UserDetail.  # noqa: E501
        :type: str
        """

        self._student_id = student_id

    @property
    def real_name(self):
        """Gets the real_name of this UserDetail.  # noqa: E501


        :return: The real_name of this UserDetail.  # noqa: E501
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """Sets the real_name of this UserDetail.


        :param real_name: The real_name of this UserDetail.  # noqa: E501
        :type: str
        """

        self._real_name = real_name

    @property
    def register_ip(self):
        """Gets the register_ip of this UserDetail.  # noqa: E501


        :return: The register_ip of this UserDetail.  # noqa: E501
        :rtype: str
        """
        return self._register_ip

    @register_ip.setter
    def register_ip(self, register_ip):
        """Sets the register_ip of this UserDetail.


        :param register_ip: The register_ip of this UserDetail.  # noqa: E501
        :type: str
        """
        if register_ip is None:
            raise ValueError("Invalid value for `register_ip`, must not be `None`")  # noqa: E501

        self._register_ip = register_ip

    @property
    def login_at(self):
        """Gets the login_at of this UserDetail.  # noqa: E501


        :return: The login_at of this UserDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._login_at

    @login_at.setter
    def login_at(self, login_at):
        """Sets the login_at of this UserDetail.


        :param login_at: The login_at of this UserDetail.  # noqa: E501
        :type: datetime
        """
        if login_at is None:
            raise ValueError("Invalid value for `login_at`, must not be `None`")  # noqa: E501

        self._login_at = login_at

    @property
    def login_ip(self):
        """Gets the login_ip of this UserDetail.  # noqa: E501


        :return: The login_ip of this UserDetail.  # noqa: E501
        :rtype: str
        """
        return self._login_ip

    @login_ip.setter
    def login_ip(self, login_ip):
        """Sets the login_ip of this UserDetail.


        :param login_ip: The login_ip of this UserDetail.  # noqa: E501
        :type: str
        """
        if login_ip is None:
            raise ValueError("Invalid value for `login_ip`, must not be `None`")  # noqa: E501

        self._login_ip = login_ip

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
        if issubclass(UserDetail, dict):
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
        if not isinstance(other, UserDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
