# joj.horse_client.RecordApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_get_record**](RecordApi.md#v1_get_record) | **GET** /domains/{domain}/records/{record} | Get Record
[**v1_get_record_code**](RecordApi.md#v1_get_record_code) | **GET** /domains/{domain}/records/{record}/code | Get Record Code
[**v1_list_records_in_domain**](RecordApi.md#v1_list_records_in_domain) | **GET** /domains/{domain}/records | List Records In Domain

# **v1_get_record**
> RecordResp v1_get_record(record, domain)

Get Record

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.RecordApi(joj.horse_client.ApiClient(configuration))
record = 'record_example' # str | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Get Record
    api_response = api_instance.v1_get_record(record, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->v1_get_record: %s\n" % e)
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

# **v1_get_record_code**
> object v1_get_record_code(record, domain)

Get Record Code

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.RecordApi(joj.horse_client.ApiClient(configuration))
record = 'record_example' # str | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Get Record Code
    api_response = api_instance.v1_get_record_code(record, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->v1_get_record_code: %s\n" % e)
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

# **v1_list_records_in_domain**
> RecordListResp v1_list_records_in_domain(domain, ordering=ordering, offset=offset, limit=limit)

List Records In Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.RecordApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Records In Domain
    api_response = api_instance.v1_list_records_in_domain(domain, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->v1_list_records_in_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**RecordListResp**](RecordListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

