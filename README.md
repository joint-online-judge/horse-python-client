# horse-python-client
Git version: e2e4bb0@2021-11-27T11:37:00Z

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
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
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Domain Roles
    api_response = api_instance.list_domain_roles_api_v1_admin_domain_roles_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_domain_roles_api_v1_admin_domain_roles_get: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Judgers
    api_response = api_instance.list_judgers_api_v1_admin_judgers_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_judgers_api_v1_admin_judgers_get: %s\n" % e)


# create an instance of the API class
api_instance = joj.horse.client.AdminApi(joj.horse.client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # List Users
    api_response = api_instance.list_users_api_v1_admin_users_get(offset=offset, limit=limit)
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
*AdminApi* | [**list_judgers_api_v1_admin_judgers_get**](docs/AdminApi.md#list_judgers_api_v1_admin_judgers_get) | **GET** /api/v1/admin/judgers | List Judgers
*AdminApi* | [**list_users_api_v1_admin_users_get**](docs/AdminApi.md#list_users_api_v1_admin_users_get) | **GET** /api/v1/admin/users | List Users
*AuthApi* | [**get_token_api_v1_auth_token_get**](docs/AuthApi.md#get_token_api_v1_auth_token_get) | **GET** /api/v1/auth/token | Get Token
*AuthApi* | [**login_api_v1_auth_login_post**](docs/AuthApi.md#login_api_v1_auth_login_post) | **POST** /api/v1/auth/login | Login
*AuthApi* | [**logout_api_v1_auth_logout_post**](docs/AuthApi.md#logout_api_v1_auth_logout_post) | **POST** /api/v1/auth/logout | Logout
*AuthApi* | [**refresh_api_v1_auth_refresh_post**](docs/AuthApi.md#refresh_api_v1_auth_refresh_post) | **POST** /api/v1/auth/refresh | Refresh
*AuthApi* | [**register_api_v1_auth_register_post**](docs/AuthApi.md#register_api_v1_auth_register_post) | **POST** /api/v1/auth/register | Register
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
*DomainApi* | [**get_domain_invitation_api_v1_domains_domain_invitations_invitation_get**](docs/DomainApi.md#get_domain_invitation_api_v1_domains_domain_invitations_invitation_get) | **GET** /api/v1/domains/{domain}/invitations/{invitation} | Get Domain Invitation
*DomainApi* | [**get_domain_role_api_v1_domains_domain_roles_role_get**](docs/DomainApi.md#get_domain_role_api_v1_domains_domain_roles_role_get) | **GET** /api/v1/domains/{domain}/roles/{role} | Get Domain Role
*DomainApi* | [**get_domain_user_api_v1_domains_domain_users_user_get**](docs/DomainApi.md#get_domain_user_api_v1_domains_domain_users_user_get) | **GET** /api/v1/domains/{domain}/users/{user} | Get Domain User
*DomainApi* | [**get_domain_user_permission_api_v1_domains_domain_users_user_permission_get**](docs/DomainApi.md#get_domain_user_permission_api_v1_domains_domain_users_user_permission_get) | **GET** /api/v1/domains/{domain}/users/{user}/permission | Get Domain User Permission
*DomainApi* | [**join_domain_by_invitation_api_v1_domains_domain_join_post**](docs/DomainApi.md#join_domain_by_invitation_api_v1_domains_domain_join_post) | **POST** /api/v1/domains/{domain}/join | Join Domain By Invitation
*DomainApi* | [**list_domain_invitations_api_v1_domains_domain_invitations_get**](docs/DomainApi.md#list_domain_invitations_api_v1_domains_domain_invitations_get) | **GET** /api/v1/domains/{domain}/invitations | List Domain Invitations
*DomainApi* | [**list_domain_roles_api_v1_domains_domain_roles_get**](docs/DomainApi.md#list_domain_roles_api_v1_domains_domain_roles_get) | **GET** /api/v1/domains/{domain}/roles | List Domain Roles
*DomainApi* | [**list_domain_users_api_v1_domains_domain_users_get**](docs/DomainApi.md#list_domain_users_api_v1_domains_domain_users_get) | **GET** /api/v1/domains/{domain}/users | List Domain Users
*DomainApi* | [**list_domains_api_v1_domains_get**](docs/DomainApi.md#list_domains_api_v1_domains_get) | **GET** /api/v1/domains | List Domains
*DomainApi* | [**remove_domain_user_api_v1_domains_domain_users_user_delete**](docs/DomainApi.md#remove_domain_user_api_v1_domains_domain_users_user_delete) | **DELETE** /api/v1/domains/{domain}/users/{user} | Remove Domain User
*DomainApi* | [**search_domain_candidates_api_v1_domains_domain_candidates_get**](docs/DomainApi.md#search_domain_candidates_api_v1_domains_domain_candidates_get) | **GET** /api/v1/domains/{domain}/candidates | Search Domain Candidates
*DomainApi* | [**transfer_domain_api_v1_domains_domain_transfer_post**](docs/DomainApi.md#transfer_domain_api_v1_domains_domain_transfer_post) | **POST** /api/v1/domains/{domain}/transfer | Transfer Domain
*DomainApi* | [**update_domain_api_v1_domains_domain_patch**](docs/DomainApi.md#update_domain_api_v1_domains_domain_patch) | **PATCH** /api/v1/domains/{domain} | Update Domain
*DomainApi* | [**update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch**](docs/DomainApi.md#update_domain_invitation_api_v1_domains_domain_invitations_invitation_patch) | **PATCH** /api/v1/domains/{domain}/invitations/{invitation} | Update Domain Invitation
*DomainApi* | [**update_domain_role_api_v1_domains_domain_roles_role_patch**](docs/DomainApi.md#update_domain_role_api_v1_domains_domain_roles_role_patch) | **PATCH** /api/v1/domains/{domain}/roles/{role} | Update Domain Role
*DomainApi* | [**update_domain_user_api_v1_domains_domain_users_user_patch**](docs/DomainApi.md#update_domain_user_api_v1_domains_domain_users_user_patch) | **PATCH** /api/v1/domains/{domain}/users/{user} | Update Domain User
*JudgeApi* | [**claim_record_by_judge_api_v1_judge_records_record_claim_post**](docs/JudgeApi.md#claim_record_by_judge_api_v1_judge_records_record_claim_post) | **POST** /api/v1/judge/records/{record}/claim | Claim Record By Judge
*JudgeApi* | [**get_judge_key_api_v1_judge_key_get**](docs/JudgeApi.md#get_judge_key_api_v1_judge_key_get) | **GET** /api/v1/judge/key | Get Judge Key
*JudgeApi* | [**submit_record_by_judge_api_v1_judge_records_record_judgment_post**](docs/JudgeApi.md#submit_record_by_judge_api_v1_judge_records_record_judgment_post) | **POST** /api/v1/judge/records/{record}/judgment | Submit Record By Judge
*JudgeApi* | [**update_record_state_by_judge_api_v1_judge_records_record_state_post**](docs/JudgeApi.md#update_record_state_by_judge_api_v1_judge_records_record_state_post) | **POST** /api/v1/judge/records/{record}/state | Update Record State By Judge
*MiscellaneousApi* | [**jwt_decoded_api_v1_jwt_decoded_get**](docs/MiscellaneousApi.md#jwt_decoded_api_v1_jwt_decoded_get) | **GET** /api/v1/jwt_decoded | Jwt Decoded
*MiscellaneousApi* | [**set_root_user_api_v1_set_root_user_post**](docs/MiscellaneousApi.md#set_root_user_api_v1_set_root_user_post) | **POST** /api/v1/set_root_user | Set Root User
*MiscellaneousApi* | [**test_error_report_api_v1_test_report_get**](docs/MiscellaneousApi.md#test_error_report_api_v1_test_report_get) | **GET** /api/v1/test/report | Test Error Report
*MiscellaneousApi* | [**version_api_v1_version_get**](docs/MiscellaneousApi.md#version_api_v1_version_get) | **GET** /api/v1/version | Version
*ProblemApi* | [**clone_problem_api_v1_domains_domain_problems_clone_post**](docs/ProblemApi.md#clone_problem_api_v1_domains_domain_problems_clone_post) | **POST** /api/v1/domains/{domain}/problems/clone | Clone Problem
*ProblemApi* | [**create_problem_api_v1_domains_domain_problems_post**](docs/ProblemApi.md#create_problem_api_v1_domains_domain_problems_post) | **POST** /api/v1/domains/{domain}/problems | Create Problem
*ProblemApi* | [**delete_problem_api_v1_domains_domain_problems_problem_delete**](docs/ProblemApi.md#delete_problem_api_v1_domains_domain_problems_problem_delete) | **DELETE** /api/v1/domains/{domain}/problems/{problem} | Delete Problem
*ProblemApi* | [**get_problem_api_v1_domains_domain_problems_problem_get**](docs/ProblemApi.md#get_problem_api_v1_domains_domain_problems_problem_get) | **GET** /api/v1/domains/{domain}/problems/{problem} | Get Problem
*ProblemApi* | [**list_problems_api_v1_domains_domain_problems_get**](docs/ProblemApi.md#list_problems_api_v1_domains_domain_problems_get) | **GET** /api/v1/domains/{domain}/problems | List Problems
*ProblemApi* | [**submit_solution_to_problem_api_v1_domains_domain_problems_problem_post**](docs/ProblemApi.md#submit_solution_to_problem_api_v1_domains_domain_problems_problem_post) | **POST** /api/v1/domains/{domain}/problems/{problem} | Submit Solution To Problem
*ProblemApi* | [**update_problem_api_v1_domains_domain_problems_problem_patch**](docs/ProblemApi.md#update_problem_api_v1_domains_domain_problems_problem_patch) | **PATCH** /api/v1/domains/{domain}/problems/{problem} | Update Problem
*ProblemConfigApi* | [**commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post**](docs/ProblemConfigApi.md#commit_problem_config_api_v1_domains_domain_problems_problem_config_commit_post) | **POST** /api/v1/domains/{domain}/problems/{problem}/config/commit | Commit Problem Config
*ProblemConfigApi* | [**delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete**](docs/ProblemConfigApi.md#delete_directory_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_dirs_path_delete) | **DELETE** /api/v1/domains/{domain}/problems/{problem}/config/dirs/{path} | Delete Directory From Uncommitted Problem Config
*ProblemConfigApi* | [**delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete**](docs/ProblemConfigApi.md#delete_file_from_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_delete) | **DELETE** /api/v1/domains/{domain}/problems/{problem}/config/files/{path} | Delete File From Uncommitted Problem Config
*ProblemConfigApi* | [**download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get**](docs/ProblemConfigApi.md#download_file_in_problem_config_api_v1_domains_domain_problems_problem_configs_config_files_path_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/configs/{config}/files/{path} | Download File In Problem Config
*ProblemConfigApi* | [**download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get**](docs/ProblemConfigApi.md#download_file_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_files_path_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/config/files/{path} | Download File In Uncommitted Problem Config
*ProblemConfigApi* | [**download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get**](docs/ProblemConfigApi.md#download_problem_config_archive_api_v1_domains_domain_problems_problem_configs_config_files_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/configs/{config}/files | Download Problem Config Archive
*ProblemConfigApi* | [**download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get**](docs/ProblemConfigApi.md#download_uncommitted_problem_config_as_archive_api_v1_domains_domain_problems_problem_config_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/config | Download Uncommitted Problem Config As Archive
*ProblemConfigApi* | [**get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get**](docs/ProblemConfigApi.md#get_file_or_directory_info_in_uncommitted_problem_config_api_v1_domains_domain_problems_problem_config_file_info_path_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/config/file_info/{path} | Get File Or Directory Info In Uncommitted Problem Config
*ProblemConfigApi* | [**get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get**](docs/ProblemConfigApi.md#get_problem_config_json_api_v1_domains_domain_problems_problem_configs_config_get) | **GET** /api/v1/domains/{domain}/problems/{problem}/configs/{config} | Get Problem Config Json
*ProblemConfigApi* | [**reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post**](docs/ProblemConfigApi.md#reset_problem_config_api_v1_domains_domain_problems_problem_config_reset_post) | **POST** /api/v1/domains/{domain}/problems/{problem}/config/reset | Reset Problem Config
*ProblemConfigApi* | [**update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put**](docs/ProblemConfigApi.md#update_problem_config_by_archive_api_v1_domains_domain_problems_problem_config_put) | **PUT** /api/v1/domains/{domain}/problems/{problem}/config | Update Problem Config By Archive
*ProblemConfigApi* | [**upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put**](docs/ProblemConfigApi.md#upload_file_to_problem_config_api_v1_domains_domain_problems_problem_config_files_path_put) | **PUT** /api/v1/domains/{domain}/problems/{problem}/config/files/{path} | Upload File To Problem Config
*ProblemConfigApi* | [**upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put**](docs/ProblemConfigApi.md#upload_file_to_root_in_problem_config_api_v1_domains_domain_problems_problem_config_files_put) | **PUT** /api/v1/domains/{domain}/problems/{problem}/config/files | Upload File To Root In Problem Config
*ProblemGroupApi* | [**list_problem_groups_api_v1_problem_groups_get**](docs/ProblemGroupApi.md#list_problem_groups_api_v1_problem_groups_get) | **GET** /api/v1/problem_groups | List Problem Groups
*ProblemSetApi* | [**add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_post**](docs/ProblemSetApi.md#add_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_post) | **POST** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem | Add Problem In Problem Set
*ProblemSetApi* | [**create_problem_set_api_v1_domains_domain_problem_sets_post**](docs/ProblemSetApi.md#create_problem_set_api_v1_domains_domain_problem_sets_post) | **POST** /api/v1/domains/{domain}/problem_sets | Create Problem Set
*ProblemSetApi* | [**delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_delete**](docs/ProblemSetApi.md#delete_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_delete) | **DELETE** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem/{problem} | Delete Problem In Problem Set
*ProblemSetApi* | [**delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete**](docs/ProblemSetApi.md#delete_problem_set_api_v1_domains_domain_problem_sets_problem_set_delete) | **DELETE** /api/v1/domains/{domain}/problem_sets/{problemSet} | Delete Problem Set
*ProblemSetApi* | [**get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_get**](docs/ProblemSetApi.md#get_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem/{problem} | Get Problem In Problem Set
*ProblemSetApi* | [**get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get**](docs/ProblemSetApi.md#get_problem_set_api_v1_domains_domain_problem_sets_problem_set_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problemSet} | Get Problem Set
*ProblemSetApi* | [**get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get**](docs/ProblemSetApi.md#get_scoreboard_api_v1_domains_domain_problem_sets_problem_set_scoreboard_get) | **GET** /api/v1/domains/{domain}/problem_sets/{problemSet}/scoreboard | Get Scoreboard
*ProblemSetApi* | [**list_problem_sets_api_v1_domains_domain_problem_sets_get**](docs/ProblemSetApi.md#list_problem_sets_api_v1_domains_domain_problem_sets_get) | **GET** /api/v1/domains/{domain}/problem_sets | List Problem Sets
*ProblemSetApi* | [**submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_submit_post**](docs/ProblemSetApi.md#submit_solution_to_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_submit_post) | **POST** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem/{problem}/submit | Submit Solution To Problem Set
*ProblemSetApi* | [**update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_patch**](docs/ProblemSetApi.md#update_problem_in_problem_set_api_v1_domains_domain_problem_sets_problem_set_problem_problem_patch) | **PATCH** /api/v1/domains/{domain}/problem_sets/{problemSet}/problem/{problem} | Update Problem In Problem Set
*ProblemSetApi* | [**update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch**](docs/ProblemSetApi.md#update_problem_set_api_v1_domains_domain_problem_sets_problem_set_patch) | **PATCH** /api/v1/domains/{domain}/problem_sets/{problemSet} | Update Problem Set
*RecordApi* | [**get_record_api_v1_domains_domain_records_record_get**](docs/RecordApi.md#get_record_api_v1_domains_domain_records_record_get) | **GET** /api/v1/domains/{domain}/records/{record} | Get Record
*RecordApi* | [**get_record_code_api_v1_domains_domain_records_record_code_get**](docs/RecordApi.md#get_record_code_api_v1_domains_domain_records_record_code_get) | **GET** /api/v1/domains/{domain}/records/{record}/code | Get Record Code
*RecordApi* | [**list_records_in_domain_api_v1_domains_domain_records_get**](docs/RecordApi.md#list_records_in_domain_api_v1_domains_domain_records_get) | **GET** /api/v1/domains/{domain}/records | List Records In Domain
*UserApi* | [**get_user_api_v1_user_get**](docs/UserApi.md#get_user_api_v1_user_get) | **GET** /api/v1/user | Get User
*UserApi* | [**get_user_api_v1_users_uid_get**](docs/UserApi.md#get_user_api_v1_users_uid_get) | **GET** /api/v1/users/{uid} | Get User
*UserApi* | [**get_user_problems_api_v1_user_problems_get**](docs/UserApi.md#get_user_problems_api_v1_user_problems_get) | **GET** /api/v1/user/problems | Get User Problems
*UserApi* | [**get_user_problems_api_v1_users_uid_problems_get**](docs/UserApi.md#get_user_problems_api_v1_users_uid_problems_get) | **GET** /api/v1/users/{uid}/problems | Get User Problems
*UserApi* | [**list_user_domains_api_v1_users_uid_domains_get**](docs/UserApi.md#list_user_domains_api_v1_users_uid_domains_get) | **GET** /api/v1/users/{uid}/domains | List User Domains
*UserApi* | [**list_users_api_v1_users_get**](docs/UserApi.md#list_users_api_v1_users_get) | **GET** /api/v1/users | List Users

## Documentation For Models

 - [AllOfDomainPermissionGeneral](docs/AllOfDomainPermissionGeneral.md)
 - [AllOfDomainPermissionProblem](docs/AllOfDomainPermissionProblem.md)
 - [AllOfDomainPermissionProblemSet](docs/AllOfDomainPermissionProblemSet.md)
 - [AllOfDomainPermissionRecord](docs/AllOfDomainPermissionRecord.md)
 - [AllOfDomainUserAddRole](docs/AllOfDomainUserAddRole.md)
 - [AllOfDomainUserUpdateRole](docs/AllOfDomainUserUpdateRole.md)
 - [AllOfRecordState](docs/AllOfRecordState.md)
 - [AnyOfFileInfoMtime](docs/AnyOfFileInfoMtime.md)
 - [ArchiveFormat](docs/ArchiveFormat.md)
 - [ArchiveFormat1](docs/ArchiveFormat1.md)
 - [ArchiveType](docs/ArchiveType.md)
 - [AuthTokens](docs/AuthTokens.md)
 - [AuthTokensResp](docs/AuthTokensResp.md)
 - [DefaultRole](docs/DefaultRole.md)
 - [Detail](docs/Detail.md)
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
 - [JWT](docs/JWT.md)
 - [JWTAccessToken](docs/JWTAccessToken.md)
 - [JWTAccessTokenResp](docs/JWTAccessTokenResp.md)
 - [JudgeClaim](docs/JudgeClaim.md)
 - [JudgeClaimResp](docs/JudgeClaimResp.md)
 - [LakeFSReset](docs/LakeFSReset.md)
 - [OAuth2PasswordRequestForm](docs/OAuth2PasswordRequestForm.md)
 - [Problem](docs/Problem.md)
 - [ProblemClone](docs/ProblemClone.md)
 - [ProblemConfig](docs/ProblemConfig.md)
 - [ProblemConfigCommit](docs/ProblemConfigCommit.md)
 - [ProblemConfigResp](docs/ProblemConfigResp.md)
 - [ProblemCreate](docs/ProblemCreate.md)
 - [ProblemDetail](docs/ProblemDetail.md)
 - [ProblemDetailResp](docs/ProblemDetailResp.md)
 - [ProblemEdit](docs/ProblemEdit.md)
 - [ProblemGroup](docs/ProblemGroup.md)
 - [ProblemGroupList](docs/ProblemGroupList.md)
 - [ProblemGroupListResp](docs/ProblemGroupListResp.md)
 - [ProblemList](docs/ProblemList.md)
 - [ProblemListResp](docs/ProblemListResp.md)
 - [ProblemPermission](docs/ProblemPermission.md)
 - [ProblemPreview](docs/ProblemPreview.md)
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
 - [Record](docs/Record.md)
 - [RecordCodeType](docs/RecordCodeType.md)
 - [RecordList](docs/RecordList.md)
 - [RecordListResp](docs/RecordListResp.md)
 - [RecordPermission](docs/RecordPermission.md)
 - [RecordResp](docs/RecordResp.md)
 - [RecordResult](docs/RecordResult.md)
 - [RecordState](docs/RecordState.md)
 - [Score](docs/Score.md)
 - [ScoreBoard](docs/ScoreBoard.md)
 - [ScoreBoardResp](docs/ScoreBoardResp.md)
 - [User](docs/User.md)
 - [UserAccessKey](docs/UserAccessKey.md)
 - [UserAccessKeyResp](docs/UserAccessKeyResp.md)
 - [UserCreate](docs/UserCreate.md)
 - [UserDetail](docs/UserDetail.md)
 - [UserDetailResp](docs/UserDetailResp.md)
 - [UserList](docs/UserList.md)
 - [UserListResp](docs/UserListResp.md)
 - [UserResp](docs/UserResp.md)
 - [UserScore](docs/UserScore.md)
 - [UserWithDomainRole](docs/UserWithDomainRole.md)
 - [UserWithDomainRoleList](docs/UserWithDomainRoleList.md)
 - [UserWithDomainRoleListResp](docs/UserWithDomainRoleListResp.md)
 - [UserWithDomainRoleResp](docs/UserWithDomainRoleResp.md)
 - [ValidationError](docs/ValidationError.md)
 - [Version](docs/Version.md)

## Documentation For Authorization


## HTTPBearer



## Author


