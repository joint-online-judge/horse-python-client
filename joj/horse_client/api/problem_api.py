# coding: utf-8

"""
    JOJ Horse

    Git version: f5d7fa1@2022-01-02T18:10:26Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse_client.api_client import ApiClient


class ProblemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_clone_problem(self, body, domain, **kwargs):  # noqa: E501
        """Clone Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_clone_problem(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemClone body: (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_clone_problem_with_http_info(body, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_clone_problem_with_http_info(body, domain, **kwargs)  # noqa: E501
            return data

    def v1_clone_problem_with_http_info(self, body, domain, **kwargs):  # noqa: E501
        """Clone Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_clone_problem_with_http_info(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemClone body: (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemListResp
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
                    " to method v1_clone_problem" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_clone_problem`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_clone_problem`")  # noqa: E501

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
            '/domains/{domain}/problems/clone', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_create_problem(self, body, domain, **kwargs):  # noqa: E501
        """Create Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_create_problem(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemCreate body: (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_create_problem_with_http_info(body, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_create_problem_with_http_info(body, domain, **kwargs)  # noqa: E501
            return data

    def v1_create_problem_with_http_info(self, body, domain, **kwargs):  # noqa: E501
        """Create Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_create_problem_with_http_info(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemCreate body: (required)
        :param str domain: url or id of the domain (required)
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
                    " to method v1_create_problem" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_create_problem`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_create_problem`")  # noqa: E501

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
            '/domains/{domain}/problems', 'POST',
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

    def v1_delete_problem(self, domain, problem, **kwargs):  # noqa: E501
        """Delete Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_delete_problem(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_delete_problem_with_http_info(domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_delete_problem_with_http_info(domain, problem, **kwargs)  # noqa: E501
            return data

    def v1_delete_problem_with_http_info(self, domain, problem, **kwargs):  # noqa: E501
        """Delete Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_delete_problem_with_http_info(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
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
                    " to method v1_delete_problem" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_delete_problem`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_delete_problem`")  # noqa: E501

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
            '/domains/{domain}/problems/{problem}', 'DELETE',
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

    def v1_get_problem(self, domain, problem, **kwargs):  # noqa: E501
        """Get Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_problem(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :return: ProblemDetailWithLatestRecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_get_problem_with_http_info(domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_get_problem_with_http_info(domain, problem, **kwargs)  # noqa: E501
            return data

    def v1_get_problem_with_http_info(self, domain, problem, **kwargs):  # noqa: E501
        """Get Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_problem_with_http_info(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :return: ProblemDetailWithLatestRecordResp
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
                    " to method v1_get_problem" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_get_problem`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_get_problem`")  # noqa: E501

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
            '/domains/{domain}/problems/{problem}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemDetailWithLatestRecordResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_list_problems(self, domain, **kwargs):  # noqa: E501
        """List Problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_problems(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str ordering: Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at
        :param int offset:
        :param int limit:
        :return: ProblemWithLatestRecordListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_list_problems_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_list_problems_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def v1_list_problems_with_http_info(self, domain, **kwargs):  # noqa: E501
        """List Problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_problems_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str ordering: Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at
        :param int offset:
        :param int limit:
        :return: ProblemWithLatestRecordListResp
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
                    " to method v1_list_problems" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_list_problems`")  # noqa: E501

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
            '/domains/{domain}/problems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemWithLatestRecordListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_submit_solution_to_problem(self, code_type, file, domain, problem, **kwargs):  # noqa: E501
        """Submit Solution To Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_submit_solution_to_problem(code_type, file, domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCodeType code_type: (required)
        :param str file: (required)
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :return: RecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_submit_solution_to_problem_with_http_info(code_type, file, domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_submit_solution_to_problem_with_http_info(code_type, file, domain, problem, **kwargs)  # noqa: E501
            return data

    def v1_submit_solution_to_problem_with_http_info(self, code_type, file, domain, problem, **kwargs):  # noqa: E501
        """Submit Solution To Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_submit_solution_to_problem_with_http_info(code_type, file, domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCodeType code_type: (required)
        :param str file: (required)
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
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
                    " to method v1_submit_solution_to_problem" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code_type' is set
        if ('code_type' not in params or
                params['code_type'] is None):
            raise ValueError("Missing the required parameter `code_type` when calling `v1_submit_solution_to_problem`")  # noqa: E501
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `v1_submit_solution_to_problem`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_submit_solution_to_problem`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_submit_solution_to_problem`")  # noqa: E501

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
            form_params.append(('codeType', params['code_type']))  # noqa: E501
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
            '/domains/{domain}/problems/{problem}', 'POST',
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

    def v1_update_problem(self, body, domain, problem, **kwargs):  # noqa: E501
        """Update Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_update_problem(body, domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemEdit body: (required)
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :return: ProblemResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_update_problem_with_http_info(body, domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_update_problem_with_http_info(body, domain, problem, **kwargs)  # noqa: E501
            return data

    def v1_update_problem_with_http_info(self, body, domain, problem, **kwargs):  # noqa: E501
        """Update Problem  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_update_problem_with_http_info(body, domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemEdit body: (required)
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
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
                    " to method v1_update_problem" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_update_problem`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_update_problem`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_update_problem`")  # noqa: E501

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
            '/domains/{domain}/problems/{problem}', 'PATCH',
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
