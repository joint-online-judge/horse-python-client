# coding: utf-8

"""
    JOJ Horse

    Git version: 59b0930@2022-05-20T21:53:14Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RecordCaseSubmit(object):
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
        'state': 'RecordCaseResult',
        'score': 'int',
        'time_ms': 'int',
        'memory_kb': 'int',
        'return_code': 'int',
        'stdout': 'str',
        'stderr': 'str'
    }

    attribute_map = {
        'state': 'state',
        'score': 'score',
        'time_ms': 'timeMs',
        'memory_kb': 'memoryKb',
        'return_code': 'returnCode',
        'stdout': 'stdout',
        'stderr': 'stderr'
    }

    def __init__(self, state=None, score=None, time_ms=None, memory_kb=None, return_code=None, stdout=None, stderr=None):  # noqa: E501
        """RecordCaseSubmit - a model defined in Swagger"""  # noqa: E501
        self._state = None
        self._score = None
        self._time_ms = None
        self._memory_kb = None
        self._return_code = None
        self._stdout = None
        self._stderr = None
        self.discriminator = None
        if state is not None:
            self.state = state
        if score is not None:
            self.score = score
        if time_ms is not None:
            self.time_ms = time_ms
        if memory_kb is not None:
            self.memory_kb = memory_kb
        if return_code is not None:
            self.return_code = return_code
        if stdout is not None:
            self.stdout = stdout
        if stderr is not None:
            self.stderr = stderr

    @property
    def state(self):
        """Gets the state of this RecordCaseSubmit.  # noqa: E501


        :return: The state of this RecordCaseSubmit.  # noqa: E501
        :rtype: RecordCaseResult
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RecordCaseSubmit.


        :param state: The state of this RecordCaseSubmit.  # noqa: E501
        :type: RecordCaseResult
        """

        self._state = state

    @property
    def score(self):
        """Gets the score of this RecordCaseSubmit.  # noqa: E501


        :return: The score of this RecordCaseSubmit.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this RecordCaseSubmit.


        :param score: The score of this RecordCaseSubmit.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def time_ms(self):
        """Gets the time_ms of this RecordCaseSubmit.  # noqa: E501


        :return: The time_ms of this RecordCaseSubmit.  # noqa: E501
        :rtype: int
        """
        return self._time_ms

    @time_ms.setter
    def time_ms(self, time_ms):
        """Sets the time_ms of this RecordCaseSubmit.


        :param time_ms: The time_ms of this RecordCaseSubmit.  # noqa: E501
        :type: int
        """

        self._time_ms = time_ms

    @property
    def memory_kb(self):
        """Gets the memory_kb of this RecordCaseSubmit.  # noqa: E501


        :return: The memory_kb of this RecordCaseSubmit.  # noqa: E501
        :rtype: int
        """
        return self._memory_kb

    @memory_kb.setter
    def memory_kb(self, memory_kb):
        """Sets the memory_kb of this RecordCaseSubmit.


        :param memory_kb: The memory_kb of this RecordCaseSubmit.  # noqa: E501
        :type: int
        """

        self._memory_kb = memory_kb

    @property
    def return_code(self):
        """Gets the return_code of this RecordCaseSubmit.  # noqa: E501


        :return: The return_code of this RecordCaseSubmit.  # noqa: E501
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this RecordCaseSubmit.


        :param return_code: The return_code of this RecordCaseSubmit.  # noqa: E501
        :type: int
        """

        self._return_code = return_code

    @property
    def stdout(self):
        """Gets the stdout of this RecordCaseSubmit.  # noqa: E501


        :return: The stdout of this RecordCaseSubmit.  # noqa: E501
        :rtype: str
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout):
        """Sets the stdout of this RecordCaseSubmit.


        :param stdout: The stdout of this RecordCaseSubmit.  # noqa: E501
        :type: str
        """

        self._stdout = stdout

    @property
    def stderr(self):
        """Gets the stderr of this RecordCaseSubmit.  # noqa: E501


        :return: The stderr of this RecordCaseSubmit.  # noqa: E501
        :rtype: str
        """
        return self._stderr

    @stderr.setter
    def stderr(self, stderr):
        """Sets the stderr of this RecordCaseSubmit.


        :param stderr: The stderr of this RecordCaseSubmit.  # noqa: E501
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
        if issubclass(RecordCaseSubmit, dict):
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
        if not isinstance(other, RecordCaseSubmit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
