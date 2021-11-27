# joj.horse.client.AuthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_api_v1_auth_token_get**](AuthApi.md#get_token_api_v1_auth_token_get) | **GET** /api/v1/auth/token | Get Token
[**login_api_v1_auth_login_post**](AuthApi.md#login_api_v1_auth_login_post) | **POST** /api/v1/auth/login | Login
[**logout_api_v1_auth_logout_post**](AuthApi.md#logout_api_v1_auth_logout_post) | **POST** /api/v1/auth/logout | Logout
[**refresh_api_v1_auth_refresh_post**](AuthApi.md#refresh_api_v1_auth_refresh_post) | **POST** /api/v1/auth/refresh | Refresh
[**register_api_v1_auth_register_post**](AuthApi.md#register_api_v1_auth_register_post) | **POST** /api/v1/auth/register | Register

# **get_token_api_v1_auth_token_get**
> AuthTokensResp get_token_api_v1_auth_token_get(response_type, cookie=cookie, redirect_url=redirect_url)

Get Token

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse.client.AuthApi()
response_type = 'response_type_example' # str | 
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Get Token
    api_response = api_instance.get_token_api_v1_auth_token_get(response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_token_api_v1_auth_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**|  | 
 **cookie** | **bool**| Add Set/Delete-Cookie on response header | [optional] [default to true]
 **redirect_url** | **str**| The redirect url after the operation | [optional] 

### Return type

[**AuthTokensResp**](AuthTokensResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_api_v1_auth_login_post**
> AuthTokensResp login_api_v1_auth_login_post(grant_type, username, password, scope, client_id, client_secret, response_type, cookie=cookie, redirect_url=redirect_url)

Login

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse.client.AuthApi()
grant_type = 'grant_type_example' # str | 
username = 'username_example' # str | 
password = 'password_example' # str | 
scope = 'scope_example' # str | 
client_id = 'client_id_example' # str | 
client_secret = 'client_secret_example' # str | 
response_type = 'response_type_example' # str | 
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Login
    api_response = api_instance.login_api_v1_auth_login_post(grant_type, username, password, scope, client_id, client_secret, response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login_api_v1_auth_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | 
 **username** | **str**|  | 
 **password** | **str**|  | 
 **scope** | **str**|  | 
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 
 **response_type** | **str**|  | 
 **cookie** | **bool**| Add Set/Delete-Cookie on response header | [optional] [default to true]
 **redirect_url** | **str**| The redirect url after the operation | [optional] 

### Return type

[**AuthTokensResp**](AuthTokensResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_api_v1_auth_logout_post**
> object logout_api_v1_auth_logout_post(response_type, cookie=cookie, redirect_url=redirect_url)

Logout

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AuthApi(joj.horse.client.ApiClient(configuration))
response_type = 'response_type_example' # str | 
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Logout
    api_response = api_instance.logout_api_v1_auth_logout_post(response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->logout_api_v1_auth_logout_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**|  | 
 **cookie** | **bool**| Add Set/Delete-Cookie on response header | [optional] [default to true]
 **redirect_url** | **str**| The redirect url after the operation | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_api_v1_auth_refresh_post**
> AuthTokensResp refresh_api_v1_auth_refresh_post(response_type, cookie=cookie, redirect_url=redirect_url)

Refresh

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse.client.AuthApi()
response_type = 'response_type_example' # str | 
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Refresh
    api_response = api_instance.refresh_api_v1_auth_refresh_post(response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->refresh_api_v1_auth_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**|  | 
 **cookie** | **bool**| Add Set/Delete-Cookie on response header | [optional] [default to true]
 **redirect_url** | **str**| The redirect url after the operation | [optional] 

### Return type

[**AuthTokensResp**](AuthTokensResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_api_v1_auth_register_post**
> AuthTokensResp register_api_v1_auth_register_post(body, response_type, cookie=cookie, redirect_url=redirect_url)

Register

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AuthApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.UserCreate() # UserCreate | 
response_type = 'response_type_example' # str | 
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Register
    api_response = api_instance.register_api_v1_auth_register_post(body, response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->register_api_v1_auth_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreate**](UserCreate.md)|  | 
 **response_type** | **str**|  | 
 **cookie** | **bool**| Add Set/Delete-Cookie on response header | [optional] [default to true]
 **redirect_url** | **str**| The redirect url after the operation | [optional] 

### Return type

[**AuthTokensResp**](AuthTokensResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

