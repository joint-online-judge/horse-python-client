# coding: utf-8

"""
    JOJ Horse

    Git version: c5741c9@2023-02-03T15:02:34Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse_client
from joj.horse_client.api.problem_config_api import ProblemConfigApi  # noqa: E501
from joj.horse_client.rest import ApiException


class TestProblemConfigApi(unittest.TestCase):
    """ProblemConfigApi unit test stubs"""

    def setUp(self):
        self.api = ProblemConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_diff_problem_config_default_branch(self):
        """Test case for v1_diff_problem_config_default_branch

        Diff Problem Config Default Branch  # noqa: E501
        """
        pass

    def test_v1_download_problem_config_archive(self):
        """Test case for v1_download_problem_config_archive

        Download Problem Config Archive  # noqa: E501
        """
        pass

    def test_v1_get_problem_config_json(self):
        """Test case for v1_get_problem_config_json

        Get Problem Config Json  # noqa: E501
        """
        pass

    def test_v1_list_latest_problem_config_objects_under_a_given_prefix(self):
        """Test case for v1_list_latest_problem_config_objects_under_a_given_prefix

        List Latest Problem Config Objects Under A Given Prefix  # noqa: E501
        """
        pass

    def test_v1_list_problem_config_commits(self):
        """Test case for v1_list_problem_config_commits

        List Problem Config Commits  # noqa: E501
        """
        pass

    def test_v1_update_problem_config_by_archive(self):
        """Test case for v1_update_problem_config_by_archive

        Update Problem Config By Archive  # noqa: E501
        """
        pass

    def test_v1_update_problem_config_json(self):
        """Test case for v1_update_problem_config_json

        Update Problem Config Json  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
