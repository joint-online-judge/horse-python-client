# coding: utf-8

"""
    JOJ Horse

    Git version: 4c1960b@2022-02-19T13:43:08Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse_client
from joj.horse_client.api.problem_group_api import ProblemGroupApi  # noqa: E501
from joj.horse_client.rest import ApiException


class TestProblemGroupApi(unittest.TestCase):
    """ProblemGroupApi unit test stubs"""

    def setUp(self):
        self.api = ProblemGroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_list_problem_groups(self):
        """Test case for v1_list_problem_groups

        List Problem Groups  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
