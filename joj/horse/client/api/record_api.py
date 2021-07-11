# coding: utf-8

"""
    JOJ Horse

    Git version: ce24503@2021-07-11 18:04:50  # noqa: E501

    OpenAPI spec version: 0.0.0
    
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

    def get_record_api_v1_records_record_get(self, record, **kwargs):  # noqa: E501
        """Get Record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_api_v1_records_record_get(record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_record_api_v1_records_record_get_with_http_info(record, **kwargs)  # noqa: E501
        else:
            (data) = self.get_record_api_v1_records_record_get_with_http_info(record, **kwargs)  # noqa: E501
            return data

    def get_record_api_v1_records_record_get_with_http_info(self, record, **kwargs):  # noqa: E501
        """Get Record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_api_v1_records_record_get_with_http_info(record, async_req=True)
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
                    " to method get_record_api_v1_records_record_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `get_record_api_v1_records_record_get`")  # noqa: E501

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
            '/api/v1/records/{record}', 'GET',
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

    def get_record_code_api_v1_records_record_code_get(self, record, **kwargs):  # noqa: E501
        """Get Record Code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_code_api_v1_records_record_code_get(record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_record_code_api_v1_records_record_code_get_with_http_info(record, **kwargs)  # noqa: E501
        else:
            (data) = self.get_record_code_api_v1_records_record_code_get_with_http_info(record, **kwargs)  # noqa: E501
            return data

    def get_record_code_api_v1_records_record_code_get_with_http_info(self, record, **kwargs):  # noqa: E501
        """Get Record Code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_code_api_v1_records_record_code_get_with_http_info(record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record: (required)
        :return: Object
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
                    " to method get_record_code_api_v1_records_record_code_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `get_record_code_api_v1_records_record_code_get`")  # noqa: E501

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
            '/api/v1/records/{record}/code', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def http_record_api_v1_records_record_http_post(self, body, record, **kwargs):  # noqa: E501
        """Http Record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.http_record_api_v1_records_record_http_post(body, record, async_req=True)
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
            return self.http_record_api_v1_records_record_http_post_with_http_info(body, record, **kwargs)  # noqa: E501
        else:
            (data) = self.http_record_api_v1_records_record_http_post_with_http_info(body, record, **kwargs)  # noqa: E501
            return data

    def http_record_api_v1_records_record_http_post_with_http_info(self, body, record, **kwargs):  # noqa: E501
        """Http Record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.http_record_api_v1_records_record_http_post_with_http_info(body, record, async_req=True)
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
                    " to method http_record_api_v1_records_record_http_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `http_record_api_v1_records_record_http_post`")  # noqa: E501
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `http_record_api_v1_records_record_http_post`")  # noqa: E501

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
            '/api/v1/records/{record}/http', 'POST',
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

    def http_record_cases_api_v1_records_record_cases_http_post(self, body, record, **kwargs):  # noqa: E501
        """Http Record Cases  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.http_record_cases_api_v1_records_record_cases_http_post(body, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCaseResult body: (required)
        :param str record: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.http_record_cases_api_v1_records_record_cases_http_post_with_http_info(body, record, **kwargs)  # noqa: E501
        else:
            (data) = self.http_record_cases_api_v1_records_record_cases_http_post_with_http_info(body, record, **kwargs)  # noqa: E501
            return data

    def http_record_cases_api_v1_records_record_cases_http_post_with_http_info(self, body, record, **kwargs):  # noqa: E501
        """Http Record Cases  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.http_record_cases_api_v1_records_record_cases_http_post_with_http_info(body, record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCaseResult body: (required)
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
                    " to method http_record_cases_api_v1_records_record_cases_http_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `http_record_cases_api_v1_records_record_cases_http_post`")  # noqa: E501
        # verify the required parameter 'record' is set
        if ('record' not in params or
                params['record'] is None):
            raise ValueError("Missing the required parameter `record` when calling `http_record_cases_api_v1_records_record_cases_http_post`")  # noqa: E501

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
            '/api/v1/records/{record}/cases/http', 'POST',
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

    def list_records_api_v1_records_get(self, **kwargs):  # noqa: E501
        """List Records  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_records_api_v1_records_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain:
        :param str problem_set:
        :param str problem:
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :param str uid: uid or 'me' or empty
        :return: ListRecordsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_records_api_v1_records_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_records_api_v1_records_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_records_api_v1_records_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Records  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_records_api_v1_records_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain:
        :param str problem_set:
        :param str problem:
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :param str uid: uid or 'me' or empty
        :return: ListRecordsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'problem_set', 'problem', 'sort', 'skip', 'limit', 'uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_records_api_v1_records_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in params:
            query_params.append(('domain', params['domain']))  # noqa: E501
        if 'problem_set' in params:
            query_params.append(('problem_set', params['problem_set']))  # noqa: E501
        if 'problem' in params:
            query_params.append(('problem', params['problem']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/api/v1/records', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListRecordsResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
