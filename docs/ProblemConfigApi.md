# joj.horse.client.ProblemConfigApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post**](ProblemConfigApi.md#commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post) | **POST** /api/v1/domains/{domain}/problems/{problem}/config/commit | Commit Problem Config
[**delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete**](ProblemConfigApi.md#delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete) | **DELETE** /api/v1/domains/{domain}/problems/{problem}/config/dirs/{path} | Delete Directory From Uncommitted Problem Config
[**delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete**](ProblemConfigApi.md#delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete) | **DELETE** /api/v1/domains/{domain}/problems/{problem}/config/files/{path} | Delete File From Uncommitted Problem Config
[**download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get**](ProblemConfigApi.md#download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/configs/{config}/files/{path} | Download File In Problem Config
[**download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get**](ProblemConfigApi.md#download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/config/files/{path} | Download File In Uncommitted Problem Config
[**download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get**](ProblemConfigApi.md#download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/configs/{config}/files | Download Problem Config Archive
[**download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get**](ProblemConfigApi.md#download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/config | Download Uncommitted Problem Config As Archive
[**get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get**](ProblemConfigApi.md#get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/config/file_info/{path} | Get File Or Directory Info In Uncommitted Problem Config
[**get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get**](ProblemConfigApi.md#get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/configs/{config} | Get Problem Config Json
[**reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post**](ProblemConfigApi.md#reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post) | **POST** /api/v1/domains/{domain}/problems/{problem}/config/reset | Reset Problem Config
[**update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put**](ProblemConfigApi.md#update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put) | **PUT** /api/v1/domains/{domain}/problems/{problem}/config | Update Problem Config By Archive
[**upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put**](ProblemConfigApi.md#upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put) | **PUT** /api/v1/domains/{domain}/problems/{problem}/config/files/{path} | Upload File To Problem Config
[**upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put**](ProblemConfigApi.md#upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put) | **PUT** /api/v1/domains/{domain}/problems/{problem}/config/files | Upload File To Root In Problem Config

# **commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post**
> ProblemConfigResp commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post(body, domain, problem)

Commit Problem Config

Commit all changes through upload / delete as a new problem config version.

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.ProblemConfigCommit() # ProblemConfigCommit | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Commit Problem Config
    api_response = api_instance.commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post(body, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProblemConfigCommit**](ProblemConfigCommit.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**ProblemConfigResp**](ProblemConfigResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete**
> FileInfoResp delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete(path, domain, problem, recursive=recursive)

Delete Directory From Uncommitted Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
recursive = false # bool | Act as -r in the rm command. If false, only empty directory can be deleted. (optional) (default to false)

try:
    # Delete Directory From Uncommitted Problem Config
    api_response = api_instance.delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete(path, domain, problem, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 
 **recursive** | **bool**| Act as -r in the rm command. If false, only empty directory can be deleted. | [optional] [default to false]

### Return type

[**FileInfoResp**](FileInfoResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete**
> FileInfoResp delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete(path, domain, problem)

Delete File From Uncommitted Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Delete File From Uncommitted Problem Config
    api_response = api_instance.delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete(path, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**FileInfoResp**](FileInfoResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get**
> object download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get(path, domain, problem, config)

Download File In Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
config = 'config_example' # str | 'latest' or id of the config

try:
    # Download File In Problem Config
    api_response = api_instance.download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get(path, domain, problem, config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 
 **config** | **str**| &#x27;latest&#x27; or id of the config | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get**
> object download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get(path, domain, problem)

Download File In Uncommitted Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Download File In Uncommitted Problem Config
    api_response = api_instance.download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get(path, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get**
> object download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get(domain, problem, config, archive_format=archive_format)

Download Problem Config Archive

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
config = 'config_example' # str | 'latest' or id of the config
archive_format = joj.horse.client.ArchiveFormat1() # ArchiveFormat1 |  (optional)

try:
    # Download Problem Config Archive
    api_response = api_instance.download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get(domain, problem, config, archive_format=archive_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 
 **config** | **str**| &#x27;latest&#x27; or id of the config | 
 **archive_format** | [**ArchiveFormat1**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get**
> EmptyResp download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get(domain, problem, archive_format=archive_format)

Download Uncommitted Problem Config As Archive

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
archive_format = joj.horse.client.ArchiveFormat() # ArchiveFormat |  (optional)

try:
    # Download Uncommitted Problem Config As Archive
    api_response = api_instance.download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get(domain, problem, archive_format=archive_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 
 **archive_format** | [**ArchiveFormat**](.md)|  | [optional] 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get**
> FileInfoResp get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get(path, domain, problem)

Get File Or Directory Info In Uncommitted Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Get File Or Directory Info In Uncommitted Problem Config
    api_response = api_instance.get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get(path, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**FileInfoResp**](FileInfoResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get**
> ProblemConfigResp get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get(domain, config, problem)

Get Problem Config Json

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
config = 'config_example' # str | 'latest' or id of the config
problem = 'problem_example' # str | url or id of the problem

try:
    # Get Problem Config Json
    api_response = api_instance.get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get(domain, config, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **config** | **str**| &#x27;latest&#x27; or id of the config | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**ProblemConfigResp**](ProblemConfigResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post**
> EmptyResp reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post(body, domain, problem)

Reset Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
body = joj.horse.client.LakeFSReset() # LakeFSReset | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Reset Problem Config
    api_response = api_instance.reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post(body, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LakeFSReset**](LakeFSReset.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put**
> EmptyResp update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put(file, domain, problem)

Update Problem Config By Archive

Completely replace the problem config with the archive. This will delete files not included in the archive.

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
file = 'file_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Update Problem Config By Archive
    api_response = api_instance.update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put(file, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put**
> FileInfoResp upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put(file, domain, problem, path)

Upload File To Problem Config

Replace the file with the same path. Create directories if needed along the path.

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
file = 'file_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
path = 'path_example' # str | 

try:
    # Upload File To Problem Config
    api_response = api_instance.upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put(file, domain, problem, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 
 **path** | **str**|  | 

### Return type

[**FileInfoResp**](FileInfoResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put**
> FileInfoResp upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put(file, domain, problem)

Upload File To Root In Problem Config

Use the filename as path, file will be uploaded to root of the problem config directory.

### Example
```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.ProblemConfigApi(joj.horse.client.ApiClient(configuration))
file = 'file_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Upload File To Root In Problem Config
    api_response = api_instance.upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put(file, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **domain** | **str**| url or id of the domain | 
 **problem** | **str**| url or id of the problem | 

### Return type

[**FileInfoResp**](FileInfoResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

