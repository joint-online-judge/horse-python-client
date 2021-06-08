# joj.horse.client.ProblemApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_problem_api_v1_problems_clone_post**](ProblemApi.md#clone_problem_api_v1_problems_clone_post) | **POST** /api/v1/problems/clone | Clone Problem
[**create_problem_api_v1_problems_post**](ProblemApi.md#create_problem_api_v1_problems_post) | **POST** /api/v1/problems | Create Problem
[**delete_problem_api_v1_problems_problem_delete**](ProblemApi.md#delete_problem_api_v1_problems_problem_delete) | **DELETE** /api/v1/problems/{problem} | Delete Problem
[**get_problem_api_v1_problems_problem_get**](ProblemApi.md#get_problem_api_v1_problems_problem_get) | **GET** /api/v1/problems/{problem} | Get Problem
[**list_problems_api_v1_problems_get**](ProblemApi.md#list_problems_api_v1_problems_get) | **GET** /api/v1/problems | List Problems
[**submit_solution_to_problem_api_v1_problems_problem_post**](ProblemApi.md#submit_solution_to_problem_api_v1_problems_problem_post) | **POST** /api/v1/problems/{problem} | Submit Solution To Problem
[**update_problem_api_v1_problems_problem_patch**](ProblemApi.md#update_problem_api_v1_problems_problem_patch) | **PATCH** /api/v1/problems/{problem} | Update Problem

# **clone_problem_api_v1_problems_clone_post**
> ListProblemsResp clone_problem_api_v1_problems_clone_post(body)

Clone Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.CloneProblem() # CloneProblem | 

try:
    # Clone Problem
    api_response = api_instance.clone_problem_api_v1_problems_clone_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->clone_problem_api_v1_problems_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloneProblem**](CloneProblem.md)|  | 

### Return type

[**ListProblemsResp**](ListProblemsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_problem_api_v1_problems_post**
> ProblemResp create_problem_api_v1_problems_post(body)

Create Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.ProblemCreate() # ProblemCreate | 

try:
    # Create Problem
    api_response = api_instance.create_problem_api_v1_problems_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->create_problem_api_v1_problems_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemCreate**](ProblemCreate.md)|  | 

### Return type

[**ProblemResp**](ProblemResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_problem_api_v1_problems_problem_delete**
> EmptyResp delete_problem_api_v1_problems_problem_delete(problem)

Delete Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemApi(joj.horse.client.ApiClient(configuration))
problem = 'problem_example' # str | 

try:
    # Delete Problem
    api_response = api_instance.delete_problem_api_v1_problems_problem_delete(problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->delete_problem_api_v1_problems_problem_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem** | **str**|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_problem_api_v1_problems_problem_get**
> ProblemResp get_problem_api_v1_problems_problem_get(problem)

Get Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemApi(joj.horse.client.ApiClient(configuration))
problem = 'problem_example' # str | 

try:
    # Get Problem
    api_response = api_instance.get_problem_api_v1_problems_problem_get(problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->get_problem_api_v1_problems_problem_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem** | **str**|  | 

### Return type

[**ProblemResp**](ProblemResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_problems_api_v1_problems_get**
> ListProblemsResp list_problems_api_v1_problems_get(domain=domain, problem_set=problem_set, problem_group=problem_group, sort=sort, skip=skip, limit=limit)

List Problems

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str |  (optional)
problem_set = 'problem_set_example' # str |  (optional)
problem_group = 'problem_group_example' # str |  (optional)
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # List Problems
    api_response = api_instance.list_problems_api_v1_problems_get(domain=domain, problem_set=problem_set, problem_group=problem_group, sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->list_problems_api_v1_problems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | [optional] 
 **problem_set** | **str**|  | [optional] 
 **problem_group** | **str**|  | [optional] 
 **sort** | [**SortEnum**](.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ListProblemsResp**](ListProblemsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_solution_to_problem_api_v1_problems_problem_post**
> RecordResp submit_solution_to_problem_api_v1_problems_problem_post(code_type, file, problem)

Submit Solution To Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemApi(joj.horse.client.ApiClient(configuration))
code_type = joj.horse.client.RecordCodeType() # RecordCodeType | 
file = 'file_example' # str | 
problem = 'problem_example' # str | 

try:
    # Submit Solution To Problem
    api_response = api_instance.submit_solution_to_problem_api_v1_problems_problem_post(code_type, file, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->submit_solution_to_problem_api_v1_problems_problem_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_type** | [**RecordCodeType**](.md)|  | 
 **file** | **str**|  | 
 **problem** | **str**|  | 

### Return type

[**RecordResp**](RecordResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_problem_api_v1_problems_problem_patch**
> ProblemResp update_problem_api_v1_problems_problem_patch(body, problem)

Update Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.ProblemEdit() # ProblemEdit | 
problem = 'problem_example' # str | 

try:
    # Update Problem
    api_response = api_instance.update_problem_api_v1_problems_problem_patch(body, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->update_problem_api_v1_problems_problem_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemEdit**](ProblemEdit.md)|  | 
 **problem** | **str**|  | 

### Return type

[**ProblemResp**](ProblemResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

