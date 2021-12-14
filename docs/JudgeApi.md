# joj.horse_client.JudgeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_claim_record_by_judge**](JudgeApi.md#v1_claim_record_by_judge) | **POST** /judge/records/{record}/claim | Claim Record By Judge
[**v1_submit_record_by_judge**](JudgeApi.md#v1_submit_record_by_judge) | **POST** /judge/records/{record}/judgment | Submit Record By Judge
[**v1_update_record_state_by_judge**](JudgeApi.md#v1_update_record_state_by_judge) | **POST** /judge/records/{record}/state | Update Record State By Judge

# **v1_claim_record_by_judge**
> JudgeCredentialsResp v1_claim_record_by_judge(body, domain, record)

Claim Record By Judge

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.JudgeApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.JudgeClaim() # JudgeClaim | 
domain = 'domain_example' # str | url or id of the domain
record = 'record_example' # str | 

try:
    # Claim Record By Judge
    api_response = api_instance.v1_claim_record_by_judge(body, domain, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_claim_record_by_judge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JudgeClaim**](JudgeClaim.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **record** | **str**|  | 

### Return type

[**JudgeCredentialsResp**](JudgeCredentialsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_submit_record_by_judge**
> EmptyResp v1_submit_record_by_judge(body, domain, record)

Submit Record By Judge

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.JudgeApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.RecordResult() # RecordResult | 
domain = 'domain_example' # str | url or id of the domain
record = 'record_example' # str | 

try:
    # Submit Record By Judge
    api_response = api_instance.v1_submit_record_by_judge(body, domain, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_submit_record_by_judge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordResult**](RecordResult.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **record** | **str**|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_record_state_by_judge**
> RecordResp v1_update_record_state_by_judge(domain, record)

Update Record State By Judge

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.JudgeApi(joj.horse_client.ApiClient(configuration))
domain = 'domain_example' # str | url or id of the domain
record = 'record_example' # str | 

try:
    # Update Record State By Judge
    api_response = api_instance.v1_update_record_state_by_judge(domain, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_update_record_state_by_judge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| url or id of the domain | 
 **record** | **str**|  | 

### Return type

[**RecordResp**](RecordResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

