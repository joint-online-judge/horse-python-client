# coding: utf-8

"""
    JOJ Horse

    Git version: ed873b1@2021-07-10 15:20:47  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse.client.api_client import ApiClient


class ProblemGroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_problem_groups_api_v1_problem_groups_get(self, **kwargs):  # noqa: E501
        """List Problem Groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_problem_groups_api_v1_problem_groups_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListProblemGroupsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_problem_groups_api_v1_problem_groups_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_problem_groups_api_v1_problem_groups_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_problem_groups_api_v1_problem_groups_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Problem Groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_problem_groups_api_v1_problem_groups_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListProblemGroupsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'skip', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_problem_groups_api_v1_problem_groups_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/api/v1/problem_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListProblemGroupsResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
