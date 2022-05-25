# joj.horse_client.MiscellaneousApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_jwt_decoded**](MiscellaneousApi.md#v1_jwt_decoded) | **GET** /jwt_decoded | Jwt Decoded
[**v1_test_error_report**](MiscellaneousApi.md#v1_test_error_report) | **GET** /test/report | Test Error Report
[**v1_version**](MiscellaneousApi.md#v1_version) | **GET** /version | Version

# **v1_jwt_decoded**
> JWTAccessTokenResp v1_jwt_decoded()

Jwt Decoded

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.MiscellaneousApi(joj.horse_client.ApiClient(configuration))

try:
    # Jwt Decoded
    api_response = api_instance.v1_jwt_decoded()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->v1_jwt_decoded: %s\n" % e)
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

# **v1_test_error_report**
> EmptyResp v1_test_error_report()

Test Error Report

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse_client.MiscellaneousApi()

try:
    # Test Error Report
    api_response = api_instance.v1_test_error_report()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->v1_test_error_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_version**
> Version v1_version()

Version

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse_client.MiscellaneousApi()

try:
    # Version
    api_response = api_instance.v1_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->v1_version: %s\n" % e)
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

