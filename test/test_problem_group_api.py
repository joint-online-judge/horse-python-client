# coding: utf-8

"""
    JOJ Horse

    Git version: e3511c4@2021-07-12 17:57:12  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse.client
from joj.horse.client.api.problem_group_api import ProblemGroupApi  # noqa: E501
from joj.horse.client.rest import ApiException


class TestProblemGroupApi(unittest.TestCase):
    """ProblemGroupApi unit test stubs"""

    def setUp(self):
        self.api = ProblemGroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_problem_groups_api_v1_problem_groups_get(self):
        """Test case for list_problem_groups_api_v1_problem_groups_get

        List Problem Groups  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
