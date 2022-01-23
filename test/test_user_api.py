# coding: utf-8

"""
    JOJ Horse

    Git version: f3b5abe@2022-01-23T23:30:52Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse_client
from joj.horse_client.api.user_api import UserApi  # noqa: E501
from joj.horse_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_change_password(self):
        """Test case for v1_change_password

        Change Password  # noqa: E501
        """
        pass

    def test_v1_get_current_user(self):
        """Test case for v1_get_current_user

        Get Current User  # noqa: E501
        """
        pass

    def test_v1_get_user(self):
        """Test case for v1_get_user

        Get User  # noqa: E501
        """
        pass

    def test_v1_get_user_problems(self):
        """Test case for v1_get_user_problems

        Get User Problems  # noqa: E501
        """
        pass

    def test_v1_list_user_domains(self):
        """Test case for v1_list_user_domains

        List User Domains  # noqa: E501
        """
        pass

    def test_v1_list_users(self):
        """Test case for v1_list_users

        List Users  # noqa: E501
        """
        pass

    def test_v1_update_current_user(self):
        """Test case for v1_update_current_user

        Update Current User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
