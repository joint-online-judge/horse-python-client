# joj.horse.client.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_api_v1_user_get**](UserApi.md#get_user_api_v1_user_get) | **GET** /api/v1/user | Get User
[**get_user_api_v1_users_uid_get**](UserApi.md#get_user_api_v1_users_uid_get) | **GET** /api/v1/users/{uid} | Get User
[**get_user_problems_api_v1_user_problems_get**](UserApi.md#get_user_problems_api_v1_user_problems_get) | **GET** /api/v1/user/problems | Get User Problems
[**get_user_problems_api_v1_users_uid_problems_get**](UserApi.md#get_user_problems_api_v1_users_uid_problems_get) | **GET** /api/v1/users/{uid}/problems | Get User Problems
[**list_user_domains_api_v1_users_uid_domains_get**](UserApi.md#list_user_domains_api_v1_users_uid_domains_get) | **GET** /api/v1/users/{uid}/domains | List User Domains
[**list_users_api_v1_users_get**](UserApi.md#list_users_api_v1_users_get) | **GET** /api/v1/users | List Users

# **get_user_api_v1_user_get**
> UserDetailResp get_user_api_v1_user_get()

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

[**UserDetailResp**](UserDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_v1_users_uid_get**
> UserResp get_user_api_v1_users_uid_get(uid)

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

[**UserResp**](UserResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_problems_api_v1_user_problems_get**
> ProblemListResp get_user_problems_api_v1_user_problems_get(offset=offset, limit=limit)

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
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get User Problems
    api_response = api_instance.get_user_problems_api_v1_user_problems_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_problems_api_v1_user_problems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ProblemListResp**](ProblemListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_problems_api_v1_users_uid_problems_get**
> ProblemListResp get_user_problems_api_v1_users_uid_problems_get(uid, offset=offset, limit=limit)

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
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get User Problems
    api_response = api_instance.get_user_problems_api_v1_users_uid_problems_get(uid, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_problems_api_v1_users_uid_problems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ProblemListResp**](ProblemListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_domains_api_v1_users_uid_domains_get**
> DomainListResp list_user_domains_api_v1_users_uid_domains_get(uid, role=role, ordering=ordering, offset=offset, limit=limit)

List User Domains

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
role = ['role_example'] # list[str] |  (optional)
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: name (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List User Domains
    api_response = api_instance.list_user_domains_api_v1_users_uid_domains_get(uid, role=role, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_domains_api_v1_users_uid_domains_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **role** | [**list[str]**](str.md)|  | [optional] 
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: name | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**DomainListResp**](DomainListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_api_v1_users_get**
> UserListResp list_users_api_v1_users_get(query=query, ordering=ordering, offset=offset, limit=limit)

List Users

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.UserApi(joj.horse.client.ApiClient(configuration))
query = '' # str |  (optional)
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: username (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Users
    api_response = api_instance.list_users_api_v1_users_get(query=query, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users_api_v1_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: username | [optional] 
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

