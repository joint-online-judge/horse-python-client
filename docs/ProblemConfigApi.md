# joj.horse_client.ProblemConfigApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_diff_problem_config_default_branch**](ProblemConfigApi.md#v1_diff_problem_config_default_branch) | **GET** /domains/{domain}/problems/{problem}/configs/latest/diff | Diff Problem Config Default Branch
[**v1_download_problem_config_archive**](ProblemConfigApi.md#v1_download_problem_config_archive) | **GET** /domains/{domain}/problems/{problem}/configs/{config} | Download Problem Config Archive
[**v1_get_problem_config_json**](ProblemConfigApi.md#v1_get_problem_config_json) | **GET** /domains/{domain}/problems/{problem}/configs/{config}/json | Get Problem Config Json
[**v1_list_latest_problem_config_objects_under_a_given_prefix**](ProblemConfigApi.md#v1_list_latest_problem_config_objects_under_a_given_prefix) | **GET** /domains/{domain}/problems/{problem}/configs/latest/ls | List Latest Problem Config Objects Under A Given Prefix
[**v1_list_problem_config_commits**](ProblemConfigApi.md#v1_list_problem_config_commits) | **GET** /domains/{domain}/problems/{problem}/configs | List Problem Config Commits
[**v1_update_problem_config_by_archive**](ProblemConfigApi.md#v1_update_problem_config_by_archive) | **POST** /domains/{domain}/problems/{problem}/configs | Update Problem Config By Archive
[**v1_update_problem_config_json**](ProblemConfigApi.md#v1_update_problem_config_json) | **POST** /domains/{domain}/problems/{problem}/configs/json | Update Problem Config Json

# **v1_diff_problem_config_default_branch**
> DiffListResp v1_diff_problem_config_default_branch(domain, problem, after=after, amount=amount, delimiter=delimiter, prefix=prefix)

Diff Problem Config Default Branch

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
after = '' # str | return items after this value (optional)
amount = 100 # int | how many items to return (optional) (default to 100)
delimiter = '' # str | delimiter used to group common prefixes by (optional)
prefix = '' # str | return items prefixed with this value (optional)

try:
    # Diff Problem Config Default Branch
    api_response = api_instance.v1_diff_problem_config_default_branch(domain, problem, after=after, amount=amount, delimiter=delimiter, prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_diff_problem_config_default_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 
 **after** | **str**| return items after this value | [optional] 
 **amount** | **int**| how many items to return | [optional] [default to 100]
 **delimiter** | **str**| delimiter used to group common prefixes by | [optional] 
 **prefix** | **str**| return items prefixed with this value | [optional] 

### Return type

[**DiffListResp**](DiffListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_download_problem_config_archive**
> object v1_download_problem_config_archive(domain, problem, config, archive_format=archive_format)

Download Problem Config Archive

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
config = 'config_example' # str | 'latest' or id of the config
archive_format = joj.horse_client.ArchiveFormat() # ArchiveFormat |  (optional)

try:
    # Download Problem Config Archive
    api_response = api_instance.v1_download_problem_config_archive(domain, problem, config, archive_format=archive_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_download_problem_config_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 
 **config** | **str**| &#x27;latest&#x27; or id of the config | 
 **archive_format** | [**ArchiveFormat**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_problem_config_json**
> ProblemConfigDataDetailResp v1_get_problem_config_json(domain, config, problem)

Get Problem Config Json

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
config = 'config_example' # str | 'latest' or id of the config
problem = 'problem_example' # str | url or id of the problem

try:
    # Get Problem Config Json
    api_response = api_instance.v1_get_problem_config_json(domain, config, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_get_problem_config_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **config** | **str**| &#x27;latest&#x27; or id of the config | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**ProblemConfigDataDetailResp**](ProblemConfigDataDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_latest_problem_config_objects_under_a_given_prefix**
> ObjectStatsListResp v1_list_latest_problem_config_objects_under_a_given_prefix(domain, problem, after=after, amount=amount, delimiter=delimiter, prefix=prefix)

List Latest Problem Config Objects Under A Given Prefix

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
after = '' # str | return items after this value (optional)
amount = 100 # int | how many items to return (optional) (default to 100)
delimiter = '' # str | delimiter used to group common prefixes by (optional)
prefix = '' # str | return items prefixed with this value (optional)

try:
    # List Latest Problem Config Objects Under A Given Prefix
    api_response = api_instance.v1_list_latest_problem_config_objects_under_a_given_prefix(domain, problem, after=after, amount=amount, delimiter=delimiter, prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_list_latest_problem_config_objects_under_a_given_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 
 **after** | **str**| return items after this value | [optional] 
 **amount** | **int**| how many items to return | [optional] [default to 100]
 **delimiter** | **str**| delimiter used to group common prefixes by | [optional] 
 **prefix** | **str**| return items prefixed with this value | [optional] 

### Return type

[**ObjectStatsListResp**](ObjectStatsListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_problem_config_commits**
> ProblemConfigDetailListResp v1_list_problem_config_commits(domain, problem, ordering=ordering, offset=offset, limit=limit)

List Problem Config Commits

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
ordering = '' # str | Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Problem Config Commits
    api_response = api_instance.v1_list_problem_config_commits(domain, problem, ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_list_problem_config_commits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 
 **ordering** | **str**| Comma separated list of ordering the results. You may specify reverse orderings by prefixing the field name with &#x27;-&#x27;.  Available fields: created_at,updated_at | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ProblemConfigDetailListResp**](ProblemConfigDetailListResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_problem_config_by_archive**
> ProblemConfigDetailResp v1_update_problem_config_by_archive(file, problem, domain)

Update Problem Config By Archive

Completely replace the problem config with the archive. This will delete files not included in the archive.

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
file = 'file_example' # str | 
problem = 'problem_example' # str | url or id of the problem
domain = 'domain_example' # str | url or id of the domain

try:
    # Update Problem Config By Archive
    api_response = api_instance.v1_update_problem_config_by_archive(file, problem, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_update_problem_config_by_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **problem** | **str**| url or id of the problem | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**ProblemConfigDetailResp**](ProblemConfigDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_problem_config_json**
> ProblemConfigDetailResp v1_update_problem_config_json(body, problem, domain)

Update Problem Config Json

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.ProblemConfigJson() # ProblemConfigJson | 
problem = 'problem_example' # str | url or id of the problem
domain = 'domain_example' # str | url or id of the domain

try:
    # Update Problem Config Json
    api_response = api_instance.v1_update_problem_config_json(body, problem, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_update_problem_config_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemConfigJson**](ProblemConfigJson.md)|  | 
 **problem** | **str**| url or id of the problem | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**ProblemConfigDetailResp**](ProblemConfigDetailResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

