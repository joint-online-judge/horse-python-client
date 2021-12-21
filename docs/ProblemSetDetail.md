# ProblemSetDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**domain_id** | **str** |  | 
**url** | **str** | (unique) url of the domain | [optional] [default to '']
**title** | **str** | title of the problem set | 
**content** | **str** | content of the problem set | [optional] [default to '']
**hidden** | **bool** | whether the problem set is hidden | [optional] [default to False]
**scoreboard_hidden** | **bool** | whether the scoreboard of the problem set is hidden | [optional] [default to False]
**due_at** | **datetime** | the problem set is due at this date | [optional] 
**lock_at** | **datetime** | the problem set is locked after this date | [optional] 
**unlock_at** | **datetime** | the problem set is unlocked after this date | [optional] 
**num_submit** | **int** |  | [optional] [default to 0]
**num_accept** | **int** |  | [optional] [default to 0]
**owner_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**problems** | [**list[ProblemPreviewWithLatestRecord]**](ProblemPreviewWithLatestRecord.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

