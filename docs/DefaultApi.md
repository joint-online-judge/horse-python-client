# joj.horse_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redirect_to_docs_api_get**](DefaultApi.md#redirect_to_docs_api_get) | **GET** /api | Redirect To Docs
[**redirect_to_docs_get**](DefaultApi.md#redirect_to_docs_get) | **GET** / | Redirect To Docs

# **redirect_to_docs_api_get**
> object redirect_to_docs_api_get()

Redirect To Docs

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse_client.DefaultApi()

try:
    # Redirect To Docs
    api_response = api_instance.redirect_to_docs_api_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->redirect_to_docs_api_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redirect_to_docs_get**
> object redirect_to_docs_get()

Redirect To Docs

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse_client.DefaultApi()

try:
    # Redirect To Docs
    api_response = api_instance.redirect_to_docs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->redirect_to_docs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

