# coding: utf-8

"""
    JOJ Horse

    Git version: ae0c6d5@2022-01-02T19:29:09Z  # noqa: E501

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

    def test_v1_list_users(self):
        """Test case for v1_list_users

        List Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
