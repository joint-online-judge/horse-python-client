# joj.horse_client.AuthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_get_token**](AuthApi.md#v1_get_token) | **GET** /auth/token | Get Token
[**v1_list_oauth2**](AuthApi.md#v1_list_oauth2) | **GET** /auth/oauth2 | List Oauth2
[**v1_login**](AuthApi.md#v1_login) | **POST** /auth/login | Login
[**v1_logout**](AuthApi.md#v1_logout) | **POST** /auth/logout | Logout
[**v1_oauth_authorize**](AuthApi.md#v1_oauth_authorize) | **GET** /auth/oauth2/{oauth2}/authorize | Oauth Authorize
[**v1_refresh**](AuthApi.md#v1_refresh) | **POST** /auth/refresh | Refresh
[**v1_register**](AuthApi.md#v1_register) | **POST** /auth/register | Register

# **v1_get_token**
> AuthTokensResp v1_get_token(response_type, cookie=cookie, redirect_url=redirect_url)

Get Token

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse_client.AuthApi()
response_type = 'response_type_example' # str | 
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Get Token
    api_response = api_instance.v1_get_token(response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_get_token: %s\n" % e)
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

# **v1_list_oauth2**
> OAuth2ClientListResp v1_list_oauth2()

List Oauth2

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse_client.AuthApi()

try:
    # List Oauth2
    api_response = api_instance.v1_list_oauth2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_list_oauth2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuth2ClientListResp**](OAuth2ClientListResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_login**
> AuthTokensResp v1_login(grant_type, username, password, scope, client_id, client_secret, response_type, cookie=cookie, redirect_url=redirect_url)

Login

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse_client.AuthApi()
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
    api_response = api_instance.v1_login(grant_type, username, password, scope, client_id, client_secret, response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_login: %s\n" % e)
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

# **v1_logout**
> object v1_logout(response_type, cookie=cookie, redirect_url=redirect_url)

Logout

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.AuthApi(joj.horse_client.ApiClient(configuration))
response_type = 'response_type_example' # str | 
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Logout
    api_response = api_instance.v1_logout(response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_logout: %s\n" % e)
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

# **v1_oauth_authorize**
> RedirectResp v1_oauth_authorize(oauth2, response_type, scopes=scopes, cookie=cookie, redirect_url=redirect_url)

Oauth Authorize

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse_client.AuthApi()
oauth2 = 'oauth2_example' # str | OAuth client name
response_type = 'response_type_example' # str | 
scopes = ['scopes_example'] # list[str] |  (optional)
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Oauth Authorize
    api_response = api_instance.v1_oauth_authorize(oauth2, response_type, scopes=scopes, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_oauth_authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth2** | **str**| OAuth client name | 
 **response_type** | **str**|  | 
 **scopes** | [**list[str]**](str.md)|  | [optional] 
 **cookie** | **bool**| Add Set/Delete-Cookie on response header | [optional] [default to true]
 **redirect_url** | **str**| The redirect url after the operation | [optional] 

### Return type

[**RedirectResp**](RedirectResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_refresh**
> AuthTokensResp v1_refresh(response_type, cookie=cookie, redirect_url=redirect_url)

Refresh

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse_client.AuthApi()
response_type = 'response_type_example' # str | 
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Refresh
    api_response = api_instance.v1_refresh(response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_refresh: %s\n" % e)
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

# **v1_register**
> AuthTokensResp v1_register(body, response_type, cookie=cookie, redirect_url=redirect_url)

Register

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.AuthApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.UserCreate() # UserCreate | 
response_type = 'response_type_example' # str | 
cookie = true # bool | Add Set/Delete-Cookie on response header (optional) (default to true)
redirect_url = 'redirect_url_example' # str | The redirect url after the operation (optional)

try:
    # Register
    api_response = api_instance.v1_register(body, response_type, cookie=cookie, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->v1_register: %s\n" % e)
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

