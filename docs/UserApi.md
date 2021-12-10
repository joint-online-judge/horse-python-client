# joj.horse_client.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_get_user**](UserApi.md#v1_get_user) | **GET** /user | Get User
[**v1_get_user_0**](UserApi.md#v1_get_user_0) | **GET** /users/{uid} | Get User
[**v1_get_user_problems**](UserApi.md#v1_get_user_problems) | **GET** /user/problems | Get User Problems
[**v1_get_user_problems_0**](UserApi.md#v1_get_user_problems_0) | **GET** /users/{uid}/problems | Get User Problems
[**v1_list_user_domains**](UserApi.md#v1_list_user_domains) | **GET** /users/{uid}/domains | List User Domains
[**v1_list_users**](UserApi.md#v1_list_users) | **GET** /users | List Users

# **v1_get_user**
> UserDetailResp v1_get_user()

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

try:
    # Get User
    api_response = api_instance.v1_get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_get_user: %s\n" % e)
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

# **v1_get_user_0**
> UserResp v1_get_user_0(uid)

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
    api_response = api_instance.v1_get_user_0(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_get_user_0: %s\n" % e)
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

# **v1_get_user_problems**
> ProblemListResp v1_get_user_problems(offset=offset, limit=limit)

Get User Problems

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.UserApi(joj.horse_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get User Problems
    api_response = api_instance.v1_get_user_problems(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_get_user_problems: %s\n" % e)
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

# **v1_get_user_problems_0**
> ProblemListResp v1_get_user_problems_0(uid, offset=offset, limit=limit)

Get User Problems

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
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get User Problems
    api_response = api_instance.v1_get_user_problems_0(uid, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_get_user_problems_0: %s\n" % e)
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

# **v1_list_user_domains**
> DomainListResp v1_list_user_domains(uid, role=role, ordering=ordering, offset=offset, limit=limit)

List User Domains

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
role = ['role_example'] # list[str] |  (optional)
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List User Domains
    api_response = api_instance.v1_list_user_domains(uid, role=role, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_list_user_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **role** | [**list[str]**](str.md)|  | [optional] 
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
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

# **v1_list_users**
> UserListResp v1_list_users(query=query, ordering=ordering, offset=offset, limit=limit)

List Users

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.UserApi(joj.horse_client.ApiClient(configuration))
query = '' # str |  (optional)
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: username (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Users
    api_response = api_instance.v1_list_users(query=query, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_list_users: %s\n" % e)
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

