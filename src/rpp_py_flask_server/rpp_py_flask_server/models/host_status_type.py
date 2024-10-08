from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class HostStatusType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, lang=None, s=None):  # noqa: E501
        """HostStatusType - a model defined in OpenAPI

        :param value: The value of this HostStatusType.  # noqa: E501
        :type value: str
        :param lang: The lang of this HostStatusType.  # noqa: E501
        :type lang: str
        :param s: The s of this HostStatusType.  # noqa: E501
        :type s: str
        """
        self.openapi_types = {
            'value': str,
            'lang': str,
            's': str
        }

        self.attribute_map = {
            'value': '#value',
            'lang': '@lang',
            's': '@s'
        }

        self._value = value
        self._lang = lang
        self._s = s

    @classmethod
    def from_dict(cls, dikt) -> 'HostStatusType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The host_statusType of this HostStatusType.  # noqa: E501
        :rtype: HostStatusType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this HostStatusType.


        :return: The value of this HostStatusType.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this HostStatusType.


        :param value: The value of this HostStatusType.
        :type value: str
        """

        self._value = value

    @property
    def lang(self) -> str:
        """Gets the lang of this HostStatusType.


        :return: The lang of this HostStatusType.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang: str):
        """Sets the lang of this HostStatusType.


        :param lang: The lang of this HostStatusType.
        :type lang: str
        """

        self._lang = lang

    @property
    def s(self) -> str:
        """Gets the s of this HostStatusType.


        :return: The s of this HostStatusType.
        :rtype: str
        """
        return self._s

    @s.setter
    def s(self, s: str):
        """Sets the s of this HostStatusType.


        :param s: The s of this HostStatusType.
        :type s: str
        """
        allowed_values = ["clientDeleteProhibited", "clientUpdateProhibited", "linked", "ok", "pendingCreate", "pendingDelete", "pendingTransfer", "pendingUpdate", "serverDeleteProhibited", "serverUpdateProhibited"]  # noqa: E501
        if s not in allowed_values:
            raise ValueError(
                "Invalid value for `s` ({0}), must be one of {1}"
                .format(s, allowed_values)
            )

        self._s = s
