# coding: utf-8

"""
    JOJ Horse

    Git version: c5741c9@2023-02-03T15:02:34Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Case(object):
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
        'category': 'str',
        'time': 'str',
        'memory': 'str',
        'score': 'int',
        'ignore_whitespace': 'bool',
        'execute_files': 'list[str]',
        'execute_args': 'list[str]',
        'execute_input_file': 'str',
        'execute_output_file': 'str'
    }

    attribute_map = {
        'category': 'category',
        'time': 'time',
        'memory': 'memory',
        'score': 'score',
        'ignore_whitespace': 'ignoreWhitespace',
        'execute_files': 'executeFiles',
        'execute_args': 'executeArgs',
        'execute_input_file': 'executeInputFile',
        'execute_output_file': 'executeOutputFile'
    }

    def __init__(self, category='pretest', time='1s', memory='64m', score=10, ignore_whitespace=True, execute_files=None, execute_args=None, execute_input_file='case.in', execute_output_file='case.out'):  # noqa: E501
        """Case - a model defined in Swagger"""  # noqa: E501
        self._category = None
        self._time = None
        self._memory = None
        self._score = None
        self._ignore_whitespace = None
        self._execute_files = None
        self._execute_args = None
        self._execute_input_file = None
        self._execute_output_file = None
        self.discriminator = None
        if category is not None:
            self.category = category
        if time is not None:
            self.time = time
        if memory is not None:
            self.memory = memory
        if score is not None:
            self.score = score
        if ignore_whitespace is not None:
            self.ignore_whitespace = ignore_whitespace
        if execute_files is not None:
            self.execute_files = execute_files
        if execute_args is not None:
            self.execute_args = execute_args
        if execute_input_file is not None:
            self.execute_input_file = execute_input_file
        if execute_output_file is not None:
            self.execute_output_file = execute_output_file

    @property
    def category(self):
        """Gets the category of this Case.  # noqa: E501


        :return: The category of this Case.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Case.


        :param category: The category of this Case.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def time(self):
        """Gets the time of this Case.  # noqa: E501


        :return: The time of this Case.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Case.


        :param time: The time of this Case.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def memory(self):
        """Gets the memory of this Case.  # noqa: E501


        :return: The memory of this Case.  # noqa: E501
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this Case.


        :param memory: The memory of this Case.  # noqa: E501
        :type: str
        """

        self._memory = memory

    @property
    def score(self):
        """Gets the score of this Case.  # noqa: E501


        :return: The score of this Case.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Case.


        :param score: The score of this Case.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def ignore_whitespace(self):
        """Gets the ignore_whitespace of this Case.  # noqa: E501


        :return: The ignore_whitespace of this Case.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_whitespace

    @ignore_whitespace.setter
    def ignore_whitespace(self, ignore_whitespace):
        """Sets the ignore_whitespace of this Case.


        :param ignore_whitespace: The ignore_whitespace of this Case.  # noqa: E501
        :type: bool
        """

        self._ignore_whitespace = ignore_whitespace

    @property
    def execute_files(self):
        """Gets the execute_files of this Case.  # noqa: E501


        :return: The execute_files of this Case.  # noqa: E501
        :rtype: list[str]
        """
        return self._execute_files

    @execute_files.setter
    def execute_files(self, execute_files):
        """Sets the execute_files of this Case.


        :param execute_files: The execute_files of this Case.  # noqa: E501
        :type: list[str]
        """

        self._execute_files = execute_files

    @property
    def execute_args(self):
        """Gets the execute_args of this Case.  # noqa: E501


        :return: The execute_args of this Case.  # noqa: E501
        :rtype: list[str]
        """
        return self._execute_args

    @execute_args.setter
    def execute_args(self, execute_args):
        """Sets the execute_args of this Case.


        :param execute_args: The execute_args of this Case.  # noqa: E501
        :type: list[str]
        """

        self._execute_args = execute_args

    @property
    def execute_input_file(self):
        """Gets the execute_input_file of this Case.  # noqa: E501


        :return: The execute_input_file of this Case.  # noqa: E501
        :rtype: str
        """
        return self._execute_input_file

    @execute_input_file.setter
    def execute_input_file(self, execute_input_file):
        """Sets the execute_input_file of this Case.


        :param execute_input_file: The execute_input_file of this Case.  # noqa: E501
        :type: str
        """

        self._execute_input_file = execute_input_file

    @property
    def execute_output_file(self):
        """Gets the execute_output_file of this Case.  # noqa: E501


        :return: The execute_output_file of this Case.  # noqa: E501
        :rtype: str
        """
        return self._execute_output_file

    @execute_output_file.setter
    def execute_output_file(self, execute_output_file):
        """Sets the execute_output_file of this Case.


        :param execute_output_file: The execute_output_file of this Case.  # noqa: E501
        :type: str
        """

        self._execute_output_file = execute_output_file

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
        if issubclass(Case, dict):
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
        if not isinstance(other, Case):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
