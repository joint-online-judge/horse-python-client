# coding: utf-8

"""
    JOJ Horse

    Git version: e54a297@2021-11-30T11:09:19Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemSetPermission(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'create': 'bool',
        'view': 'bool',
        'view_hidden': 'bool',
        'claim': 'bool',
        'scoreboard': 'bool',
        'manage': 'bool',
        'edit': 'bool',
        'view_config': 'bool'
    }

    attribute_map = {
        'create': 'create',
        'view': 'view',
        'view_hidden': 'viewHidden',
        'claim': 'claim',
        'scoreboard': 'scoreboard',
        'manage': 'manage',
        'edit': 'edit',
        'view_config': 'viewConfig'
    }

    def __init__(self, create=False, view=True, view_hidden=False, claim=True, scoreboard=False, manage=False, edit=False, view_config=False):  # noqa: E501
        """ProblemSetPermission - a model defined in Swagger"""  # noqa: E501
        self._create = None
        self._view = None
        self._view_hidden = None
        self._claim = None
        self._scoreboard = None
        self._manage = None
        self._edit = None
        self._view_config = None
        self.discriminator = None
        if create is not None:
            self.create = create
        if view is not None:
            self.view = view
        if view_hidden is not None:
            self.view_hidden = view_hidden
        if claim is not None:
            self.claim = claim
        if scoreboard is not None:
            self.scoreboard = scoreboard
        if manage is not None:
            self.manage = manage
        if edit is not None:
            self.edit = edit
        if view_config is not None:
            self.view_config = view_config

    @property
    def create(self):
        """Gets the create of this ProblemSetPermission.  # noqa: E501


        :return: The create of this ProblemSetPermission.  # noqa: E501
        :rtype: bool
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this ProblemSetPermission.


        :param create: The create of this ProblemSetPermission.  # noqa: E501
        :type: bool
        """

        self._create = create

    @property
    def view(self):
        """Gets the view of this ProblemSetPermission.  # noqa: E501


        :return: The view of this ProblemSetPermission.  # noqa: E501
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this ProblemSetPermission.


        :param view: The view of this ProblemSetPermission.  # noqa: E501
        :type: bool
        """

        self._view = view

    @property
    def view_hidden(self):
        """Gets the view_hidden of this ProblemSetPermission.  # noqa: E501


        :return: The view_hidden of this ProblemSetPermission.  # noqa: E501
        :rtype: bool
        """
        return self._view_hidden

    @view_hidden.setter
    def view_hidden(self, view_hidden):
        """Sets the view_hidden of this ProblemSetPermission.


        :param view_hidden: The view_hidden of this ProblemSetPermission.  # noqa: E501
        :type: bool
        """

        self._view_hidden = view_hidden

    @property
    def claim(self):
        """Gets the claim of this ProblemSetPermission.  # noqa: E501


        :return: The claim of this ProblemSetPermission.  # noqa: E501
        :rtype: bool
        """
        return self._claim

    @claim.setter
    def claim(self, claim):
        """Sets the claim of this ProblemSetPermission.


        :param claim: The claim of this ProblemSetPermission.  # noqa: E501
        :type: bool
        """

        self._claim = claim

    @property
    def scoreboard(self):
        """Gets the scoreboard of this ProblemSetPermission.  # noqa: E501


        :return: The scoreboard of this ProblemSetPermission.  # noqa: E501
        :rtype: bool
        """
        return self._scoreboard

    @scoreboard.setter
    def scoreboard(self, scoreboard):
        """Sets the scoreboard of this ProblemSetPermission.


        :param scoreboard: The scoreboard of this ProblemSetPermission.  # noqa: E501
        :type: bool
        """

        self._scoreboard = scoreboard

    @property
    def manage(self):
        """Gets the manage of this ProblemSetPermission.  # noqa: E501


        :return: The manage of this ProblemSetPermission.  # noqa: E501
        :rtype: bool
        """
        return self._manage

    @manage.setter
    def manage(self, manage):
        """Sets the manage of this ProblemSetPermission.


        :param manage: The manage of this ProblemSetPermission.  # noqa: E501
        :type: bool
        """

        self._manage = manage

    @property
    def edit(self):
        """Gets the edit of this ProblemSetPermission.  # noqa: E501


        :return: The edit of this ProblemSetPermission.  # noqa: E501
        :rtype: bool
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        """Sets the edit of this ProblemSetPermission.


        :param edit: The edit of this ProblemSetPermission.  # noqa: E501
        :type: bool
        """

        self._edit = edit

    @property
    def view_config(self):
        """Gets the view_config of this ProblemSetPermission.  # noqa: E501


        :return: The view_config of this ProblemSetPermission.  # noqa: E501
        :rtype: bool
        """
        return self._view_config

    @view_config.setter
    def view_config(self, view_config):
        """Sets the view_config of this ProblemSetPermission.


        :param view_config: The view_config of this ProblemSetPermission.  # noqa: E501
        :type: bool
        """

        self._view_config = view_config

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
        if issubclass(ProblemSetPermission, dict):
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
        if not isinstance(other, ProblemSetPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
