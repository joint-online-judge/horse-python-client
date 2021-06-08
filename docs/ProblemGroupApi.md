# joj.horse.client.ProblemGroupApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_problem_groups_api_v1_problem_groups_get**](ProblemGroupApi.md#list_problem_groups_api_v1_problem_groups_get) | **GET** /api/v1/problem_groups | List Problem Groups

# **list_problem_groups_api_v1_problem_groups_get**
> ListProblemGroupsResp list_problem_groups_api_v1_problem_groups_get(sort=sort, skip=skip, limit=limit)

List Problem Groups

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemGroupApi(joj.horse.client.ApiClient(configuration))
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # List Problem Groups
    api_response = api_instance.list_problem_groups_api_v1_problem_groups_get(sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemGroupApi->list_problem_groups_api_v1_problem_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**SortEnum**](.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ListProblemGroupsResp**](ListProblemGroupsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

