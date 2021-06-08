# joj.horse.client.RecordApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_record_api_v1_records_record_get**](RecordApi.md#get_record_api_v1_records_record_get) | **GET** /api/v1/records/{record} | Get Record
[**get_record_code_api_v1_records_record_code_get**](RecordApi.md#get_record_code_api_v1_records_record_code_get) | **GET** /api/v1/records/{record}/code | Get Record Code
[**http_record_api_v1_records_record_http_post**](RecordApi.md#http_record_api_v1_records_record_http_post) | **POST** /api/v1/records/{record}/http | Http Record
[**http_record_cases_api_v1_records_record_cases_http_post**](RecordApi.md#http_record_cases_api_v1_records_record_cases_http_post) | **POST** /api/v1/records/{record}/cases/http | Http Record Cases
[**list_records_api_v1_records_get**](RecordApi.md#list_records_api_v1_records_get) | **GET** /api/v1/records | List Records

# **get_record_api_v1_records_record_get**
> RecordResp get_record_api_v1_records_record_get(record)

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

try:
    # Get Record
    api_response = api_instance.get_record_api_v1_records_record_get(record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->get_record_api_v1_records_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record** | **str**|  | 

### Return type

[**RecordResp**](RecordResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_record_code_api_v1_records_record_code_get**
> Object get_record_code_api_v1_records_record_code_get(record)

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

try:
    # Get Record Code
    api_response = api_instance.get_record_code_api_v1_records_record_code_get(record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->get_record_code_api_v1_records_record_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record** | **str**|  | 

### Return type

[**Object**](Object.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_record_api_v1_records_record_http_post**
> EmptyResp http_record_api_v1_records_record_http_post(body, record)

Http Record

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.RecordApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.RecordResult() # RecordResult | 
record = 'record_example' # str | 

try:
    # Http Record
    api_response = api_instance.http_record_api_v1_records_record_http_post(body, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->http_record_api_v1_records_record_http_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordResult**](RecordResult.md)|  | 
 **record** | **str**|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_record_cases_api_v1_records_record_cases_http_post**
> EmptyResp http_record_cases_api_v1_records_record_cases_http_post(body, record)

Http Record Cases

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.RecordApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.RecordCaseResult() # RecordCaseResult | 
record = 'record_example' # str | 

try:
    # Http Record Cases
    api_response = api_instance.http_record_cases_api_v1_records_record_cases_http_post(body, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->http_record_cases_api_v1_records_record_cases_http_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordCaseResult**](RecordCaseResult.md)|  | 
 **record** | **str**|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_records_api_v1_records_get**
> ListRecordsResp list_records_api_v1_records_get(domain=domain, problem_set=problem_set, problem=problem, sort=sort, skip=skip, limit=limit, uid=uid)

List Records

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.RecordApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str |  (optional)
problem_set = 'problem_set_example' # str |  (optional)
problem = 'problem_example' # str |  (optional)
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)
uid = '' # str | uid or 'me' or empty (optional)

try:
    # List Records
    api_response = api_instance.list_records_api_v1_records_get(domain=domain, problem_set=problem_set, problem=problem, sort=sort, skip=skip, limit=limit, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->list_records_api_v1_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | [optional] 
 **problem_set** | **str**|  | [optional] 
 **problem** | **str**|  | [optional] 
 **sort** | [**SortEnum**](.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **uid** | **str**| uid or &#x27;me&#x27; or empty | [optional] 

### Return type

[**ListRecordsResp**](ListRecordsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

