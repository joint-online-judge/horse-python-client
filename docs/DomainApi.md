# joj.horse.client.DomainApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain_user_api_v1_domains_domain_users_post**](DomainApi.md#add_domain_user_api_v1_domains_domain_users_post) | **POST** /api/v1/domains/{domain}/users | Add Domain User
[**create_domain_api_v1_domains_post**](DomainApi.md#create_domain_api_v1_domains_post) | **POST** /api/v1/domains | Create Domain
[**create_domain_invitation_api_v1_domains_domain_invitations_post**](DomainApi.md#create_domain_invitation_api_v1_domains_domain_invitations_post) | **POST** /api/v1/domains/{domain}/invitations | Create Domain Invitation
[**create_domain_role_api_v1_domains_domain_roles_post**](DomainApi.md#create_domain_role_api_v1_domains_domain_roles_post) | **POST** /api/v1/domains/{domain}/roles | Create Domain Role
[**delete_domain_api_v1_domains_domain_delete**](DomainApi.md#delete_domain_api_v1_domains_domain_delete) | **DELETE** /api/v1/domains/{domain} | Delete Domain
[**delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete**](DomainApi.md#delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete) | **DELETE** /api/v1/domains/{domain}/invitations/{invitation} | Delete Domain Invitation
[**delete_domain_role_api_v1_domains_domain_roles_role_delete**](DomainApi.md#delete_domain_role_api_v1_domains_domain_roles_role_delete) | **DELETE** /api/v1/domains/{domain}/roles/{role} | Delete Domain Role
[**get_domain_api_v1_domains_domain_get**](DomainApi.md#get_domain_api_v1_domains_domain_get) | **GET** /api/v1/domains/{domain} | Get Domain
[**get_domain_user_api_v1_domains_domain_users_user_get**](DomainApi.md#get_domain_user_api_v1_domains_domain_users_user_get) | **GET** /api/v1/domains/{domain}/users/{user} | Get Domain User
[**join_domain_by_invitation_api_v1_domains_domain_join_post**](DomainApi.md#join_domain_by_invitation_api_v1_domains_domain_join_post) | **POST** /api/v1/domains/{domain}/join | Join Domain By Invitation
[**list_domain_roles_api_v1_domains_domain_roles_get**](DomainApi.md#list_domain_roles_api_v1_domains_domain_roles_get) | **GET** /api/v1/domains/{domain}/roles | List Domain Roles
[**list_domain_users_api_v1_domains_domain_users_get**](DomainApi.md#list_domain_users_api_v1_domains_domain_users_get) | **GET** /api/v1/domains/{domain}/users | List Domain Users
[**list_domains_api_v1_domains_get**](DomainApi.md#list_domains_api_v1_domains_get) | **GET** /api/v1/domains | List Domains
[**remove_domain_user_api_v1_domains_domain_users_user_delete**](DomainApi.md#remove_domain_user_api_v1_domains_domain_users_user_delete) | **DELETE** /api/v1/domains/{domain}/users/{user} | Remove Domain User
[**transfer_domain_api_v1_domains_domain_transfer_post**](DomainApi.md#transfer_domain_api_v1_domains_domain_transfer_post) | **POST** /api/v1/domains/{domain}/transfer | Transfer Domain
[**update_domain_api_v1_domains_domain_patch**](DomainApi.md#update_domain_api_v1_domains_domain_patch) | **PATCH** /api/v1/domains/{domain} | Update Domain
[**update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch**](DomainApi.md#update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch) | **PATCH** /api/v1/domains/{domain}/invitations/{invitation} | Update Domain Invitation
[**update_domain_role_api_v1_domains_domain_roles_role_patch**](DomainApi.md#update_domain_role_api_v1_domains_domain_roles_role_patch) | **PATCH** /api/v1/domains/{domain}/roles/{role} | Update Domain Role
[**update_domain_user_api_v1_domains_domain_users_user_patch**](DomainApi.md#update_domain_user_api_v1_domains_domain_users_user_patch) | **PATCH** /api/v1/domains/{domain}/users/{user} | Update Domain User

# **add_domain_user_api_v1_domains_domain_users_post**
> DomainUserResp add_domain_user_api_v1_domains_domain_users_post(body, domain)

Add Domain User

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.DomainUserAdd() # DomainUserAdd | 
domain = 'domain_example' # str | url or ObjectId of the domain

try:
    # Add Domain User
    api_response = api_instance.add_domain_user_api_v1_domains_domain_users_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->add_domain_user_api_v1_domains_domain_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainUserAdd**](DomainUserAdd.md)|  | 
 **domain** | **str**| url or ObjectId of the domain | 

### Return type

[**DomainUserResp**](DomainUserResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain_api_v1_domains_post**
> DomainResp create_domain_api_v1_domains_post(body)

Create Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.DomainCreate() # DomainCreate | 

try:
    # Create Domain
    api_response = api_instance.create_domain_api_v1_domains_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->create_domain_api_v1_domains_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainCreate**](DomainCreate.md)|  | 

### Return type

[**DomainResp**](DomainResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain_invitation_api_v1_domains_domain_invitations_post**
> DomainInvitationResp create_domain_invitation_api_v1_domains_domain_invitations_post(body, domain)

Create Domain Invitation

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.DomainInvitationCreate() # DomainInvitationCreate | 
domain = 'domain_example' # str | url or ObjectId of the domain

try:
    # Create Domain Invitation
    api_response = api_instance.create_domain_invitation_api_v1_domains_domain_invitations_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->create_domain_invitation_api_v1_domains_domain_invitations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainInvitationCreate**](DomainInvitationCreate.md)|  | 
 **domain** | **str**| url or ObjectId of the domain | 

### Return type

[**DomainInvitationResp**](DomainInvitationResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain_role_api_v1_domains_domain_roles_post**
> DomainRoleResp create_domain_role_api_v1_domains_domain_roles_post(body, domain)

Create Domain Role

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.DomainRoleCreate() # DomainRoleCreate | 
domain = 'domain_example' # str | url or ObjectId of the domain

try:
    # Create Domain Role
    api_response = api_instance.create_domain_role_api_v1_domains_domain_roles_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->create_domain_role_api_v1_domains_domain_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRoleCreate**](DomainRoleCreate.md)|  | 
 **domain** | **str**| url or ObjectId of the domain | 

### Return type

[**DomainRoleResp**](DomainRoleResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_api_v1_domains_domain_delete**
> EmptyResp delete_domain_api_v1_domains_domain_delete(domain)

Delete Domain

TODO: finish this part  tc-imba: delete domain have many side effects, and is not urgent,          marked it deprecated and implement it later

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain

try:
    # Delete Domain
    api_response = api_instance.delete_domain_api_v1_domains_domain_delete(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->delete_domain_api_v1_domains_domain_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete**
> EmptyResp delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete(domain, invitation)

Delete Domain Invitation

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain
invitation = 'invitation_example' # str | ObjectId of the domain invitation

try:
    # Delete Domain Invitation
    api_response = api_instance.delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete(domain, invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 
 **invitation** | **str**| ObjectId of the domain invitation | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_role_api_v1_domains_domain_roles_role_delete**
> EmptyResp delete_domain_role_api_v1_domains_domain_roles_role_delete(domain, role)

Delete Domain Role

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain
role = 'role_example' # str | name of the domain role

try:
    # Delete Domain Role
    api_response = api_instance.delete_domain_role_api_v1_domains_domain_roles_role_delete(domain, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->delete_domain_role_api_v1_domains_domain_roles_role_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 
 **role** | **str**| name of the domain role | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_api_v1_domains_domain_get**
> DomainResp get_domain_api_v1_domains_domain_get(domain)

Get Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain

try:
    # Get Domain
    api_response = api_instance.get_domain_api_v1_domains_domain_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->get_domain_api_v1_domains_domain_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 

### Return type

[**DomainResp**](DomainResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_user_api_v1_domains_domain_users_user_get**
> DomainUserResp get_domain_user_api_v1_domains_domain_users_user_get(domain, user)

Get Domain User

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain
user = 'user_example' # str | 'me' or ObjectId of the user

try:
    # Get Domain User
    api_response = api_instance.get_domain_user_api_v1_domains_domain_users_user_get(domain, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->get_domain_user_api_v1_domains_domain_users_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 
 **user** | **str**| &#x27;me&#x27; or ObjectId of the user | 

### Return type

[**DomainUserResp**](DomainUserResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_domain_by_invitation_api_v1_domains_domain_join_post**
> DomainUserResp join_domain_by_invitation_api_v1_domains_domain_join_post(domain, invitation_code)

Join Domain By Invitation

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain
invitation_code = 'invitation_code_example' # str | 

try:
    # Join Domain By Invitation
    api_response = api_instance.join_domain_by_invitation_api_v1_domains_domain_join_post(domain, invitation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->join_domain_by_invitation_api_v1_domains_domain_join_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 
 **invitation_code** | **str**|  | 

### Return type

[**DomainUserResp**](DomainUserResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_roles_api_v1_domains_domain_roles_get**
> ListDomainRolesResp list_domain_roles_api_v1_domains_domain_roles_get(domain)

List Domain Roles

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain

try:
    # List Domain Roles
    api_response = api_instance.list_domain_roles_api_v1_domains_domain_roles_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->list_domain_roles_api_v1_domains_domain_roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 

### Return type

[**ListDomainRolesResp**](ListDomainRolesResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_users_api_v1_domains_domain_users_get**
> ListDomainUsersResp list_domain_users_api_v1_domains_domain_users_get(domain)

List Domain Users

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain

try:
    # List Domain Users
    api_response = api_instance.list_domain_users_api_v1_domains_domain_users_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->list_domain_users_api_v1_domains_domain_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 

### Return type

[**ListDomainUsersResp**](ListDomainUsersResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domains_api_v1_domains_get**
> ListDomainsResp list_domains_api_v1_domains_get(role=role, sort=sort, skip=skip, limit=limit)

List Domains

List all domains that the current user has a role.

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
role = ['role_example'] # list[str] |  (optional)
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # List Domains
    api_response = api_instance.list_domains_api_v1_domains_get(role=role, sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->list_domains_api_v1_domains_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**list[str]**](str.md)|  | [optional] 
 **sort** | [**SortEnum**](.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ListDomainsResp**](ListDomainsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domain_user_api_v1_domains_domain_users_user_delete**
> EmptyResp remove_domain_user_api_v1_domains_domain_users_user_delete(domain, user)

Remove Domain User

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain
user = 'user_example' # str | 'me' or ObjectId of the user

try:
    # Remove Domain User
    api_response = api_instance.remove_domain_user_api_v1_domains_domain_users_user_delete(domain, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->remove_domain_user_api_v1_domains_domain_users_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 
 **user** | **str**| &#x27;me&#x27; or ObjectId of the user | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_domain_api_v1_domains_domain_transfer_post**
> DomainResp transfer_domain_api_v1_domains_domain_transfer_post(body, domain)

Transfer Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.DomainTransfer() # DomainTransfer | 
domain = 'domain_example' # str | url or ObjectId of the domain

try:
    # Transfer Domain
    api_response = api_instance.transfer_domain_api_v1_domains_domain_transfer_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->transfer_domain_api_v1_domains_domain_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainTransfer**](DomainTransfer.md)|  | 
 **domain** | **str**| url or ObjectId of the domain | 

### Return type

[**DomainResp**](DomainResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_api_v1_domains_domain_patch**
> DomainResp update_domain_api_v1_domains_domain_patch(body, domain)

Update Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.DomainEdit() # DomainEdit | 
domain = 'domain_example' # str | url or ObjectId of the domain

try:
    # Update Domain
    api_response = api_instance.update_domain_api_v1_domains_domain_patch(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->update_domain_api_v1_domains_domain_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainEdit**](DomainEdit.md)|  | 
 **domain** | **str**| url or ObjectId of the domain | 

### Return type

[**DomainResp**](DomainResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch**
> DomainInvitationResp update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch(body, domain, invitation)

Update Domain Invitation

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.DomainInvitationEdit() # DomainInvitationEdit | 
domain = 'domain_example' # str | url or ObjectId of the domain
invitation = 'invitation_example' # str | ObjectId of the domain invitation

try:
    # Update Domain Invitation
    api_response = api_instance.update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch(body, domain, invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainInvitationEdit**](DomainInvitationEdit.md)|  | 
 **domain** | **str**| url or ObjectId of the domain | 
 **invitation** | **str**| ObjectId of the domain invitation | 

### Return type

[**DomainInvitationResp**](DomainInvitationResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_role_api_v1_domains_domain_roles_role_patch**
> DomainRoleResp update_domain_role_api_v1_domains_domain_roles_role_patch(body, domain, role)

Update Domain Role

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.DomainRoleEdit() # DomainRoleEdit | 
domain = 'domain_example' # str | url or ObjectId of the domain
role = 'role_example' # str | name of the domain role

try:
    # Update Domain Role
    api_response = api_instance.update_domain_role_api_v1_domains_domain_roles_role_patch(body, domain, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->update_domain_role_api_v1_domains_domain_roles_role_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRoleEdit**](DomainRoleEdit.md)|  | 
 **domain** | **str**| url or ObjectId of the domain | 
 **role** | **str**| name of the domain role | 

### Return type

[**DomainRoleResp**](DomainRoleResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_user_api_v1_domains_domain_users_user_patch**
> DomainUserResp update_domain_user_api_v1_domains_domain_users_user_patch(domain, user, body=body)

Update Domain User

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.DomainApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or ObjectId of the domain
user = 'user_example' # str | 'me' or ObjectId of the user
body = 'body_example' # str |  (optional)

try:
    # Update Domain User
    api_response = api_instance.update_domain_user_api_v1_domains_domain_users_user_patch(domain, user, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->update_domain_user_api_v1_domains_domain_users_user_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or ObjectId of the domain | 
 **user** | **str**| &#x27;me&#x27; or ObjectId of the user | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

[**DomainUserResp**](DomainUserResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

