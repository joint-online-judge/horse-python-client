# coding: utf-8

"""
    JOJ Horse

    Git version: ae0c6d5@2022-01-02T19:29:09Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse_client.api_client import ApiClient


class RecordApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_get_record(self, record, domain, **kwargs):  # noqa: E501
        """Get Record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_record(record, domain, async_req=True)
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
            return self.v1_get_record_with_http_info(record, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_get_record_with_http_info(record, domain, **kwargs)  # noqa: E501
            return data

    def v1_get_record_with_http_info(self, record, domain, **kwargs):  # noqa: E501
        """Get Record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_record_with_http_info(record, domain, async_req=True)
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
                    " to method v1_get_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `v1_get_record`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_get_record`")  # noqa: E501

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
            '/domains/{domain}/records/{record}', 'GET',
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

    def v1_get_record_code(self, record, domain, **kwargs):  # noqa: E501
        """Get Record Code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_record_code(record, domain, async_req=True)
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
            return self.v1_get_record_code_with_http_info(record, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_get_record_code_with_http_info(record, domain, **kwargs)  # noqa: E501
            return data

    def v1_get_record_code_with_http_info(self, record, domain, **kwargs):  # noqa: E501
        """Get Record Code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_record_code_with_http_info(record, domain, async_req=True)
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
                    " to method v1_get_record_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `v1_get_record_code`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_get_record_code`")  # noqa: E501

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
            '/domains/{domain}/records/{record}/code', 'GET',
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

    def v1_list_records_in_domain(self, domain, **kwargs):  # noqa: E501
        """List Records In Domain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_records_in_domain(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str ordering: Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at
        :param int offset:
        :param int limit:
        :return: RecordListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_list_records_in_domain_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_list_records_in_domain_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def v1_list_records_in_domain_with_http_info(self, domain, **kwargs):  # noqa: E501
        """List Records In Domain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_records_in_domain_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str ordering: Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at
        :param int offset:
        :param int limit:
        :return: RecordListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'ordering', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_list_records_in_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_list_records_in_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501

        query_params = []
        if 'ordering' in params:
            query_params.append(('ordering', params['ordering']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/domains/{domain}/records', 'GET',
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
