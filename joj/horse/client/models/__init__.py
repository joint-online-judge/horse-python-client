# coding: utf-8

# flake8: noqa
"""
    JOJ Horse

    Git version: bd11f07@2021-11-03T11:20:31Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from joj.horse.client.models.all_of_domain_permission_general import AllOfDomainPermissionGeneral
from joj.horse.client.models.all_of_domain_permission_problem import AllOfDomainPermissionProblem
from joj.horse.client.models.all_of_domain_permission_problem_set import AllOfDomainPermissionProblemSet
from joj.horse.client.models.all_of_domain_permission_record import AllOfDomainPermissionRecord
from joj.horse.client.models.all_of_domain_role_create_permission import AllOfDomainRoleCreatePermission
from joj.horse.client.models.all_of_domain_user_add_role import AllOfDomainUserAddRole
from joj.horse.client.models.all_of_domain_user_update_role import AllOfDomainUserUpdateRole
from joj.horse.client.models.all_of_record_case_status import AllOfRecordCaseStatus
from joj.horse.client.models.auth_tokens import AuthTokens
from joj.horse.client.models.auth_tokens_resp import AuthTokensResp
from joj.horse.client.models.body_login_api_v1_auth_login_post import BodyLoginApiV1AuthLoginPost
from joj.horse.client.models.default_role import DefaultRole
from joj.horse.client.models.detail import Detail
from joj.horse.client.models.domain import Domain
from joj.horse.client.models.domain_create import DomainCreate
from joj.horse.client.models.domain_edit import DomainEdit
from joj.horse.client.models.domain_invitation import DomainInvitation
from joj.horse.client.models.domain_invitation_create import DomainInvitationCreate
from joj.horse.client.models.domain_invitation_edit import DomainInvitationEdit
from joj.horse.client.models.domain_invitation_resp import DomainInvitationResp
from joj.horse.client.models.domain_list import DomainList
from joj.horse.client.models.domain_list_resp import DomainListResp
from joj.horse.client.models.domain_permission import DomainPermission
from joj.horse.client.models.domain_resp import DomainResp
from joj.horse.client.models.domain_role import DomainRole
from joj.horse.client.models.domain_role_create import DomainRoleCreate
from joj.horse.client.models.domain_role_edit import DomainRoleEdit
from joj.horse.client.models.domain_role_list import DomainRoleList
from joj.horse.client.models.domain_role_list_resp import DomainRoleListResp
from joj.horse.client.models.domain_role_resp import DomainRoleResp
from joj.horse.client.models.domain_transfer import DomainTransfer
from joj.horse.client.models.domain_user import DomainUser
from joj.horse.client.models.domain_user_add import DomainUserAdd
from joj.horse.client.models.domain_user_list import DomainUserList
from joj.horse.client.models.domain_user_list_resp import DomainUserListResp
from joj.horse.client.models.domain_user_permission import DomainUserPermission
from joj.horse.client.models.domain_user_permission_resp import DomainUserPermissionResp
from joj.horse.client.models.domain_user_resp import DomainUserResp
from joj.horse.client.models.domain_user_update import DomainUserUpdate
from joj.horse.client.models.empty import Empty
from joj.horse.client.models.empty_resp import EmptyResp
from joj.horse.client.models.error_code import ErrorCode
from joj.horse.client.models.general_permission import GeneralPermission
from joj.horse.client.models.http_validation_error import HTTPValidationError
from joj.horse.client.models.jwt import JWT
from joj.horse.client.models.jwt_access_token import JWTAccessToken
from joj.horse.client.models.jwt_access_token_resp import JWTAccessTokenResp
from joj.horse.client.models.joj_horse_models_problem_set_problem_set import JojHorseModelsProblemSetProblemSet
from joj.horse.client.models.joj_horse_models_record_record import JojHorseModelsRecordRecord
from joj.horse.client.models.joj_horse_schemas_problem_set_problem_set import JojHorseSchemasProblemSetProblemSet
from joj.horse.client.models.joj_horse_schemas_record_record import JojHorseSchemasRecordRecord
from joj.horse.client.models.list_problem_sets import ListProblemSets
from joj.horse.client.models.list_problem_sets_resp import ListProblemSetsResp
from joj.horse.client.models.list_records import ListRecords
from joj.horse.client.models.list_records_resp import ListRecordsResp
from joj.horse.client.models.problem import Problem
from joj.horse.client.models.problem_clone import ProblemClone
from joj.horse.client.models.problem_config_edit import ProblemConfigEdit
from joj.horse.client.models.problem_create import ProblemCreate
from joj.horse.client.models.problem_edit import ProblemEdit
from joj.horse.client.models.problem_group import ProblemGroup
from joj.horse.client.models.problem_group_list import ProblemGroupList
from joj.horse.client.models.problem_group_list_resp import ProblemGroupListResp
from joj.horse.client.models.problem_list import ProblemList
from joj.horse.client.models.problem_list_resp import ProblemListResp
from joj.horse.client.models.problem_permission import ProblemPermission
from joj.horse.client.models.problem_resp import ProblemResp
from joj.horse.client.models.problem_set_create import ProblemSetCreate
from joj.horse.client.models.problem_set_edit import ProblemSetEdit
from joj.horse.client.models.problem_set_permission import ProblemSetPermission
from joj.horse.client.models.problem_set_resp import ProblemSetResp
from joj.horse.client.models.problem_solution_submit import ProblemSolutionSubmit
from joj.horse.client.models.record_case import RecordCase
from joj.horse.client.models.record_case_result import RecordCaseResult
from joj.horse.client.models.record_code_type import RecordCodeType
from joj.horse.client.models.record_permission import RecordPermission
from joj.horse.client.models.record_resp import RecordResp
from joj.horse.client.models.record_result import RecordResult
from joj.horse.client.models.record_status import RecordStatus
from joj.horse.client.models.score import Score
from joj.horse.client.models.score_board import ScoreBoard
from joj.horse.client.models.score_board_resp import ScoreBoardResp
from joj.horse.client.models.user import User
from joj.horse.client.models.user_base import UserBase
from joj.horse.client.models.user_base_list import UserBaseList
from joj.horse.client.models.user_base_list_resp import UserBaseListResp
from joj.horse.client.models.user_base_resp import UserBaseResp
from joj.horse.client.models.user_create import UserCreate
from joj.horse.client.models.user_detail import UserDetail
from joj.horse.client.models.user_detail_resp import UserDetailResp
from joj.horse.client.models.user_list import UserList
from joj.horse.client.models.user_list_resp import UserListResp
from joj.horse.client.models.user_resp import UserResp
from joj.horse.client.models.user_score import UserScore
from joj.horse.client.models.validation_error import ValidationError
from joj.horse.client.models.version import Version
