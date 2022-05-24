# joj.horse_client.UserApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_change_password**](UserApi.md#v1_change_password) | **PATCH** /users/me/password | Change Password
[**v1_get_current_user**](UserApi.md#v1_get_current_user) | **GET** /users/me | Get Current User
[**v1_get_user**](UserApi.md#v1_get_user) | **GET** /users/{uid} | Get User
[**v1_update_current_user**](UserApi.md#v1_update_current_user) | **PATCH** /users/me | Update Current User

# **v1_change_password**
> UserDetailResp v1_change_password(body)

Change Password

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.UserApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.UserResetPassword() # UserResetPassword | 

try:
    # Change Password
    api_response = api_instance.v1_change_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserResetPassword**](UserResetPassword.md)|  | 

### Return type

[**UserDetailResp**](UserDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_current_user**
> UserDetailResp v1_get_current_user()

Get Current User

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.UserApi(joj.horse_client.ApiClient(configuration))

try:
    # Get Current User
    api_response = api_instance.v1_get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDetailResp**](UserDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user**
> UserPreviewResp v1_get_user(uid)

Get User

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.UserApi(joj.horse_client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Get User
    api_response = api_instance.v1_get_user(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**UserPreviewResp**](UserPreviewResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_current_user**
> UserDetailResp v1_update_current_user(body)

Update Current User

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.UserApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.UserEdit() # UserEdit | 

try:
    # Update Current User
    api_response = api_instance.v1_update_current_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_update_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserEdit**](UserEdit.md)|  | 

### Return type

[**UserDetailResp**](UserDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

