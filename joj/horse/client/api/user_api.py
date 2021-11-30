# coding: utf-8

"""
    JOJ Horse

    Git version: e54a297@2021-11-30T11:09:19Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse.client.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_user_api_v1_user_get(self, **kwargs):  # noqa: E501
        """Get User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_v1_user_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserDetailResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_api_v1_user_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_api_v1_user_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_api_v1_user_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_v1_user_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserDetailResp
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
                    " to method get_user_api_v1_user_get" % key
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
            '/api/v1/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserDetailResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_api_v1_users_uid_get(self, uid, **kwargs):  # noqa: E501
        """Get User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_v1_users_uid_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :return: UserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_api_v1_users_uid_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_api_v1_users_uid_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def get_user_api_v1_users_uid_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """Get User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_v1_users_uid_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :return: UserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_api_v1_users_uid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_user_api_v1_users_uid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

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
            '/api/v1/users/{uid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_problems_api_v1_user_problems_get(self, **kwargs):  # noqa: E501
        """Get User Problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_problems_api_v1_user_problems_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: ProblemListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_problems_api_v1_user_problems_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_problems_api_v1_user_problems_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_problems_api_v1_user_problems_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get User Problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_problems_api_v1_user_problems_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: ProblemListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_problems_api_v1_user_problems_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/user/problems', 'GET',
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

    def get_user_problems_api_v1_users_uid_problems_get(self, uid, **kwargs):  # noqa: E501
        """Get User Problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_problems_api_v1_users_uid_problems_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :param int offset:
        :param int limit:
        :return: ProblemListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_problems_api_v1_users_uid_problems_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_problems_api_v1_users_uid_problems_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def get_user_problems_api_v1_users_uid_problems_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """Get User Problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_problems_api_v1_users_uid_problems_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :param int offset:
        :param int limit:
        :return: ProblemListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_problems_api_v1_users_uid_problems_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_user_problems_api_v1_users_uid_problems_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

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
            '/api/v1/users/{uid}/problems', 'GET',
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

    def list_user_domains_api_v1_users_uid_domains_get(self, uid, **kwargs):  # noqa: E501
        """List User Domains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_domains_api_v1_users_uid_domains_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :param list[str] role:
        :param str ordering: Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: name
        :param int offset:
        :param int limit:
        :return: DomainListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_domains_api_v1_users_uid_domains_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_domains_api_v1_users_uid_domains_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def list_user_domains_api_v1_users_uid_domains_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """List User Domains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_domains_api_v1_users_uid_domains_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :param list[str] role:
        :param str ordering: Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: name
        :param int offset:
        :param int limit:
        :return: DomainListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'role', 'ordering', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_domains_api_v1_users_uid_domains_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_user_domains_api_v1_users_uid_domains_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

        query_params = []
        if 'role' in params:
            query_params.append(('role', params['role']))  # noqa: E501
            collection_formats['role'] = 'multi'  # noqa: E501
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
            '/api/v1/users/{uid}/domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_users_api_v1_users_get(self, **kwargs):  # noqa: E501
        """List Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_users_api_v1_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query:
        :param str ordering: Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: username
        :param int offset:
        :param int limit:
        :return: UserListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_users_api_v1_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_users_api_v1_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_users_api_v1_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_users_api_v1_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query:
        :param str ordering: Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: username
        :param int offset:
        :param int limit:
        :return: UserListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'ordering', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_users_api_v1_users_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
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
            '/api/v1/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
