# joj.horse_client.JudgeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_claim_record_by_judger**](JudgeApi.md#v1_claim_record_by_judger) | **POST** /domains/{domain}/records/{record}/judge/claim | Claim Record By Judger
[**v1_submit_case_by_judger**](JudgeApi.md#v1_submit_case_by_judger) | **PUT** /domains/{domain}/records/{record}/cases/{case}/judge | Submit Case By Judger
[**v1_submit_record_by_judger**](JudgeApi.md#v1_submit_record_by_judger) | **PUT** /domains/{domain}/records/{record}/judge | Submit Record By Judger

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

# **v1_submit_case_by_judger**
> EmptyResp v1_submit_case_by_judger(body, case, record, domain)

Submit Case By Judger

### Example
```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.JudgeApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.RecordCaseSubmit() # RecordCaseSubmit | 
case = 56 # int | 
record = 'record_example' # str | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Submit Case By Judger
    api_response = api_instance.v1_submit_case_by_judger(body, case, record, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_submit_case_by_judger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordCaseSubmit**](RecordCaseSubmit.md)|  | 
 **case** | **int**|  | 
 **record** | **str**|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_submit_record_by_judger**
> EmptyResp v1_submit_record_by_judger(body, record, domain)

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
body = joj.horse_client.RecordSubmit() # RecordSubmit | 
record = 'record_example' # str | 
domain = 'domain_example' # str | url or id of the domain

try:
    # Submit Record By Judger
    api_response = api_instance.v1_submit_record_by_judger(body, record, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JudgeApi->v1_submit_record_by_judger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordSubmit**](RecordSubmit.md)|  | 
 **record** | **str**|  | 
 **domain** | **str**| url or id of the domain | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

