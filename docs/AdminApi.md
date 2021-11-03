# joj.horse.client.AdminApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_judger_api_v1_admin_judgers_post**](AdminApi.md#create_judger_api_v1_admin_judgers_post) | **POST** /api/v1/admin/judgers | Create Judger
[**create_user_api_v1_admin_users_post**](AdminApi.md#create_user_api_v1_admin_users_post) | **POST** /api/v1/admin/users | Create User
[**delete_user_api_v1_admin_users_uid_delete**](AdminApi.md#delete_user_api_v1_admin_users_uid_delete) | **DELETE** /api/v1/admin/users/{uid} | Delete User
[**get_judger_jwt_api_v1_admin_judgers_uid_jwt_get**](AdminApi.md#get_judger_jwt_api_v1_admin_judgers_uid_jwt_get) | **GET** /api/v1/admin/judgers/{uid}/jwt | Get Judger Jwt
[**list_domain_roles_api_v1_admin_domain_roles_get**](AdminApi.md#list_domain_roles_api_v1_admin_domain_roles_get) | **GET** /api/v1/admin/domain_roles | List Domain Roles
[**list_domain_users_api_v1_admin_domain_users_get**](AdminApi.md#list_domain_users_api_v1_admin_domain_users_get) | **GET** /api/v1/admin/domain_users | List Domain Users
[**list_judgers_api_v1_admin_judgers_get**](AdminApi.md#list_judgers_api_v1_admin_judgers_get) | **GET** /api/v1/admin/judgers | List Judgers
[**list_users_api_v1_admin_users_get**](AdminApi.md#list_users_api_v1_admin_users_get) | **GET** /api/v1/admin/users | List Users

# **create_judger_api_v1_admin_judgers_post**
> UserResp create_judger_api_v1_admin_judgers_post(uname, mail)

Create Judger

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
uname = 'uname_example' # str | 
mail = 'mail_example' # str | 

try:
    # Create Judger
    api_response = api_instance.create_judger_api_v1_admin_judgers_post(uname, mail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_judger_api_v1_admin_judgers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uname** | **str**|  | 
 **mail** | **str**|  | 

### Return type

[**UserResp**](UserResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_api_v1_admin_users_post**
> UserResp create_user_api_v1_admin_users_post(student_id, jaccount_name, real_name, ip)

Create User

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
student_id = 'student_id_example' # str | 
jaccount_name = 'jaccount_name_example' # str | 
real_name = 'real_name_example' # str | 
ip = 'ip_example' # str | 

try:
    # Create User
    api_response = api_instance.create_user_api_v1_admin_users_post(student_id, jaccount_name, real_name, ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_user_api_v1_admin_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student_id** | **str**|  | 
 **jaccount_name** | **str**|  | 
 **real_name** | **str**|  | 
 **ip** | **str**|  | 

### Return type

[**UserResp**](UserResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_api_v1_admin_users_uid_delete**
> EmptyResp delete_user_api_v1_admin_users_uid_delete(uid)

Delete User

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Delete User
    api_response = api_instance.delete_user_api_v1_admin_users_uid_delete(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->delete_user_api_v1_admin_users_uid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_judger_jwt_api_v1_admin_judgers_uid_jwt_get**
> JWT get_judger_jwt_api_v1_admin_judgers_uid_jwt_get(uid)

Get Judger Jwt

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Get Judger Jwt
    api_response = api_instance.get_judger_jwt_api_v1_admin_judgers_uid_jwt_get(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_judger_jwt_api_v1_admin_judgers_uid_jwt_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**JWT**](JWT.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_roles_api_v1_admin_domain_roles_get**
> DomainRoleListResp list_domain_roles_api_v1_admin_domain_roles_get(offset=offset, limit=limit)

List Domain Roles

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Domain Roles
    api_response = api_instance.list_domain_roles_api_v1_admin_domain_roles_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_domain_roles_api_v1_admin_domain_roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**DomainRoleListResp**](DomainRoleListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_users_api_v1_admin_domain_users_get**
> DomainUserListResp list_domain_users_api_v1_admin_domain_users_get(offset=offset, limit=limit)

List Domain Users

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Domain Users
    api_response = api_instance.list_domain_users_api_v1_admin_domain_users_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_domain_users_api_v1_admin_domain_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**DomainUserListResp**](DomainUserListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_judgers_api_v1_admin_judgers_get**
> UserListResp list_judgers_api_v1_admin_judgers_get(offset=offset, limit=limit)

List Judgers

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Judgers
    api_response = api_instance.list_judgers_api_v1_admin_judgers_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_judgers_api_v1_admin_judgers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**UserListResp**](UserListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_api_v1_admin_users_get**
> UserBaseListResp list_users_api_v1_admin_users_get(offset=offset, limit=limit)

List Users

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Users
    api_response = api_instance.list_users_api_v1_admin_users_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_users_api_v1_admin_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**UserBaseListResp**](UserBaseListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

