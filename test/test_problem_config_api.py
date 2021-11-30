# coding: utf-8

"""
    JOJ Horse

    Git version: e54a297@2021-11-30T11:09:19Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse.client
from joj.horse.client.api.problem_config_api import ProblemConfigApi  # noqa: E501
from joj.horse.client.rest import ApiException


class TestProblemConfigApi(unittest.TestCase):
    """ProblemConfigApi unit test stubs"""

    def setUp(self):
        self.api = ProblemConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post(self):
        """Test case for commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post

        Commit Problem Config  # noqa: E501
        """
        pass

    def test_delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete(self):
        """Test case for delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete

        Delete Directory From Uncommitted Problem Config  # noqa: E501
        """
        pass

    def test_delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete(self):
        """Test case for delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete

        Delete File From Uncommitted Problem Config  # noqa: E501
        """
        pass

    def test_download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get(self):
        """Test case for download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get

        Download File In Problem Config  # noqa: E501
        """
        pass

    def test_download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get(self):
        """Test case for download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get

        Download File In Uncommitted Problem Config  # noqa: E501
        """
        pass

    def test_download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get(self):
        """Test case for download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get

        Download Problem Config Archive  # noqa: E501
        """
        pass

    def test_download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get(self):
        """Test case for download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get

        Download Uncommitted Problem Config As Archive  # noqa: E501
        """
        pass

    def test_get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get(self):
        """Test case for get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get

        Get File Or Directory Info In Uncommitted Problem Config  # noqa: E501
        """
        pass

    def test_get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get(self):
        """Test case for get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get

        Get Problem Config Json  # noqa: E501
        """
        pass

    def test_reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post(self):
        """Test case for reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post

        Reset Problem Config  # noqa: E501
        """
        pass

    def test_update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put(self):
        """Test case for update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put

        Update Problem Config By Archive  # noqa: E501
        """
        pass

    def test_upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put(self):
        """Test case for upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put

        Upload File To Problem Config  # noqa: E501
        """
        pass

    def test_upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put(self):
        """Test case for upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put

        Upload File To Root In Problem Config  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
