from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.host_m_name_type import HostMNameType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.host_m_name_type import HostMNameType  # noqa: E501

class EppReadWriteTypeOneOf6(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host_check=None):  # noqa: E501
        """EppReadWriteTypeOneOf6 - a model defined in OpenAPI

        :param host_check: The host_check of this EppReadWriteTypeOneOf6.  # noqa: E501
        :type host_check: HostMNameType
        """
        self.openapi_types = {
            'host_check': HostMNameType
        }

        self.attribute_map = {
            'host_check': 'host_check'
        }

        self._host_check = host_check

    @classmethod
    def from_dict(cls, dikt) -> 'EppReadWriteTypeOneOf6':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_readWriteType_oneOf_6 of this EppReadWriteTypeOneOf6.  # noqa: E501
        :rtype: EppReadWriteTypeOneOf6
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host_check(self) -> HostMNameType:
        """Gets the host_check of this EppReadWriteTypeOneOf6.


        :return: The host_check of this EppReadWriteTypeOneOf6.
        :rtype: HostMNameType
        """
        return self._host_check

    @host_check.setter
    def host_check(self, host_check: HostMNameType):
        """Sets the host_check of this EppReadWriteTypeOneOf6.


        :param host_check: The host_check of this EppReadWriteTypeOneOf6.
        :type host_check: HostMNameType
        """
        if host_check is None:
            raise ValueError("Invalid value for `host_check`, must not be `None`")  # noqa: E501

        self._host_check = host_check
