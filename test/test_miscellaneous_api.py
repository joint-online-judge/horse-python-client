# coding: utf-8

"""
    JOJ Horse

    Git version: c4a9464@2022-05-31T05:05:16Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse_client
from joj.horse_client.api.miscellaneous_api import MiscellaneousApi  # noqa: E501
from joj.horse_client.rest import ApiException


class TestMiscellaneousApi(unittest.TestCase):
    """MiscellaneousApi unit test stubs"""

    def setUp(self):
        self.api = MiscellaneousApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_jwt_decoded(self):
        """Test case for v1_jwt_decoded

        Jwt Decoded  # noqa: E501
        """
        pass

    def test_v1_test_error_report(self):
        """Test case for v1_test_error_report

        Test Error Report  # noqa: E501
        """
        pass

    def test_v1_version(self):
        """Test case for v1_version

        Version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
