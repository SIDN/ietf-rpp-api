from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.host_s_name_type import HostSNameType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.host_s_name_type import HostSNameType  # noqa: E501

class EppReadWriteTypeOneOf8(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host_delete=None):  # noqa: E501
        """EppReadWriteTypeOneOf8 - a model defined in OpenAPI

        :param host_delete: The host_delete of this EppReadWriteTypeOneOf8.  # noqa: E501
        :type host_delete: HostSNameType
        """
        self.openapi_types = {
            'host_delete': HostSNameType
        }

        self.attribute_map = {
            'host_delete': 'host_delete'
        }

        self._host_delete = host_delete

    @classmethod
    def from_dict(cls, dikt) -> 'EppReadWriteTypeOneOf8':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_readWriteType_oneOf_8 of this EppReadWriteTypeOneOf8.  # noqa: E501
        :rtype: EppReadWriteTypeOneOf8
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host_delete(self) -> HostSNameType:
        """Gets the host_delete of this EppReadWriteTypeOneOf8.


        :return: The host_delete of this EppReadWriteTypeOneOf8.
        :rtype: HostSNameType
        """
        return self._host_delete

    @host_delete.setter
    def host_delete(self, host_delete: HostSNameType):
        """Sets the host_delete of this EppReadWriteTypeOneOf8.


        :param host_delete: The host_delete of this EppReadWriteTypeOneOf8.
        :type host_delete: HostSNameType
        """
        if host_delete is None:
            raise ValueError("Invalid value for `host_delete`, must not be `None`")  # noqa: E501

        self._host_delete = host_delete
