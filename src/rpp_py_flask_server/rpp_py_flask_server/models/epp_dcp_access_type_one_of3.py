from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class EppDcpAccessTypeOneOf3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, personal=False):  # noqa: E501
        """EppDcpAccessTypeOneOf3 - a model defined in OpenAPI

        :param personal: The personal of this EppDcpAccessTypeOneOf3.  # noqa: E501
        :type personal: bool
        """
        self.openapi_types = {
            'personal': bool
        }

        self.attribute_map = {
            'personal': 'personal'
        }

        self._personal = personal

    @classmethod
    def from_dict(cls, dikt) -> 'EppDcpAccessTypeOneOf3':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_dcpAccessType_oneOf_3 of this EppDcpAccessTypeOneOf3.  # noqa: E501
        :rtype: EppDcpAccessTypeOneOf3
        """
        return util.deserialize_model(dikt, cls)

    @property
    def personal(self) -> bool:
        """Gets the personal of this EppDcpAccessTypeOneOf3.


        :return: The personal of this EppDcpAccessTypeOneOf3.
        :rtype: bool
        """
        return self._personal

    @personal.setter
    def personal(self, personal: bool):
        """Sets the personal of this EppDcpAccessTypeOneOf3.


        :param personal: The personal of this EppDcpAccessTypeOneOf3.
        :type personal: bool
        """
        if personal is None:
            raise ValueError("Invalid value for `personal`, must not be `None`")  # noqa: E501

        self._personal = personal
