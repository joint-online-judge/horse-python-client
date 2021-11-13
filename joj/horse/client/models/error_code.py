# coding: utf-8

"""
    JOJ Horse

    Git version: bef9fbf@2021-11-13T17:48:31Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ErrorCode(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    SUCCESS = "Success"
    ERROR = "Error"
    INTERNALSERVERERROR = "InternalServerError"
    UNKNOWNFIELDERROR = "UnknownFieldError"
    ILLEGALFIELDERROR = "IllegalFieldError"
    INTEGRITYERROR = "IntegrityError"
    APINOTIMPLEMENTEDERROR = "APINotImplementedError"
    USERNOTFOUNDERROR = "UserNotFoundError"
    USERREGISTERERROR = "UserRegisterError"
    DOMAINNOTFOUNDERROR = "DomainNotFoundError"
    INVALIDURLERROR = "InvalidUrlError"
    PROBLEMNOTFOUNDERROR = "ProblemNotFoundError"
    PROBLEMSETNOTFOUNDERROR = "ProblemSetNotFoundError"
    PROBLEMGROUPNOTFOUNDERROR = "ProblemGroupNotFoundError"
    RECORDNOTFOUNDERROR = "RecordNotFoundError"
    DELETEPROBLEMBADREQUESTERROR = "DeleteProblemBadRequestError"
    USERALREADYINDOMAINBADREQUESTERROR = "UserAlreadyInDomainBadRequestError"
    DOMAININVITATIONBADREQUESTERROR = "DomainInvitationBadRequestError"
    SCOREBOARDHIDDENBADREQUESTERROR = "ScoreboardHiddenBadRequestError"
    PROBLEMSETBEFOREAVAILABLEERROR = "ProblemSetBeforeAvailableError"
    PROBLEMSETAFTERDUEERROR = "ProblemSetAfterDueError"
    USERNOTJUDGERERROR = "UserNotJudgerError"
    DOMAINNOTOWNERERROR = "DomainNotOwnerError"
    DOMAINNOTROOTERROR = "DomainNotRootError"
    DOMAINROLENOTFOUNDERROR = "DomainRoleNotFoundError"
    DOMAINROLENOTUNIQUEERROR = "DomainRoleNotUniqueError"
    DOMAINROLEREADONLYERROR = "DomainRoleReadOnlyError"
    DOMAINROLEUSEDERROR = "DomainRoleUsedError"
    DOMAINUSERNOTFOUNDERROR = "DomainUserNotFoundError"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """ErrorCode - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ErrorCode, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ErrorCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
