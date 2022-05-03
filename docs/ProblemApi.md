# joj.horse_client.ProblemApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_clone_problem**](ProblemApi.md#v1_clone_problem) | **POST** /domains/{domain}/problems/clone | Clone Problem
[**v1_create_problem**](ProblemApi.md#v1_create_problem) | **POST** /domains/{domain}/problems | Create Problem
[**v1_delete_problem**](ProblemApi.md#v1_delete_problem) | **DELETE** /domains/{domain}/problems/{problem} | Delete Problem
[**v1_get_problem**](ProblemApi.md#v1_get_problem) | **GET** /domains/{domain}/problems/{problem} | Get Problem
[**v1_list_problems**](ProblemApi.md#v1_list_problems) | **GET** /domains/{domain}/problems | List Problems
[**v1_submit_solution_to_problem**](ProblemApi.md#v1_submit_solution_to_problem) | **POST** /domains/{domain}/problems/{problem} | Submit Solution To Problem
[**v1_update_problem**](ProblemApi.md#v1_update_problem) | **PATCH** /domains/{domain}/problems/{problem} | Update Problem

# **v1_clone_problem**
> ProblemListResp v1_clone_problem(body, domain)

Clone Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.ProblemClone() # ProblemClone | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Clone Problem
    api_response = api_instance.v1_clone_problem(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->v1_clone_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemClone**](ProblemClone.md)|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**ProblemListResp**](ProblemListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_problem**
> ProblemDetailResp v1_create_problem(body, domain)

Create Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.ProblemCreate() # ProblemCreate | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Create Problem
    api_response = api_instance.v1_create_problem(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->v1_create_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemCreate**](ProblemCreate.md)|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**ProblemDetailResp**](ProblemDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_problem**
> EmptyResp v1_delete_problem(domain, problem)

Delete Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Delete Problem
    api_response = api_instance.v1_delete_problem(domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->v1_delete_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_problem**
> ProblemDetailWithLatestRecordResp v1_get_problem(domain, problem)

Get Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Get Problem
    api_response = api_instance.v1_get_problem(domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->v1_get_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**ProblemDetailWithLatestRecordResp**](ProblemDetailWithLatestRecordResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_problems**
> ProblemWithLatestRecordListResp v1_list_problems(domain, ordering=ordering, offset=offset, limit=limit)

List Problems

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Problems
    api_response = api_instance.v1_list_problems(domain, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->v1_list_problems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ProblemWithLatestRecordListResp**](ProblemWithLatestRecordListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_submit_solution_to_problem**
> RecordResp v1_submit_solution_to_problem(language, files, domain, problem)

Submit Solution To Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemApi(joj.horse_client.ApiClient(configuration))
language = 'language_example' # str | 
files = ['files_example'] # list[str] | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Submit Solution To Problem
    api_response = api_instance.v1_submit_solution_to_problem(language, files, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->v1_submit_solution_to_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | 
 **files** | [**list[str]**](str.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**RecordResp**](RecordResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_problem**
> ProblemResp v1_update_problem(body, domain, problem)

Update Problem

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.ProblemEdit() # ProblemEdit | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Update Problem
    api_response = api_instance.v1_update_problem(body, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->v1_update_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemEdit**](ProblemEdit.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**ProblemResp**](ProblemResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

