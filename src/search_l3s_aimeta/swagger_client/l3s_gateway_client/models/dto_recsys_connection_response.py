# coding: utf-8

"""
    L3S Gateway for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoRecsysConnectionResponse(object):
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
        'host_url': 'str',
        'status': 'str'
    }

    attribute_map = {
        'host_url': 'host_url',
        'status': 'status'
    }

    def __init__(self, host_url=None, status=None):  # noqa: E501
        """DtoRecsysConnectionResponse - a model defined in Swagger"""  # noqa: E501
        self._host_url = None
        self._status = None
        self.discriminator = None
        if host_url is not None:
            self.host_url = host_url
        if status is not None:
            self.status = status

    @property
    def host_url(self):
        """Gets the host_url of this DtoRecsysConnectionResponse.  # noqa: E501


        :return: The host_url of this DtoRecsysConnectionResponse.  # noqa: E501
        :rtype: str
        """
        return self._host_url

    @host_url.setter
    def host_url(self, host_url):
        """Sets the host_url of this DtoRecsysConnectionResponse.


        :param host_url: The host_url of this DtoRecsysConnectionResponse.  # noqa: E501
        :type: str
        """

        self._host_url = host_url

    @property
    def status(self):
        """Gets the status of this DtoRecsysConnectionResponse.  # noqa: E501


        :return: The status of this DtoRecsysConnectionResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DtoRecsysConnectionResponse.


        :param status: The status of this DtoRecsysConnectionResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(DtoRecsysConnectionResponse, dict):
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
        if not isinstance(other, DtoRecsysConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
