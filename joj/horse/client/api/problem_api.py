# coding: utf-8

"""
    JOJ Horse

    Git version: cb3a7ee@2021-06-22 09:30:15  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse.client.api_client import ApiClient


class ProblemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def clone_problem_api_v1_domains_domain_problems_clone_post(self, body, domain, **kwargs):  # noqa: E501
        """Clone Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clone_problem_api_v1_domains_domain_problems_clone_post(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloneProblem body: (required)
        :param str domain: url or ObjectId of the domain (required)
        :return: ListProblemsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clone_problem_api_v1_domains_domain_problems_clone_post_with_http_info(body, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.clone_problem_api_v1_domains_domain_problems_clone_post_with_http_info(body, domain, **kwargs)  # noqa: E501
            return data

    def clone_problem_api_v1_domains_domain_problems_clone_post_with_http_info(self, body, domain, **kwargs):  # noqa: E501
        """Clone Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clone_problem_api_v1_domains_domain_problems_clone_post_with_http_info(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloneProblem body: (required)
        :param str domain: url or ObjectId of the domain (required)
        :return: ListProblemsResp
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
                    " to method clone_problem_api_v1_domains_domain_problems_clone_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `clone_problem_api_v1_domains_domain_problems_clone_post`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `clone_problem_api_v1_domains_domain_problems_clone_post`")  # noqa: E501

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
            '/api/v1/domains/{domain}/problems/clone', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListProblemsResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_problem_api_v1_domains_domain_problems_post(self, body, domain, **kwargs):  # noqa: E501
        """Create Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_problem_api_v1_domains_domain_problems_post(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemCreate body: (required)
        :param str domain: url or ObjectId of the domain (required)
        :return: ProblemResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_problem_api_v1_domains_domain_problems_post_with_http_info(body, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.create_problem_api_v1_domains_domain_problems_post_with_http_info(body, domain, **kwargs)  # noqa: E501
            return data

    def create_problem_api_v1_domains_domain_problems_post_with_http_info(self, body, domain, **kwargs):  # noqa: E501
        """Create Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_problem_api_v1_domains_domain_problems_post_with_http_info(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemCreate body: (required)
        :param str domain: url or ObjectId of the domain (required)
        :return: ProblemResp
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
                    " to method create_problem_api_v1_domains_domain_problems_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_problem_api_v1_domains_domain_problems_post`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `create_problem_api_v1_domains_domain_problems_post`")  # noqa: E501

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
            '/api/v1/domains/{domain}/problems', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_problem_api_v1_domains_domain_problems_problem_delete(self, domain, problem, **kwargs):  # noqa: E501
        """Delete Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_problem_api_v1_domains_domain_problems_problem_delete(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or ObjectId of the domain (required)
        :param str problem: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_problem_api_v1_domains_domain_problems_problem_delete_with_http_info(domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_problem_api_v1_domains_domain_problems_problem_delete_with_http_info(domain, problem, **kwargs)  # noqa: E501
            return data

    def delete_problem_api_v1_domains_domain_problems_problem_delete_with_http_info(self, domain, problem, **kwargs):  # noqa: E501
        """Delete Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_problem_api_v1_domains_domain_problems_problem_delete_with_http_info(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or ObjectId of the domain (required)
        :param str problem: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'problem']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_problem_api_v1_domains_domain_problems_problem_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `delete_problem_api_v1_domains_domain_problems_problem_delete`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `delete_problem_api_v1_domains_domain_problems_problem_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501

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
            '/api/v1/domains/{domain}/problems/{problem}', 'DELETE',
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

    def get_problem_api_v1_domains_domain_problems_problem_get(self, domain, problem, **kwargs):  # noqa: E501
        """Get Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_problem_api_v1_domains_domain_problems_problem_get(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or ObjectId of the domain (required)
        :param str problem: (required)
        :return: ProblemResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_problem_api_v1_domains_domain_problems_problem_get_with_http_info(domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.get_problem_api_v1_domains_domain_problems_problem_get_with_http_info(domain, problem, **kwargs)  # noqa: E501
            return data

    def get_problem_api_v1_domains_domain_problems_problem_get_with_http_info(self, domain, problem, **kwargs):  # noqa: E501
        """Get Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_problem_api_v1_domains_domain_problems_problem_get_with_http_info(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or ObjectId of the domain (required)
        :param str problem: (required)
        :return: ProblemResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'problem']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_problem_api_v1_domains_domain_problems_problem_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_problem_api_v1_domains_domain_problems_problem_get`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `get_problem_api_v1_domains_domain_problems_problem_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501

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
            '/api/v1/domains/{domain}/problems/{problem}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_problems_api_v1_domains_domain_problems_get(self, domain, **kwargs):  # noqa: E501
        """List Problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_problems_api_v1_domains_domain_problems_get(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or ObjectId of the domain (required)
        :param str problem_set:
        :param str problem_group:
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListProblemsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_problems_api_v1_domains_domain_problems_get_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.list_problems_api_v1_domains_domain_problems_get_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def list_problems_api_v1_domains_domain_problems_get_with_http_info(self, domain, **kwargs):  # noqa: E501
        """List Problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_problems_api_v1_domains_domain_problems_get_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or ObjectId of the domain (required)
        :param str problem_set:
        :param str problem_group:
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListProblemsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'problem_set', 'problem_group', 'sort', 'skip', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_problems_api_v1_domains_domain_problems_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `list_problems_api_v1_domains_domain_problems_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501

        query_params = []
        if 'problem_set' in params:
            query_params.append(('problem_set', params['problem_set']))  # noqa: E501
        if 'problem_group' in params:
            query_params.append(('problem_group', params['problem_group']))  # noqa: E501
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
            '/api/v1/domains/{domain}/problems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListProblemsResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def submit_solution_to_problem_api_v1_domains_domain_problems_problem_post(self, code_type, file, domain, problem, **kwargs):  # noqa: E501
        """Submit Solution To Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_solution_to_problem_api_v1_domains_domain_problems_problem_post(code_type, file, domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCodeType code_type: (required)
        :param str file: (required)
        :param str domain: url or ObjectId of the domain (required)
        :param str problem: (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.submit_solution_to_problem_api_v1_domains_domain_problems_problem_post_with_http_info(code_type, file, domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.submit_solution_to_problem_api_v1_domains_domain_problems_problem_post_with_http_info(code_type, file, domain, problem, **kwargs)  # noqa: E501
            return data

    def submit_solution_to_problem_api_v1_domains_domain_problems_problem_post_with_http_info(self, code_type, file, domain, problem, **kwargs):  # noqa: E501
        """Submit Solution To Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_solution_to_problem_api_v1_domains_domain_problems_problem_post_with_http_info(code_type, file, domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCodeType code_type: (required)
        :param str file: (required)
        :param str domain: url or ObjectId of the domain (required)
        :param str problem: (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_type', 'file', 'domain', 'problem']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_solution_to_problem_api_v1_domains_domain_problems_problem_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code_type' is set
        if ('code_type' not in params or
                params['code_type'] is None):
            raise ValueError("Missing the required parameter `code_type` when calling `submit_solution_to_problem_api_v1_domains_domain_problems_problem_post`")  # noqa: E501
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `submit_solution_to_problem_api_v1_domains_domain_problems_problem_post`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `submit_solution_to_problem_api_v1_domains_domain_problems_problem_post`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `submit_solution_to_problem_api_v1_domains_domain_problems_problem_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'code_type' in params:
            form_params.append(('code_type', params['code_type']))  # noqa: E501
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/domains/{domain}/problems/{problem}', 'POST',
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

    def update_problem_api_v1_domains_domain_problems_problem_patch(self, body, domain, problem, **kwargs):  # noqa: E501
        """Update Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_problem_api_v1_domains_domain_problems_problem_patch(body, domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemEdit body: (required)
        :param str domain: url or ObjectId of the domain (required)
        :param str problem: (required)
        :return: ProblemResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_problem_api_v1_domains_domain_problems_problem_patch_with_http_info(body, domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.update_problem_api_v1_domains_domain_problems_problem_patch_with_http_info(body, domain, problem, **kwargs)  # noqa: E501
            return data

    def update_problem_api_v1_domains_domain_problems_problem_patch_with_http_info(self, body, domain, problem, **kwargs):  # noqa: E501
        """Update Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_problem_api_v1_domains_domain_problems_problem_patch_with_http_info(body, domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemEdit body: (required)
        :param str domain: url or ObjectId of the domain (required)
        :param str problem: (required)
        :return: ProblemResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain', 'problem']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_problem_api_v1_domains_domain_problems_problem_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_problem_api_v1_domains_domain_problems_problem_patch`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `update_problem_api_v1_domains_domain_problems_problem_patch`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `update_problem_api_v1_domains_domain_problems_problem_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501

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
            '/api/v1/domains/{domain}/problems/{problem}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
