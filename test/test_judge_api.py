# coding: utf-8

"""
    JOJ Horse

    Git version: 5882f3b@2021-12-15T14:55:00Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import joj.horse_client
from joj.horse_client.api.judge_api import JudgeApi  # noqa: E501
from joj.horse_client.rest import ApiException


class TestJudgeApi(unittest.TestCase):
    """JudgeApi unit test stubs"""

    def setUp(self):
        self.api = JudgeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_claim_record_by_judge(self):
        """Test case for v1_claim_record_by_judge

        Claim Record By Judge  # noqa: E501
        """
        pass

    def test_v1_submit_record_by_judge(self):
        """Test case for v1_submit_record_by_judge

        Submit Record By Judge  # noqa: E501
        """
        pass

    def test_v1_update_record_state_by_judge(self):
        """Test case for v1_update_record_state_by_judge

        Update Record State By Judge  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
