# coding: utf-8

"""
    JOJ Horse

    Git version: 3b82b34@2021-09-28 14:44:31  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse.client
from joj.horse.client.api.admin_api import AdminApi  # noqa: E501
from joj.horse.client.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_judger_api_v1_admin_judgers_post(self):
        """Test case for create_judger_api_v1_admin_judgers_post

        Create Judger  # noqa: E501
        """
        pass

    def test_create_user_api_v1_admin_users_post(self):
        """Test case for create_user_api_v1_admin_users_post

        Create User  # noqa: E501
        """
        pass

    def test_delete_user_api_v1_admin_users_uid_delete(self):
        """Test case for delete_user_api_v1_admin_users_uid_delete

        Delete User  # noqa: E501
        """
        pass

    def test_get_judger_jwt_api_v1_admin_judgers_uid_jwt_get(self):
        """Test case for get_judger_jwt_api_v1_admin_judgers_uid_jwt_get

        Get Judger Jwt  # noqa: E501
        """
        pass

    def test_list_domain_roles_api_v1_admin_domain_roles_get(self):
        """Test case for list_domain_roles_api_v1_admin_domain_roles_get

        List Domain Roles  # noqa: E501
        """
        pass

    def test_list_domain_users_api_v1_admin_domain_users_get(self):
        """Test case for list_domain_users_api_v1_admin_domain_users_get

        List Domain Users  # noqa: E501
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
