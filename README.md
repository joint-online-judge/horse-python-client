# horse-python-client
Git version: 4bafe89@2022-05-14T18:47:05Z

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/joint-online-judge/horse-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/joint-online-judge/horse-python-client.git`)

Then import the package:
```python
import joj.horse_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import joj.horse_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import joj.horse_client
from joj.horse_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
body = joj.horse_client.JudgerCreate() # JudgerCreate | 

try:
    # Create Judger
    api_response = api_instance.v1_create_judger(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_create_judger: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Domain Roles
    api_response = api_instance.v1_list_domain_roles(ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_list_domain_roles: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Judgers
    api_response = api_instance.v1_list_judgers(ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_list_judgers: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse_client.AdminApi(joj.horse_client.ApiClient(configuration))
ordering = '' # str | Comma seperated list of ordering the results. You may specify reverse orderings by prefixing the field name with '-'.  Available fields: created_at,updated_at (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Users
    api_response = api_instance.v1_list_users(ordering=ordering, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->v1_list_users: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**v1_create_judger**](docs/AdminApi.md#v1_create_judger) | **POST** /admin/judgers | Create Judger
*AdminApi* | [**v1_list_domain_roles**](docs/AdminApi.md#v1_list_domain_roles) | **GET** /admin/domain_roles | List Domain Roles
*AdminApi* | [**v1_list_judgers**](docs/AdminApi.md#v1_list_judgers) | **GET** /admin/judgers | List Judgers
*AdminApi* | [**v1_list_users**](docs/AdminApi.md#v1_list_users) | **GET** /admin/users | List Users
*AuthApi* | [**v1_get_token**](docs/AuthApi.md#v1_get_token) | **GET** /auth/token | Get Token
*AuthApi* | [**v1_list_oauth2**](docs/AuthApi.md#v1_list_oauth2) | **GET** /auth/oauth2 | List Oauth2
*AuthApi* | [**v1_login**](docs/AuthApi.md#v1_login) | **POST** /auth/login | Login
*AuthApi* | [**v1_logout**](docs/AuthApi.md#v1_logout) | **POST** /auth/logout | Logout
*AuthApi* | [**v1_oauth_authorize**](docs/AuthApi.md#v1_oauth_authorize) | **GET** /auth/oauth2/{oauth2}/authorize | Oauth Authorize
*AuthApi* | [**v1_refresh**](docs/AuthApi.md#v1_refresh) | **POST** /auth/refresh | Refresh
*AuthApi* | [**v1_register**](docs/AuthApi.md#v1_register) | **POST** /auth/register | Register
*DomainApi* | [**v1_add_domain_user**](docs/DomainApi.md#v1_add_domain_user) | **POST** /domains/{domain}/users | Add Domain User
*DomainApi* | [**v1_create_domain**](docs/DomainApi.md#v1_create_domain) | **POST** /domains | Create Domain
*DomainApi* | [**v1_create_domain_invitation**](docs/DomainApi.md#v1_create_domain_invitation) | **POST** /domains/{domain}/invitations | Create Domain Invitation
*DomainApi* | [**v1_create_domain_role**](docs/DomainApi.md#v1_create_domain_role) | **POST** /domains/{domain}/roles | Create Domain Role
*DomainApi* | [**v1_delete_domain**](docs/DomainApi.md#v1_delete_domain) | **DELETE** /domains/{domain} | Delete Domain
*DomainApi* | [**v1_delete_domain_invitation**](docs/DomainApi.md#v1_delete_domain_invitation) | **DELETE** /domains/{domain}/invitations/{invitation} | Delete Domain Invitation
*DomainApi* | [**v1_delete_domain_role**](docs/DomainApi.md#v1_delete_domain_role) | **DELETE** /domains/{domain}/roles/{role} | Delete Domain Role
*DomainApi* | [**v1_get_domain**](docs/DomainApi.md#v1_get_domain) | **GET** /domains/{domain} | Get Domain
*DomainApi* | [**v1_get_domain_invitation**](docs/DomainApi.md#v1_get_domain_invitation) | **GET** /domains/{domain}/invitations/{invitation} | Get Domain Invitation
*DomainApi* | [**v1_get_domain_role**](docs/DomainApi.md#v1_get_domain_role) | **GET** /domains/{domain}/roles/{role} | Get Domain Role
*DomainApi* | [**v1_get_domain_user**](docs/DomainApi.md#v1_get_domain_user) | **GET** /domains/{domain}/users/{user} | Get Domain User
*DomainApi* | [**v1_get_domain_user_permission**](docs/DomainApi.md#v1_get_domain_user_permission) | **GET** /domains/{domain}/users/{user}/permission | Get Domain User Permission
*DomainApi* | [**v1_join_domain_by_invitation**](docs/DomainApi.md#v1_join_domain_by_invitation) | **POST** /domains/{domain}/join | Join Domain By Invitation
*DomainApi* | [**v1_list_domain_invitations**](docs/DomainApi.md#v1_list_domain_invitations) | **GET** /domains/{domain}/invitations | List Domain Invitations
*DomainApi* | [**v1_list_domain_roles**](docs/DomainApi.md#v1_list_domain_roles) | **GET** /domains/{domain}/roles | List Domain Roles
*DomainApi* | [**v1_list_domain_users**](docs/DomainApi.md#v1_list_domain_users) | **GET** /domains/{domain}/users | List Domain Users
*DomainApi* | [**v1_list_domains**](docs/DomainApi.md#v1_list_domains) | **GET** /domains | List Domains
*DomainApi* | [**v1_remove_domain_user**](docs/DomainApi.md#v1_remove_domain_user) | **DELETE** /domains/{domain}/users/{user} | Remove Domain User
*DomainApi* | [**v1_search_domain_candidates**](docs/DomainApi.md#v1_search_domain_candidates) | **GET** /domains/{domain}/candidates | Search Domain Candidates
*DomainApi* | [**v1_search_domain_groups**](docs/DomainApi.md#v1_search_domain_groups) | **GET** /domains/groups | Search Domain Groups
*DomainApi* | [**v1_transfer_domain**](docs/DomainApi.md#v1_transfer_domain) | **POST** /domains/{domain}/transfer | Transfer Domain
*DomainApi* | [**v1_update_domain**](docs/DomainApi.md#v1_update_domain) | **PATCH** /domains/{domain} | Update Domain
*DomainApi* | [**v1_update_domain_invitation**](docs/DomainApi.md#v1_update_domain_invitation) | **PATCH** /domains/{domain}/invitations/{invitation} | Update Domain Invitation
*DomainApi* | [**v1_update_domain_role**](docs/DomainApi.md#v1_update_domain_role) | **PATCH** /domains/{domain}/roles/{role} | Update Domain Role
*DomainApi* | [**v1_update_domain_user**](docs/DomainApi.md#v1_update_domain_user) | **PATCH** /domains/{domain}/users/{user} | Update Domain User
*JudgeApi* | [**v1_claim_record_by_judger**](docs/JudgeApi.md#v1_claim_record_by_judger) | **POST** /domains/{domain}/records/{record}/judge/claim | Claim Record By Judger
*JudgeApi* | [**v1_submit_case_by_judger**](docs/JudgeApi.md#v1_submit_case_by_judger) | **PUT** /domains/{domain}/records/{record}/cases/{index}/judge | Submit Case By Judger
*JudgeApi* | [**v1_submit_record_by_judger**](docs/JudgeApi.md#v1_submit_record_by_judger) | **PUT** /domains/{domain}/records/{record}/judge | Submit Record By Judger
*MiscellaneousApi* | [**v1_jwt_decoded**](docs/MiscellaneousApi.md#v1_jwt_decoded) | **GET** /jwt_decoded | Jwt Decoded
*MiscellaneousApi* | [**v1_set_root_user**](docs/MiscellaneousApi.md#v1_set_root_user) | **POST** /set_root_user | Set Root User
*MiscellaneousApi* | [**v1_test_error_report**](docs/MiscellaneousApi.md#v1_test_error_report) | **GET** /test/report | Test Error Report
*MiscellaneousApi* | [**v1_version**](docs/MiscellaneousApi.md#v1_version) | **GET** /version | Version
*ProblemApi* | [**v1_clone_problem**](docs/ProblemApi.md#v1_clone_problem) | **POST** /domains/{domain}/problems/clone | Clone Problem
*ProblemApi* | [**v1_create_problem**](docs/ProblemApi.md#v1_create_problem) | **POST** /domains/{domain}/problems | Create Problem
*ProblemApi* | [**v1_delete_problem**](docs/ProblemApi.md#v1_delete_problem) | **DELETE** /domains/{domain}/problems/{problem} | Delete Problem
*ProblemApi* | [**v1_get_problem**](docs/ProblemApi.md#v1_get_problem) | **GET** /domains/{domain}/problems/{problem} | Get Problem
*ProblemApi* | [**v1_list_problems**](docs/ProblemApi.md#v1_list_problems) | **GET** /domains/{domain}/problems | List Problems
*ProblemApi* | [**v1_submit_solution_to_problem**](docs/ProblemApi.md#v1_submit_solution_to_problem) | **POST** /domains/{domain}/problems/{problem} | Submit Solution To Problem
*ProblemApi* | [**v1_update_problem**](docs/ProblemApi.md#v1_update_problem) | **PATCH** /domains/{domain}/problems/{problem} | Update Problem
*ProblemConfigApi* | [**v1_commit_problem_config**](docs/ProblemConfigApi.md#v1_commit_problem_config) | **POST** /domains/{domain}/problems/{problem}/config/commit | Commit Problem Config
*ProblemConfigApi* | [**v1_delete_directory_from_uncommitted_problem_config**](docs/ProblemConfigApi.md#v1_delete_directory_from_uncommitted_problem_config) | **DELETE** /domains/{domain}/problems/{problem}/config/dirs/{path} | Delete Directory From Uncommitted Problem Config
*ProblemConfigApi* | [**v1_delete_file_from_uncommitted_problem_config**](docs/ProblemConfigApi.md#v1_delete_file_from_uncommitted_problem_config) | **DELETE** /domains/{domain}/problems/{problem}/config/files/{path} | Delete File From Uncommitted Problem Config
*ProblemConfigApi* | [**v1_diff_problem_config_default_branch**](docs/ProblemConfigApi.md#v1_diff_problem_config_default_branch) | **GET** /domains/{domain}/problems/{problem}/config/diff | Diff Problem Config Default Branch
*ProblemConfigApi* | [**v1_download_file_in_problem_config**](docs/ProblemConfigApi.md#v1_download_file_in_problem_config) | **GET** /domains/{domain}/problems/{problem}/configs/{config}/files/{path} | Download File In Problem Config
*ProblemConfigApi* | [**v1_download_file_in_uncommitted_problem_config**](docs/ProblemConfigApi.md#v1_download_file_in_uncommitted_problem_config) | **GET** /domains/{domain}/problems/{problem}/config/files/{path} | Download File In Uncommitted Problem Config
*ProblemConfigApi* | [**v1_download_problem_config_archive**](docs/ProblemConfigApi.md#v1_download_problem_config_archive) | **GET** /domains/{domain}/problems/{problem}/configs/{config}/files | Download Problem Config Archive
*ProblemConfigApi* | [**v1_download_uncommitted_problem_config_as_archive**](docs/ProblemConfigApi.md#v1_download_uncommitted_problem_config_as_archive) | **GET** /domains/{domain}/problems/{problem}/config | Download Uncommitted Problem Config As Archive
*ProblemConfigApi* | [**v1_get_file_or_directory_info_in_uncommitted_problem_config**](docs/ProblemConfigApi.md#v1_get_file_or_directory_info_in_uncommitted_problem_config) | **GET** /domains/{domain}/problems/{problem}/config/file_info/{path} | Get File Or Directory Info In Uncommitted Problem Config
*ProblemConfigApi* | [**v1_get_problem_config_json**](docs/ProblemConfigApi.md#v1_get_problem_config_json) | **GET** /domains/{domain}/problems/{problem}/configs/{config} | Get Problem Config Json
*ProblemConfigApi* | [**v1_list_latest_problem_config_objects_under_a_given_prefix**](docs/ProblemConfigApi.md#v1_list_latest_problem_config_objects_under_a_given_prefix) | **GET** /domains/{domain}/problems/{problem}/config/ls | List Latest Problem Config Objects Under A Given Prefix
*ProblemConfigApi* | [**v1_reset_problem_config**](docs/ProblemConfigApi.md#v1_reset_problem_config) | **POST** /domains/{domain}/problems/{problem}/config/reset | Reset Problem Config
*ProblemConfigApi* | [**v1_update_problem_config_by_archive**](docs/ProblemConfigApi.md#v1_update_problem_config_by_archive) | **PUT** /domains/{domain}/problems/{problem}/config | Update Problem Config By Archive
*ProblemConfigApi* | [**v1_update_problem_config_json**](docs/ProblemConfigApi.md#v1_update_problem_config_json) | **PUT** /domains/{domain}/problems/{problem}/configs | Update Problem Config Json
*ProblemConfigApi* | [**v1_upload_file_to_problem_config**](docs/ProblemConfigApi.md#v1_upload_file_to_problem_config) | **PUT** /domains/{domain}/problems/{problem}/config/files/{path} | Upload File To Problem Config
*ProblemConfigApi* | [**v1_upload_file_to_root_in_problem_config**](docs/ProblemConfigApi.md#v1_upload_file_to_root_in_problem_config) | **PUT** /domains/{domain}/problems/{problem}/config/files | Upload File To Root In Problem Config
*ProblemGroupApi* | [**v1_list_problem_groups**](docs/ProblemGroupApi.md#v1_list_problem_groups) | **GET** /problem_groups | List Problem Groups
*ProblemSetApi* | [**v1_add_problem_in_problem_set**](docs/ProblemSetApi.md#v1_add_problem_in_problem_set) | **POST** /domains/{domain}/problem_sets/{problemSet}/problems | Add Problem In Problem Set
*ProblemSetApi* | [**v1_create_problem_set**](docs/ProblemSetApi.md#v1_create_problem_set) | **POST** /domains/{domain}/problem_sets | Create Problem Set
*ProblemSetApi* | [**v1_delete_problem_in_problem_set**](docs/ProblemSetApi.md#v1_delete_problem_in_problem_set) | **DELETE** /domains/{domain}/problem_sets/{problemSet}/problems/{problem} | Delete Problem In Problem Set
*ProblemSetApi* | [**v1_delete_problem_set**](docs/ProblemSetApi.md#v1_delete_problem_set) | **DELETE** /domains/{domain}/problem_sets/{problemSet} | Delete Problem Set
*ProblemSetApi* | [**v1_get_problem_in_problem_set**](docs/ProblemSetApi.md#v1_get_problem_in_problem_set) | **GET** /domains/{domain}/problem_sets/{problemSet}/problems/{problem} | Get Problem In Problem Set
*ProblemSetApi* | [**v1_get_problem_set**](docs/ProblemSetApi.md#v1_get_problem_set) | **GET** /domains/{domain}/problem_sets/{problemSet} | Get Problem Set
*ProblemSetApi* | [**v1_list_problem_sets**](docs/ProblemSetApi.md#v1_list_problem_sets) | **GET** /domains/{domain}/problem_sets | List Problem Sets
*ProblemSetApi* | [**v1_list_problems_in_problem_set**](docs/ProblemSetApi.md#v1_list_problems_in_problem_set) | **GET** /domains/{domain}/problem_sets/{problemSet}/problems | List Problems In Problem Set
*ProblemSetApi* | [**v1_submit_solution_to_problem_set**](docs/ProblemSetApi.md#v1_submit_solution_to_problem_set) | **POST** /domains/{domain}/problem_sets/{problemSet}/problems/{problem}/submit | Submit Solution To Problem Set
*ProblemSetApi* | [**v1_update_problem_in_problem_set**](docs/ProblemSetApi.md#v1_update_problem_in_problem_set) | **PATCH** /domains/{domain}/problem_sets/{problemSet}/problems/{problem} | Update Problem In Problem Set
*ProblemSetApi* | [**v1_update_problem_set**](docs/ProblemSetApi.md#v1_update_problem_set) | **PATCH** /domains/{domain}/problem_sets/{problemSet} | Update Problem Set
*RecordApi* | [**v1_get_record**](docs/RecordApi.md#v1_get_record) | **GET** /domains/{domain}/records/{record} | Get Record
*RecordApi* | [**v1_list_records_in_domain**](docs/RecordApi.md#v1_list_records_in_domain) | **GET** /domains/{domain}/records | List Records In Domain
*UserApi* | [**v1_change_password**](docs/UserApi.md#v1_change_password) | **PATCH** /user/password | Change Password
*UserApi* | [**v1_get_current_user**](docs/UserApi.md#v1_get_current_user) | **GET** /user | Get Current User
*UserApi* | [**v1_get_user**](docs/UserApi.md#v1_get_user) | **GET** /users/{uid} | Get User
*UserApi* | [**v1_get_user_problems**](docs/UserApi.md#v1_get_user_problems) | **GET** /users/{uid}/problems | Get User Problems
*UserApi* | [**v1_list_user_domains**](docs/UserApi.md#v1_list_user_domains) | **GET** /users/{uid}/domains | List User Domains
*UserApi* | [**v1_list_users**](docs/UserApi.md#v1_list_users) | **GET** /users | List Users
*UserApi* | [**v1_update_current_user**](docs/UserApi.md#v1_update_current_user) | **PATCH** /user | Update Current User

## Documentation For Models

 - [AllOfDomainPermissionGeneral](docs/AllOfDomainPermissionGeneral.md)
 - [AllOfDomainPermissionProblem](docs/AllOfDomainPermissionProblem.md)
 - [AllOfDomainPermissionProblemSet](docs/AllOfDomainPermissionProblemSet.md)
 - [AllOfDomainPermissionRecord](docs/AllOfDomainPermissionRecord.md)
 - [AllOfRecordCaseState](docs/AllOfRecordCaseState.md)
 - [AllOfRecordDetailState](docs/AllOfRecordDetailState.md)
 - [AllOfRecordListDetailState](docs/AllOfRecordListDetailState.md)
 - [AllOfRecordState](docs/AllOfRecordState.md)
 - [AnyOfFileInfoMtime](docs/AnyOfFileInfoMtime.md)
 - [ArchiveFormat](docs/ArchiveFormat.md)
 - [ArchiveFormat1](docs/ArchiveFormat1.md)
 - [ArchiveType](docs/ArchiveType.md)
 - [AuthTokens](docs/AuthTokens.md)
 - [AuthTokensResp](docs/AuthTokensResp.md)
 - [Case](docs/Case.md)
 - [Detail](docs/Detail.md)
 - [Diff](docs/Diff.md)
 - [DiffList](docs/DiffList.md)
 - [DiffListResp](docs/DiffListResp.md)
 - [DiffTypeEnum](docs/DiffTypeEnum.md)
 - [Domain](docs/Domain.md)
 - [DomainCreate](docs/DomainCreate.md)
 - [DomainDetail](docs/DomainDetail.md)
 - [DomainDetailResp](docs/DomainDetailResp.md)
 - [DomainEdit](docs/DomainEdit.md)
 - [DomainInvitation](docs/DomainInvitation.md)
 - [DomainInvitationCreate](docs/DomainInvitationCreate.md)
 - [DomainInvitationEdit](docs/DomainInvitationEdit.md)
 - [DomainInvitationList](docs/DomainInvitationList.md)
 - [DomainInvitationListResp](docs/DomainInvitationListResp.md)
 - [DomainInvitationResp](docs/DomainInvitationResp.md)
 - [DomainList](docs/DomainList.md)
 - [DomainListResp](docs/DomainListResp.md)
 - [DomainPermission](docs/DomainPermission.md)
 - [DomainResp](docs/DomainResp.md)
 - [DomainRole](docs/DomainRole.md)
 - [DomainRoleCreate](docs/DomainRoleCreate.md)
 - [DomainRoleDetail](docs/DomainRoleDetail.md)
 - [DomainRoleDetailResp](docs/DomainRoleDetailResp.md)
 - [DomainRoleEdit](docs/DomainRoleEdit.md)
 - [DomainRoleList](docs/DomainRoleList.md)
 - [DomainRoleListResp](docs/DomainRoleListResp.md)
 - [DomainRoleResp](docs/DomainRoleResp.md)
 - [DomainTag](docs/DomainTag.md)
 - [DomainTagList](docs/DomainTagList.md)
 - [DomainTagListResp](docs/DomainTagListResp.md)
 - [DomainTransfer](docs/DomainTransfer.md)
 - [DomainUserAdd](docs/DomainUserAdd.md)
 - [DomainUserPermission](docs/DomainUserPermission.md)
 - [DomainUserPermissionResp](docs/DomainUserPermissionResp.md)
 - [DomainUserUpdate](docs/DomainUserUpdate.md)
 - [Empty](docs/Empty.md)
 - [EmptyResp](docs/EmptyResp.md)
 - [ErrorCode](docs/ErrorCode.md)
 - [FileInfo](docs/FileInfo.md)
 - [FileInfoResp](docs/FileInfoResp.md)
 - [FileUpload](docs/FileUpload.md)
 - [GeneralPermission](docs/GeneralPermission.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [JWTAccessToken](docs/JWTAccessToken.md)
 - [JWTAccessTokenResp](docs/JWTAccessTokenResp.md)
 - [JudgerClaim](docs/JudgerClaim.md)
 - [JudgerCreate](docs/JudgerCreate.md)
 - [JudgerCredentials](docs/JudgerCredentials.md)
 - [JudgerCredentialsResp](docs/JudgerCredentialsResp.md)
 - [LakeFSReset](docs/LakeFSReset.md)
 - [Language](docs/Language.md)
 - [LanguageDefault](docs/LanguageDefault.md)
 - [OAuth2Client](docs/OAuth2Client.md)
 - [OAuth2ClientList](docs/OAuth2ClientList.md)
 - [OAuth2ClientListResp](docs/OAuth2ClientListResp.md)
 - [OAuth2PasswordRequestForm](docs/OAuth2PasswordRequestForm.md)
 - [ObjectStats](docs/ObjectStats.md)
 - [ObjectStatsList](docs/ObjectStatsList.md)
 - [ObjectStatsListResp](docs/ObjectStatsListResp.md)
 - [Pagination](docs/Pagination.md)
 - [PathTypeEnum](docs/PathTypeEnum.md)
 - [Problem](docs/Problem.md)
 - [ProblemClone](docs/ProblemClone.md)
 - [ProblemConfig](docs/ProblemConfig.md)
 - [ProblemConfigCommit](docs/ProblemConfigCommit.md)
 - [ProblemConfigDataDetail](docs/ProblemConfigDataDetail.md)
 - [ProblemConfigDataDetailResp](docs/ProblemConfigDataDetailResp.md)
 - [ProblemConfigJson](docs/ProblemConfigJson.md)
 - [ProblemConfigResp](docs/ProblemConfigResp.md)
 - [ProblemCreate](docs/ProblemCreate.md)
 - [ProblemDetail](docs/ProblemDetail.md)
 - [ProblemDetailResp](docs/ProblemDetailResp.md)
 - [ProblemDetailWithLatestRecord](docs/ProblemDetailWithLatestRecord.md)
 - [ProblemDetailWithLatestRecordResp](docs/ProblemDetailWithLatestRecordResp.md)
 - [ProblemEdit](docs/ProblemEdit.md)
 - [ProblemGroup](docs/ProblemGroup.md)
 - [ProblemGroupList](docs/ProblemGroupList.md)
 - [ProblemGroupListResp](docs/ProblemGroupListResp.md)
 - [ProblemList](docs/ProblemList.md)
 - [ProblemListResp](docs/ProblemListResp.md)
 - [ProblemPermission](docs/ProblemPermission.md)
 - [ProblemPreviewWithLatestRecord](docs/ProblemPreviewWithLatestRecord.md)
 - [ProblemResp](docs/ProblemResp.md)
 - [ProblemSet](docs/ProblemSet.md)
 - [ProblemSetAddProblem](docs/ProblemSetAddProblem.md)
 - [ProblemSetCreate](docs/ProblemSetCreate.md)
 - [ProblemSetDetail](docs/ProblemSetDetail.md)
 - [ProblemSetDetailResp](docs/ProblemSetDetailResp.md)
 - [ProblemSetEdit](docs/ProblemSetEdit.md)
 - [ProblemSetList](docs/ProblemSetList.md)
 - [ProblemSetListResp](docs/ProblemSetListResp.md)
 - [ProblemSetPermission](docs/ProblemSetPermission.md)
 - [ProblemSetResp](docs/ProblemSetResp.md)
 - [ProblemSetUpdateProblem](docs/ProblemSetUpdateProblem.md)
 - [ProblemSolutionSubmit](docs/ProblemSolutionSubmit.md)
 - [ProblemWithLatestRecord](docs/ProblemWithLatestRecord.md)
 - [ProblemWithLatestRecordList](docs/ProblemWithLatestRecordList.md)
 - [ProblemWithLatestRecordListResp](docs/ProblemWithLatestRecordListResp.md)
 - [Record](docs/Record.md)
 - [RecordCase](docs/RecordCase.md)
 - [RecordCaseResult](docs/RecordCaseResult.md)
 - [RecordCaseSubmit](docs/RecordCaseSubmit.md)
 - [RecordDetail](docs/RecordDetail.md)
 - [RecordDetailResp](docs/RecordDetailResp.md)
 - [RecordListDetail](docs/RecordListDetail.md)
 - [RecordListDetailList](docs/RecordListDetailList.md)
 - [RecordListDetailListResp](docs/RecordListDetailListResp.md)
 - [RecordPermission](docs/RecordPermission.md)
 - [RecordPreview](docs/RecordPreview.md)
 - [RecordResp](docs/RecordResp.md)
 - [RecordState](docs/RecordState.md)
 - [RecordSubmit](docs/RecordSubmit.md)
 - [Redirect](docs/Redirect.md)
 - [RedirectResp](docs/RedirectResp.md)
 - [User](docs/User.md)
 - [UserCreate](docs/UserCreate.md)
 - [UserDetail](docs/UserDetail.md)
 - [UserDetailResp](docs/UserDetailResp.md)
 - [UserDetailWithDomainRole](docs/UserDetailWithDomainRole.md)
 - [UserDetailWithDomainRoleList](docs/UserDetailWithDomainRoleList.md)
 - [UserDetailWithDomainRoleListResp](docs/UserDetailWithDomainRoleListResp.md)
 - [UserDetailWithDomainRoleResp](docs/UserDetailWithDomainRoleResp.md)
 - [UserEdit](docs/UserEdit.md)
 - [UserList](docs/UserList.md)
 - [UserListResp](docs/UserListResp.md)
 - [UserResetPassword](docs/UserResetPassword.md)
 - [UserResp](docs/UserResp.md)
 - [UserWithDomainRole](docs/UserWithDomainRole.md)
 - [UserWithDomainRoleList](docs/UserWithDomainRoleList.md)
 - [UserWithDomainRoleListResp](docs/UserWithDomainRoleListResp.md)
 - [UserWithDomainRoleResp](docs/UserWithDomainRoleResp.md)
 - [ValidationError](docs/ValidationError.md)
 - [Version](docs/Version.md)

## Documentation For Authorization


## HTTPBearer



## Author


