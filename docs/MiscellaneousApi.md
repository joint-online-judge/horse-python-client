# joj.horse.client.MiscellaneousApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jwt_api_v1_jwt_get**](MiscellaneousApi.md#jwt_api_v1_jwt_get) | **GET** /api/v1/jwt | Jwt
[**test_sentry_api_v1_test_sentry_get**](MiscellaneousApi.md#test_sentry_api_v1_test_sentry_get) | **GET** /api/v1/test/sentry | Test Sentry
[**version_api_v1_version_get**](MiscellaneousApi.md#version_api_v1_version_get) | **GET** /api/v1/version | Version

# **jwt_api_v1_jwt_get**
> JWT jwt_api_v1_jwt_get()

Jwt

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.MiscellaneousApi(joj.horse.client.ApiClient(configuration))

try:
    # Jwt
    api_response = api_instance.jwt_api_v1_jwt_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->jwt_api_v1_jwt_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JWT**](JWT.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_sentry_api_v1_test_sentry_get**
> str test_sentry_api_v1_test_sentry_get()

Test Sentry

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse.client.MiscellaneousApi()

try:
    # Test Sentry
    api_response = api_instance.test_sentry_api_v1_test_sentry_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->test_sentry_api_v1_test_sentry_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_api_v1_version_get**
> Version version_api_v1_version_get()

Version

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse.client.MiscellaneousApi()

try:
    # Version
    api_response = api_instance.version_api_v1_version_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->version_api_v1_version_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

