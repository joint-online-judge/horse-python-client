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
from joj.horse_client.api.judge_api import JudgeApi  # noqa: E501
from joj.horse_client.rest import ApiException


class TestJudgeApi(unittest.TestCase):
    """JudgeApi unit test stubs"""

    def setUp(self):
        self.api = JudgeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_claim_record_by_judge_api_v1_judge_records_record_claim_post(self):
        """Test case for claim_record_by_judge_api_v1_judge_records_record_claim_post

        Claim Record By Judge  # noqa: E501
        """
        pass

    def test_get_judge_key_api_v1_judge_key_get(self):
        """Test case for get_judge_key_api_v1_judge_key_get

        Get Judge Key  # noqa: E501
        """
        pass

    def test_submit_record_by_judge_api_v1_judge_records_record_judgment_post(self):
        """Test case for submit_record_by_judge_api_v1_judge_records_record_judgment_post

        Submit Record By Judge  # noqa: E501
        """
        pass

    def test_update_record_state_by_judge_api_v1_judge_records_record_state_post(self):
        """Test case for update_record_state_by_judge_api_v1_judge_records_record_state_post

        Update Record State By Judge  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
