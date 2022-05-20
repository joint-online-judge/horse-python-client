# coding: utf-8

"""
    JOJ Horse

    Git version: fc491db@2022-05-20T21:40:10Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse_client.api_client import ApiClient


class AuthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_get_token(self, response_type, **kwargs):  # noqa: E501
        """Get Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_token(response_type, async_req=True)
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
            return self.v1_get_token_with_http_info(response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_get_token_with_http_info(response_type, **kwargs)  # noqa: E501
            return data

    def v1_get_token_with_http_info(self, response_type, **kwargs):  # noqa: E501
        """Get Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_token_with_http_info(response_type, async_req=True)
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
                    " to method v1_get_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `v1_get_token`")  # noqa: E501

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
            '/auth/token', 'GET',
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

    def v1_list_oauth2(self, **kwargs):  # noqa: E501
        """List Oauth2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_oauth2(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: OAuth2ClientListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_list_oauth2_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_list_oauth2_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_list_oauth2_with_http_info(self, **kwargs):  # noqa: E501
        """List Oauth2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_oauth2_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: OAuth2ClientListResp
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
                    " to method v1_list_oauth2" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/oauth2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OAuth2ClientListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_login(self, grant_type, username, password, scope, client_id, client_secret, response_type, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_login(grant_type, username, password, scope, client_id, client_secret, response_type, async_req=True)
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
            return self.v1_login_with_http_info(grant_type, username, password, scope, client_id, client_secret, response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_login_with_http_info(grant_type, username, password, scope, client_id, client_secret, response_type, **kwargs)  # noqa: E501
            return data

    def v1_login_with_http_info(self, grant_type, username, password, scope, client_id, client_secret, response_type, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_login_with_http_info(grant_type, username, password, scope, client_id, client_secret, response_type, async_req=True)
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
                    " to method v1_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grant_type' is set
        if ('grant_type' not in params or
                params['grant_type'] is None):
            raise ValueError("Missing the required parameter `grant_type` when calling `v1_login`")  # noqa: E501
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `v1_login`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in params or
                params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `v1_login`")  # noqa: E501
        # verify the required parameter 'scope' is set
        if ('scope' not in params or
                params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `v1_login`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `v1_login`")  # noqa: E501
        # verify the required parameter 'client_secret' is set
        if ('client_secret' not in params or
                params['client_secret'] is None):
            raise ValueError("Missing the required parameter `client_secret` when calling `v1_login`")  # noqa: E501
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `v1_login`")  # noqa: E501

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
            '/auth/login', 'POST',
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

    def v1_logout(self, response_type, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_logout(response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_logout_with_http_info(response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_logout_with_http_info(response_type, **kwargs)  # noqa: E501
            return data

    def v1_logout_with_http_info(self, response_type, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_logout_with_http_info(response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_type: (required)
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: object
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
                    " to method v1_logout" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `v1_logout`")  # noqa: E501

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
            '/auth/logout', 'POST',
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

    def v1_oauth_authorize(self, oauth2, response_type, **kwargs):  # noqa: E501
        """Oauth Authorize  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_oauth_authorize(oauth2, response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str oauth2: OAuth client name (required)
        :param str response_type: (required)
        :param list[str] scopes:
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: RedirectResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_oauth_authorize_with_http_info(oauth2, response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_oauth_authorize_with_http_info(oauth2, response_type, **kwargs)  # noqa: E501
            return data

    def v1_oauth_authorize_with_http_info(self, oauth2, response_type, **kwargs):  # noqa: E501
        """Oauth Authorize  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_oauth_authorize_with_http_info(oauth2, response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str oauth2: OAuth client name (required)
        :param str response_type: (required)
        :param list[str] scopes:
        :param bool cookie: Add Set/Delete-Cookie on response header
        :param str redirect_url: The redirect url after the operation
        :return: RedirectResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['oauth2', 'response_type', 'scopes', 'cookie', 'redirect_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_oauth_authorize" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'oauth2' is set
        if ('oauth2' not in params or
                params['oauth2'] is None):
            raise ValueError("Missing the required parameter `oauth2` when calling `v1_oauth_authorize`")  # noqa: E501
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `v1_oauth_authorize`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'oauth2' in params:
            path_params['oauth2'] = params['oauth2']  # noqa: E501

        query_params = []
        if 'scopes' in params:
            query_params.append(('scopes', params['scopes']))  # noqa: E501
            collection_formats['scopes'] = 'multi'  # noqa: E501
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
            '/auth/oauth2/{oauth2}/authorize', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RedirectResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_refresh(self, response_type, **kwargs):  # noqa: E501
        """Refresh  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refresh(response_type, async_req=True)
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
            return self.v1_refresh_with_http_info(response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_refresh_with_http_info(response_type, **kwargs)  # noqa: E501
            return data

    def v1_refresh_with_http_info(self, response_type, **kwargs):  # noqa: E501
        """Refresh  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refresh_with_http_info(response_type, async_req=True)
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
                    " to method v1_refresh" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `v1_refresh`")  # noqa: E501

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
            '/auth/refresh', 'POST',
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

    def v1_register(self, body, response_type, **kwargs):  # noqa: E501
        """Register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_register(body, response_type, async_req=True)
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
            return self.v1_register_with_http_info(body, response_type, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_register_with_http_info(body, response_type, **kwargs)  # noqa: E501
            return data

    def v1_register_with_http_info(self, body, response_type, **kwargs):  # noqa: E501
        """Register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_register_with_http_info(body, response_type, async_req=True)
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
                    " to method v1_register" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_register`")  # noqa: E501
        # verify the required parameter 'response_type' is set
        if ('response_type' not in params or
                params['response_type'] is None):
            raise ValueError("Missing the required parameter `response_type` when calling `v1_register`")  # noqa: E501

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
            '/auth/register', 'POST',
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
