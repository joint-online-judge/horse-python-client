# coding: utf-8

"""
    JOJ Horse

    Git version: c1be001@2021-11-30T11:32:42Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse.client.api_client import ApiClient


class RecordApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_record_api_v1_domains_domain_records_record_get(self, record, domain, **kwargs):  # noqa: E501
        """Get Record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_api_v1_domains_domain_records_record_get(record, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :param str domain: url or id of the domain (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_record_api_v1_domains_domain_records_record_get_with_http_info(record, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_record_api_v1_domains_domain_records_record_get_with_http_info(record, domain, **kwargs)  # noqa: E501
            return data

    def get_record_api_v1_domains_domain_records_record_get_with_http_info(self, record, domain, **kwargs):  # noqa: E501
        """Get Record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_api_v1_domains_domain_records_record_get_with_http_info(record, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :param str domain: url or id of the domain (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_record_api_v1_domains_domain_records_record_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `get_record_api_v1_domains_domain_records_record_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_record_api_v1_domains_domain_records_record_get`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/{domain}/records/{record}', 'GET',
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

    def get_record_code_api_v1_domains_domain_records_record_code_get(self, record, domain, **kwargs):  # noqa: E501
        """Get Record Code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_code_api_v1_domains_domain_records_record_code_get(record, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :param str domain: url or id of the domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_record_code_api_v1_domains_domain_records_record_code_get_with_http_info(record, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_record_code_api_v1_domains_domain_records_record_code_get_with_http_info(record, domain, **kwargs)  # noqa: E501
            return data

    def get_record_code_api_v1_domains_domain_records_record_code_get_with_http_info(self, record, domain, **kwargs):  # noqa: E501
        """Get Record Code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_code_api_v1_domains_domain_records_record_code_get_with_http_info(record, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :param str domain: url or id of the domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_record_code_api_v1_domains_domain_records_record_code_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `get_record_code_api_v1_domains_domain_records_record_code_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_record_code_api_v1_domains_domain_records_record_code_get`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/{domain}/records/{record}/code', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_records_in_domain_api_v1_domains_domain_records_get(self, domain, **kwargs):  # noqa: E501
        """List Records In Domain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_records_in_domain_api_v1_domains_domain_records_get(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: (required)
        :param str problem_set:
        :param str problem:
        :param int offset:
        :param int limit:
        :param str uid: user id or 'me' or empty
        :return: RecordListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_records_in_domain_api_v1_domains_domain_records_get_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.list_records_in_domain_api_v1_domains_domain_records_get_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def list_records_in_domain_api_v1_domains_domain_records_get_with_http_info(self, domain, **kwargs):  # noqa: E501
        """List Records In Domain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_records_in_domain_api_v1_domains_domain_records_get_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: (required)
        :param str problem_set:
        :param str problem:
        :param int offset:
        :param int limit:
        :param str uid: user id or 'me' or empty
        :return: RecordListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'problem_set', 'problem', 'offset', 'limit', 'uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_records_in_domain_api_v1_domains_domain_records_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `list_records_in_domain_api_v1_domains_domain_records_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501

        query_params = []
        if 'problem_set' in params:
            query_params.append(('problemSet', params['problem_set']))  # noqa: E501
        if 'problem' in params:
            query_params.append(('problem', params['problem']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501

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
            '/api/v1/domains/{domain}/records', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecordListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
