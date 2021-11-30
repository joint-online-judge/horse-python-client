# ProblemDetailWithRecordState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**domain_id** | **str** |  | 
**url** | **str** | (unique) url of the domain | [optional] [default to '']
**title** | **str** | title of the problem | 
**content** | **str** | content of the problem | [optional] [default to '']
**hidden** | **bool** | is the problem hidden | [optional] [default to False]
**num_submit** | **int** |  | [optional] [default to 0]
**num_accept** | **int** |  | [optional] [default to 0]
**owner_id** | **str** |  | [optional] 
**problem_group_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**record_id** | **str** |  | [optional] 
**record_state** | [**RecordState**](RecordState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

