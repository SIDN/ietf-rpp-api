from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.eppcom_reason_type import EppcomReasonType
from rpp_py_flask_server.models.host_check_name_type import HostCheckNameType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.eppcom_reason_type import EppcomReasonType  # noqa: E501
from rpp_py_flask_server.models.host_check_name_type import HostCheckNameType  # noqa: E501

class HostCheckType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, reason=None):  # noqa: E501
        """HostCheckType - a model defined in OpenAPI

        :param name: The name of this HostCheckType.  # noqa: E501
        :type name: HostCheckNameType
        :param reason: The reason of this HostCheckType.  # noqa: E501
        :type reason: EppcomReasonType
        """
        self.openapi_types = {
            'name': HostCheckNameType,
            'reason': EppcomReasonType
        }

        self.attribute_map = {
            'name': 'name',
            'reason': 'reason'
        }

        self._name = name
        self._reason = reason

    @classmethod
    def from_dict(cls, dikt) -> 'HostCheckType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The host_checkType of this HostCheckType.  # noqa: E501
        :rtype: HostCheckType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> HostCheckNameType:
        """Gets the name of this HostCheckType.


        :return: The name of this HostCheckType.
        :rtype: HostCheckNameType
        """
        return self._name

    @name.setter
    def name(self, name: HostCheckNameType):
        """Sets the name of this HostCheckType.


        :param name: The name of this HostCheckType.
        :type name: HostCheckNameType
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def reason(self) -> EppcomReasonType:
        """Gets the reason of this HostCheckType.


        :return: The reason of this HostCheckType.
        :rtype: EppcomReasonType
        """
        return self._reason

    @reason.setter
    def reason(self, reason: EppcomReasonType):
        """Sets the reason of this HostCheckType.


        :param reason: The reason of this HostCheckType.
        :type reason: EppcomReasonType
        """

        self._reason = reason
