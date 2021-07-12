# coding: utf-8

"""
    JOJ Horse

    Git version: 545e91f@2021-07-12 10:49:50  # noqa: E501

    OpenAPI spec version: 0.0.0
    
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

    def test_get_user_domains_api_v1_users_uid_domains_get(self):
        """Test case for get_user_domains_api_v1_users_uid_domains_get

        Get User Domains  # noqa: E501
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

    def test_jaccount_auth_api_v1_user_jaccount_auth_get(self):
        """Test case for jaccount_auth_api_v1_user_jaccount_auth_get

        Jaccount Auth  # noqa: E501
        """
        pass

    def test_jaccount_login_api_v1_user_jaccount_login_get(self):
        """Test case for jaccount_login_api_v1_user_jaccount_login_get

        Jaccount Login  # noqa: E501
        """
        pass

    def test_logout_api_v1_user_logout_get(self):
        """Test case for logout_api_v1_user_logout_get

        Logout  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
