# coding: utf-8

"""
    JOJ Horse

    Git version: 5c38b66@2021-06-15 12:19:18  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse.client
from joj.horse.client.api.domain_api import DomainApi  # noqa: E501
from joj.horse.client.rest import ApiException


class TestDomainApi(unittest.TestCase):
    """DomainApi unit test stubs"""

    def setUp(self):
        self.api = DomainApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_domain_user_api_v1_domains_domain_users_post(self):
        """Test case for add_domain_user_api_v1_domains_domain_users_post

        Add Domain User  # noqa: E501
        """
        pass

    def test_create_domain_api_v1_domains_post(self):
        """Test case for create_domain_api_v1_domains_post

        Create Domain  # noqa: E501
        """
        pass

    def test_create_domain_invitation_api_v1_domains_domain_invitations_post(self):
        """Test case for create_domain_invitation_api_v1_domains_domain_invitations_post

        Create Domain Invitation  # noqa: E501
        """
        pass

    def test_create_domain_role_api_v1_domains_domain_roles_post(self):
        """Test case for create_domain_role_api_v1_domains_domain_roles_post

        Create Domain Role  # noqa: E501
        """
        pass

    def test_delete_domain_api_v1_domains_domain_delete(self):
        """Test case for delete_domain_api_v1_domains_domain_delete

        Delete Domain  # noqa: E501
        """
        pass

    def test_delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete(self):
        """Test case for delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete

        Delete Domain Invitation  # noqa: E501
        """
        pass

    def test_delete_domain_role_api_v1_domains_domain_roles_role_delete(self):
        """Test case for delete_domain_role_api_v1_domains_domain_roles_role_delete

        Delete Domain Role  # noqa: E501
        """
        pass

    def test_get_domain_api_v1_domains_domain_get(self):
        """Test case for get_domain_api_v1_domains_domain_get

        Get Domain  # noqa: E501
        """
        pass

    def test_get_domain_user_api_v1_domains_domain_users_user_get(self):
        """Test case for get_domain_user_api_v1_domains_domain_users_user_get

        Get Domain User  # noqa: E501
        """
        pass

    def test_join_domain_by_invitation_api_v1_domains_domain_join_post(self):
        """Test case for join_domain_by_invitation_api_v1_domains_domain_join_post

        Join Domain By Invitation  # noqa: E501
        """
        pass

    def test_list_domain_roles_api_v1_domains_domain_roles_get(self):
        """Test case for list_domain_roles_api_v1_domains_domain_roles_get

        List Domain Roles  # noqa: E501
        """
        pass

    def test_list_domain_users_api_v1_domains_domain_users_get(self):
        """Test case for list_domain_users_api_v1_domains_domain_users_get

        List Domain Users  # noqa: E501
        """
        pass

    def test_list_domains_api_v1_domains_get(self):
        """Test case for list_domains_api_v1_domains_get

        List Domains  # noqa: E501
        """
        pass

    def test_remove_domain_user_api_v1_domains_domain_users_user_delete(self):
        """Test case for remove_domain_user_api_v1_domains_domain_users_user_delete

        Remove Domain User  # noqa: E501
        """
        pass

    def test_update_domain_api_v1_domains_domain_patch(self):
        """Test case for update_domain_api_v1_domains_domain_patch

        Update Domain  # noqa: E501
        """
        pass

    def test_update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch(self):
        """Test case for update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch

        Update Domain Invitation  # noqa: E501
        """
        pass

    def test_update_domain_role_api_v1_domains_domain_roles_role_patch(self):
        """Test case for update_domain_role_api_v1_domains_domain_roles_role_patch

        Update Domain Role  # noqa: E501
        """
        pass

    def test_update_domain_user_api_v1_domains_domain_users_user_patch(self):
        """Test case for update_domain_user_api_v1_domains_domain_users_user_patch

        Update Domain User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()