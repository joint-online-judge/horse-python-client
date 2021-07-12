# horse-python-client
Git version: d47939f@2021-07-12 17:53:41

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.0
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
import joj.horse.client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import joj.horse.client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import joj.horse.client
from joj.horse.client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
uname = 'uname_example' # str | 
mail = 'mail_example' # str | 

try:
    # Create Judger
    api_response = api_instance.create_judger_api_v1_admin_judgers_post(uname, mail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_judger_api_v1_admin_judgers_post: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
student_id = 'student_id_example' # str | 
jaccount_name = 'jaccount_name_example' # str | 
real_name = 'real_name_example' # str | 
ip = 'ip_example' # str | 

try:
    # Create User
    api_response = api_instance.create_user_api_v1_admin_users_post(student_id, jaccount_name, real_name, ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_user_api_v1_admin_users_post: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Delete User
    api_response = api_instance.delete_user_api_v1_admin_users_uid_delete(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->delete_user_api_v1_admin_users_uid_delete: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Get Judger Jwt
    api_response = api_instance.get_judger_jwt_api_v1_admin_judgers_uid_jwt_get(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_judger_jwt_api_v1_admin_judgers_uid_jwt_get: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # List Domain Roles
    api_response = api_instance.list_domain_roles_api_v1_admin_domain_roles_get(sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_domain_roles_api_v1_admin_domain_roles_get: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # List Domain Users
    api_response = api_instance.list_domain_users_api_v1_admin_domain_users_get(sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_domain_users_api_v1_admin_domain_users_get: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # List Judgers
    api_response = api_instance.list_judgers_api_v1_admin_judgers_get(sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_judgers_api_v1_admin_judgers_get: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
sort = joj.horse.client.SortEnum() # SortEnum |  (optional)
skip = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # List Users
    api_response = api_instance.list_users_api_v1_admin_users_get(sort=sort, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_users_api_v1_admin_users_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**create_judger_api_v1_admin_judgers_post**](docs/AdminApi.md#create_judger_api_v1_admin_judgers_post) | **POST** /api/v1/admin/judgers | Create Judger
*AdminApi* | [**create_user_api_v1_admin_users_post**](docs/AdminApi.md#create_user_api_v1_admin_users_post) | **POST** /api/v1/admin/users | Create User
*AdminApi* | [**delete_user_api_v1_admin_users_uid_delete**](docs/AdminApi.md#delete_user_api_v1_admin_users_uid_delete) | **DELETE** /api/v1/admin/users/{uid} | Delete User
*AdminApi* | [**get_judger_jwt_api_v1_admin_judgers_uid_jwt_get**](docs/AdminApi.md#get_judger_jwt_api_v1_admin_judgers_uid_jwt_get) | **GET** /api/v1/admin/judgers/{uid}/jwt | Get Judger Jwt
*AdminApi* | [**list_domain_roles_api_v1_admin_domain_roles_get**](docs/AdminApi.md#list_domain_roles_api_v1_admin_domain_roles_get) | **GET** /api/v1/admin/domain_roles | List Domain Roles
*AdminApi* | [**list_domain_users_api_v1_admin_domain_users_get**](docs/AdminApi.md#list_domain_users_api_v1_admin_domain_users_get) | **GET** /api/v1/admin/domain_users | List Domain Users
*AdminApi* | [**list_judgers_api_v1_admin_judgers_get**](docs/AdminApi.md#list_judgers_api_v1_admin_judgers_get) | **GET** /api/v1/admin/judgers | List Judgers
*AdminApi* | [**list_users_api_v1_admin_users_get**](docs/AdminApi.md#list_users_api_v1_admin_users_get) | **GET** /api/v1/admin/users | List Users
*DefaultApi* | [**redirect_to_docs_api_get**](docs/DefaultApi.md#redirect_to_docs_api_get) | **GET** /api | Redirect To Docs
*DefaultApi* | [**redirect_to_docs_get**](docs/DefaultApi.md#redirect_to_docs_get) | **GET** / | Redirect To Docs
*DomainApi* | [**add_domain_user_api_v1_domains_domain_users_post**](docs/DomainApi.md#add_domain_user_api_v1_domains_domain_users_post) | **POST** /api/v1/domains/{domain}/users | Add Domain User
*DomainApi* | [**create_domain_api_v1_domains_post**](docs/DomainApi.md#create_domain_api_v1_domains_post) | **POST** /api/v1/domains | Create Domain
*DomainApi* | [**create_domain_invitation_api_v1_domains_domain_invitations_post**](docs/DomainApi.md#create_domain_invitation_api_v1_domains_domain_invitations_post) | **POST** /api/v1/domains/{domain}/invitations | Create Domain Invitation
*DomainApi* | [**create_domain_role_api_v1_domains_domain_roles_post**](docs/DomainApi.md#create_domain_role_api_v1_domains_domain_roles_post) | **POST** /api/v1/domains/{domain}/roles | Create Domain Role
*DomainApi* | [**delete_domain_api_v1_domains_domain_delete**](docs/DomainApi.md#delete_domain_api_v1_domains_domain_delete) | **DELETE** /api/v1/domains/{domain} | Delete Domain
*DomainApi* | [**delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete**](docs/DomainApi.md#delete_domain_invitation_api_v1_domains_domain_invitations_invitation_delete) | **DELETE** /api/v1/domains/{domain}/invitations/{invitation} | Delete Domain Invitation
*DomainApi* | [**delete_domain_role_api_v1_domains_domain_roles_role_delete**](docs/DomainApi.md#delete_domain_role_api_v1_domains_domain_roles_role_delete) | **DELETE** /api/v1/domains/{domain}/roles/{role} | Delete Domain Role
*DomainApi* | [**get_domain_api_v1_domains_domain_get**](docs/DomainApi.md#get_domain_api_v1_domains_domain_get) | **GET** /api/v1/domains/{domain} | Get Domain
*DomainApi* | [**get_domain_user_api_v1_domains_domain_users_user_get**](docs/DomainApi.md#get_domain_user_api_v1_domains_domain_users_user_get) | **GET** /api/v1/domains/{domain}/users/{user} | Get Domain User
*DomainApi* | [**join_domain_by_invitation_api_v1_domains_domain_join_post**](docs/DomainApi.md#join_domain_by_invitation_api_v1_domains_domain_join_post) | **POST** /api/v1/domains/{domain}/join | Join Domain By Invitation
*DomainApi* | [**list_domain_roles_api_v1_domains_domain_roles_get**](docs/DomainApi.md#list_domain_roles_api_v1_domains_domain_roles_get) | **GET** /api/v1/domains/{domain}/roles | List Domain Roles
*DomainApi* | [**list_domain_users_api_v1_domains_domain_users_get**](docs/DomainApi.md#list_domain_users_api_v1_domains_domain_users_get) | **GET** /api/v1/domains/{domain}/users | List Domain Users
*DomainApi* | [**list_domains_api_v1_domains_get**](docs/DomainApi.md#list_domains_api_v1_domains_get) | **GET** /api/v1/domains | List Domains
*DomainApi* | [**remove_domain_user_api_v1_domains_domain_users_user_delete**](docs/DomainApi.md#remove_domain_user_api_v1_domains_domain_users_user_delete) | **DELETE** /api/v1/domains/{domain}/users/{user} | Remove Domain User
*DomainApi* | [**update_domain_api_v1_domains_domain_patch**](docs/DomainApi.md#update_domain_api_v1_domains_domain_patch) | **PATCH** /api/v1/domains/{domain} | Update Domain
*DomainApi* | [**update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch**](docs/DomainApi.md#update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch) | **PATCH** /api/v1/domains/{domain}/invitations/{invitation} | Update Domain Invitation
*DomainApi* | [**update_domain_role_api_v1_domains_domain_roles_role_patch**](docs/DomainApi.md#update_domain_role_api_v1_domains_domain_roles_role_patch) | **PATCH** /api/v1/domains/{domain}/roles/{role} | Update Domain Role
*DomainApi* | [**update_domain_user_api_v1_domains_domain_users_user_patch**](docs/DomainApi.md#update_domain_user_api_v1_domains_domain_users_user_patch) | **PATCH** /api/v1/domains/{domain}/users/{user} | Update Domain User
*MiscellaneousApi* | [**jwt_api_v1_jwt_get**](docs/MiscellaneousApi.md#jwt_api_v1_jwt_get) | **GET** /api/v1/jwt | Jwt
*MiscellaneousApi* | [**test_sentry_api_v1_test_sentry_get**](docs/MiscellaneousApi.md#test_sentry_api_v1_test_sentry_get) | **GET** /api/v1/test/sentry | Test Sentry
*MiscellaneousApi* | [**version_api_v1_version_get**](docs/MiscellaneousApi.md#version_api_v1_version_get) | **GET** /api/v1/version | Version
*ProblemApi* | [**clone_problem_api_v1_domains_domain_problems_clone_post**](docs/ProblemApi.md#clone_problem_api_v1_domains_domain_problems_clone_post) | **POST** /api/v1/domains/{domain}/problems/clone | Clone Problem
*ProblemApi* | [**create_problem_api_v1_domains_domain_problems_post**](docs/ProblemApi.md#create_problem_api_v1_domains_domain_problems_post) | **POST** /api/v1/domains/{domain}/problems | Create Problem
*ProblemApi* | [**delete_problem_api_v1_domains_domain_problems_problem_delete**](docs/ProblemApi.md#delete_problem_api_v1_domains_domain_problems_problem_delete) | **DELETE** /api/v1/domains/{domain}/problems/{problem} | Delete Problem
*ProblemApi* | [**get_problem_api_v1_domains_domain_problems_problem_get**](docs/ProblemApi.md#get_problem_api_v1_domains_domain_problems_problem_get) | **GET** /api/v1/domains/{domain}/problems/{problem} | Get Problem
*ProblemApi* | [**list_problems_api_v1_domains_domain_problems_get**](docs/ProblemApi.md#list_problems_api_v1_domains_domain_problems_get) | **GET** /api/v1/domains/{domain}/problems | List Problems
*ProblemApi* | [**submit_solution_to_problem_api_v1_domains_domain_problems_problem_post**](docs/ProblemApi.md#submit_solution_to_problem_api_v1_domains_domain_problems_problem_post) | **POST** /api/v1/domains/{domain}/problems/{problem} | Submit Solution To Problem
*ProblemApi* | [**update_problem_api_v1_domains_domain_problems_problem_patch**](docs/ProblemApi.md#update_problem_api_v1_domains_domain_problems_problem_patch) | **PATCH** /api/v1/domains/{domain}/problems/{problem} | Update Problem
*ProblemApi* | [**update_problem_config_api_v1_domains_domain_problems_problem_config_patch**](docs/ProblemApi.md#update_problem_config_api_v1_domains_domain_problems_problem_config_patch) | **PATCH** /api/v1/domains/{domain}/problems/{problem}/config | Update Problem Config
*ProblemGroupApi* | [**list_problem_groups_api_v1_problem_groups_get**](docs/ProblemGroupApi.md#list_problem_groups_api_v1_problem_groups_get) | **GET** /api/v1/problem_groups | List Problem Groups
*ProblemSetApi* | [**create_problem_set_api_v1_domains_domain_problem_sets_post**](docs/ProblemSetApi.md#create_problem_set_api_v1_domains_domain_problem_sets_post) | **POST** /api/v1/domains/{domain}/problem_sets | Create Problem Set
*ProblemSetApi* | [**delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete**](docs/ProblemSetApi.md#delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete) | **DELETE** /api/v1/domains/{domain}/problem_sets/{problem_set} | Delete Problem Set
*ProblemSetApi* | [**get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get**](docs/ProblemSetApi.md#get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problem_set} | Get Problem Set
*ProblemSetApi* | [**get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get**](docs/ProblemSetApi.md#get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problem_set}/scoreboard | Get Scoreboard
*ProblemSetApi* | [**list_problem_sets_api_v1_domains_domain_problem_sets_get**](docs/ProblemSetApi.md#list_problem_sets_api_v1_domains_domain_problem_sets_get) | **GET** /api/v1/domains/{domain}/problem_sets | List Problem Sets
*ProblemSetApi* | [**update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch**](docs/ProblemSetApi.md#update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch) | **PATCH** /api/v1/domains/{domain}/problem_sets/{problem_set} | Update Problem Set
*RecordApi* | [**get_record_api_v1_records_record_get**](docs/RecordApi.md#get_record_api_v1_records_record_get) | **GET** /api/v1/records/{record} | Get Record
*RecordApi* | [**get_record_code_api_v1_records_record_code_get**](docs/RecordApi.md#get_record_code_api_v1_records_record_code_get) | **GET** /api/v1/records/{record}/code | Get Record Code
*RecordApi* | [**http_record_api_v1_records_record_http_post**](docs/RecordApi.md#http_record_api_v1_records_record_http_post) | **POST** /api/v1/records/{record}/http | Http Record
*RecordApi* | [**http_record_cases_api_v1_records_record_cases_http_post**](docs/RecordApi.md#http_record_cases_api_v1_records_record_cases_http_post) | **POST** /api/v1/records/{record}/cases/http | Http Record Cases
*RecordApi* | [**list_records_api_v1_records_get**](docs/RecordApi.md#list_records_api_v1_records_get) | **GET** /api/v1/records | List Records
*UserApi* | [**get_user_api_v1_user_get**](docs/UserApi.md#get_user_api_v1_user_get) | **GET** /api/v1/user | Get User
*UserApi* | [**get_user_api_v1_users_uid_get**](docs/UserApi.md#get_user_api_v1_users_uid_get) | **GET** /api/v1/users/{uid} | Get User
*UserApi* | [**get_user_domains_api_v1_users_uid_domains_get**](docs/UserApi.md#get_user_domains_api_v1_users_uid_domains_get) | **GET** /api/v1/users/{uid}/domains | Get User Domains
*UserApi* | [**get_user_problems_api_v1_user_problems_get**](docs/UserApi.md#get_user_problems_api_v1_user_problems_get) | **GET** /api/v1/user/problems | Get User Problems
*UserApi* | [**get_user_problems_api_v1_users_uid_problems_get**](docs/UserApi.md#get_user_problems_api_v1_users_uid_problems_get) | **GET** /api/v1/users/{uid}/problems | Get User Problems
*UserApi* | [**jaccount_auth_api_v1_user_jaccount_auth_get**](docs/UserApi.md#jaccount_auth_api_v1_user_jaccount_auth_get) | **GET** /api/v1/user/jaccount/auth | Jaccount Auth
*UserApi* | [**jaccount_login_api_v1_user_jaccount_login_get**](docs/UserApi.md#jaccount_login_api_v1_user_jaccount_login_get) | **GET** /api/v1/user/jaccount/login | Jaccount Login
*UserApi* | [**logout_api_v1_user_logout_get**](docs/UserApi.md#logout_api_v1_user_logout_get) | **GET** /api/v1/user/logout | Logout

## Documentation For Models

 - [AllOfDomainUserAddRole](docs/AllOfDomainUserAddRole.md)
 - [AllOfProblemConfig](docs/AllOfProblemConfig.md)
 - [AllOfProblemDataVersion](docs/AllOfProblemDataVersion.md)
 - [AllOfRecordCaseStatus](docs/AllOfRecordCaseStatus.md)
 - [AllOfRecordStatus](docs/AllOfRecordStatus.md)
 - [AnyOfDomainInvitationDomain](docs/AnyOfDomainInvitationDomain.md)
 - [AnyOfDomainOwner](docs/AnyOfDomainOwner.md)
 - [AnyOfDomainRoleDomain](docs/AnyOfDomainRoleDomain.md)
 - [AnyOfDomainUserDomain](docs/AnyOfDomainUserDomain.md)
 - [AnyOfDomainUserUser](docs/AnyOfDomainUserUser.md)
 - [AnyOfProblemDomain](docs/AnyOfProblemDomain.md)
 - [AnyOfProblemOwner](docs/AnyOfProblemOwner.md)
 - [AnyOfProblemProblemGroup](docs/AnyOfProblemProblemGroup.md)
 - [AnyOfProblemSetDomain](docs/AnyOfProblemSetDomain.md)
 - [AnyOfProblemSetOwner](docs/AnyOfProblemSetOwner.md)
 - [AnyOfProblemSetProblemsItems](docs/AnyOfProblemSetProblemsItems.md)
 - [AnyOfRecordDomain](docs/AnyOfRecordDomain.md)
 - [AnyOfRecordJudgeUser](docs/AnyOfRecordJudgeUser.md)
 - [AnyOfRecordProblem](docs/AnyOfRecordProblem.md)
 - [AnyOfRecordUser](docs/AnyOfRecordUser.md)
 - [Config](docs/Config.md)
 - [DataVersion](docs/DataVersion.md)
 - [DefaultRole](docs/DefaultRole.md)
 - [Detail](docs/Detail.md)
 - [Domain](docs/Domain.md)
 - [DomainCreate](docs/DomainCreate.md)
 - [DomainEdit](docs/DomainEdit.md)
 - [DomainInvitation](docs/DomainInvitation.md)
 - [DomainInvitationCreate](docs/DomainInvitationCreate.md)
 - [DomainInvitationEdit](docs/DomainInvitationEdit.md)
 - [DomainInvitationResp](docs/DomainInvitationResp.md)
 - [DomainResp](docs/DomainResp.md)
 - [DomainRole](docs/DomainRole.md)
 - [DomainRoleCreate](docs/DomainRoleCreate.md)
 - [DomainRoleEdit](docs/DomainRoleEdit.md)
 - [DomainRoleResp](docs/DomainRoleResp.md)
 - [DomainUser](docs/DomainUser.md)
 - [DomainUserAdd](docs/DomainUserAdd.md)
 - [DomainUserResp](docs/DomainUserResp.md)
 - [Empty](docs/Empty.md)
 - [EmptyResp](docs/EmptyResp.md)
 - [ErrorCode](docs/ErrorCode.md)
 - [File](docs/File.md)
 - [FileType](docs/FileType.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [JWT](docs/JWT.md)
 - [ListDomainRoles](docs/ListDomainRoles.md)
 - [ListDomainRolesResp](docs/ListDomainRolesResp.md)
 - [ListDomainUsers](docs/ListDomainUsers.md)
 - [ListDomainUsersResp](docs/ListDomainUsersResp.md)
 - [ListDomains](docs/ListDomains.md)
 - [ListDomainsResp](docs/ListDomainsResp.md)
 - [ListProblemGroups](docs/ListProblemGroups.md)
 - [ListProblemGroupsResp](docs/ListProblemGroupsResp.md)
 - [ListProblemSets](docs/ListProblemSets.md)
 - [ListProblemSetsResp](docs/ListProblemSetsResp.md)
 - [ListProblems](docs/ListProblems.md)
 - [ListProblemsResp](docs/ListProblemsResp.md)
 - [ListRecords](docs/ListRecords.md)
 - [ListRecordsResp](docs/ListRecordsResp.md)
 - [ListUsers](docs/ListUsers.md)
 - [ListUsersResp](docs/ListUsersResp.md)
 - [Problem](docs/Problem.md)
 - [ProblemClone](docs/ProblemClone.md)
 - [ProblemConfigEdit](docs/ProblemConfigEdit.md)
 - [ProblemCreate](docs/ProblemCreate.md)
 - [ProblemEdit](docs/ProblemEdit.md)
 - [ProblemGroup](docs/ProblemGroup.md)
 - [ProblemResp](docs/ProblemResp.md)
 - [ProblemSet](docs/ProblemSet.md)
 - [ProblemSetCreate](docs/ProblemSetCreate.md)
 - [ProblemSetEdit](docs/ProblemSetEdit.md)
 - [ProblemSetResp](docs/ProblemSetResp.md)
 - [ProblemSolutionSubmit](docs/ProblemSolutionSubmit.md)
 - [Record](docs/Record.md)
 - [RecordCase](docs/RecordCase.md)
 - [RecordCaseResult](docs/RecordCaseResult.md)
 - [RecordCodeType](docs/RecordCodeType.md)
 - [RecordResp](docs/RecordResp.md)
 - [RecordResult](docs/RecordResult.md)
 - [RecordStatus](docs/RecordStatus.md)
 - [RedirectModel](docs/RedirectModel.md)
 - [Score](docs/Score.md)
 - [ScoreBoard](docs/ScoreBoard.md)
 - [ScoreBoardResp](docs/ScoreBoardResp.md)
 - [SortEnum](docs/SortEnum.md)
 - [User](docs/User.md)
 - [UserBase](docs/UserBase.md)
 - [UserBaseResp](docs/UserBaseResp.md)
 - [UserResp](docs/UserResp.md)
 - [UserScore](docs/UserScore.md)
 - [ValidationError](docs/ValidationError.md)
 - [Version](docs/Version.md)

## Documentation For Authorization


## HTTPBearer



## Author


