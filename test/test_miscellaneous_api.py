# coding: utf-8

"""
    JOJ Horse

    Git version: d7c0f43@2021-06-19 09:51:51  # noqa: E501

    OpenAPI spec version: 0.0.0
    
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

    def test_jwt_api_v1_jwt_get(self):
        """Test case for jwt_api_v1_jwt_get

        Jwt  # noqa: E501
        """
        pass

    def test_test_sentry_api_v1_test_sentry_get(self):
        """Test case for test_sentry_api_v1_test_sentry_get

        Test Sentry  # noqa: E501
        """
        pass

    def test_version_api_v1_version_get(self):
        """Test case for version_api_v1_version_get

        Version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
