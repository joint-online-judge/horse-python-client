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

class JWTAccessToken(object):
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
        'sub': 'str',
        'iat': 'int',
        'nbf': 'int',
        'jti': 'str',
        'exp': 'int',
        'type': 'str',
        'fresh': 'bool',
        'csrf': 'str',
        'category': 'str',
        'username': 'str',
        'email': 'str',
        'gravatar': 'str',
        'student_id': 'str',
        'real_name': 'str',
        'role': 'str',
        'oauth_name': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'sub': 'sub',
        'iat': 'iat',
        'nbf': 'nbf',
        'jti': 'jti',
        'exp': 'exp',
        'type': 'type',
        'fresh': 'fresh',
        'csrf': 'csrf',
        'category': 'category',
        'username': 'username',
        'email': 'email',
        'gravatar': 'gravatar',
        'student_id': 'studentId',
        'real_name': 'realName',
        'role': 'role',
        'oauth_name': 'oauthName',
        'is_active': 'isActive'
    }

    def __init__(self, sub=None, iat=None, nbf=None, jti=None, exp=None, type=None, fresh=False, csrf=None, category=None, username=None, email=None, gravatar='', student_id='', real_name='', role=None, oauth_name=None, is_active=None):  # noqa: E501
        """JWTAccessToken - a model defined in Swagger"""  # noqa: E501
        self._sub = None
        self._iat = None
        self._nbf = None
        self._jti = None
        self._exp = None
        self._type = None
        self._fresh = None
        self._csrf = None
        self._category = None
        self._username = None
        self._email = None
        self._gravatar = None
        self._student_id = None
        self._real_name = None
        self._role = None
        self._oauth_name = None
        self._is_active = None
        self.discriminator = None
        self.sub = sub
        self.iat = iat
        self.nbf = nbf
        self.jti = jti
        self.exp = exp
        self.type = type
        if fresh is not None:
            self.fresh = fresh
        if csrf is not None:
            self.csrf = csrf
        self.category = category
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
        if oauth_name is not None:
            self.oauth_name = oauth_name
        self.is_active = is_active

    @property
    def sub(self):
        """Gets the sub of this JWTAccessToken.  # noqa: E501


        :return: The sub of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        """Sets the sub of this JWTAccessToken.


        :param sub: The sub of this JWTAccessToken.  # noqa: E501
        :type: str
        """
        if sub is None:
            raise ValueError("Invalid value for `sub`, must not be `None`")  # noqa: E501

        self._sub = sub

    @property
    def iat(self):
        """Gets the iat of this JWTAccessToken.  # noqa: E501


        :return: The iat of this JWTAccessToken.  # noqa: E501
        :rtype: int
        """
        return self._iat

    @iat.setter
    def iat(self, iat):
        """Sets the iat of this JWTAccessToken.


        :param iat: The iat of this JWTAccessToken.  # noqa: E501
        :type: int
        """
        if iat is None:
            raise ValueError("Invalid value for `iat`, must not be `None`")  # noqa: E501

        self._iat = iat

    @property
    def nbf(self):
        """Gets the nbf of this JWTAccessToken.  # noqa: E501


        :return: The nbf of this JWTAccessToken.  # noqa: E501
        :rtype: int
        """
        return self._nbf

    @nbf.setter
    def nbf(self, nbf):
        """Sets the nbf of this JWTAccessToken.


        :param nbf: The nbf of this JWTAccessToken.  # noqa: E501
        :type: int
        """
        if nbf is None:
            raise ValueError("Invalid value for `nbf`, must not be `None`")  # noqa: E501

        self._nbf = nbf

    @property
    def jti(self):
        """Gets the jti of this JWTAccessToken.  # noqa: E501


        :return: The jti of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._jti

    @jti.setter
    def jti(self, jti):
        """Sets the jti of this JWTAccessToken.


        :param jti: The jti of this JWTAccessToken.  # noqa: E501
        :type: str
        """
        if jti is None:
            raise ValueError("Invalid value for `jti`, must not be `None`")  # noqa: E501

        self._jti = jti

    @property
    def exp(self):
        """Gets the exp of this JWTAccessToken.  # noqa: E501


        :return: The exp of this JWTAccessToken.  # noqa: E501
        :rtype: int
        """
        return self._exp

    @exp.setter
    def exp(self, exp):
        """Sets the exp of this JWTAccessToken.


        :param exp: The exp of this JWTAccessToken.  # noqa: E501
        :type: int
        """
        if exp is None:
            raise ValueError("Invalid value for `exp`, must not be `None`")  # noqa: E501

        self._exp = exp

    @property
    def type(self):
        """Gets the type of this JWTAccessToken.  # noqa: E501


        :return: The type of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JWTAccessToken.


        :param type: The type of this JWTAccessToken.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fresh(self):
        """Gets the fresh of this JWTAccessToken.  # noqa: E501


        :return: The fresh of this JWTAccessToken.  # noqa: E501
        :rtype: bool
        """
        return self._fresh

    @fresh.setter
    def fresh(self, fresh):
        """Sets the fresh of this JWTAccessToken.


        :param fresh: The fresh of this JWTAccessToken.  # noqa: E501
        :type: bool
        """

        self._fresh = fresh

    @property
    def csrf(self):
        """Gets the csrf of this JWTAccessToken.  # noqa: E501


        :return: The csrf of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._csrf

    @csrf.setter
    def csrf(self, csrf):
        """Sets the csrf of this JWTAccessToken.


        :param csrf: The csrf of this JWTAccessToken.  # noqa: E501
        :type: str
        """

        self._csrf = csrf

    @property
    def category(self):
        """Gets the category of this JWTAccessToken.  # noqa: E501


        :return: The category of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this JWTAccessToken.


        :param category: The category of this JWTAccessToken.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        allowed_values = ["user", "oauth"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def username(self):
        """Gets the username of this JWTAccessToken.  # noqa: E501


        :return: The username of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this JWTAccessToken.


        :param username: The username of this JWTAccessToken.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email(self):
        """Gets the email of this JWTAccessToken.  # noqa: E501


        :return: The email of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this JWTAccessToken.


        :param email: The email of this JWTAccessToken.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def gravatar(self):
        """Gets the gravatar of this JWTAccessToken.  # noqa: E501


        :return: The gravatar of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._gravatar

    @gravatar.setter
    def gravatar(self, gravatar):
        """Sets the gravatar of this JWTAccessToken.


        :param gravatar: The gravatar of this JWTAccessToken.  # noqa: E501
        :type: str
        """

        self._gravatar = gravatar

    @property
    def student_id(self):
        """Gets the student_id of this JWTAccessToken.  # noqa: E501


        :return: The student_id of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        """Sets the student_id of this JWTAccessToken.


        :param student_id: The student_id of this JWTAccessToken.  # noqa: E501
        :type: str
        """

        self._student_id = student_id

    @property
    def real_name(self):
        """Gets the real_name of this JWTAccessToken.  # noqa: E501


        :return: The real_name of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """Sets the real_name of this JWTAccessToken.


        :param real_name: The real_name of this JWTAccessToken.  # noqa: E501
        :type: str
        """

        self._real_name = real_name

    @property
    def role(self):
        """Gets the role of this JWTAccessToken.  # noqa: E501


        :return: The role of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this JWTAccessToken.


        :param role: The role of this JWTAccessToken.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def oauth_name(self):
        """Gets the oauth_name of this JWTAccessToken.  # noqa: E501


        :return: The oauth_name of this JWTAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._oauth_name

    @oauth_name.setter
    def oauth_name(self, oauth_name):
        """Sets the oauth_name of this JWTAccessToken.


        :param oauth_name: The oauth_name of this JWTAccessToken.  # noqa: E501
        :type: str
        """

        self._oauth_name = oauth_name

    @property
    def is_active(self):
        """Gets the is_active of this JWTAccessToken.  # noqa: E501


        :return: The is_active of this JWTAccessToken.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this JWTAccessToken.


        :param is_active: The is_active of this JWTAccessToken.  # noqa: E501
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

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
        if issubclass(JWTAccessToken, dict):
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
        if not isinstance(other, JWTAccessToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
