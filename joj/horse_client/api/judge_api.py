# coding: utf-8

"""
    JOJ Horse

    Git version: 95652f1@2022-05-08T17:53:17Z  # noqa: E501

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

    def v1_claim_record_by_judger(self, body, domain, record, **kwargs):  # noqa: E501
        """Claim Record By Judger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_claim_record_by_judger(body, domain, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JudgerClaim body: (required)
        :param str domain: url or id of the domain (required)
        :param str record: (required)
        :return: JudgerCredentialsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_claim_record_by_judger_with_http_info(body, domain, record, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_claim_record_by_judger_with_http_info(body, domain, record, **kwargs)  # noqa: E501
            return data

    def v1_claim_record_by_judger_with_http_info(self, body, domain, record, **kwargs):  # noqa: E501
        """Claim Record By Judger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_claim_record_by_judger_with_http_info(body, domain, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JudgerClaim body: (required)
        :param str domain: url or id of the domain (required)
        :param str record: (required)
        :return: JudgerCredentialsResp
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
                    " to method v1_claim_record_by_judger" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_claim_record_by_judger`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_claim_record_by_judger`")  # noqa: E501
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `v1_claim_record_by_judger`")  # noqa: E501

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
            '/domains/{domain}/records/{record}/judge/claim', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JudgerCredentialsResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_submit_case_by_judger(self, body, case, record, domain, **kwargs):  # noqa: E501
        """Submit Case By Judger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_submit_case_by_judger(body, case, record, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCaseSubmit body: (required)
        :param int case: (required)
        :param str record: (required)
        :param str domain: url or id of the domain (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_submit_case_by_judger_with_http_info(body, case, record, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_submit_case_by_judger_with_http_info(body, case, record, domain, **kwargs)  # noqa: E501
            return data

    def v1_submit_case_by_judger_with_http_info(self, body, case, record, domain, **kwargs):  # noqa: E501
        """Submit Case By Judger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_submit_case_by_judger_with_http_info(body, case, record, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCaseSubmit body: (required)
        :param int case: (required)
        :param str record: (required)
        :param str domain: url or id of the domain (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'case', 'record', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_submit_case_by_judger" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_submit_case_by_judger`")  # noqa: E501
        # verify the required parameter 'case' is set
        if ('case' not in params or
                params['case'] is None):
            raise ValueError("Missing the required parameter `case` when calling `v1_submit_case_by_judger`")  # noqa: E501
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `v1_submit_case_by_judger`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_submit_case_by_judger`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'case' in params:
            path_params['case'] = params['case']  # noqa: E501
        if 'record' in params:
            path_params['record'] = params['record']  # noqa: E501
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501

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
            '/domains/{domain}/records/{record}/cases/{case}/judge', 'PUT',
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

    def v1_submit_record_by_judger(self, body, record, domain, **kwargs):  # noqa: E501
        """Submit Record By Judger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_submit_record_by_judger(body, record, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordSubmit body: (required)
        :param str record: (required)
        :param str domain: url or id of the domain (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_submit_record_by_judger_with_http_info(body, record, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_submit_record_by_judger_with_http_info(body, record, domain, **kwargs)  # noqa: E501
            return data

    def v1_submit_record_by_judger_with_http_info(self, body, record, domain, **kwargs):  # noqa: E501
        """Submit Record By Judger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_submit_record_by_judger_with_http_info(body, record, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordSubmit body: (required)
        :param str record: (required)
        :param str domain: url or id of the domain (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'record', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_submit_record_by_judger" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_submit_record_by_judger`")  # noqa: E501
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `v1_submit_record_by_judger`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_submit_record_by_judger`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'record' in params:
            path_params['record'] = params['record']  # noqa: E501
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501

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
            '/domains/{domain}/records/{record}/judge', 'PUT',
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
