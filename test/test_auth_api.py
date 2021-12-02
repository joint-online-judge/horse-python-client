# coding: utf-8

"""
    JOJ Horse

    Git version: bfefbbd@2021-12-02T07:55:13Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse.client
from joj.horse.client.api.auth_api import AuthApi  # noqa: E501
from joj.horse.client.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_token_api_v1_auth_token_get(self):
        """Test case for get_token_api_v1_auth_token_get

        Get Token  # noqa: E501
        """
        pass

    def test_login_api_v1_auth_login_post(self):
        """Test case for login_api_v1_auth_login_post

        Login  # noqa: E501
        """
        pass

    def test_logout_api_v1_auth_logout_post(self):
        """Test case for logout_api_v1_auth_logout_post

        Logout  # noqa: E501
        """
        pass

    def test_refresh_api_v1_auth_refresh_post(self):
        """Test case for refresh_api_v1_auth_refresh_post

        Refresh  # noqa: E501
        """
        pass

    def test_register_api_v1_auth_register_post(self):
        """Test case for register_api_v1_auth_register_post

        Register  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
