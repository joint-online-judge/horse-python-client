# Problem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** | title of the problem | 
**content** | **str** | content of the problem | [optional] [default to '']
**data_version** | [**AllOfProblemDataVersion**](AllOfProblemDataVersion.md) |  | [optional] 
**languages** | **list[str]** | acceptable language of the problem | [optional] 
**problem_set** | [**AnyOfProblemProblemSet**](AnyOfProblemProblemSet.md) |  | 
**domain** | [**AnyOfProblemDomain**](AnyOfProblemDomain.md) |  | 
**owner** | [**AnyOfProblemOwner**](AnyOfProblemOwner.md) |  | 
**problem_group** | [**AnyOfProblemProblemGroup**](AnyOfProblemProblemGroup.md) |  | 
**num_submit** | **int** |  | [optional] [default to 0]
**num_accept** | **int** |  | [optional] [default to 0]
**data** | **int** |  | [optional] 
**total_score** | **int** |  | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

