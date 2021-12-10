# joj.horse_client.ProblemConfigApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_commit_problem_config**](ProblemConfigApi.md#v1_commit_problem_config) | **POST** /domains/{domain}/problems/{problem}/config/commit | Commit Problem Config
[**v1_delete_directory_from_uncommitted_problem_config**](ProblemConfigApi.md#v1_delete_directory_from_uncommitted_problem_config) | **DELETE** /domains/{domain}/problems/{problem}/config/dirs/{path} | Delete Directory From Uncommitted Problem Config
[**v1_delete_file_from_uncommitted_problem_config**](ProblemConfigApi.md#v1_delete_file_from_uncommitted_problem_config) | **DELETE** /domains/{domain}/problems/{problem}/config/files/{path} | Delete File From Uncommitted Problem Config
[**v1_download_file_in_problem_config**](ProblemConfigApi.md#v1_download_file_in_problem_config) | **GET** /domains/{domain}/problems/{problem}/configs/{config}/files/{path} | Download File In Problem Config
[**v1_download_file_in_uncommitted_problem_config**](ProblemConfigApi.md#v1_download_file_in_uncommitted_problem_config) | **GET** /domains/{domain}/problems/{problem}/config/files/{path} | Download File In Uncommitted Problem Config
[**v1_download_problem_config_archive**](ProblemConfigApi.md#v1_download_problem_config_archive) | **GET** /domains/{domain}/problems/{problem}/configs/{config}/files | Download Problem Config Archive
[**v1_download_uncommitted_problem_config_as_archive**](ProblemConfigApi.md#v1_download_uncommitted_problem_config_as_archive) | **GET** /domains/{domain}/problems/{problem}/config | Download Uncommitted Problem Config As Archive
[**v1_get_file_or_directory_info_in_uncommitted_problem_config**](ProblemConfigApi.md#v1_get_file_or_directory_info_in_uncommitted_problem_config) | **GET** /domains/{domain}/problems/{problem}/config/file_info/{path} | Get File Or Directory Info In Uncommitted Problem Config
[**v1_get_problem_config_json**](ProblemConfigApi.md#v1_get_problem_config_json) | **GET** /domains/{domain}/problems/{problem}/configs/{config} | Get Problem Config Json
[**v1_reset_problem_config**](ProblemConfigApi.md#v1_reset_problem_config) | **POST** /domains/{domain}/problems/{problem}/config/reset | Reset Problem Config
[**v1_update_problem_config_by_archive**](ProblemConfigApi.md#v1_update_problem_config_by_archive) | **PUT** /domains/{domain}/problems/{problem}/config | Update Problem Config By Archive
[**v1_upload_file_to_problem_config**](ProblemConfigApi.md#v1_upload_file_to_problem_config) | **PUT** /domains/{domain}/problems/{problem}/config/files/{path} | Upload File To Problem Config
[**v1_upload_file_to_root_in_problem_config**](ProblemConfigApi.md#v1_upload_file_to_root_in_problem_config) | **PUT** /domains/{domain}/problems/{problem}/config/files | Upload File To Root In Problem Config

# **v1_commit_problem_config**
> ProblemConfigResp v1_commit_problem_config(body, domain, problem)

Commit Problem Config

Commit all changes through upload / delete as a new problem config version.

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.ProblemConfigCommit() # ProblemConfigCommit | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Commit Problem Config
    api_response = api_instance.v1_commit_problem_config(body, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_commit_problem_config: %s\n" % e)
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

# **v1_delete_directory_from_uncommitted_problem_config**
> FileInfoResp v1_delete_directory_from_uncommitted_problem_config(path, domain, problem, recursive=recursive)

Delete Directory From Uncommitted Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
recursive = false # bool | Act as -r in the rm command. If false, only empty directory can be deleted. (optional) (default to false)

try:
    # Delete Directory From Uncommitted Problem Config
    api_response = api_instance.v1_delete_directory_from_uncommitted_problem_config(path, domain, problem, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_delete_directory_from_uncommitted_problem_config: %s\n" % e)
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

# **v1_delete_file_from_uncommitted_problem_config**
> FileInfoResp v1_delete_file_from_uncommitted_problem_config(path, domain, problem)

Delete File From Uncommitted Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Delete File From Uncommitted Problem Config
    api_response = api_instance.v1_delete_file_from_uncommitted_problem_config(path, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_delete_file_from_uncommitted_problem_config: %s\n" % e)
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

# **v1_download_file_in_problem_config**
> object v1_download_file_in_problem_config(path, domain, problem, config)

Download File In Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
config = 'config_example' # str | 'latest' or id of the config

try:
    # Download File In Problem Config
    api_response = api_instance.v1_download_file_in_problem_config(path, domain, problem, config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_download_file_in_problem_config: %s\n" % e)
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

# **v1_download_file_in_uncommitted_problem_config**
> object v1_download_file_in_uncommitted_problem_config(path, domain, problem)

Download File In Uncommitted Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Download File In Uncommitted Problem Config
    api_response = api_instance.v1_download_file_in_uncommitted_problem_config(path, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_download_file_in_uncommitted_problem_config: %s\n" % e)
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
archive_format = joj.horse_client.ArchiveFormat1() # ArchiveFormat1 |  (optional)

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
 **archive_format** | [**ArchiveFormat1**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_download_uncommitted_problem_config_as_archive**
> EmptyResp v1_download_uncommitted_problem_config_as_archive(domain, problem, archive_format=archive_format)

Download Uncommitted Problem Config As Archive

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
archive_format = joj.horse_client.ArchiveFormat() # ArchiveFormat |  (optional)

try:
    # Download Uncommitted Problem Config As Archive
    api_response = api_instance.v1_download_uncommitted_problem_config_as_archive(domain, problem, archive_format=archive_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_download_uncommitted_problem_config_as_archive: %s\n" % e)
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

# **v1_get_file_or_directory_info_in_uncommitted_problem_config**
> FileInfoResp v1_get_file_or_directory_info_in_uncommitted_problem_config(path, domain, problem)

Get File Or Directory Info In Uncommitted Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
path = 'path_example' # str | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Get File Or Directory Info In Uncommitted Problem Config
    api_response = api_instance.v1_get_file_or_directory_info_in_uncommitted_problem_config(path, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_get_file_or_directory_info_in_uncommitted_problem_config: %s\n" % e)
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

# **v1_get_problem_config_json**
> ProblemConfigResp v1_get_problem_config_json(domain, config, problem)

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

[**ProblemConfigResp**](ProblemConfigResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_reset_problem_config**
> EmptyResp v1_reset_problem_config(body, domain, problem)

Reset Problem Config

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.ProblemConfigApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.LakeFSReset() # LakeFSReset | 
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Reset Problem Config
    api_response = api_instance.v1_reset_problem_config(body, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_reset_problem_config: %s\n" % e)
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

# **v1_update_problem_config_by_archive**
> EmptyResp v1_update_problem_config_by_archive(file, domain, problem)

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
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Update Problem Config By Archive
    api_response = api_instance.v1_update_problem_config_by_archive(file, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_update_problem_config_by_archive: %s\n" % e)
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

# **v1_upload_file_to_problem_config**
> FileInfoResp v1_upload_file_to_problem_config(file, domain, problem, path)

Upload File To Problem Config

Replace the file with the same path. Create directories if needed along the path.

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
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem
path = 'path_example' # str | 

try:
    # Upload File To Problem Config
    api_response = api_instance.v1_upload_file_to_problem_config(file, domain, problem, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_upload_file_to_problem_config: %s\n" % e)
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

# **v1_upload_file_to_root_in_problem_config**
> FileInfoResp v1_upload_file_to_root_in_problem_config(file, domain, problem)

Upload File To Root In Problem Config

Use the filename as path, file will be uploaded to root of the problem config directory.

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
domain = 'domain_example' # str | url or id of the domain
problem = 'problem_example' # str | url or id of the problem

try:
    # Upload File To Root In Problem Config
    api_response = api_instance.v1_upload_file_to_root_in_problem_config(file, domain, problem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemConfigApi->v1_upload_file_to_root_in_problem_config: %s\n" % e)
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

