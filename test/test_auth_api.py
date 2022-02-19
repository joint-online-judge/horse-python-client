# coding: utf-8

"""
    JOJ Horse

    Git version: 07316f1@2022-02-19T10:40:47Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse_client
from joj.horse_client.api.auth_api import AuthApi  # noqa: E501
from joj.horse_client.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_get_token(self):
        """Test case for v1_get_token

        Get Token  # noqa: E501
        """
        pass

    def test_v1_list_oauth2(self):
        """Test case for v1_list_oauth2

        List Oauth2  # noqa: E501
        """
        pass

    def test_v1_login(self):
        """Test case for v1_login

        Login  # noqa: E501
        """
        pass

    def test_v1_logout(self):
        """Test case for v1_logout

        Logout  # noqa: E501
        """
        pass

    def test_v1_oauth_authorize(self):
        """Test case for v1_oauth_authorize

        Oauth Authorize  # noqa: E501
        """
        pass

    def test_v1_refresh(self):
        """Test case for v1_refresh

        Refresh  # noqa: E501
        """
        pass

    def test_v1_register(self):
        """Test case for v1_register

        Register  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
