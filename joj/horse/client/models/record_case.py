# coding: utf-8

"""
    JOJ Horse

    Git version: 8fbec78@2021-07-16 09:35:08  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RecordCase(object):
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
        'status': 'AllOfRecordCaseStatus',
        'score': 'int',
        'time_ms': 'int',
        'memory_kb': 'int',
        'execute_status': 'int',
        'stdout': 'str',
        'stderr': 'str'
    }

    attribute_map = {
        'status': 'status',
        'score': 'score',
        'time_ms': 'time_ms',
        'memory_kb': 'memory_kb',
        'execute_status': 'execute_status',
        'stdout': 'stdout',
        'stderr': 'stderr'
    }

    def __init__(self, status=None, score=0, time_ms=0, memory_kb=0, execute_status=0, stdout='', stderr=''):  # noqa: E501
        """RecordCase - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._score = None
        self._time_ms = None
        self._memory_kb = None
        self._execute_status = None
        self._stdout = None
        self._stderr = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if score is not None:
            self.score = score
        if time_ms is not None:
            self.time_ms = time_ms
        if memory_kb is not None:
            self.memory_kb = memory_kb
        if execute_status is not None:
            self.execute_status = execute_status
        if stdout is not None:
            self.stdout = stdout
        if stderr is not None:
            self.stderr = stderr

    @property
    def status(self):
        """Gets the status of this RecordCase.  # noqa: E501


        :return: The status of this RecordCase.  # noqa: E501
        :rtype: AllOfRecordCaseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RecordCase.


        :param status: The status of this RecordCase.  # noqa: E501
        :type: AllOfRecordCaseStatus
        """

        self._status = status

    @property
    def score(self):
        """Gets the score of this RecordCase.  # noqa: E501


        :return: The score of this RecordCase.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this RecordCase.


        :param score: The score of this RecordCase.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def time_ms(self):
        """Gets the time_ms of this RecordCase.  # noqa: E501


        :return: The time_ms of this RecordCase.  # noqa: E501
        :rtype: int
        """
        return self._time_ms

    @time_ms.setter
    def time_ms(self, time_ms):
        """Sets the time_ms of this RecordCase.


        :param time_ms: The time_ms of this RecordCase.  # noqa: E501
        :type: int
        """

        self._time_ms = time_ms

    @property
    def memory_kb(self):
        """Gets the memory_kb of this RecordCase.  # noqa: E501


        :return: The memory_kb of this RecordCase.  # noqa: E501
        :rtype: int
        """
        return self._memory_kb

    @memory_kb.setter
    def memory_kb(self, memory_kb):
        """Sets the memory_kb of this RecordCase.


        :param memory_kb: The memory_kb of this RecordCase.  # noqa: E501
        :type: int
        """

        self._memory_kb = memory_kb

    @property
    def execute_status(self):
        """Gets the execute_status of this RecordCase.  # noqa: E501


        :return: The execute_status of this RecordCase.  # noqa: E501
        :rtype: int
        """
        return self._execute_status

    @execute_status.setter
    def execute_status(self, execute_status):
        """Sets the execute_status of this RecordCase.


        :param execute_status: The execute_status of this RecordCase.  # noqa: E501
        :type: int
        """

        self._execute_status = execute_status

    @property
    def stdout(self):
        """Gets the stdout of this RecordCase.  # noqa: E501


        :return: The stdout of this RecordCase.  # noqa: E501
        :rtype: str
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout):
        """Sets the stdout of this RecordCase.


        :param stdout: The stdout of this RecordCase.  # noqa: E501
        :type: str
        """

        self._stdout = stdout

    @property
    def stderr(self):
        """Gets the stderr of this RecordCase.  # noqa: E501


        :return: The stderr of this RecordCase.  # noqa: E501
        :rtype: str
        """
        return self._stderr

    @stderr.setter
    def stderr(self, stderr):
        """Sets the stderr of this RecordCase.


        :param stderr: The stderr of this RecordCase.  # noqa: E501
        :type: str
        """

        self._stderr = stderr

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
        if issubclass(RecordCase, dict):
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
        if not isinstance(other, RecordCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
