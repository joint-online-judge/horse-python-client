# ProblemSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**domain** | [**AnyOfProblemSetDomain**](AnyOfProblemSetDomain.md) |  | 
**url** | **str** | (in domain unique) url of the problem | [optional] 
**title** | **str** | title of the problem set | 
**content** | **str** | content of the problem set | [optional] [default to '']
**hidden** | **bool** | whether the problem set is hidden | [optional] [default to False]
**scoreboard_hidden** | **bool** |  | 
**available_time** | **datetime** |  | 
**due_time** | **datetime** |  | 
**owner** | [**AnyOfProblemSetOwner**](AnyOfProblemSetOwner.md) |  | 
**num_submit** | **int** |  | [optional] [default to 0]
**num_accept** | **int** |  | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

