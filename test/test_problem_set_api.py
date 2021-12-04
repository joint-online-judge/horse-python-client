# coding: utf-8

"""
    JOJ Horse

    Git version: 635361f@2021-12-04T19:06:33Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse.client
from joj.horse.client.api.problem_set_api import ProblemSetApi  # noqa: E501
from joj.horse.client.rest import ApiException


class TestProblemSetApi(unittest.TestCase):
    """ProblemSetApi unit test stubs"""

    def setUp(self):
        self.api = ProblemSetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_post(self):
        """Test case for add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_post

        Add Problem In Problem Set  # noqa: E501
        """
        pass

    def test_create_problem_set_api_v1_domains_domain_problem_sets_post(self):
        """Test case for create_problem_set_api_v1_domains_domain_problem_sets_post

        Create Problem Set  # noqa: E501
        """
        pass

    def test_delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_problem_delete(self):
        """Test case for delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_problem_delete

        Delete Problem In Problem Set  # noqa: E501
        """
        pass

    def test_delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete(self):
        """Test case for delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete

        Delete Problem Set  # noqa: E501
        """
        pass

    def test_get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_problem_get(self):
        """Test case for get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_problem_get

        Get Problem In Problem Set  # noqa: E501
        """
        pass

    def test_get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get(self):
        """Test case for get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get

        Get Problem Set  # noqa: E501
        """
        pass

    def test_get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get(self):
        """Test case for get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get

        Get Scoreboard  # noqa: E501
        """
        pass

    def test_list_problem_sets_api_v1_domains_domain_problem_sets_get(self):
        """Test case for list_problem_sets_api_v1_domains_domain_problem_sets_get

        List Problem Sets  # noqa: E501
        """
        pass

    def test_list_problems_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_get(self):
        """Test case for list_problems_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_get

        List Problems In Problem Set  # noqa: E501
        """
        pass

    def test_submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_problem_submit_post(self):
        """Test case for submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_problem_submit_post

        Submit Solution To Problem Set  # noqa: E501
        """
        pass

    def test_update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_problem_patch(self):
        """Test case for update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problems_problem_patch

        Update Problem In Problem Set  # noqa: E501
        """
        pass

    def test_update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch(self):
        """Test case for update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch

        Update Problem Set  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
