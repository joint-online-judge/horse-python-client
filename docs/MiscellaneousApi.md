# joj.horse.client.MiscellaneousApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jwt_decoded_api_v1_jwt_decoded_get**](MiscellaneousApi.md#jwt_decoded_api_v1_jwt_decoded_get) | **GET** /api/v1/jwt_decoded | Jwt Decoded
[**set_root_user_api_v1_set_root_user_post**](MiscellaneousApi.md#set_root_user_api_v1_set_root_user_post) | **POST** /api/v1/set_root_user | Set Root User
[**test_error_report_api_v1_test_report_get**](MiscellaneousApi.md#test_error_report_api_v1_test_report_get) | **GET** /api/v1/test/report | Test Error Report
[**version_api_v1_version_get**](MiscellaneousApi.md#version_api_v1_version_get) | **GET** /api/v1/version | Version

# **jwt_decoded_api_v1_jwt_decoded_get**
> JWTAccessTokenResp jwt_decoded_api_v1_jwt_decoded_get()

Jwt Decoded

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
    # Jwt Decoded
    api_response = api_instance.jwt_decoded_api_v1_jwt_decoded_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->jwt_decoded_api_v1_jwt_decoded_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JWTAccessTokenResp**](JWTAccessTokenResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_root_user_api_v1_set_root_user_post**
> UserBaseResp set_root_user_api_v1_set_root_user_post()

Set Root User

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
    # Set Root User
    api_response = api_instance.set_root_user_api_v1_set_root_user_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->set_root_user_api_v1_set_root_user_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserBaseResp**](UserBaseResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_error_report_api_v1_test_report_get**
> Null test_error_report_api_v1_test_report_get()

Test Error Report

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
    # Test Error Report
    api_response = api_instance.test_error_report_api_v1_test_report_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->test_error_report_api_v1_test_report_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Null**](Null.md)

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

