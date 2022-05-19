# joj.horse_client.ProblemSetApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_add_problem_in_problem_set**](ProblemSetApi.md#v1_add_problem_in_problem_set) | **POST** /domains/{domain}/problem_sets/{problemSet}/problems | Add Problem In Problem Set
[**v1_create_problem_set**](ProblemSetApi.md#v1_create_problem_set) | **POST** /domains/{domain}/problem_sets | Create Problem Set
[**v1_delete_problem_in_problem_set**](ProblemSetApi.md#v1_delete_problem_in_problem_set) | **DELETE** /domains/{domain}/problem_sets/{problemSet}/problems/{problem} | Delete Problem In Problem Set
[**v1_delete_problem_set**](ProblemSetApi.md#v1_delete_problem_set) | **DELETE** /domains/{domain}/problem_sets/{problemSet} | Delete Problem Set
[**v1_get_problem_in_problem_set**](ProblemSetApi.md#v1_get_problem_in_problem_set) | **GET** /domains/{domain}/problem_sets/{problemSet}/problems/{problem} | Get Problem In Problem Set
[**v1_get_problem_set**](ProblemSetApi.md#v1_get_problem_set) | **GET** /domains/{domain}/problem_sets/{problemSet} | Get Problem Set
[**v1_list_problem_sets**](ProblemSetApi.md#v1_list_problem_sets) | **GET** /domains/{domain}/problem_sets | List Problem Sets
[**v1_list_problems_in_problem_set**](ProblemSetApi.md#v1_list_problems_in_problem_set) | **GET** /domains/{domain}/problem_sets/{problemSet}/problems | List Problems In Problem Set
[**v1_submit_solution_to_problem_set**](ProblemSetApi.md#v1_submit_solution_to_problem_set) | **POST** /domains/{domain}/problem_sets/{problemSet}/problems/{problem}/submit | Submit Solution To Problem Set
[**v1_update_problem_in_problem_set**](ProblemSetApi.md#v1_update_problem_in_problem_set) | **PATCH** /domains/{domain}/problem_sets/{problemSet}/problems/{problem} | Update Problem In Problem Set
[**v1_update_problem_set**](ProblemSetApi.md#v1_update_problem_set) | **PATCH** /domains/{domain}/problem_sets/{problemSet} | Update Problem Set

# **v1_add_problem_in_problem_set**
> ProblemSetResp v1_add_problem_in_problem_set(body, domain, problem_set)

Add Problem In Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.ProblemSetAddProblem() # ProblemSetAddProblem | 
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set

try:
    # Add Problem In Problem Set
    api_response = api_instance.v1_add_problem_in_problem_set(body, domain, problem_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_add_problem_in_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemSetAddProblem**](ProblemSetAddProblem.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 

### Return type

[**ProblemSetResp**](ProblemSetResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_problem_set**
> ProblemSetResp v1_create_problem_set(body, domain)

Create Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.ProblemSetCreate() # ProblemSetCreate | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Create Problem Set
    api_response = api_instance.v1_create_problem_set(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_create_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemSetCreate**](ProblemSetCreate.md)|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**ProblemSetResp**](ProblemSetResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_problem_in_problem_set**
> ProblemSetResp v1_delete_problem_in_problem_set(domain, problem_set, problem)

Delete Problem In Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set
problem = 'problem_example' # str | url or id of the problem

try:
    # Delete Problem In Problem Set
    api_response = api_instance.v1_delete_problem_in_problem_set(domain, problem_set, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_delete_problem_in_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**ProblemSetResp**](ProblemSetResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_problem_set**
> EmptyResp v1_delete_problem_set(domain, problem_set)

Delete Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set

try:
    # Delete Problem Set
    api_response = api_instance.v1_delete_problem_set(domain, problem_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_delete_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_problem_in_problem_set**
> ProblemDetailWithLatestRecordResp v1_get_problem_in_problem_set(domain, problem_set, problem)

Get Problem In Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set
problem = 'problem_example' # str | url or id of the problem

try:
    # Get Problem In Problem Set
    api_response = api_instance.v1_get_problem_in_problem_set(domain, problem_set, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_get_problem_in_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**ProblemDetailWithLatestRecordResp**](ProblemDetailWithLatestRecordResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_problem_set**
> ProblemSetDetailResp v1_get_problem_set(domain, problem_set)

Get Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set

try:
    # Get Problem Set
    api_response = api_instance.v1_get_problem_set(domain, problem_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_get_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 

### Return type

[**ProblemSetDetailResp**](ProblemSetDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_problem_sets**
> ProblemSetListResp v1_list_problem_sets(domain, ordering=ordering, offset=offset, limit=limit)

List Problem Sets

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
ordering = '' # str | Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Problem Sets
    api_response = api_instance.v1_list_problem_sets(domain, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_list_problem_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **ordering** | **str**| Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ProblemSetListResp**](ProblemSetListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_problems_in_problem_set**
> ProblemWithLatestRecordListResp v1_list_problems_in_problem_set(domain, problem_set)

List Problems In Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set

try:
    # List Problems In Problem Set
    api_response = api_instance.v1_list_problems_in_problem_set(domain, problem_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_list_problems_in_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 

### Return type

[**ProblemWithLatestRecordListResp**](ProblemWithLatestRecordListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_submit_solution_to_problem_set**
> RecordResp v1_submit_solution_to_problem_set(language, files, domain, problem_set, problem)

Submit Solution To Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
language = 'language_example' # str | 
files = ['files_example'] # list[str] | 
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set
problem = 'problem_example' # str | url or id of the problem

try:
    # Submit Solution To Problem Set
    api_response = api_instance.v1_submit_solution_to_problem_set(language, files, domain, problem_set, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_submit_solution_to_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | 
 **files** | [**list[str]**](str.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**RecordResp**](RecordResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_problem_in_problem_set**
> ProblemSetResp v1_update_problem_in_problem_set(body, domain, problem_set, problem)

Update Problem In Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.ProblemSetUpdateProblem() # ProblemSetUpdateProblem | 
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set
problem = 'problem_example' # str | url or id of the problem

try:
    # Update Problem In Problem Set
    api_response = api_instance.v1_update_problem_in_problem_set(body, domain, problem_set, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_update_problem_in_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemSetUpdateProblem**](ProblemSetUpdateProblem.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**ProblemSetResp**](ProblemSetResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_problem_set**
> ProblemSetResp v1_update_problem_set(body, domain, problem_set)

Update Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemSetApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.ProblemSetEdit() # ProblemSetEdit | 
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set

try:
    # Update Problem Set
    api_response = api_instance.v1_update_problem_set(body, domain, problem_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->v1_update_problem_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemSetEdit**](ProblemSetEdit.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 

### Return type

[**ProblemSetResp**](ProblemSetResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

