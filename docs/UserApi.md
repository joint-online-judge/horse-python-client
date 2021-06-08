# joj.horse.client.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_api_v1_user_get**](UserApi.md#get_user_api_v1_user_get) | **GET** /api/v1/user | Get User
[**get_user_api_v1_users_uid_get**](UserApi.md#get_user_api_v1_users_uid_get) | **GET** /api/v1/users/{uid} | Get User
[**get_user_domains_api_v1_users_uid_domains_get**](UserApi.md#get_user_domains_api_v1_users_uid_domains_get) | **GET** /api/v1/users/{uid}/domains | Get User Domains
[**get_user_problems_api_v1_user_problems_get**](UserApi.md#get_user_problems_api_v1_user_problems_get) | **GET** /api/v1/user/problems | Get User Problems
[**get_user_problems_api_v1_users_uid_problems_get**](UserApi.md#get_user_problems_api_v1_users_uid_problems_get) | **GET** /api/v1/users/{uid}/problems | Get User Problems
[**jaccount_auth_api_v1_user_jaccount_auth_get**](UserApi.md#jaccount_auth_api_v1_user_jaccount_auth_get) | **GET** /api/v1/user/jaccount/auth | Jaccount Auth
[**jaccount_login_api_v1_user_jaccount_login_get**](UserApi.md#jaccount_login_api_v1_user_jaccount_login_get) | **GET** /api/v1/user/jaccount/login | Jaccount Login
[**logout_api_v1_user_logout_get**](UserApi.md#logout_api_v1_user_logout_get) | **GET** /api/v1/user/logout | Logout

# **get_user_api_v1_user_get**
> UserResp get_user_api_v1_user_get()

Get User

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.UserApi(joj.horse.client.ApiClient(configuration))

try:
    # Get User
    api_response = api_instance.get_user_api_v1_user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_api_v1_user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserResp**](UserResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_v1_users_uid_get**
> UserBaseResp get_user_api_v1_users_uid_get(uid)

Get User

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.UserApi(joj.horse.client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Get User
    api_response = api_instance.get_user_api_v1_users_uid_get(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_api_v1_users_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**UserBaseResp**](UserBaseResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_domains_api_v1_users_uid_domains_get**
> ListDomainUsersResp get_user_domains_api_v1_users_uid_domains_get(uid, role=role, sort=sort, skip=skip, limit=limit)

Get User Domains

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.UserApi(joj.horse.client.ApiClient(configuration))
uid = 'uid_example' # str | 
role = ['[]'] # list[str] |  (optional) (default to [])
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # Get User Domains
    api_response = api_instance.get_user_domains_api_v1_users_uid_domains_get(uid, role=role, sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_domains_api_v1_users_uid_domains_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **role** | [**list[str]**](str.md)|  | [optional] [default to []]
 **sort** | [**SortEnum**](.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ListDomainUsersResp**](ListDomainUsersResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_problems_api_v1_user_problems_get**
> ListProblemsResp get_user_problems_api_v1_user_problems_get(sort=sort, skip=skip, limit=limit)

Get User Problems

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.UserApi(joj.horse.client.ApiClient(configuration))
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # Get User Problems
    api_response = api_instance.get_user_problems_api_v1_user_problems_get(sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_problems_api_v1_user_problems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**SortEnum**](.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ListProblemsResp**](ListProblemsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_problems_api_v1_users_uid_problems_get**
> ListProblemsResp get_user_problems_api_v1_users_uid_problems_get(uid, sort=sort, skip=skip, limit=limit)

Get User Problems

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.UserApi(joj.horse.client.ApiClient(configuration))
uid = 'uid_example' # str | 
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # Get User Problems
    api_response = api_instance.get_user_problems_api_v1_users_uid_problems_get(uid, sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_problems_api_v1_users_uid_problems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **sort** | [**SortEnum**](.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ListProblemsResp**](ListProblemsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jaccount_auth_api_v1_user_jaccount_auth_get**
> RedirectModel jaccount_auth_api_v1_user_jaccount_auth_get(state, code, jaccount_state=jaccount_state, redirect_url=redirect_url)

Jaccount Auth

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse.client.UserApi()
state = 'state_example' # str | 
code = 'code_example' # str | 
jaccount_state = 'jaccount_state_example' # str |  (optional)
redirect_url = 'redirect_url_example' # str |  (optional)

try:
    # Jaccount Auth
    api_response = api_instance.jaccount_auth_api_v1_user_jaccount_auth_get(state, code, jaccount_state=jaccount_state, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->jaccount_auth_api_v1_user_jaccount_auth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **code** | **str**|  | 
 **jaccount_state** | **str**|  | [optional] 
 **redirect_url** | **str**|  | [optional] 

### Return type

[**RedirectModel**](RedirectModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jaccount_login_api_v1_user_jaccount_login_get**
> RedirectModel jaccount_login_api_v1_user_jaccount_login_get(redirect_url=redirect_url, redirect=redirect)

Jaccount Login

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = joj.horse.client.UserApi()
redirect_url = 'http://127.0.0.1:34765' # str | Set the redirect url after the authorization. (optional) (default to http://127.0.0.1:34765)
redirect = true # bool | If true (html link mode), redirect to jaccount site; If false (ajax mode), return the redirect url to the jaccount site, you also need to set the cookies returned manually in ajax mode. (optional) (default to true)

try:
    # Jaccount Login
    api_response = api_instance.jaccount_login_api_v1_user_jaccount_login_get(redirect_url=redirect_url, redirect=redirect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->jaccount_login_api_v1_user_jaccount_login_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_url** | **str**| Set the redirect url after the authorization. | [optional] [default to http://127.0.0.1:34765]
 **redirect** | **bool**| If true (html link mode), redirect to jaccount site; If false (ajax mode), return the redirect url to the jaccount site, you also need to set the cookies returned manually in ajax mode. | [optional] [default to true]

### Return type

[**RedirectModel**](RedirectModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_api_v1_user_logout_get**
> RedirectModel logout_api_v1_user_logout_get(redirect_url=redirect_url, redirect=redirect)

Logout

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.UserApi(joj.horse.client.ApiClient(configuration))
redirect_url = 'http://127.0.0.1:34765' # str | Set the redirect url after the logout. (optional) (default to http://127.0.0.1:34765)
redirect = true # bool | If true (html link mode), redirect to a url; If false (ajax mode), return the redirect url, you also need to unset all cookies manually in ajax mode. (optional) (default to true)

try:
    # Logout
    api_response = api_instance.logout_api_v1_user_logout_get(redirect_url=redirect_url, redirect=redirect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->logout_api_v1_user_logout_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_url** | **str**| Set the redirect url after the logout. | [optional] [default to http://127.0.0.1:34765]
 **redirect** | **bool**| If true (html link mode), redirect to a url; If false (ajax mode), return the redirect url, you also need to unset all cookies manually in ajax mode. | [optional] [default to true]

### Return type

[**RedirectModel**](RedirectModel.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

