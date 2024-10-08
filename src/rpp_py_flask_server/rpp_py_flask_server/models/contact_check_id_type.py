from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class ContactCheckIDType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, avail=None):  # noqa: E501
        """ContactCheckIDType - a model defined in OpenAPI

        :param value: The value of this ContactCheckIDType.  # noqa: E501
        :type value: str
        :param avail: The avail of this ContactCheckIDType.  # noqa: E501
        :type avail: bool
        """
        self.openapi_types = {
            'value': str,
            'avail': bool
        }

        self.attribute_map = {
            'value': '#value',
            'avail': '@avail'
        }

        self._value = value
        self._avail = avail

    @classmethod
    def from_dict(cls, dikt) -> 'ContactCheckIDType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The contact_checkIDType of this ContactCheckIDType.  # noqa: E501
        :rtype: ContactCheckIDType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this ContactCheckIDType.


        :return: The value of this ContactCheckIDType.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this ContactCheckIDType.


        :param value: The value of this ContactCheckIDType.
        :type value: str
        """
        if value is not None and len(value) > 16:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `16`")  # noqa: E501
        if value is not None and len(value) < 3:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `3`")  # noqa: E501

        self._value = value

    @property
    def avail(self) -> bool:
        """Gets the avail of this ContactCheckIDType.


        :return: The avail of this ContactCheckIDType.
        :rtype: bool
        """
        return self._avail

    @avail.setter
    def avail(self, avail: bool):
        """Sets the avail of this ContactCheckIDType.


        :param avail: The avail of this ContactCheckIDType.
        :type avail: bool
        """

        self._avail = avail
