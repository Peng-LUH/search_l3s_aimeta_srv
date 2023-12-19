# coding: utf-8

"""
    L3S Gateway for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from search_l3s_aimeta.swagger_client.l3s_gateway_client.api_client import ApiClient


class SearchServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_search_service(self, user_id, query, **kwargs):  # noqa: E501
        """get_search_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_service(user_id, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str query: (required)
        :param list[str] owner:
        :param bool use_skill_profile:
        :param bool use_learning_profile:
        :param str entity_type:
        :param int num_results:
        :return: DtoSearchResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_search_service_with_http_info(user_id, query, **kwargs)  # noqa: E501
        else:
            (data) = self.get_search_service_with_http_info(user_id, query, **kwargs)  # noqa: E501
            return data

    def get_search_service_with_http_info(self, user_id, query, **kwargs):  # noqa: E501
        """get_search_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_service_with_http_info(user_id, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str query: (required)
        :param list[str] owner:
        :param bool use_skill_profile:
        :param bool use_learning_profile:
        :param str entity_type:
        :param int num_results:
        :return: DtoSearchResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'query', 'owner', 'use_skill_profile', 'use_learning_profile', 'entity_type', 'num_results']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_search_service`")  # noqa: E501
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `get_search_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501
            collection_formats['owner'] = 'multi'  # noqa: E501
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'use_skill_profile' in params:
            query_params.append(('use_skill_profile', params['use_skill_profile']))  # noqa: E501
        if 'use_learning_profile' in params:
            query_params.append(('use_learning_profile', params['use_learning_profile']))  # noqa: E501
        if 'entity_type' in params:
            query_params.append(('entity_type', params['entity_type']))  # noqa: E501
        if 'num_results' in params:
            query_params.append(('num_results', params['num_results']))  # noqa: E501

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
            '/l3s-search/search/{user_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoSearchResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_service_datasets(self, **kwargs):  # noqa: E501
        """get the name of datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_service_datasets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DtoGetDatasetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_search_service_datasets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_search_service_datasets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_search_service_datasets_with_http_info(self, **kwargs):  # noqa: E501
        """get the name of datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_service_datasets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DtoGetDatasetResponse
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
                    " to method get_search_service_datasets" % key
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
            '/l3s-search/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoGetDatasetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_service_encode_types(self, **kwargs):  # noqa: E501
        """get the name of encoding types as list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_service_encode_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_search_service_encode_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_search_service_encode_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_search_service_encode_types_with_http_info(self, **kwargs):  # noqa: E501
        """get the name of encoding types as list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_service_encode_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method get_search_service_encode_types" % key
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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-search/encode-type', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_service_ok(self, **kwargs):  # noqa: E501
        """get_search_service_ok  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_service_ok(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DtoSearchSrvConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_search_service_ok_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_search_service_ok_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_search_service_ok_with_http_info(self, **kwargs):  # noqa: E501
        """get_search_service_ok  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_service_ok_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DtoSearchSrvConnectionResponse
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
                    " to method get_search_service_ok" % key
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
            '/l3s-search/connection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoSearchSrvConnectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_unit_search(self, **kwargs):  # noqa: E501
        """get_unit_search  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unit_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] requirements:
        :param list[str] target:
        :return: DtoUnitSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_unit_search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_unit_search_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_unit_search_with_http_info(self, **kwargs):  # noqa: E501
        """get_unit_search  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unit_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] requirements:
        :param list[str] target:
        :return: DtoUnitSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['requirements', 'target']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_unit_search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'requirements' in params:
            query_params.append(('requirements', params['requirements']))  # noqa: E501
            collection_formats['requirements'] = 'csv'  # noqa: E501
        if 'target' in params:
            query_params.append(('target', params['target']))  # noqa: E501
            collection_formats['target'] = 'csv'  # noqa: E501

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
            '/l3s-search/unit-search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoUnitSearchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
