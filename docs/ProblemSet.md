# ProblemSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | 
**title** | **str** | title of the problem set | 
**content** | **str** | content of the problem set | [optional] [default to '']
**hidden** | **bool** | whether the problem set is hidden | [optional] [default to False]
**scoreboard_hidden** | **bool** | whether the scoreboard of the problem set is hidden | [optional] [default to False]
**available_time** | **datetime** | the problem set is available from | [optional] 
**due_time** | **datetime** | the problem set is due at | [optional] 
**domain** | [**AnyOfProblemSetDomain**](AnyOfProblemSetDomain.md) |  | 
**owner** | [**AnyOfProblemSetOwner**](AnyOfProblemSetOwner.md) |  | 
**num_submit** | **int** |  | [optional] [default to 0]
**num_accept** | **int** |  | [optional] [default to 0]
**problems** | [**list[AnyOfProblemSetProblemsItems]**](Object.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

