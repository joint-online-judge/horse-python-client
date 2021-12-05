# coding: utf-8

"""
    JOJ Horse

    Git version: 1525419@2021-12-05T09:30:14Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse.client
from joj.horse.client.api.user_api import UserApi  # noqa: E501
from joj.horse.client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_api_v1_user_get(self):
        """Test case for get_user_api_v1_user_get

        Get User  # noqa: E501
        """
        pass

    def test_get_user_api_v1_users_uid_get(self):
        """Test case for get_user_api_v1_users_uid_get

        Get User  # noqa: E501
        """
        pass

    def test_get_user_problems_api_v1_user_problems_get(self):
        """Test case for get_user_problems_api_v1_user_problems_get

        Get User Problems  # noqa: E501
        """
        pass

    def test_get_user_problems_api_v1_users_uid_problems_get(self):
        """Test case for get_user_problems_api_v1_users_uid_problems_get

        Get User Problems  # noqa: E501
        """
        pass

    def test_list_user_domains_api_v1_users_uid_domains_get(self):
        """Test case for list_user_domains_api_v1_users_uid_domains_get

        List User Domains  # noqa: E501
        """
        pass

    def test_list_users_api_v1_users_get(self):
        """Test case for list_users_api_v1_users_get

        List Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
