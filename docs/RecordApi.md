# joj.horse.client.RecordApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_record_api_v1_domains_domain_records_record_get**](RecordApi.md#get_record_api_v1_domains_domain_records_record_get) | **GET** /api/v1/domains/{domain}/records/{record} | Get Record
[**get_record_code_api_v1_domains_domain_records_record_code_get**](RecordApi.md#get_record_code_api_v1_domains_domain_records_record_code_get) | **GET** /api/v1/domains/{domain}/records/{record}/code | Get Record Code
[**list_records_in_domain_api_v1_domains_domain_records_get**](RecordApi.md#list_records_in_domain_api_v1_domains_domain_records_get) | **GET** /api/v1/domains/{domain}/records | List Records In Domain

# **get_record_api_v1_domains_domain_records_record_get**
> RecordResp get_record_api_v1_domains_domain_records_record_get(record, domain)

Get Record

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.RecordApi(joj.horse.client.ApiClient(configuration))
record = 'record_example' # str | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Get Record
    api_response = api_instance.get_record_api_v1_domains_domain_records_record_get(record, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->get_record_api_v1_domains_domain_records_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record** | **str**|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**RecordResp**](RecordResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_record_code_api_v1_domains_domain_records_record_code_get**
> object get_record_code_api_v1_domains_domain_records_record_code_get(record, domain)

Get Record Code

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.RecordApi(joj.horse.client.ApiClient(configuration))
record = 'record_example' # str | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Get Record Code
    api_response = api_instance.get_record_code_api_v1_domains_domain_records_record_code_get(record, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->get_record_code_api_v1_domains_domain_records_record_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record** | **str**|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_records_in_domain_api_v1_domains_domain_records_get**
> RecordListResp list_records_in_domain_api_v1_domains_domain_records_get(domain, problem_set=problem_set, problem=problem, ordering=ordering, offset=offset, limit=limit, uid=uid)

List Records In Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.RecordApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | 
problem_set = 'problem_set_example' # str |  (optional)
problem = 'problem_example' # str |  (optional)
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
uid = '' # str | user id or 'me' or empty (optional)

try:
    # List Records In Domain
    api_response = api_instance.list_records_in_domain_api_v1_domains_domain_records_get(domain, problem_set=problem_set, problem=problem, ordering=ordering, offset=offset, limit=limit, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->list_records_in_domain_api_v1_domains_domain_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 
 **problem_set** | **str**|  | [optional] 
 **problem** | **str**|  | [optional] 
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **uid** | **str**| user id or &#x27;me&#x27; or empty | [optional] 

### Return type

[**RecordListResp**](RecordListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

