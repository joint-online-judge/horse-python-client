# coding: utf-8

"""
    JOJ Horse

    Git version: 36ea0f6@2021-11-15T03:52:57Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse.client.api_client import ApiClient


class AuthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_token_api_v1_auth_token_get(self, response_type, **kwargs):  # noqa: E501
        """Get Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_api_v1_auth_token_get(response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: AuthTokensResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_token_api_v1_auth_token_get_with_http_info(response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_token_api_v1_auth_token_get_with_http_info(response_type, **kwargs)  # noqa: E501
            return data

    def get_token_api_v1_auth_token_get_with_http_info(self, response_type, **kwargs):  # noqa: E501
        """Get Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_api_v1_auth_token_get_with_http_info(response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: AuthTokensResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['response_type', 'cookie', 'redirect_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_api_v1_auth_token_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `get_token_api_v1_auth_token_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501
        if 'response_type' in params:
            query_params.append(('responseType', params['response_type']))  # noqa: E501
        if 'redirect_url' in params:
            query_params.append(('redirectUrl', params['redirect_url']))  # noqa: E501

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
            '/api/v1/auth/token', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthTokensResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def login_api_v1_auth_login_post(self, grant_type, username, password, scope, client_id, client_secret, response_type, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_api_v1_auth_login_post(grant_type, username, password, scope, client_id, client_secret, response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grant_type: (required)
        :param str username: (required)
        :param str password: (required)
        :param str scope: (required)
        :param str client_id: (required)
        :param str client_secret: (required)
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: AuthTokensResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.login_api_v1_auth_login_post_with_http_info(grant_type, username, password, scope, client_id, client_secret, response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.login_api_v1_auth_login_post_with_http_info(grant_type, username, password, scope, client_id, client_secret, response_type, **kwargs)  # noqa: E501
            return data

    def login_api_v1_auth_login_post_with_http_info(self, grant_type, username, password, scope, client_id, client_secret, response_type, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_api_v1_auth_login_post_with_http_info(grant_type, username, password, scope, client_id, client_secret, response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grant_type: (required)
        :param str username: (required)
        :param str password: (required)
        :param str scope: (required)
        :param str client_id: (required)
        :param str client_secret: (required)
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: AuthTokensResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['grant_type', 'username', 'password', 'scope', 'client_id', 'client_secret', 'response_type', 'cookie', 'redirect_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login_api_v1_auth_login_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grant_type' is set
        if ('grant_type' not in params or
                params['grant_type'] is None):
            raise ValueError("Missing the required parameter `grant_type` when calling `login_api_v1_auth_login_post`")  # noqa: E501
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `login_api_v1_auth_login_post`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in params or
                params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `login_api_v1_auth_login_post`")  # noqa: E501
        # verify the required parameter 'scope' is set
        if ('scope' not in params or
                params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `login_api_v1_auth_login_post`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `login_api_v1_auth_login_post`")  # noqa: E501
        # verify the required parameter 'client_secret' is set
        if ('client_secret' not in params or
                params['client_secret'] is None):
            raise ValueError("Missing the required parameter `client_secret` when calling `login_api_v1_auth_login_post`")  # noqa: E501
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `login_api_v1_auth_login_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501
        if 'response_type' in params:
            query_params.append(('responseType', params['response_type']))  # noqa: E501
        if 'redirect_url' in params:
            query_params.append(('redirectUrl', params['redirect_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'grant_type' in params:
            form_params.append(('grantType', params['grant_type']))  # noqa: E501
        if 'username' in params:
            form_params.append(('username', params['username']))  # noqa: E501
        if 'password' in params:
            form_params.append(('password', params['password']))  # noqa: E501
        if 'scope' in params:
            form_params.append(('scope', params['scope']))  # noqa: E501
        if 'client_id' in params:
            form_params.append(('clientId', params['client_id']))  # noqa: E501
        if 'client_secret' in params:
            form_params.append(('clientSecret', params['client_secret']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/auth/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthTokensResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def logout_api_v1_auth_logout_post(self, response_type, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_api_v1_auth_logout_post(response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logout_api_v1_auth_logout_post_with_http_info(response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.logout_api_v1_auth_logout_post_with_http_info(response_type, **kwargs)  # noqa: E501
            return data

    def logout_api_v1_auth_logout_post_with_http_info(self, response_type, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_api_v1_auth_logout_post_with_http_info(response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['response_type', 'cookie', 'redirect_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout_api_v1_auth_logout_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `logout_api_v1_auth_logout_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501
        if 'response_type' in params:
            query_params.append(('responseType', params['response_type']))  # noqa: E501
        if 'redirect_url' in params:
            query_params.append(('redirectUrl', params['redirect_url']))  # noqa: E501

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
            '/api/v1/auth/logout', 'POST',
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

    def refresh_api_v1_auth_refresh_post(self, response_type, **kwargs):  # noqa: E501
        """Refresh  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_api_v1_auth_refresh_post(response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: AuthTokensResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refresh_api_v1_auth_refresh_post_with_http_info(response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.refresh_api_v1_auth_refresh_post_with_http_info(response_type, **kwargs)  # noqa: E501
            return data

    def refresh_api_v1_auth_refresh_post_with_http_info(self, response_type, **kwargs):  # noqa: E501
        """Refresh  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_api_v1_auth_refresh_post_with_http_info(response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: AuthTokensResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['response_type', 'cookie', 'redirect_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refresh_api_v1_auth_refresh_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `refresh_api_v1_auth_refresh_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501
        if 'response_type' in params:
            query_params.append(('responseType', params['response_type']))  # noqa: E501
        if 'redirect_url' in params:
            query_params.append(('redirectUrl', params['redirect_url']))  # noqa: E501

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
            '/api/v1/auth/refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthTokensResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_api_v1_auth_register_post(self, body, response_type, **kwargs):  # noqa: E501
        """Register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_api_v1_auth_register_post(body, response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCreate body: (required)
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: AuthTokensResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.register_api_v1_auth_register_post_with_http_info(body, response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.register_api_v1_auth_register_post_with_http_info(body, response_type, **kwargs)  # noqa: E501
            return data

    def register_api_v1_auth_register_post_with_http_info(self, body, response_type, **kwargs):  # noqa: E501
        """Register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_api_v1_auth_register_post_with_http_info(body, response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCreate body: (required)
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: AuthTokensResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'response_type', 'cookie', 'redirect_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_api_v1_auth_register_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `register_api_v1_auth_register_post`")  # noqa: E501
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `register_api_v1_auth_register_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501
        if 'response_type' in params:
            query_params.append(('responseType', params['response_type']))  # noqa: E501
        if 'redirect_url' in params:
            query_params.append(('redirectUrl', params['redirect_url']))  # noqa: E501

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
            '/api/v1/auth/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthTokensResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
