# coding: utf-8

"""
    JOJ Horse

    Git version: 335bcde@2021-07-15 17:24:35  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse.client.api_client import ApiClient


class AdminApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_judger_api_v1_admin_judgers_post(self, uname, mail, **kwargs):  # noqa: E501
        """Create Judger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_judger_api_v1_admin_judgers_post(uname, mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uname: (required)
        :param str mail: (required)
        :return: UserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_judger_api_v1_admin_judgers_post_with_http_info(uname, mail, **kwargs)  # noqa: E501
        else:
            (data) = self.create_judger_api_v1_admin_judgers_post_with_http_info(uname, mail, **kwargs)  # noqa: E501
            return data

    def create_judger_api_v1_admin_judgers_post_with_http_info(self, uname, mail, **kwargs):  # noqa: E501
        """Create Judger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_judger_api_v1_admin_judgers_post_with_http_info(uname, mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uname: (required)
        :param str mail: (required)
        :return: UserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uname', 'mail']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_judger_api_v1_admin_judgers_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uname' is set
        if ('uname' not in params or
                params['uname'] is None):
            raise ValueError("Missing the required parameter `uname` when calling `create_judger_api_v1_admin_judgers_post`")  # noqa: E501
        # verify the required parameter 'mail' is set
        if ('mail' not in params or
                params['mail'] is None):
            raise ValueError("Missing the required parameter `mail` when calling `create_judger_api_v1_admin_judgers_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uname' in params:
            query_params.append(('uname', params['uname']))  # noqa: E501
        if 'mail' in params:
            query_params.append(('mail', params['mail']))  # noqa: E501

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
            '/api/v1/admin/judgers', 'POST',
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

    def create_user_api_v1_admin_users_post(self, student_id, jaccount_name, real_name, ip, **kwargs):  # noqa: E501
        """Create User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_api_v1_admin_users_post(student_id, jaccount_name, real_name, ip, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str student_id: (required)
        :param str jaccount_name: (required)
        :param str real_name: (required)
        :param str ip: (required)
        :return: UserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_api_v1_admin_users_post_with_http_info(student_id, jaccount_name, real_name, ip, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_api_v1_admin_users_post_with_http_info(student_id, jaccount_name, real_name, ip, **kwargs)  # noqa: E501
            return data

    def create_user_api_v1_admin_users_post_with_http_info(self, student_id, jaccount_name, real_name, ip, **kwargs):  # noqa: E501
        """Create User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_api_v1_admin_users_post_with_http_info(student_id, jaccount_name, real_name, ip, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str student_id: (required)
        :param str jaccount_name: (required)
        :param str real_name: (required)
        :param str ip: (required)
        :return: UserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['student_id', 'jaccount_name', 'real_name', 'ip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user_api_v1_admin_users_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'student_id' is set
        if ('student_id' not in params or
                params['student_id'] is None):
            raise ValueError("Missing the required parameter `student_id` when calling `create_user_api_v1_admin_users_post`")  # noqa: E501
        # verify the required parameter 'jaccount_name' is set
        if ('jaccount_name' not in params or
                params['jaccount_name'] is None):
            raise ValueError("Missing the required parameter `jaccount_name` when calling `create_user_api_v1_admin_users_post`")  # noqa: E501
        # verify the required parameter 'real_name' is set
        if ('real_name' not in params or
                params['real_name'] is None):
            raise ValueError("Missing the required parameter `real_name` when calling `create_user_api_v1_admin_users_post`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if ('ip' not in params or
                params['ip'] is None):
            raise ValueError("Missing the required parameter `ip` when calling `create_user_api_v1_admin_users_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'student_id' in params:
            query_params.append(('student_id', params['student_id']))  # noqa: E501
        if 'jaccount_name' in params:
            query_params.append(('jaccount_name', params['jaccount_name']))  # noqa: E501
        if 'real_name' in params:
            query_params.append(('real_name', params['real_name']))  # noqa: E501
        if 'ip' in params:
            query_params.append(('ip', params['ip']))  # noqa: E501

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
            '/api/v1/admin/users', 'POST',
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

    def delete_user_api_v1_admin_users_uid_delete(self, uid, **kwargs):  # noqa: E501
        """Delete User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_api_v1_admin_users_uid_delete(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_api_v1_admin_users_uid_delete_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_api_v1_admin_users_uid_delete_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def delete_user_api_v1_admin_users_uid_delete_with_http_info(self, uid, **kwargs):  # noqa: E501
        """Delete User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_api_v1_admin_users_uid_delete_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :return: EmptyResp
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
                    " to method delete_user_api_v1_admin_users_uid_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `delete_user_api_v1_admin_users_uid_delete`")  # noqa: E501

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
            '/api/v1/admin/users/{uid}', 'DELETE',
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

    def get_judger_jwt_api_v1_admin_judgers_uid_jwt_get(self, uid, **kwargs):  # noqa: E501
        """Get Judger Jwt  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_judger_jwt_api_v1_admin_judgers_uid_jwt_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :return: JWT
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_judger_jwt_api_v1_admin_judgers_uid_jwt_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_judger_jwt_api_v1_admin_judgers_uid_jwt_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def get_judger_jwt_api_v1_admin_judgers_uid_jwt_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """Get Judger Jwt  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_judger_jwt_api_v1_admin_judgers_uid_jwt_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: (required)
        :return: JWT
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
                    " to method get_judger_jwt_api_v1_admin_judgers_uid_jwt_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_judger_jwt_api_v1_admin_judgers_uid_jwt_get`")  # noqa: E501

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
            '/api/v1/admin/judgers/{uid}/jwt', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JWT',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_domain_roles_api_v1_admin_domain_roles_get(self, **kwargs):  # noqa: E501
        """List Domain Roles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_domain_roles_api_v1_admin_domain_roles_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListDomainRolesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_domain_roles_api_v1_admin_domain_roles_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_domain_roles_api_v1_admin_domain_roles_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_domain_roles_api_v1_admin_domain_roles_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Domain Roles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_domain_roles_api_v1_admin_domain_roles_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListDomainRolesResp
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
                    " to method list_domain_roles_api_v1_admin_domain_roles_get" % key
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
            '/api/v1/admin/domain_roles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListDomainRolesResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_domain_users_api_v1_admin_domain_users_get(self, **kwargs):  # noqa: E501
        """List Domain Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_domain_users_api_v1_admin_domain_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListDomainUsersResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_domain_users_api_v1_admin_domain_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_domain_users_api_v1_admin_domain_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_domain_users_api_v1_admin_domain_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Domain Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_domain_users_api_v1_admin_domain_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListDomainUsersResp
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
                    " to method list_domain_users_api_v1_admin_domain_users_get" % key
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
            '/api/v1/admin/domain_users', 'GET',
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

    def list_judgers_api_v1_admin_judgers_get(self, **kwargs):  # noqa: E501
        """List Judgers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_judgers_api_v1_admin_judgers_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListUsersResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_judgers_api_v1_admin_judgers_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_judgers_api_v1_admin_judgers_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_judgers_api_v1_admin_judgers_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Judgers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_judgers_api_v1_admin_judgers_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListUsersResp
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
                    " to method list_judgers_api_v1_admin_judgers_get" % key
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
            '/api/v1/admin/judgers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListUsersResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_users_api_v1_admin_users_get(self, **kwargs):  # noqa: E501
        """List Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_users_api_v1_admin_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListUsersResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_users_api_v1_admin_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_users_api_v1_admin_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_users_api_v1_admin_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_users_api_v1_admin_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortEnum sort:
        :param int skip:
        :param int limit:
        :return: ListUsersResp
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
                    " to method list_users_api_v1_admin_users_get" % key
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
            '/api/v1/admin/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListUsersResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
