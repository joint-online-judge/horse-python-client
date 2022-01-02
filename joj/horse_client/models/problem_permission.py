# coding: utf-8

"""
    JOJ Horse

    Git version: df076fe@2022-01-02T17:18:29Z  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProblemPermission(object):
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
        'submit': 'bool',
        'edit': 'bool',
        'view_config': 'bool'
    }

    attribute_map = {
        'create': 'create',
        'view': 'view',
        'view_hidden': 'viewHidden',
        'submit': 'submit',
        'edit': 'edit',
        'view_config': 'viewConfig'
    }

    def __init__(self, create=False, view=True, view_hidden=False, submit=True, edit=False, view_config=False):  # noqa: E501
        """ProblemPermission - a model defined in Swagger"""  # noqa: E501
        self._create = None
        self._view = None
        self._view_hidden = None
        self._submit = None
        self._edit = None
        self._view_config = None
        self.discriminator = None
        if create is not None:
            self.create = create
        if view is not None:
            self.view = view
        if view_hidden is not None:
            self.view_hidden = view_hidden
        if submit is not None:
            self.submit = submit
        if edit is not None:
            self.edit = edit
        if view_config is not None:
            self.view_config = view_config

    @property
    def create(self):
        """Gets the create of this ProblemPermission.  # noqa: E501


        :return: The create of this ProblemPermission.  # noqa: E501
        :rtype: bool
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this ProblemPermission.


        :param create: The create of this ProblemPermission.  # noqa: E501
        :type: bool
        """

        self._create = create

    @property
    def view(self):
        """Gets the view of this ProblemPermission.  # noqa: E501


        :return: The view of this ProblemPermission.  # noqa: E501
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this ProblemPermission.


        :param view: The view of this ProblemPermission.  # noqa: E501
        :type: bool
        """

        self._view = view

    @property
    def view_hidden(self):
        """Gets the view_hidden of this ProblemPermission.  # noqa: E501


        :return: The view_hidden of this ProblemPermission.  # noqa: E501
        :rtype: bool
        """
        return self._view_hidden

    @view_hidden.setter
    def view_hidden(self, view_hidden):
        """Sets the view_hidden of this ProblemPermission.


        :param view_hidden: The view_hidden of this ProblemPermission.  # noqa: E501
        :type: bool
        """

        self._view_hidden = view_hidden

    @property
    def submit(self):
        """Gets the submit of this ProblemPermission.  # noqa: E501


        :return: The submit of this ProblemPermission.  # noqa: E501
        :rtype: bool
        """
        return self._submit

    @submit.setter
    def submit(self, submit):
        """Sets the submit of this ProblemPermission.


        :param submit: The submit of this ProblemPermission.  # noqa: E501
        :type: bool
        """

        self._submit = submit

    @property
    def edit(self):
        """Gets the edit of this ProblemPermission.  # noqa: E501


        :return: The edit of this ProblemPermission.  # noqa: E501
        :rtype: bool
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        """Sets the edit of this ProblemPermission.


        :param edit: The edit of this ProblemPermission.  # noqa: E501
        :type: bool
        """

        self._edit = edit

    @property
    def view_config(self):
        """Gets the view_config of this ProblemPermission.  # noqa: E501


        :return: The view_config of this ProblemPermission.  # noqa: E501
        :rtype: bool
        """
        return self._view_config

    @view_config.setter
    def view_config(self, view_config):
        """Sets the view_config of this ProblemPermission.


        :param view_config: The view_config of this ProblemPermission.  # noqa: E501
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
        if issubclass(ProblemPermission, dict):
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
        if not isinstance(other, ProblemPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
