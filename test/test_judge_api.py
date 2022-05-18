# coding: utf-8

"""
    JOJ Horse

    Git version: c41bfc4@2022-05-18T21:45:42Z  # noqa: E501

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

    def test_v1_claim_record_by_judger(self):
        """Test case for v1_claim_record_by_judger

        Claim Record By Judger  # noqa: E501
        """
        pass

    def test_v1_submit_case_by_judger(self):
        """Test case for v1_submit_case_by_judger

        Submit Case By Judger  # noqa: E501
        """
        pass

    def test_v1_submit_record_by_judger(self):
        """Test case for v1_submit_record_by_judger

        Submit Record By Judger  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
