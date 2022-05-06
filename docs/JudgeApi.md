# joj.horse_client.JudgeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_claim_record_by_judger**](JudgeApi.md#v1_claim_record_by_judger) | **POST** /domains/{domain}/records/{record}/judge/claim | Claim Record By Judger
[**v1_submit_record_by_judger**](JudgeApi.md#v1_submit_record_by_judger) | **POST** /domains/{domain}/records/{record}/judge/judgment | Submit Record By Judger
[**v1_update_record_state_by_judger**](JudgeApi.md#v1_update_record_state_by_judger) | **POST** /domains/{domain}/records/{record}/judge/state | Update Record State By Judger

# **v1_claim_record_by_judger**
> JudgerCredentialsResp v1_claim_record_by_judger(body, domain, record)

Claim Record By Judger

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.JudgeApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.JudgerClaim() # JudgerClaim | 
domain = 'domain_example' # str | url or id of the domain
record = 'record_example' # str | 

try:
    # Claim Record By Judger
    api_response = api_instance.v1_claim_record_by_judger(body, domain, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_claim_record_by_judger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JudgerClaim**](JudgerClaim.md)|  | 
 **domain** | **str**| url or id of the domain | 
 **record** | **str**|  | 

### Return type

[**JudgerCredentialsResp**](JudgerCredentialsResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_submit_record_by_judger**
> EmptyResp v1_submit_record_by_judger(body, domain, record)

Submit Record By Judger

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
    # Submit Record By Judger
    api_response = api_instance.v1_submit_record_by_judger(body, domain, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_submit_record_by_judger: %s\n" % e)
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

# **v1_update_record_state_by_judger**
> RecordResp v1_update_record_state_by_judger(domain, record)

Update Record State By Judger

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
    # Update Record State By Judger
    api_response = api_instance.v1_update_record_state_by_judger(domain, record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_update_record_state_by_judger: %s\n" % e)
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

