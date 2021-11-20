# coding: utf-8

"""
    JOJ Horse

    Git version: cd9daeb@2021-11-20T15:28:43Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse.client
from joj.horse.client.api.miscellaneous_api import MiscellaneousApi  # noqa: E501
from joj.horse.client.rest import ApiException


class TestMiscellaneousApi(unittest.TestCase):
    """MiscellaneousApi unit test stubs"""

    def setUp(self):
        self.api = MiscellaneousApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_jwt_decoded_api_v1_jwt_decoded_get(self):
        """Test case for jwt_decoded_api_v1_jwt_decoded_get

        Jwt Decoded  # noqa: E501
        """
        pass

    def test_set_root_user_api_v1_set_root_user_post(self):
        """Test case for set_root_user_api_v1_set_root_user_post

        Set Root User  # noqa: E501
        """
        pass

    def test_test_error_report_api_v1_test_report_get(self):
        """Test case for test_error_report_api_v1_test_report_get

        Test Error Report  # noqa: E501
        """
        pass

    def test_version_api_v1_version_get(self):
        """Test case for version_api_v1_version_get

        Version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
