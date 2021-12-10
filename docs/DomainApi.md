# joj.horse_client.DomainApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_add_domain_user**](DomainApi.md#v1_add_domain_user) | **POST** /domains/{domain}/users | Add Domain User
[**v1_create_domain**](DomainApi.md#v1_create_domain) | **POST** /domains | Create Domain
[**v1_create_domain_invitation**](DomainApi.md#v1_create_domain_invitation) | **POST** /domains/{domain}/invitations | Create Domain Invitation
[**v1_create_domain_role**](DomainApi.md#v1_create_domain_role) | **POST** /domains/{domain}/roles | Create Domain Role
[**v1_delete_domain**](DomainApi.md#v1_delete_domain) | **DELETE** /domains/{domain} | Delete Domain
[**v1_delete_domain_invitation**](DomainApi.md#v1_delete_domain_invitation) | **DELETE** /domains/{domain}/invitations/{invitation} | Delete Domain Invitation
[**v1_delete_domain_role**](DomainApi.md#v1_delete_domain_role) | **DELETE** /domains/{domain}/roles/{role} | Delete Domain Role
[**v1_get_domain**](DomainApi.md#v1_get_domain) | **GET** /domains/{domain} | Get Domain
[**v1_get_domain_invitation**](DomainApi.md#v1_get_domain_invitation) | **GET** /domains/{domain}/invitations/{invitation} | Get Domain Invitation
[**v1_get_domain_role**](DomainApi.md#v1_get_domain_role) | **GET** /domains/{domain}/roles/{role} | Get Domain Role
[**v1_get_domain_user**](DomainApi.md#v1_get_domain_user) | **GET** /domains/{domain}/users/{user} | Get Domain User
[**v1_get_domain_user_permission**](DomainApi.md#v1_get_domain_user_permission) | **GET** /domains/{domain}/users/{user}/permission | Get Domain User Permission
[**v1_join_domain_by_invitation**](DomainApi.md#v1_join_domain_by_invitation) | **POST** /domains/{domain}/join | Join Domain By Invitation
[**v1_list_domain_invitations**](DomainApi.md#v1_list_domain_invitations) | **GET** /domains/{domain}/invitations | List Domain Invitations
[**v1_list_domain_roles**](DomainApi.md#v1_list_domain_roles) | **GET** /domains/{domain}/roles | List Domain Roles
[**v1_list_domain_users**](DomainApi.md#v1_list_domain_users) | **GET** /domains/{domain}/users | List Domain Users
[**v1_list_domains**](DomainApi.md#v1_list_domains) | **GET** /domains | List Domains
[**v1_remove_domain_user**](DomainApi.md#v1_remove_domain_user) | **DELETE** /domains/{domain}/users/{user} | Remove Domain User
[**v1_search_domain_candidates**](DomainApi.md#v1_search_domain_candidates) | **GET** /domains/{domain}/candidates | Search Domain Candidates
[**v1_transfer_domain**](DomainApi.md#v1_transfer_domain) | **POST** /domains/{domain}/transfer | Transfer Domain
[**v1_update_domain**](DomainApi.md#v1_update_domain) | **PATCH** /domains/{domain} | Update Domain
[**v1_update_domain_invitation**](DomainApi.md#v1_update_domain_invitation) | **PATCH** /domains/{domain}/invitations/{invitation} | Update Domain Invitation
[**v1_update_domain_role**](DomainApi.md#v1_update_domain_role) | **PATCH** /domains/{domain}/roles/{role} | Update Domain Role
[**v1_update_domain_user**](DomainApi.md#v1_update_domain_user) | **PATCH** /domains/{domain}/users/{user} | Update Domain User

# **v1_add_domain_user**
> UserWithDomainRoleResp v1_add_domain_user(body, domain)

Add Domain User

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.DomainUserAdd() # DomainUserAdd | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Add Domain User
    api_response = api_instance.v1_add_domain_user(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_add_domain_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainUserAdd**](DomainUserAdd.md)|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**UserWithDomainRoleResp**](UserWithDomainRoleResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_domain**
> DomainResp v1_create_domain(body)

Create Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.DomainCreate() # DomainCreate | 

try:
    # Create Domain
    api_response = api_instance.v1_create_domain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_create_domain: %s\n" % e)
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

# **v1_create_domain_invitation**
> DomainInvitationResp v1_create_domain_invitation(body, domain)

Create Domain Invitation

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.DomainInvitationCreate() # DomainInvitationCreate | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Create Domain Invitation
    api_response = api_instance.v1_create_domain_invitation(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_create_domain_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainInvitationCreate**](DomainInvitationCreate.md)|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**DomainInvitationResp**](DomainInvitationResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_domain_role**
> DomainRoleResp v1_create_domain_role(body, domain)

Create Domain Role

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.DomainRoleCreate() # DomainRoleCreate | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Create Domain Role
    api_response = api_instance.v1_create_domain_role(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_create_domain_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRoleCreate**](DomainRoleCreate.md)|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**DomainRoleResp**](DomainRoleResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_domain**
> EmptyResp v1_delete_domain(domain)

Delete Domain

TODO: finish this part  tc-imba: delete domain have many side effects, and is not urgent,          marked it deprecated and implement it later

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain

try:
    # Delete Domain
    api_response = api_instance.v1_delete_domain(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_delete_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_domain_invitation**
> EmptyResp v1_delete_domain_invitation(domain, invitation)

Delete Domain Invitation

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
invitation = 'invitation_example' # str | url or id of the domain invitation

try:
    # Delete Domain Invitation
    api_response = api_instance.v1_delete_domain_invitation(domain, invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_delete_domain_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **invitation** | **str**| url or id of the domain invitation | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_domain_role**
> EmptyResp v1_delete_domain_role(domain, role)

Delete Domain Role

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
role = 'role_example' # str | name of the domain role

try:
    # Delete Domain Role
    api_response = api_instance.v1_delete_domain_role(domain, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_delete_domain_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **role** | **str**| name of the domain role | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_domain**
> DomainDetailResp v1_get_domain(domain)

Get Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain

try:
    # Get Domain
    api_response = api_instance.v1_get_domain(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_get_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 

### Return type

[**DomainDetailResp**](DomainDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_domain_invitation**
> DomainInvitationResp v1_get_domain_invitation(domain, invitation)

Get Domain Invitation

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
invitation = 'invitation_example' # str | url or id of the domain invitation

try:
    # Get Domain Invitation
    api_response = api_instance.v1_get_domain_invitation(domain, invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_get_domain_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **invitation** | **str**| url or id of the domain invitation | 

### Return type

[**DomainInvitationResp**](DomainInvitationResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_domain_role**
> DomainRoleDetailResp v1_get_domain_role(domain, role)

Get Domain Role

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
role = 'role_example' # str | name of the domain role

try:
    # Get Domain Role
    api_response = api_instance.v1_get_domain_role(domain, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_get_domain_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **role** | **str**| name of the domain role | 

### Return type

[**DomainRoleDetailResp**](DomainRoleDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_domain_user**
> UserWithDomainRoleResp v1_get_domain_user(domain, user)

Get Domain User

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
user = 'user_example' # str | user id or 'me' or empty

try:
    # Get Domain User
    api_response = api_instance.v1_get_domain_user(domain, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_get_domain_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **user** | **str**| user id or &#x27;me&#x27; or empty | 

### Return type

[**UserWithDomainRoleResp**](UserWithDomainRoleResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_domain_user_permission**
> DomainUserPermissionResp v1_get_domain_user_permission(domain, user)

Get Domain User Permission

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
user = 'user_example' # str | user id or 'me' or empty

try:
    # Get Domain User Permission
    api_response = api_instance.v1_get_domain_user_permission(domain, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_get_domain_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **user** | **str**| user id or &#x27;me&#x27; or empty | 

### Return type

[**DomainUserPermissionResp**](DomainUserPermissionResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_join_domain_by_invitation**
> UserWithDomainRoleResp v1_join_domain_by_invitation(domain, invitation_code)

Join Domain By Invitation

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
invitation_code = 'invitation_code_example' # str | 

try:
    # Join Domain By Invitation
    api_response = api_instance.v1_join_domain_by_invitation(domain, invitation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_join_domain_by_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **invitation_code** | **str**|  | 

### Return type

[**UserWithDomainRoleResp**](UserWithDomainRoleResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_domain_invitations**
> DomainInvitationListResp v1_list_domain_invitations(domain)

List Domain Invitations

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain

try:
    # List Domain Invitations
    api_response = api_instance.v1_list_domain_invitations(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_list_domain_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 

### Return type

[**DomainInvitationListResp**](DomainInvitationListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_domain_roles**
> DomainRoleListResp v1_list_domain_roles(domain)

List Domain Roles

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain

try:
    # List Domain Roles
    api_response = api_instance.v1_list_domain_roles(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_list_domain_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 

### Return type

[**DomainRoleListResp**](DomainRoleListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_domain_users**
> UserWithDomainRoleListResp v1_list_domain_users(domain, ordering=ordering, offset=offset, limit=limit)

List Domain Users

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Domain Users
    api_response = api_instance.v1_list_domain_users(domain, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_list_domain_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**UserWithDomainRoleListResp**](UserWithDomainRoleListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_domains**
> DomainListResp v1_list_domains(role=role, ordering=ordering, offset=offset, limit=limit)

List Domains

List all domains that the current user has a role.

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
role = ['role_example'] # list[str] |  (optional)
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Domains
    api_response = api_instance.v1_list_domains(role=role, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_list_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **v1_remove_domain_user**
> EmptyResp v1_remove_domain_user(domain, user)

Remove Domain User

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
user = 'user_example' # str | user id or 'me' or empty

try:
    # Remove Domain User
    api_response = api_instance.v1_remove_domain_user(domain, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_remove_domain_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **user** | **str**| user id or &#x27;me&#x27; or empty | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_search_domain_candidates**
> UserWithDomainRoleListResp v1_search_domain_candidates(domain, query, ordering=ordering)

Search Domain Candidates

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
query = 'query_example' # str | search query
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: username (optional)

try:
    # Search Domain Candidates
    api_response = api_instance.v1_search_domain_candidates(domain, query, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_search_domain_candidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **query** | **str**| search query | 
 **ordering** | **str**| Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: username | [optional] 

### Return type

[**UserWithDomainRoleListResp**](UserWithDomainRoleListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfer_domain**
> DomainResp v1_transfer_domain(body, domain)

Transfer Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.DomainTransfer() # DomainTransfer | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Transfer Domain
    api_response = api_instance.v1_transfer_domain(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_transfer_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainTransfer**](DomainTransfer.md)|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**DomainResp**](DomainResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_domain**
> DomainResp v1_update_domain(body, domain)

Update Domain

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.DomainEdit() # DomainEdit | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Update Domain
    api_response = api_instance.v1_update_domain(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_update_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainEdit**](DomainEdit.md)|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**DomainResp**](DomainResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_domain_invitation**
> DomainInvitationResp v1_update_domain_invitation(body, domain, invitation)

Update Domain Invitation

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.DomainInvitationEdit() # DomainInvitationEdit | 
domain = 'domain_example' # str | url or id of the domain
invitation = 'invitation_example' # str | url or id of the domain invitation

try:
    # Update Domain Invitation
    api_response = api_instance.v1_update_domain_invitation(body, domain, invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_update_domain_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainInvitationEdit**](DomainInvitationEdit.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **invitation** | **str**| url or id of the domain invitation | 

### Return type

[**DomainInvitationResp**](DomainInvitationResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_domain_role**
> DomainRoleResp v1_update_domain_role(body, domain, role)

Update Domain Role

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.DomainRoleEdit() # DomainRoleEdit | 
domain = 'domain_example' # str | url or id of the domain
role = 'role_example' # str | name of the domain role

try:
    # Update Domain Role
    api_response = api_instance.v1_update_domain_role(body, domain, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_update_domain_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRoleEdit**](DomainRoleEdit.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **role** | **str**| name of the domain role | 

### Return type

[**DomainRoleResp**](DomainRoleResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_domain_user**
> UserWithDomainRoleResp v1_update_domain_user(body, domain, user)

Update Domain User

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.DomainApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.DomainUserUpdate() # DomainUserUpdate | 
domain = 'domain_example' # str | url or id of the domain
user = 'user_example' # str | user id or 'me' or empty

try:
    # Update Domain User
    api_response = api_instance.v1_update_domain_user(body, domain, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->v1_update_domain_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainUserUpdate**](DomainUserUpdate.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **user** | **str**| user id or &#x27;me&#x27; or empty | 

### Return type

[**UserWithDomainRoleResp**](UserWithDomainRoleResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

