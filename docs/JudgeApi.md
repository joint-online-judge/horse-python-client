# joj.horse_client.JudgeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_claim_record_by_judge**](JudgeApi.md#v1_claim_record_by_judge) | **POST** /judge/records/{record}/claim | Claim Record By Judge
[**v1_get_judge_key**](JudgeApi.md#v1_get_judge_key) | **GET** /judge/key | Get Judge Key
[**v1_submit_record_by_judge**](JudgeApi.md#v1_submit_record_by_judge) | **POST** /judge/records/{record}/judgment | Submit Record By Judge
[**v1_update_record_state_by_judge**](JudgeApi.md#v1_update_record_state_by_judge) | **POST** /judge/records/{record}/state | Update Record State By Judge

# **v1_claim_record_by_judge**
> JudgeClaimResp v1_claim_record_by_judge(record)

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
record = 'record_example' # str | 

try:
    # Claim Record By Judge
    api_response = api_instance.v1_claim_record_by_judge(record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_claim_record_by_judge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record** | **str**|  | 

### Return type

[**JudgeClaimResp**](JudgeClaimResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_judge_key**
> UserAccessKeyResp v1_get_judge_key()

Get Judge Key

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.JudgeApi(joj.horse_client.ApiClient(configuration))

try:
    # Get Judge Key
    api_response = api_instance.v1_get_judge_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_get_judge_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAccessKeyResp**](UserAccessKeyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_submit_record_by_judge**
> EmptyResp v1_submit_record_by_judge(body, record)

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
record = 'record_example' # str | 

try:
    # Submit Record By Judge
    api_response = api_instance.v1_submit_record_by_judge(body, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_submit_record_by_judge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordResult**](RecordResult.md)|  | 
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
> RecordResp v1_update_record_state_by_judge(record)

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
record = 'record_example' # str | 

try:
    # Update Record State By Judge
    api_response = api_instance.v1_update_record_state_by_judge(record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_update_record_state_by_judge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record** | **str**|  | 

### Return type

[**RecordResp**](RecordResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

