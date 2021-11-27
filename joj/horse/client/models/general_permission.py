# coding: utf-8

"""
    JOJ Horse

    Git version: f6a791e@2021-11-27T07:58:36Z  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GeneralPermission(object):
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
        'view': 'bool',
        'edit_permission': 'bool',
        'view_mod_badge': 'bool',
        'edit': 'bool',
        'unlimited_quota': 'bool'
    }

    attribute_map = {
        'view': 'view',
        'edit_permission': 'editPermission',
        'view_mod_badge': 'viewModBadge',
        'edit': 'edit',
        'unlimited_quota': 'unlimitedQuota'
    }

    def __init__(self, view=True, edit_permission=False, view_mod_badge=True, edit=False, unlimited_quota=False):  # noqa: E501
        """GeneralPermission - a model defined in Swagger"""  # noqa: E501
        self._view = None
        self._edit_permission = None
        self._view_mod_badge = None
        self._edit = None
        self._unlimited_quota = None
        self.discriminator = None
        if view is not None:
            self.view = view
        if edit_permission is not None:
            self.edit_permission = edit_permission
        if view_mod_badge is not None:
            self.view_mod_badge = view_mod_badge
        if edit is not None:
            self.edit = edit
        if unlimited_quota is not None:
            self.unlimited_quota = unlimited_quota

    @property
    def view(self):
        """Gets the view of this GeneralPermission.  # noqa: E501


        :return: The view of this GeneralPermission.  # noqa: E501
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this GeneralPermission.


        :param view: The view of this GeneralPermission.  # noqa: E501
        :type: bool
        """

        self._view = view

    @property
    def edit_permission(self):
        """Gets the edit_permission of this GeneralPermission.  # noqa: E501


        :return: The edit_permission of this GeneralPermission.  # noqa: E501
        :rtype: bool
        """
        return self._edit_permission

    @edit_permission.setter
    def edit_permission(self, edit_permission):
        """Sets the edit_permission of this GeneralPermission.


        :param edit_permission: The edit_permission of this GeneralPermission.  # noqa: E501
        :type: bool
        """

        self._edit_permission = edit_permission

    @property
    def view_mod_badge(self):
        """Gets the view_mod_badge of this GeneralPermission.  # noqa: E501


        :return: The view_mod_badge of this GeneralPermission.  # noqa: E501
        :rtype: bool
        """
        return self._view_mod_badge

    @view_mod_badge.setter
    def view_mod_badge(self, view_mod_badge):
        """Sets the view_mod_badge of this GeneralPermission.


        :param view_mod_badge: The view_mod_badge of this GeneralPermission.  # noqa: E501
        :type: bool
        """

        self._view_mod_badge = view_mod_badge

    @property
    def edit(self):
        """Gets the edit of this GeneralPermission.  # noqa: E501


        :return: The edit of this GeneralPermission.  # noqa: E501
        :rtype: bool
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        """Sets the edit of this GeneralPermission.


        :param edit: The edit of this GeneralPermission.  # noqa: E501
        :type: bool
        """

        self._edit = edit

    @property
    def unlimited_quota(self):
        """Gets the unlimited_quota of this GeneralPermission.  # noqa: E501


        :return: The unlimited_quota of this GeneralPermission.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_quota

    @unlimited_quota.setter
    def unlimited_quota(self, unlimited_quota):
        """Sets the unlimited_quota of this GeneralPermission.


        :param unlimited_quota: The unlimited_quota of this GeneralPermission.  # noqa: E501
        :type: bool
        """

        self._unlimited_quota = unlimited_quota

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
        if issubclass(GeneralPermission, dict):
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
        if not isinstance(other, GeneralPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
