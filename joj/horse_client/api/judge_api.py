# coding: utf-8

"""
    JOJ Horse

    Git version: 4e88176@2022-02-19T13:04:07Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse_client.api_client import ApiClient


class JudgeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_claim_record_by_judge(self, body, domain, record, **kwargs):  # noqa: E501
        """Claim Record By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_claim_record_by_judge(body, domain, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JudgeClaim body: (required)
        :param str domain: url or id of the domain (required)
        :param str record: (required)
        :return: JudgeCredentialsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_claim_record_by_judge_with_http_info(body, domain, record, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_claim_record_by_judge_with_http_info(body, domain, record, **kwargs)  # noqa: E501
            return data

    def v1_claim_record_by_judge_with_http_info(self, body, domain, record, **kwargs):  # noqa: E501
        """Claim Record By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_claim_record_by_judge_with_http_info(body, domain, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JudgeClaim body: (required)
        :param str domain: url or id of the domain (required)
        :param str record: (required)
        :return: JudgeCredentialsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain', 'record']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_claim_record_by_judge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_claim_record_by_judge`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_claim_record_by_judge`")  # noqa: E501
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `v1_claim_record_by_judge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
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
            '/judge/records/{record}/claim', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JudgeCredentialsResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_submit_record_by_judge(self, body, domain, record, **kwargs):  # noqa: E501
        """Submit Record By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_submit_record_by_judge(body, domain, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordResult body: (required)
        :param str domain: url or id of the domain (required)
        :param str record: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_submit_record_by_judge_with_http_info(body, domain, record, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_submit_record_by_judge_with_http_info(body, domain, record, **kwargs)  # noqa: E501
            return data

    def v1_submit_record_by_judge_with_http_info(self, body, domain, record, **kwargs):  # noqa: E501
        """Submit Record By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_submit_record_by_judge_with_http_info(body, domain, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordResult body: (required)
        :param str domain: url or id of the domain (required)
        :param str record: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain', 'record']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_submit_record_by_judge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_submit_record_by_judge`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_submit_record_by_judge`")  # noqa: E501
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `v1_submit_record_by_judge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
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
            '/judge/records/{record}/judgment', 'POST',
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

    def v1_update_record_state_by_judge(self, domain, record, **kwargs):  # noqa: E501
        """Update Record State By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_update_record_state_by_judge(domain, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str record: (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_update_record_state_by_judge_with_http_info(domain, record, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_update_record_state_by_judge_with_http_info(domain, record, **kwargs)  # noqa: E501
            return data

    def v1_update_record_state_by_judge_with_http_info(self, domain, record, **kwargs):  # noqa: E501
        """Update Record State By Judge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_update_record_state_by_judge_with_http_info(domain, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str record: (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'record']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_update_record_state_by_judge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_update_record_state_by_judge`")  # noqa: E501
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `v1_update_record_state_by_judge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
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
            '/judge/records/{record}/state', 'POST',
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
