# coding: utf-8

"""
    JOJ Horse

    Git version: 18a8a27@2021-12-08T21:19:12Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
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

    def test_list_domain_roles_api_v1_admin_domain_roles_get(self):
        """Test case for list_domain_roles_api_v1_admin_domain_roles_get

        List Domain Roles  # noqa: E501
        """
        pass

    def test_list_judgers_api_v1_admin_judgers_get(self):
        """Test case for list_judgers_api_v1_admin_judgers_get

        List Judgers  # noqa: E501
        """
        pass

    def test_list_users_api_v1_admin_users_get(self):
        """Test case for list_users_api_v1_admin_users_get

        List Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
