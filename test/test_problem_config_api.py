# coding: utf-8

"""
    JOJ Horse

    Git version: eb69285@2022-05-16T11:33:39Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse_client
from joj.horse_client.api.problem_config_api import ProblemConfigApi  # noqa: E501
from joj.horse_client.rest import ApiException


class TestProblemConfigApi(unittest.TestCase):
    """ProblemConfigApi unit test stubs"""

    def setUp(self):
        self.api = ProblemConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_commit_problem_config(self):
        """Test case for v1_commit_problem_config

        Commit Problem Config  # noqa: E501
        """
        pass

    def test_v1_delete_directory_from_uncommitted_problem_config(self):
        """Test case for v1_delete_directory_from_uncommitted_problem_config

        Delete Directory From Uncommitted Problem Config  # noqa: E501
        """
        pass

    def test_v1_delete_file_from_uncommitted_problem_config(self):
        """Test case for v1_delete_file_from_uncommitted_problem_config

        Delete File From Uncommitted Problem Config  # noqa: E501
        """
        pass

    def test_v1_diff_problem_config_default_branch(self):
        """Test case for v1_diff_problem_config_default_branch

        Diff Problem Config Default Branch  # noqa: E501
        """
        pass

    def test_v1_download_file_in_problem_config(self):
        """Test case for v1_download_file_in_problem_config

        Download File In Problem Config  # noqa: E501
        """
        pass

    def test_v1_download_file_in_uncommitted_problem_config(self):
        """Test case for v1_download_file_in_uncommitted_problem_config

        Download File In Uncommitted Problem Config  # noqa: E501
        """
        pass

    def test_v1_download_problem_config_archive(self):
        """Test case for v1_download_problem_config_archive

        Download Problem Config Archive  # noqa: E501
        """
        pass

    def test_v1_download_uncommitted_problem_config_as_archive(self):
        """Test case for v1_download_uncommitted_problem_config_as_archive

        Download Uncommitted Problem Config As Archive  # noqa: E501
        """
        pass

    def test_v1_get_file_or_directory_info_in_uncommitted_problem_config(self):
        """Test case for v1_get_file_or_directory_info_in_uncommitted_problem_config

        Get File Or Directory Info In Uncommitted Problem Config  # noqa: E501
        """
        pass

    def test_v1_get_problem_config_json(self):
        """Test case for v1_get_problem_config_json

        Get Problem Config Json  # noqa: E501
        """
        pass

    def test_v1_list_latest_problem_config_objects_under_a_given_prefix(self):
        """Test case for v1_list_latest_problem_config_objects_under_a_given_prefix

        List Latest Problem Config Objects Under A Given Prefix  # noqa: E501
        """
        pass

    def test_v1_reset_problem_config(self):
        """Test case for v1_reset_problem_config

        Reset Problem Config  # noqa: E501
        """
        pass

    def test_v1_update_problem_config_by_archive(self):
        """Test case for v1_update_problem_config_by_archive

        Update Problem Config By Archive  # noqa: E501
        """
        pass

    def test_v1_update_problem_config_json(self):
        """Test case for v1_update_problem_config_json

        Update Problem Config Json  # noqa: E501
        """
        pass

    def test_v1_upload_file_to_problem_config(self):
        """Test case for v1_upload_file_to_problem_config

        Upload File To Problem Config  # noqa: E501
        """
        pass

    def test_v1_upload_file_to_root_in_problem_config(self):
        """Test case for v1_upload_file_to_root_in_problem_config

        Upload File To Root In Problem Config  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
