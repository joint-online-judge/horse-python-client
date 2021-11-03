# joj.horse.client.ProblemSetApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_problem_set_api_v1_domains_domain_problem_sets_post**](ProblemSetApi.md#create_problem_set_api_v1_domains_domain_problem_sets_post) | **POST** /api/v1/domains/{domain}/problem_sets | Create Problem Set
[**delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete**](ProblemSetApi.md#delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete) | **DELETE** /api/v1/domains/{domain}/problem_sets/{problem_set} | Delete Problem Set
[**get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get**](ProblemSetApi.md#get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problem_set} | Get Problem Set
[**get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get**](ProblemSetApi.md#get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problem_set}/scoreboard | Get Scoreboard
[**list_problem_sets_api_v1_domains_domain_problem_sets_get**](ProblemSetApi.md#list_problem_sets_api_v1_domains_domain_problem_sets_get) | **GET** /api/v1/domains/{domain}/problem_sets | List Problem Sets
[**update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch**](ProblemSetApi.md#update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch) | **PATCH** /api/v1/domains/{domain}/problem_sets/{problem_set} | Update Problem Set

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

# **delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete**
> EmptyResp delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete(problem_set, domain)

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
problem_set = 'problem_set_example' # str | url or id of the problem set
domain = 'domain_example' # str | url or id of the domain

try:
    # Delete Problem Set
    api_response = api_instance.delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete(problem_set, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_set** | **str**| url or id of the problem set | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get**
> ProblemSetResp get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get(problem_set, domain)

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
problem_set = 'problem_set_example' # str | url or id of the problem set
domain = 'domain_example' # str | url or id of the domain

try:
    # Get Problem Set
    api_response = api_instance.get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get(problem_set, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_set** | **str**| url or id of the problem set | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**ProblemSetResp**](ProblemSetResp.md)

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
> ListProblemSetsResp list_problem_sets_api_v1_domains_domain_problem_sets_get(domain, offset=offset, limit=limit)

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
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Problem Sets
    api_response = api_instance.list_problem_sets_api_v1_domains_domain_problem_sets_get(domain, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->list_problem_sets_api_v1_domains_domain_problem_sets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ListProblemSetsResp**](ListProblemSetsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch**
> ProblemSetResp update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch(body, problem_set, domain)

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
problem_set = 'problem_set_example' # str | url or id of the problem set
domain = 'domain_example' # str | url or id of the domain

try:
    # Update Problem Set
    api_response = api_instance.update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch(body, problem_set, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemSetApi->update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemSetEdit**](ProblemSetEdit.md)|  | 
 **problem_set** | **str**| url or id of the problem set | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**ProblemSetResp**](ProblemSetResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

