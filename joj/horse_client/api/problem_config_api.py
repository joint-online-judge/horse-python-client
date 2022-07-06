# coding: utf-8

"""
    JOJ Horse

    Git version: f4a351d@2022-07-06T03:30:14Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from joj.horse_client.api_client import ApiClient


class ProblemConfigApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_diff_problem_config_default_branch(self, domain, problem, **kwargs):  # noqa: E501
        """Diff Problem Config Default Branch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_diff_problem_config_default_branch(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :param str after: return items after this value
        :param int amount: how many items to return
        :param str delimiter: delimiter used to group common prefixes by
        :param str prefix: return items prefixed with this value
        :return: DiffListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_diff_problem_config_default_branch_with_http_info(domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_diff_problem_config_default_branch_with_http_info(domain, problem, **kwargs)  # noqa: E501
            return data

    def v1_diff_problem_config_default_branch_with_http_info(self, domain, problem, **kwargs):  # noqa: E501
        """Diff Problem Config Default Branch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_diff_problem_config_default_branch_with_http_info(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :param str after: return items after this value
        :param int amount: how many items to return
        :param str delimiter: delimiter used to group common prefixes by
        :param str prefix: return items prefixed with this value
        :return: DiffListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'problem', 'after', 'amount', 'delimiter', 'prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_diff_problem_config_default_branch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_diff_problem_config_default_branch`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_diff_problem_config_default_branch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501

        query_params = []
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'delimiter' in params:
            query_params.append(('delimiter', params['delimiter']))  # noqa: E501
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501

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
            '/domains/{domain}/problems/{problem}/configs/latest/diff', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiffListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_download_problem_config_archive(self, domain, problem, config, **kwargs):  # noqa: E501
        """Download Problem Config Archive  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_download_problem_config_archive(domain, problem, config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :param str config: 'latest' or id of the config (required)
        :param ArchiveFormat archive_format:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_download_problem_config_archive_with_http_info(domain, problem, config, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_download_problem_config_archive_with_http_info(domain, problem, config, **kwargs)  # noqa: E501
            return data

    def v1_download_problem_config_archive_with_http_info(self, domain, problem, config, **kwargs):  # noqa: E501
        """Download Problem Config Archive  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_download_problem_config_archive_with_http_info(domain, problem, config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :param str config: 'latest' or id of the config (required)
        :param ArchiveFormat archive_format:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'problem', 'config', 'archive_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_download_problem_config_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_download_problem_config_archive`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_download_problem_config_archive`")  # noqa: E501
        # verify the required parameter 'config' is set
        if ('config' not in params or
                params['config'] is None):
            raise ValueError("Missing the required parameter `config` when calling `v1_download_problem_config_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501
        if 'config' in params:
            path_params['config'] = params['config']  # noqa: E501

        query_params = []
        if 'archive_format' in params:
            query_params.append(('archiveFormat', params['archive_format']))  # noqa: E501

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
            '/domains/{domain}/problems/{problem}/configs/{config}', 'GET',
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

    def v1_get_problem_config_json(self, domain, config, problem, **kwargs):  # noqa: E501
        """Get Problem Config Json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_problem_config_json(domain, config, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str config: 'latest' or id of the config (required)
        :param str problem: url or id of the problem (required)
        :return: ProblemConfigDataDetailResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_get_problem_config_json_with_http_info(domain, config, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_get_problem_config_json_with_http_info(domain, config, problem, **kwargs)  # noqa: E501
            return data

    def v1_get_problem_config_json_with_http_info(self, domain, config, problem, **kwargs):  # noqa: E501
        """Get Problem Config Json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_get_problem_config_json_with_http_info(domain, config, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str config: 'latest' or id of the config (required)
        :param str problem: url or id of the problem (required)
        :return: ProblemConfigDataDetailResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'config', 'problem']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_get_problem_config_json" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_get_problem_config_json`")  # noqa: E501
        # verify the required parameter 'config' is set
        if ('config' not in params or
                params['config'] is None):
            raise ValueError("Missing the required parameter `config` when calling `v1_get_problem_config_json`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_get_problem_config_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'config' in params:
            path_params['config'] = params['config']  # noqa: E501
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
            '/domains/{domain}/problems/{problem}/configs/{config}/json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemConfigDataDetailResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_list_latest_problem_config_objects_under_a_given_prefix(self, domain, problem, **kwargs):  # noqa: E501
        """List Latest Problem Config Objects Under A Given Prefix  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_latest_problem_config_objects_under_a_given_prefix(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :param str after: return items after this value
        :param int amount: how many items to return
        :param str delimiter: delimiter used to group common prefixes by
        :param str prefix: return items prefixed with this value
        :return: ObjectStatsListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_list_latest_problem_config_objects_under_a_given_prefix_with_http_info(domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_list_latest_problem_config_objects_under_a_given_prefix_with_http_info(domain, problem, **kwargs)  # noqa: E501
            return data

    def v1_list_latest_problem_config_objects_under_a_given_prefix_with_http_info(self, domain, problem, **kwargs):  # noqa: E501
        """List Latest Problem Config Objects Under A Given Prefix  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_latest_problem_config_objects_under_a_given_prefix_with_http_info(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :param str after: return items after this value
        :param int amount: how many items to return
        :param str delimiter: delimiter used to group common prefixes by
        :param str prefix: return items prefixed with this value
        :return: ObjectStatsListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'problem', 'after', 'amount', 'delimiter', 'prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_list_latest_problem_config_objects_under_a_given_prefix" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_list_latest_problem_config_objects_under_a_given_prefix`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_list_latest_problem_config_objects_under_a_given_prefix`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501

        query_params = []
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'delimiter' in params:
            query_params.append(('delimiter', params['delimiter']))  # noqa: E501
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501

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
            '/domains/{domain}/problems/{problem}/configs/latest/ls', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectStatsListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_list_problem_config_commits(self, domain, problem, **kwargs):  # noqa: E501
        """List Problem Config Commits  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_problem_config_commits(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :param str ordering: Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at
        :param int offset:
        :param int limit:
        :return: ProblemConfigDetailListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_list_problem_config_commits_with_http_info(domain, problem, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_list_problem_config_commits_with_http_info(domain, problem, **kwargs)  # noqa: E501
            return data

    def v1_list_problem_config_commits_with_http_info(self, domain, problem, **kwargs):  # noqa: E501
        """List Problem Config Commits  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_list_problem_config_commits_with_http_info(domain, problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: url or id of the domain (required)
        :param str problem: url or id of the problem (required)
        :param str ordering: Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at
        :param int offset:
        :param int limit:
        :return: ProblemConfigDetailListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'problem', 'ordering', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_list_problem_config_commits" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_list_problem_config_commits`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_list_problem_config_commits`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501

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
            '/domains/{domain}/problems/{problem}/configs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemConfigDetailListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_update_problem_config_by_archive(self, file, problem, domain, **kwargs):  # noqa: E501
        """Update Problem Config By Archive  # noqa: E501

        Completely replace the problem config with the archive. This will delete files not included in the archive.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_update_problem_config_by_archive(file, problem, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :param str problem: url or id of the problem (required)
        :param str domain: url or id of the domain (required)
        :param ConfigJsonOnMissing config_json_on_missing:
        :return: ProblemConfigDetailResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_update_problem_config_by_archive_with_http_info(file, problem, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_update_problem_config_by_archive_with_http_info(file, problem, domain, **kwargs)  # noqa: E501
            return data

    def v1_update_problem_config_by_archive_with_http_info(self, file, problem, domain, **kwargs):  # noqa: E501
        """Update Problem Config By Archive  # noqa: E501

        Completely replace the problem config with the archive. This will delete files not included in the archive.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_update_problem_config_by_archive_with_http_info(file, problem, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :param str problem: url or id of the problem (required)
        :param str domain: url or id of the domain (required)
        :param ConfigJsonOnMissing config_json_on_missing:
        :return: ProblemConfigDetailResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'problem', 'domain', 'config_json_on_missing']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_update_problem_config_by_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `v1_update_problem_config_by_archive`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_update_problem_config_by_archive`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_update_problem_config_by_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501

        query_params = []
        if 'config_json_on_missing' in params:
            query_params.append(('configJsonOnMissing', params['config_json_on_missing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
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
            '/domains/{domain}/problems/{problem}/configs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemConfigDetailResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_update_problem_config_json(self, body, problem, domain, **kwargs):  # noqa: E501
        """Update Problem Config Json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_update_problem_config_json(body, problem, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemConfigJson body: (required)
        :param str problem: url or id of the problem (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemConfigDetailResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_update_problem_config_json_with_http_info(body, problem, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_update_problem_config_json_with_http_info(body, problem, domain, **kwargs)  # noqa: E501
            return data

    def v1_update_problem_config_json_with_http_info(self, body, problem, domain, **kwargs):  # noqa: E501
        """Update Problem Config Json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_update_problem_config_json_with_http_info(body, problem, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProblemConfigJson body: (required)
        :param str problem: url or id of the problem (required)
        :param str domain: url or id of the domain (required)
        :return: ProblemConfigDetailResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'problem', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_update_problem_config_json" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_update_problem_config_json`")  # noqa: E501
        # verify the required parameter 'problem' is set
        if ('problem' not in params or
                params['problem'] is None):
            raise ValueError("Missing the required parameter `problem` when calling `v1_update_problem_config_json`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `v1_update_problem_config_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'problem' in params:
            path_params['problem'] = params['problem']  # noqa: E501
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
            '/domains/{domain}/problems/{problem}/configs/json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemConfigDetailResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
