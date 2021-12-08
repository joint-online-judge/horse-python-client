# joj.horse_client.JudgeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_record_by_judge_api_v1_judge_records_record_claim_post**](JudgeApi.md#claim_record_by_judge_api_v1_judge_records_record_claim_post) | **POST** /api/v1/judge/records/{record}/claim | Claim Record By Judge
[**get_judge_key_api_v1_judge_key_get**](JudgeApi.md#get_judge_key_api_v1_judge_key_get) | **GET** /api/v1/judge/key | Get Judge Key
[**submit_record_by_judge_api_v1_judge_records_record_judgment_post**](JudgeApi.md#submit_record_by_judge_api_v1_judge_records_record_judgment_post) | **POST** /api/v1/judge/records/{record}/judgment | Submit Record By Judge
[**update_record_state_by_judge_api_v1_judge_records_record_state_post**](JudgeApi.md#update_record_state_by_judge_api_v1_judge_records_record_state_post) | **POST** /api/v1/judge/records/{record}/state | Update Record State By Judge

# **claim_record_by_judge_api_v1_judge_records_record_claim_post**
> JudgeClaimResp claim_record_by_judge_api_v1_judge_records_record_claim_post(record)

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
    api_response = api_instance.claim_record_by_judge_api_v1_judge_records_record_claim_post(record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->claim_record_by_judge_api_v1_judge_records_record_claim_post: %s\n" % e)
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

# **get_judge_key_api_v1_judge_key_get**
> UserAccessKeyResp get_judge_key_api_v1_judge_key_get()

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
    api_response = api_instance.get_judge_key_api_v1_judge_key_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->get_judge_key_api_v1_judge_key_get: %s\n" % e)
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

# **submit_record_by_judge_api_v1_judge_records_record_judgment_post**
> EmptyResp submit_record_by_judge_api_v1_judge_records_record_judgment_post(body, record)

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
    api_response = api_instance.submit_record_by_judge_api_v1_judge_records_record_judgment_post(body, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->submit_record_by_judge_api_v1_judge_records_record_judgment_post: %s\n" % e)
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

# **update_record_state_by_judge_api_v1_judge_records_record_state_post**
> RecordResp update_record_state_by_judge_api_v1_judge_records_record_state_post(record)

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
    api_response = api_instance.update_record_state_by_judge_api_v1_judge_records_record_state_post(record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->update_record_state_by_judge_api_v1_judge_records_record_state_post: %s\n" % e)
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

