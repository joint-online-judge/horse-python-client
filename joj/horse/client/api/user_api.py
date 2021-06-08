# coding: utf-8

"""
    JOJ Horse

    Git version: 3b2baac@2021-06-08 19:39:58  # noqa: E501

    OpenAPI spec version: 0.0.0
    
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
        :return: UserResp
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
        :return: UserResp
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
            response_type='UserResp',  # noqa: E501
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
        :return: UserBaseResp
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
        :return: UserBaseResp
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
            response_type='UserBaseResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_domains_api_v1_users_uid_domains_get(self, uid, **kwargs):  # noqa: E501
        """Get User Domains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_domains_api_v1_users_uid_domains_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :param list[str] role:
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListDomainUsersResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_domains_api_v1_users_uid_domains_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_domains_api_v1_users_uid_domains_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def get_user_domains_api_v1_users_uid_domains_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """Get User Domains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_domains_api_v1_users_uid_domains_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :param list[str] role:
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListDomainUsersResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'role', 'sort', 'skip', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_domains_api_v1_users_uid_domains_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_user_domains_api_v1_users_uid_domains_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

        query_params = []
        if 'role' in params:
            query_params.append(('role', params['role']))  # noqa: E501
            collection_formats['role'] = 'multi'  # noqa: E501
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
            '/api/v1/users/{uid}/domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListDomainUsersResp',  # noqa: E501
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
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListProblemsResp
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
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListProblemsResp
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
                    " to method get_user_problems_api_v1_user_problems_get" % key
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
            '/api/v1/user/problems', 'GET',
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

    def get_user_problems_api_v1_users_uid_problems_get(self, uid, **kwargs):  # noqa: E501
        """Get User Problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_problems_api_v1_users_uid_problems_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListProblemsResp
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
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListProblemsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'sort', 'skip', 'limit']  # noqa: E501
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
            '/api/v1/users/{uid}/problems', 'GET',
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

    def jaccount_auth_api_v1_user_jaccount_auth_get(self, state, code, **kwargs):  # noqa: E501
        """Jaccount Auth  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jaccount_auth_api_v1_user_jaccount_auth_get(state, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state: (required)
        :param str code: (required)
        :param str jaccount_state:
        :param str redirect_url:
        :return: RedirectModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.jaccount_auth_api_v1_user_jaccount_auth_get_with_http_info(state, code, **kwargs)  # noqa: E501
        else:
            (data) = self.jaccount_auth_api_v1_user_jaccount_auth_get_with_http_info(state, code, **kwargs)  # noqa: E501
            return data

    def jaccount_auth_api_v1_user_jaccount_auth_get_with_http_info(self, state, code, **kwargs):  # noqa: E501
        """Jaccount Auth  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jaccount_auth_api_v1_user_jaccount_auth_get_with_http_info(state, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state: (required)
        :param str code: (required)
        :param str jaccount_state:
        :param str redirect_url:
        :return: RedirectModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state', 'code', 'jaccount_state', 'redirect_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method jaccount_auth_api_v1_user_jaccount_auth_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'state' is set
        if ('state' not in params or
                params['state'] is None):
            raise ValueError("Missing the required parameter `state` when calling `jaccount_auth_api_v1_user_jaccount_auth_get`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `jaccount_auth_api_v1_user_jaccount_auth_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/user/jaccount/auth', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RedirectModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def jaccount_login_api_v1_user_jaccount_login_get(self, **kwargs):  # noqa: E501
        """Jaccount Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jaccount_login_api_v1_user_jaccount_login_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str redirect_url: Set the redirect url after the authorization.
        :param bool redirect: If true (html link mode), redirect to jaccount site; If false (ajax mode), return the redirect url to the jaccount site, you also need to set the cookies returned manually in ajax mode.
        :return: RedirectModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.jaccount_login_api_v1_user_jaccount_login_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.jaccount_login_api_v1_user_jaccount_login_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def jaccount_login_api_v1_user_jaccount_login_get_with_http_info(self, **kwargs):  # noqa: E501
        """Jaccount Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jaccount_login_api_v1_user_jaccount_login_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str redirect_url: Set the redirect url after the authorization.
        :param bool redirect: If true (html link mode), redirect to jaccount site; If false (ajax mode), return the redirect url to the jaccount site, you also need to set the cookies returned manually in ajax mode.
        :return: RedirectModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['redirect_url', 'redirect']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method jaccount_login_api_v1_user_jaccount_login_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'redirect_url' in params:
            query_params.append(('redirect_url', params['redirect_url']))  # noqa: E501
        if 'redirect' in params:
            query_params.append(('redirect', params['redirect']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/user/jaccount/login', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RedirectModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def logout_api_v1_user_logout_get(self, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_api_v1_user_logout_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str redirect_url: Set the redirect url after the logout.
        :param bool redirect: If true (html link mode), redirect to a url; If false (ajax mode), return the redirect url, you also need to unset all cookies manually in ajax mode.
        :return: RedirectModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logout_api_v1_user_logout_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.logout_api_v1_user_logout_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def logout_api_v1_user_logout_get_with_http_info(self, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_api_v1_user_logout_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str redirect_url: Set the redirect url after the logout.
        :param bool redirect: If true (html link mode), redirect to a url; If false (ajax mode), return the redirect url, you also need to unset all cookies manually in ajax mode.
        :return: RedirectModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['redirect_url', 'redirect']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout_api_v1_user_logout_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'redirect_url' in params:
            query_params.append(('redirect_url', params['redirect_url']))  # noqa: E501
        if 'redirect' in params:
            query_params.append(('redirect', params['redirect']))  # noqa: E501

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
            '/api/v1/user/logout', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RedirectModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
