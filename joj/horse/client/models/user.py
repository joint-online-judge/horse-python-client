# coding: utf-8

"""
    JOJ Horse

    Git version: a5c2259@2021-11-03T09:25:38Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class User(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'username': 'str',
        'email': 'str',
        'gravatar': 'str',
        'student_id': 'str',
        'real_name': 'str',
        'role': 'str',
        'is_active': 'bool',
        'register_ip': 'str',
        'login_at': 'datetime',
        'login_ip': 'str',
        'hashed_password': 'str',
        'username_lower': 'str',
        'email_lower': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'username': 'username',
        'email': 'email',
        'gravatar': 'gravatar',
        'student_id': 'student_id',
        'real_name': 'real_name',
        'role': 'role',
        'is_active': 'is_active',
        'register_ip': 'register_ip',
        'login_at': 'login_at',
        'login_ip': 'login_ip',
        'hashed_password': 'hashed_password',
        'username_lower': 'username_lower',
        'email_lower': 'email_lower'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, username=None, email=None, gravatar='', student_id='', real_name='', role='user', is_active=False, register_ip='0.0.0.0', login_at=None, login_ip='0.0.0.0', hashed_password='', username_lower=None, email_lower=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._username = None
        self._email = None
        self._gravatar = None
        self._student_id = None
        self._real_name = None
        self._role = None
        self._is_active = None
        self._register_ip = None
        self._login_at = None
        self._login_ip = None
        self._hashed_password = None
        self._username_lower = None
        self._email_lower = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.username = username
        self.email = email
        if gravatar is not None:
            self.gravatar = gravatar
        if student_id is not None:
            self.student_id = student_id
        if real_name is not None:
            self.real_name = real_name
        if role is not None:
            self.role = role
        if is_active is not None:
            self.is_active = is_active
        if register_ip is not None:
            self.register_ip = register_ip
        self.login_at = login_at
        if login_ip is not None:
            self.login_ip = login_ip
        if hashed_password is not None:
            self.hashed_password = hashed_password
        self.username_lower = username_lower
        self.email_lower = email_lower

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501


        :return: The created_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.


        :param created_at: The created_at of this User.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this User.  # noqa: E501


        :return: The updated_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this User.


        :param updated_at: The updated_at of this User.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501


        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.


        :param username: The username of this User.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def gravatar(self):
        """Gets the gravatar of this User.  # noqa: E501


        :return: The gravatar of this User.  # noqa: E501
        :rtype: str
        """
        return self._gravatar

    @gravatar.setter
    def gravatar(self, gravatar):
        """Sets the gravatar of this User.


        :param gravatar: The gravatar of this User.  # noqa: E501
        :type: str
        """

        self._gravatar = gravatar

    @property
    def student_id(self):
        """Gets the student_id of this User.  # noqa: E501


        :return: The student_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        """Sets the student_id of this User.


        :param student_id: The student_id of this User.  # noqa: E501
        :type: str
        """

        self._student_id = student_id

    @property
    def real_name(self):
        """Gets the real_name of this User.  # noqa: E501


        :return: The real_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """Sets the real_name of this User.


        :param real_name: The real_name of this User.  # noqa: E501
        :type: str
        """

        self._real_name = real_name

    @property
    def role(self):
        """Gets the role of this User.  # noqa: E501


        :return: The role of this User.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this User.


        :param role: The role of this User.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def is_active(self):
        """Gets the is_active of this User.  # noqa: E501


        :return: The is_active of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this User.


        :param is_active: The is_active of this User.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def register_ip(self):
        """Gets the register_ip of this User.  # noqa: E501


        :return: The register_ip of this User.  # noqa: E501
        :rtype: str
        """
        return self._register_ip

    @register_ip.setter
    def register_ip(self, register_ip):
        """Sets the register_ip of this User.


        :param register_ip: The register_ip of this User.  # noqa: E501
        :type: str
        """

        self._register_ip = register_ip

    @property
    def login_at(self):
        """Gets the login_at of this User.  # noqa: E501


        :return: The login_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._login_at

    @login_at.setter
    def login_at(self, login_at):
        """Sets the login_at of this User.


        :param login_at: The login_at of this User.  # noqa: E501
        :type: datetime
        """
        if login_at is None:
            raise ValueError("Invalid value for `login_at`, must not be `None`")  # noqa: E501

        self._login_at = login_at

    @property
    def login_ip(self):
        """Gets the login_ip of this User.  # noqa: E501


        :return: The login_ip of this User.  # noqa: E501
        :rtype: str
        """
        return self._login_ip

    @login_ip.setter
    def login_ip(self, login_ip):
        """Sets the login_ip of this User.


        :param login_ip: The login_ip of this User.  # noqa: E501
        :type: str
        """

        self._login_ip = login_ip

    @property
    def hashed_password(self):
        """Gets the hashed_password of this User.  # noqa: E501


        :return: The hashed_password of this User.  # noqa: E501
        :rtype: str
        """
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, hashed_password):
        """Sets the hashed_password of this User.


        :param hashed_password: The hashed_password of this User.  # noqa: E501
        :type: str
        """

        self._hashed_password = hashed_password

    @property
    def username_lower(self):
        """Gets the username_lower of this User.  # noqa: E501


        :return: The username_lower of this User.  # noqa: E501
        :rtype: str
        """
        return self._username_lower

    @username_lower.setter
    def username_lower(self, username_lower):
        """Sets the username_lower of this User.


        :param username_lower: The username_lower of this User.  # noqa: E501
        :type: str
        """
        if username_lower is None:
            raise ValueError("Invalid value for `username_lower`, must not be `None`")  # noqa: E501

        self._username_lower = username_lower

    @property
    def email_lower(self):
        """Gets the email_lower of this User.  # noqa: E501


        :return: The email_lower of this User.  # noqa: E501
        :rtype: str
        """
        return self._email_lower

    @email_lower.setter
    def email_lower(self, email_lower):
        """Sets the email_lower of this User.


        :param email_lower: The email_lower of this User.  # noqa: E501
        :type: str
        """
        if email_lower is None:
            raise ValueError("Invalid value for `email_lower`, must not be `None`")  # noqa: E501

        self._email_lower = email_lower

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
