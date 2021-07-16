# coding: utf-8

"""
    JOJ Horse

    Git version: 8a4e1ee@2021-07-16 09:35:37  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserBase(object):
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
        'scope': 'str',
        'uname': 'str',
        'mail': 'str',
        'uname_lower': 'str',
        'mail_lower': 'str',
        'gravatar': 'str',
        'student_id': 'str',
        'real_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'scope': 'scope',
        'uname': 'uname',
        'mail': 'mail',
        'uname_lower': 'uname_lower',
        'mail_lower': 'mail_lower',
        'gravatar': 'gravatar',
        'student_id': 'student_id',
        'real_name': 'real_name'
    }

    def __init__(self, id=None, scope=None, uname=None, mail=None, uname_lower='', mail_lower='', gravatar='', student_id='', real_name=''):  # noqa: E501
        """UserBase - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._scope = None
        self._uname = None
        self._mail = None
        self._uname_lower = None
        self._mail_lower = None
        self._gravatar = None
        self._student_id = None
        self._real_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.scope = scope
        self.uname = uname
        self.mail = mail
        if uname_lower is not None:
            self.uname_lower = uname_lower
        if mail_lower is not None:
            self.mail_lower = mail_lower
        if gravatar is not None:
            self.gravatar = gravatar
        if student_id is not None:
            self.student_id = student_id
        if real_name is not None:
            self.real_name = real_name

    @property
    def id(self):
        """Gets the id of this UserBase.  # noqa: E501


        :return: The id of this UserBase.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserBase.


        :param id: The id of this UserBase.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def scope(self):
        """Gets the scope of this UserBase.  # noqa: E501


        :return: The scope of this UserBase.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this UserBase.


        :param scope: The scope of this UserBase.  # noqa: E501
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def uname(self):
        """Gets the uname of this UserBase.  # noqa: E501


        :return: The uname of this UserBase.  # noqa: E501
        :rtype: str
        """
        return self._uname

    @uname.setter
    def uname(self, uname):
        """Sets the uname of this UserBase.


        :param uname: The uname of this UserBase.  # noqa: E501
        :type: str
        """
        if uname is None:
            raise ValueError("Invalid value for `uname`, must not be `None`")  # noqa: E501

        self._uname = uname

    @property
    def mail(self):
        """Gets the mail of this UserBase.  # noqa: E501


        :return: The mail of this UserBase.  # noqa: E501
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail):
        """Sets the mail of this UserBase.


        :param mail: The mail of this UserBase.  # noqa: E501
        :type: str
        """
        if mail is None:
            raise ValueError("Invalid value for `mail`, must not be `None`")  # noqa: E501

        self._mail = mail

    @property
    def uname_lower(self):
        """Gets the uname_lower of this UserBase.  # noqa: E501


        :return: The uname_lower of this UserBase.  # noqa: E501
        :rtype: str
        """
        return self._uname_lower

    @uname_lower.setter
    def uname_lower(self, uname_lower):
        """Sets the uname_lower of this UserBase.


        :param uname_lower: The uname_lower of this UserBase.  # noqa: E501
        :type: str
        """

        self._uname_lower = uname_lower

    @property
    def mail_lower(self):
        """Gets the mail_lower of this UserBase.  # noqa: E501


        :return: The mail_lower of this UserBase.  # noqa: E501
        :rtype: str
        """
        return self._mail_lower

    @mail_lower.setter
    def mail_lower(self, mail_lower):
        """Sets the mail_lower of this UserBase.


        :param mail_lower: The mail_lower of this UserBase.  # noqa: E501
        :type: str
        """

        self._mail_lower = mail_lower

    @property
    def gravatar(self):
        """Gets the gravatar of this UserBase.  # noqa: E501


        :return: The gravatar of this UserBase.  # noqa: E501
        :rtype: str
        """
        return self._gravatar

    @gravatar.setter
    def gravatar(self, gravatar):
        """Sets the gravatar of this UserBase.


        :param gravatar: The gravatar of this UserBase.  # noqa: E501
        :type: str
        """

        self._gravatar = gravatar

    @property
    def student_id(self):
        """Gets the student_id of this UserBase.  # noqa: E501


        :return: The student_id of this UserBase.  # noqa: E501
        :rtype: str
        """
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        """Sets the student_id of this UserBase.


        :param student_id: The student_id of this UserBase.  # noqa: E501
        :type: str
        """

        self._student_id = student_id

    @property
    def real_name(self):
        """Gets the real_name of this UserBase.  # noqa: E501


        :return: The real_name of this UserBase.  # noqa: E501
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """Sets the real_name of this UserBase.


        :param real_name: The real_name of this UserBase.  # noqa: E501
        :type: str
        """

        self._real_name = real_name

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
        if issubclass(UserBase, dict):
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
        if not isinstance(other, UserBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
