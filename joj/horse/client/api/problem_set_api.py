# coding: utf-8

"""
    JOJ Horse

    Git version: fcd1dab@2021-11-05T13:40:36Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse.client.api_client import ApiClient


class ProblemSetApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_problem_set_api_v1_domains_domain_problem_sets_post(self, body, domain, **kwargs):  # noqa: E501
        """Create Problem Set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_problem_set_api_v1_domains_domain_problem_sets_post(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemSetCreate body: (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemSetResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_problem_set_api_v1_domains_domain_problem_sets_post_with_http_info(body, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.create_problem_set_api_v1_domains_domain_problem_sets_post_with_http_info(body, domain, **kwargs)  # noqa: E501
            return data

    def create_problem_set_api_v1_domains_domain_problem_sets_post_with_http_info(self, body, domain, **kwargs):  # noqa: E501
        """Create Problem Set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_problem_set_api_v1_domains_domain_problem_sets_post_with_http_info(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemSetCreate body: (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemSetResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_problem_set_api_v1_domains_domain_problem_sets_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_problem_set_api_v1_domains_domain_problem_sets_post`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `create_problem_set_api_v1_domains_domain_problem_sets_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/api/v1/domains/{domain}/problem_sets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemSetResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete(self, problem_set, domain, **kwargs):  # noqa: E501
        """Delete Problem Set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete(problem_set, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem_set: url or id of the problem set (required)
        :param str domain: url or id of the domain (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete_with_http_info(problem_set, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete_with_http_info(problem_set, domain, **kwargs)  # noqa: E501
            return data

    def delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete_with_http_info(self, problem_set, domain, **kwargs):  # noqa: E501
        """Delete Problem Set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete_with_http_info(problem_set, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem_set: url or id of the problem set (required)
        :param str domain: url or id of the domain (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['problem_set', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'problem_set' is set
        if ('problem_set' not in params or
                params['problem_set'] is None):
            raise ValueError("Missing the required parameter `problem_set` when calling `delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'problem_set' in params:
            path_params['problemSet'] = params['problem_set']  # noqa: E501
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
            '/api/v1/domains/{domain}/problem_sets/{problem_set}', 'DELETE',
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

    def get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get(self, problem_set, domain, **kwargs):  # noqa: E501
        """Get Problem Set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get(problem_set, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem_set: url or id of the problem set (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemSetResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get_with_http_info(problem_set, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get_with_http_info(problem_set, domain, **kwargs)  # noqa: E501
            return data

    def get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get_with_http_info(self, problem_set, domain, **kwargs):  # noqa: E501
        """Get Problem Set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get_with_http_info(problem_set, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem_set: url or id of the problem set (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemSetResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['problem_set', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'problem_set' is set
        if ('problem_set' not in params or
                params['problem_set'] is None):
            raise ValueError("Missing the required parameter `problem_set` when calling `get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'problem_set' in params:
            path_params['problemSet'] = params['problem_set']  # noqa: E501
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
            '/api/v1/domains/{domain}/problem_sets/{problem_set}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemSetResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get(self, problem_set, domain, **kwargs):  # noqa: E501
        """Get Scoreboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get(problem_set, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem_set: url or id of the problem set (required)
        :param str domain: url or id of the domain (required)
        :return: ScoreBoardResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get_with_http_info(problem_set, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get_with_http_info(problem_set, domain, **kwargs)  # noqa: E501
            return data

    def get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get_with_http_info(self, problem_set, domain, **kwargs):  # noqa: E501
        """Get Scoreboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get_with_http_info(problem_set, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem_set: url or id of the problem set (required)
        :param str domain: url or id of the domain (required)
        :return: ScoreBoardResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['problem_set', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'problem_set' is set
        if ('problem_set' not in params or
                params['problem_set'] is None):
            raise ValueError("Missing the required parameter `problem_set` when calling `get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'problem_set' in params:
            path_params['problemSet'] = params['problem_set']  # noqa: E501
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
            '/api/v1/domains/{domain}/problem_sets/{problem_set}/scoreboard', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScoreBoardResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_problem_sets_api_v1_domains_domain_problem_sets_get(self, domain, **kwargs):  # noqa: E501
        """List Problem Sets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_problem_sets_api_v1_domains_domain_problem_sets_get(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param int offset:
        :param int limit:
        :return: ProblemSetListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_problem_sets_api_v1_domains_domain_problem_sets_get_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.list_problem_sets_api_v1_domains_domain_problem_sets_get_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def list_problem_sets_api_v1_domains_domain_problem_sets_get_with_http_info(self, domain, **kwargs):  # noqa: E501
        """List Problem Sets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_problem_sets_api_v1_domains_domain_problem_sets_get_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param int offset:
        :param int limit:
        :return: ProblemSetListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_problem_sets_api_v1_domains_domain_problem_sets_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `list_problem_sets_api_v1_domains_domain_problem_sets_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501

        query_params = []
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
            '/api/v1/domains/{domain}/problem_sets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemSetListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch(self, body, problem_set, domain, **kwargs):  # noqa: E501
        """Update Problem Set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch(body, problem_set, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemSetEdit body: (required)
        :param str problem_set: url or id of the problem set (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemSetResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch_with_http_info(body, problem_set, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch_with_http_info(body, problem_set, domain, **kwargs)  # noqa: E501
            return data

    def update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch_with_http_info(self, body, problem_set, domain, **kwargs):  # noqa: E501
        """Update Problem Set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch_with_http_info(body, problem_set, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemSetEdit body: (required)
        :param str problem_set: url or id of the problem set (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemSetResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'problem_set', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch`")  # noqa: E501
        # verify the required parameter 'problem_set' is set
        if ('problem_set' not in params or
                params['problem_set'] is None):
            raise ValueError("Missing the required parameter `problem_set` when calling `update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'problem_set' in params:
            path_params['problemSet'] = params['problem_set']  # noqa: E501
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
            '/api/v1/domains/{domain}/problem_sets/{problem_set}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemSetResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
