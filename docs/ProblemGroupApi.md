# joj.horse_client.ProblemGroupApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_problem_groups_api_v1_problem_groups_get**](ProblemGroupApi.md#list_problem_groups_api_v1_problem_groups_get) | **GET** /api/v1/problem_groups | List Problem Groups

# **list_problem_groups_api_v1_problem_groups_get**
> ProblemGroupListResp list_problem_groups_api_v1_problem_groups_get(ordering=ordering, offset=offset, limit=limit)

List Problem Groups

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemGroupApi(joj.horse_client.ApiClient(configuration))
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Problem Groups
    api_response = api_instance.list_problem_groups_api_v1_problem_groups_get(ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemGroupApi->list_problem_groups_api_v1_problem_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ProblemGroupListResp**](ProblemGroupListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

