# coding: utf-8

"""
    JOJ Horse

    Git version: e13285b@2022-06-02T06:27:27Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse_client
from joj.horse_client.api.admin_api import AdminApi  # noqa: E501
from joj.horse_client.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_create_judger(self):
        """Test case for v1_create_judger

        Create Judger  # noqa: E501
        """
        pass

    def test_v1_get_user(self):
        """Test case for v1_get_user

        Get User  # noqa: E501
        """
        pass

    def test_v1_list_domain_roles(self):
        """Test case for v1_list_domain_roles

        List Domain Roles  # noqa: E501
        """
        pass

    def test_v1_list_judgers(self):
        """Test case for v1_list_judgers

        List Judgers  # noqa: E501
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


if __name__ == '__main__':
    unittest.main()
