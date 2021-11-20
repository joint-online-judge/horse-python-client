# joj.horse.client.ProblemSetApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_post**](ProblemSetApi.md#add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_post) | **POST** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem | Add Problem In Problem Set
[**create_problem_set_api_v1_domains_domain_problem_sets_post**](ProblemSetApi.md#create_problem_set_api_v1_domains_domain_problem_sets_post) | **POST** /api/v1/domains/{domain}/problem_sets | Create Problem Set
[**delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_delete**](ProblemSetApi.md#delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_delete) | **DELETE** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem/{problem} | Delete Problem In Problem Set
[**delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete**](ProblemSetApi.md#delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete) | **DELETE** /api/v1/domains/{domain}/problem_sets/{problemSet} | Delete Problem Set
[**get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_get**](ProblemSetApi.md#get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem/{problem} | Get Problem In Problem Set
[**get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get**](ProblemSetApi.md#get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problemSet} | Get Problem Set
[**get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get**](ProblemSetApi.md#get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problemSet}/scoreboard | Get Scoreboard
[**list_problem_sets_api_v1_domains_domain_problem_sets_get**](ProblemSetApi.md#list_problem_sets_api_v1_domains_domain_problem_sets_get) | **GET** /api/v1/domains/{domain}/problem_sets | List Problem Sets
[**submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_submit_post**](ProblemSetApi.md#submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_submit_post) | **POST** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem/{problem}/submit | Submit Solution To Problem Set
[**update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_patch**](ProblemSetApi.md#update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_patch) | **PATCH** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem/{problem} | Update Problem In Problem Set
[**update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch**](ProblemSetApi.md#update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch) | **PATCH** /api/v1/domains/{domain}/problem_sets/{problemSet} | Update Problem Set

# **add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_post**
> ProblemSetResp add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_post(body, domain, problem_set)

Add Problem In Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.ProblemSetAddProblem() # ProblemSetAddProblem | 
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set

try:
    # Add Problem In Problem Set
    api_response = api_instance.add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_post(body, domain, problem_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_post: %s\n" % e)
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

# **create_problem_set_api_v1_domains_domain_problem_sets_post**
> ProblemSetResp create_problem_set_api_v1_domains_domain_problem_sets_post(body, domain)

Create Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.ProblemSetCreate() # ProblemSetCreate | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Create Problem Set
    api_response = api_instance.create_problem_set_api_v1_domains_domain_problem_sets_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->create_problem_set_api_v1_domains_domain_problem_sets_post: %s\n" % e)
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

# **delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_delete**
> ProblemSetResp delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_delete(domain, problem_set, problem)

Delete Problem In Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set
problem = 'problem_example' # str | url or id of the problem

try:
    # Delete Problem In Problem Set
    api_response = api_instance.delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_delete(domain, problem_set, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_delete: %s\n" % e)
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

# **delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete**
> EmptyResp delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete(domain, problem_set)

Delete Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set

try:
    # Delete Problem Set
    api_response = api_instance.delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete(domain, problem_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete: %s\n" % e)
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

# **get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_get**
> ProblemDetailResp get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_get(domain, problem_set, problem)

Get Problem In Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set
problem = 'problem_example' # str | url or id of the problem

try:
    # Get Problem In Problem Set
    api_response = api_instance.get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_get(domain, problem_set, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem_set** | **str**| url or id of the problem set | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**ProblemDetailResp**](ProblemDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get**
> ProblemSetDetailResp get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get(domain, problem_set)

Get Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set

try:
    # Get Problem Set
    api_response = api_instance.get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get(domain, problem_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get: %s\n" % e)
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

# **get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get**
> ScoreBoardResp get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get(problem_set, domain)

Get Scoreboard

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
problem_set = 'problem_set_example' # str | url or id of the problem set
domain = 'domain_example' # str | url or id of the domain

try:
    # Get Scoreboard
    api_response = api_instance.get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get(problem_set, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_set** | **str**| url or id of the problem set | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**ScoreBoardResp**](ScoreBoardResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_problem_sets_api_v1_domains_domain_problem_sets_get**
> ProblemSetListResp list_problem_sets_api_v1_domains_domain_problem_sets_get(domain, ordering=ordering, offset=offset, limit=limit)

List Problem Sets

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: name (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Problem Sets
    api_response = api_instance.list_problem_sets_api_v1_domains_domain_problem_sets_get(domain, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->list_problem_sets_api_v1_domains_domain_problem_sets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: name | [optional] 
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

# **submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_submit_post**
> RecordResp submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_submit_post(code_type, file, domain, problem_set, problem)

Submit Solution To Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
code_type = joj.horse.client.RecordCodeType() # RecordCodeType | 
file = 'file_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set
problem = 'problem_example' # str | url or id of the problem

try:
    # Submit Solution To Problem Set
    api_response = api_instance.submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_submit_post(code_type, file, domain, problem_set, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_submit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_type** | [**RecordCodeType**](.md)|  | 
 **file** | **str**|  | 
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

# **update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_patch**
> ProblemSetResp update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_patch(body, domain, problem_set, problem)

Update Problem In Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.ProblemSetUpdateProblem() # ProblemSetUpdateProblem | 
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set
problem = 'problem_example' # str | url or id of the problem

try:
    # Update Problem In Problem Set
    api_response = api_instance.update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_patch(body, domain, problem_set, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_patch: %s\n" % e)
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

# **update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch**
> ProblemSetResp update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch(body, domain, problem_set)

Update Problem Set

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemSetApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.ProblemSetEdit() # ProblemSetEdit | 
domain = 'domain_example' # str | url or id of the domain
problem_set = 'problem_set_example' # str | url or id of the problem set

try:
    # Update Problem Set
    api_response = api_instance.update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch(body, domain, problem_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch: %s\n" % e)
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

