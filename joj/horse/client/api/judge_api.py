# coding: utf-8

"""
    JOJ Horse

    Git version: e1ec5a4@2021-11-30T12:04:58Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse.client.api_client import ApiClient


class JudgeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def claim_record_by_judge_api_v1_judge_records_record_claim_post(self, record, **kwargs):  # noqa: E501
        """Claim Record By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.claim_record_by_judge_api_v1_judge_records_record_claim_post(record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :return: JudgeClaimResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.claim_record_by_judge_api_v1_judge_records_record_claim_post_with_http_info(record, **kwargs)  # noqa: E501
        else:
            (data) = self.claim_record_by_judge_api_v1_judge_records_record_claim_post_with_http_info(record, **kwargs)  # noqa: E501
            return data

    def claim_record_by_judge_api_v1_judge_records_record_claim_post_with_http_info(self, record, **kwargs):  # noqa: E501
        """Claim Record By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.claim_record_by_judge_api_v1_judge_records_record_claim_post_with_http_info(record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :return: JudgeClaimResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method claim_record_by_judge_api_v1_judge_records_record_claim_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `claim_record_by_judge_api_v1_judge_records_record_claim_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'record' in params:
            path_params['record'] = params['record']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/judge/records/{record}/claim', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JudgeClaimResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_judge_key_api_v1_judge_key_get(self, **kwargs):  # noqa: E501
        """Get Judge Key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_judge_key_api_v1_judge_key_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserAccessKeyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_judge_key_api_v1_judge_key_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_judge_key_api_v1_judge_key_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_judge_key_api_v1_judge_key_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Judge Key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_judge_key_api_v1_judge_key_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserAccessKeyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_judge_key_api_v1_judge_key_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/judge/key', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserAccessKeyResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def submit_record_by_judge_api_v1_judge_records_record_judgment_post(self, body, record, **kwargs):  # noqa: E501
        """Submit Record By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_record_by_judge_api_v1_judge_records_record_judgment_post(body, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordResult body: (required)
        :param str record: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.submit_record_by_judge_api_v1_judge_records_record_judgment_post_with_http_info(body, record, **kwargs)  # noqa: E501
        else:
            (data) = self.submit_record_by_judge_api_v1_judge_records_record_judgment_post_with_http_info(body, record, **kwargs)  # noqa: E501
            return data

    def submit_record_by_judge_api_v1_judge_records_record_judgment_post_with_http_info(self, body, record, **kwargs):  # noqa: E501
        """Submit Record By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_record_by_judge_api_v1_judge_records_record_judgment_post_with_http_info(body, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordResult body: (required)
        :param str record: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'record']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_record_by_judge_api_v1_judge_records_record_judgment_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `submit_record_by_judge_api_v1_judge_records_record_judgment_post`")  # noqa: E501
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `submit_record_by_judge_api_v1_judge_records_record_judgment_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'record' in params:
            path_params['record'] = params['record']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/judge/records/{record}/judgment', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_record_state_by_judge_api_v1_judge_records_record_state_post(self, record, **kwargs):  # noqa: E501
        """Update Record State By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_record_state_by_judge_api_v1_judge_records_record_state_post(record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_record_state_by_judge_api_v1_judge_records_record_state_post_with_http_info(record, **kwargs)  # noqa: E501
        else:
            (data) = self.update_record_state_by_judge_api_v1_judge_records_record_state_post_with_http_info(record, **kwargs)  # noqa: E501
            return data

    def update_record_state_by_judge_api_v1_judge_records_record_state_post_with_http_info(self, record, **kwargs):  # noqa: E501
        """Update Record State By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_record_state_by_judge_api_v1_judge_records_record_state_post_with_http_info(record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_record_state_by_judge_api_v1_judge_records_record_state_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `update_record_state_by_judge_api_v1_judge_records_record_state_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'record' in params:
            path_params['record'] = params['record']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/judge/records/{record}/state', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecordResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
