# Record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | [**AllOfRecordStatus**](AllOfRecordStatus.md) |  | [optional] 
**score** | **int** |  | [optional] [default to 0]
**time_ms** | **int** |  | [optional] [default to 0]
**memory_kb** | **int** |  | [optional] [default to 0]
**domain** | [**AnyOfRecordDomain**](AnyOfRecordDomain.md) |  | 
**problem** | [**AnyOfRecordProblem**](AnyOfRecordProblem.md) |  | 
**problem_data** | **int** |  | [optional] [default to 0]
**user** | [**AnyOfRecordUser**](AnyOfRecordUser.md) |  | 
**code_type** | [**RecordCodeType**](RecordCodeType.md) |  | 
**code** | **str** |  | 
**judge_category** | **list[str]** |  | 
**submit_at** | **datetime** |  | 
**judge_at** | **datetime** |  | [optional] 
**judge_user** | [**AnyOfRecordJudgeUser**](AnyOfRecordJudgeUser.md) |  | [optional] 
**compiler_texts** | **str** |  | [optional] [default to '']
**cases** | [**list[RecordCase]**](RecordCase.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

