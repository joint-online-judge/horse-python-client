# joj.horse_client.AdminApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_admin_create_judger**](AdminApi.md#v1_admin_create_judger) | **POST** /admin/judgers | Admin Create Judger
[**v1_admin_get_user**](AdminApi.md#v1_admin_get_user) | **GET** /admin/{uid} | Admin Get User
[**v1_admin_list_domain_roles**](AdminApi.md#v1_admin_list_domain_roles) | **GET** /admin/domain_roles | Admin List Domain Roles
[**v1_admin_list_judgers**](AdminApi.md#v1_admin_list_judgers) | **GET** /admin/judgers | Admin List Judgers
[**v1_admin_list_user_domains**](AdminApi.md#v1_admin_list_user_domains) | **GET** /admin/{uid}/domains | Admin List User Domains
[**v1_admin_list_users**](AdminApi.md#v1_admin_list_users) | **GET** /admin/users | Admin List Users

# **v1_admin_create_judger**
> AuthTokensWithLakefsResp v1_admin_create_judger(body)

Admin Create Judger

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.JudgerCreate() # JudgerCreate | 

try:
    # Admin Create Judger
    api_response = api_instance.v1_admin_create_judger(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_admin_create_judger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JudgerCreate**](JudgerCreate.md)|  | 

### Return type

[**AuthTokensWithLakefsResp**](AuthTokensWithLakefsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_admin_get_user**
> UserDetailResp v1_admin_get_user(uid)

Admin Get User

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Admin Get User
    api_response = api_instance.v1_admin_get_user(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_admin_get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**UserDetailResp**](UserDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_admin_list_domain_roles**
> DomainRoleListResp v1_admin_list_domain_roles(ordering=ordering, offset=offset, limit=limit)

Admin List Domain Roles

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
ordering = '' # str | Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Admin List Domain Roles
    api_response = api_instance.v1_admin_list_domain_roles(ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_admin_list_domain_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
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

# **v1_admin_list_judgers**
> JudgerDetailListResp v1_admin_list_judgers(ordering=ordering, offset=offset, limit=limit)

Admin List Judgers

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
ordering = '' # str | Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Admin List Judgers
    api_response = api_instance.v1_admin_list_judgers(ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_admin_list_judgers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**JudgerDetailListResp**](JudgerDetailListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_admin_list_user_domains**
> DomainListResp v1_admin_list_user_domains(uid, role=role, groups=groups, ordering=ordering, offset=offset, limit=limit)

Admin List User Domains

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
uid = 'uid_example' # str | 
role = ['role_example'] # list[str] |  (optional)
groups = ['groups_example'] # list[str] |  (optional)
ordering = '' # str | Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Admin List User Domains
    api_response = api_instance.v1_admin_list_user_domains(uid, role=role, groups=groups, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_admin_list_user_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **role** | [**list[str]**](str.md)|  | [optional] 
 **groups** | [**list[str]**](str.md)|  | [optional] 
 **ordering** | **str**| Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
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

# **v1_admin_list_users**
> UserListResp v1_admin_list_users(ordering=ordering, offset=offset, limit=limit)

Admin List Users

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
ordering = '' # str | Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Admin List Users
    api_response = api_instance.v1_admin_list_users(ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_admin_list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
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

