# coding: utf-8

"""
    JOJ Horse

    Git version: f94044f@2021-07-13 06:06:59  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Record(object):
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
        'status': 'AllOfRecordStatus',
        'score': 'int',
        'time_ms': 'int',
        'memory_kb': 'int',
        'domain': 'AnyOfRecordDomain',
        'problem': 'AnyOfRecordProblem',
        'problem_data': 'int',
        'user': 'AnyOfRecordUser',
        'code_type': 'RecordCodeType',
        'code': 'str',
        'judge_category': 'list[str]',
        'submit_at': 'datetime',
        'judge_at': 'datetime',
        'judge_user': 'AnyOfRecordJudgeUser',
        'compiler_texts': 'str',
        'cases': 'list[RecordCase]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'score': 'score',
        'time_ms': 'time_ms',
        'memory_kb': 'memory_kb',
        'domain': 'domain',
        'problem': 'problem',
        'problem_data': 'problem_data',
        'user': 'user',
        'code_type': 'code_type',
        'code': 'code',
        'judge_category': 'judge_category',
        'submit_at': 'submit_at',
        'judge_at': 'judge_at',
        'judge_user': 'judge_user',
        'compiler_texts': 'compiler_texts',
        'cases': 'cases'
    }

    def __init__(self, id=None, status=None, score=0, time_ms=0, memory_kb=0, domain=None, problem=None, problem_data=0, user=None, code_type=None, code=None, judge_category=None, submit_at=None, judge_at=None, judge_user=None, compiler_texts='', cases=None):  # noqa: E501
        """Record - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._score = None
        self._time_ms = None
        self._memory_kb = None
        self._domain = None
        self._problem = None
        self._problem_data = None
        self._user = None
        self._code_type = None
        self._code = None
        self._judge_category = None
        self._submit_at = None
        self._judge_at = None
        self._judge_user = None
        self._compiler_texts = None
        self._cases = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if score is not None:
            self.score = score
        if time_ms is not None:
            self.time_ms = time_ms
        if memory_kb is not None:
            self.memory_kb = memory_kb
        self.domain = domain
        self.problem = problem
        if problem_data is not None:
            self.problem_data = problem_data
        self.user = user
        self.code_type = code_type
        self.code = code
        self.judge_category = judge_category
        self.submit_at = submit_at
        if judge_at is not None:
            self.judge_at = judge_at
        if judge_user is not None:
            self.judge_user = judge_user
        if compiler_texts is not None:
            self.compiler_texts = compiler_texts
        if cases is not None:
            self.cases = cases

    @property
    def id(self):
        """Gets the id of this Record.  # noqa: E501


        :return: The id of this Record.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Record.


        :param id: The id of this Record.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this Record.  # noqa: E501


        :return: The status of this Record.  # noqa: E501
        :rtype: AllOfRecordStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Record.


        :param status: The status of this Record.  # noqa: E501
        :type: AllOfRecordStatus
        """

        self._status = status

    @property
    def score(self):
        """Gets the score of this Record.  # noqa: E501


        :return: The score of this Record.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Record.


        :param score: The score of this Record.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def time_ms(self):
        """Gets the time_ms of this Record.  # noqa: E501


        :return: The time_ms of this Record.  # noqa: E501
        :rtype: int
        """
        return self._time_ms

    @time_ms.setter
    def time_ms(self, time_ms):
        """Sets the time_ms of this Record.


        :param time_ms: The time_ms of this Record.  # noqa: E501
        :type: int
        """

        self._time_ms = time_ms

    @property
    def memory_kb(self):
        """Gets the memory_kb of this Record.  # noqa: E501


        :return: The memory_kb of this Record.  # noqa: E501
        :rtype: int
        """
        return self._memory_kb

    @memory_kb.setter
    def memory_kb(self, memory_kb):
        """Sets the memory_kb of this Record.


        :param memory_kb: The memory_kb of this Record.  # noqa: E501
        :type: int
        """

        self._memory_kb = memory_kb

    @property
    def domain(self):
        """Gets the domain of this Record.  # noqa: E501


        :return: The domain of this Record.  # noqa: E501
        :rtype: AnyOfRecordDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Record.


        :param domain: The domain of this Record.  # noqa: E501
        :type: AnyOfRecordDomain
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def problem(self):
        """Gets the problem of this Record.  # noqa: E501


        :return: The problem of this Record.  # noqa: E501
        :rtype: AnyOfRecordProblem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this Record.


        :param problem: The problem of this Record.  # noqa: E501
        :type: AnyOfRecordProblem
        """
        if problem is None:
            raise ValueError("Invalid value for `problem`, must not be `None`")  # noqa: E501

        self._problem = problem

    @property
    def problem_data(self):
        """Gets the problem_data of this Record.  # noqa: E501


        :return: The problem_data of this Record.  # noqa: E501
        :rtype: int
        """
        return self._problem_data

    @problem_data.setter
    def problem_data(self, problem_data):
        """Sets the problem_data of this Record.


        :param problem_data: The problem_data of this Record.  # noqa: E501
        :type: int
        """

        self._problem_data = problem_data

    @property
    def user(self):
        """Gets the user of this Record.  # noqa: E501


        :return: The user of this Record.  # noqa: E501
        :rtype: AnyOfRecordUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Record.


        :param user: The user of this Record.  # noqa: E501
        :type: AnyOfRecordUser
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def code_type(self):
        """Gets the code_type of this Record.  # noqa: E501


        :return: The code_type of this Record.  # noqa: E501
        :rtype: RecordCodeType
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this Record.


        :param code_type: The code_type of this Record.  # noqa: E501
        :type: RecordCodeType
        """
        if code_type is None:
            raise ValueError("Invalid value for `code_type`, must not be `None`")  # noqa: E501

        self._code_type = code_type

    @property
    def code(self):
        """Gets the code of this Record.  # noqa: E501


        :return: The code of this Record.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Record.


        :param code: The code of this Record.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def judge_category(self):
        """Gets the judge_category of this Record.  # noqa: E501


        :return: The judge_category of this Record.  # noqa: E501
        :rtype: list[str]
        """
        return self._judge_category

    @judge_category.setter
    def judge_category(self, judge_category):
        """Sets the judge_category of this Record.


        :param judge_category: The judge_category of this Record.  # noqa: E501
        :type: list[str]
        """
        if judge_category is None:
            raise ValueError("Invalid value for `judge_category`, must not be `None`")  # noqa: E501

        self._judge_category = judge_category

    @property
    def submit_at(self):
        """Gets the submit_at of this Record.  # noqa: E501


        :return: The submit_at of this Record.  # noqa: E501
        :rtype: datetime
        """
        return self._submit_at

    @submit_at.setter
    def submit_at(self, submit_at):
        """Sets the submit_at of this Record.


        :param submit_at: The submit_at of this Record.  # noqa: E501
        :type: datetime
        """
        if submit_at is None:
            raise ValueError("Invalid value for `submit_at`, must not be `None`")  # noqa: E501

        self._submit_at = submit_at

    @property
    def judge_at(self):
        """Gets the judge_at of this Record.  # noqa: E501


        :return: The judge_at of this Record.  # noqa: E501
        :rtype: datetime
        """
        return self._judge_at

    @judge_at.setter
    def judge_at(self, judge_at):
        """Sets the judge_at of this Record.


        :param judge_at: The judge_at of this Record.  # noqa: E501
        :type: datetime
        """

        self._judge_at = judge_at

    @property
    def judge_user(self):
        """Gets the judge_user of this Record.  # noqa: E501


        :return: The judge_user of this Record.  # noqa: E501
        :rtype: AnyOfRecordJudgeUser
        """
        return self._judge_user

    @judge_user.setter
    def judge_user(self, judge_user):
        """Sets the judge_user of this Record.


        :param judge_user: The judge_user of this Record.  # noqa: E501
        :type: AnyOfRecordJudgeUser
        """

        self._judge_user = judge_user

    @property
    def compiler_texts(self):
        """Gets the compiler_texts of this Record.  # noqa: E501


        :return: The compiler_texts of this Record.  # noqa: E501
        :rtype: str
        """
        return self._compiler_texts

    @compiler_texts.setter
    def compiler_texts(self, compiler_texts):
        """Sets the compiler_texts of this Record.


        :param compiler_texts: The compiler_texts of this Record.  # noqa: E501
        :type: str
        """

        self._compiler_texts = compiler_texts

    @property
    def cases(self):
        """Gets the cases of this Record.  # noqa: E501


        :return: The cases of this Record.  # noqa: E501
        :rtype: list[RecordCase]
        """
        return self._cases

    @cases.setter
    def cases(self, cases):
        """Sets the cases of this Record.


        :param cases: The cases of this Record.  # noqa: E501
        :type: list[RecordCase]
        """

        self._cases = cases

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
        if issubclass(Record, dict):
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
        if not isinstance(other, Record):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
