from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.host_update_type import HostUpdateType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.host_update_type import HostUpdateType  # noqa: E501

class EppReadWriteTypeOneOf10(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host_update=None):  # noqa: E501
        """EppReadWriteTypeOneOf10 - a model defined in OpenAPI

        :param host_update: The host_update of this EppReadWriteTypeOneOf10.  # noqa: E501
        :type host_update: HostUpdateType
        """
        self.openapi_types = {
            'host_update': HostUpdateType
        }

        self.attribute_map = {
            'host_update': 'host_update'
        }

        self._host_update = host_update

    @classmethod
    def from_dict(cls, dikt) -> 'EppReadWriteTypeOneOf10':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_readWriteType_oneOf_10 of this EppReadWriteTypeOneOf10.  # noqa: E501
        :rtype: EppReadWriteTypeOneOf10
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host_update(self) -> HostUpdateType:
        """Gets the host_update of this EppReadWriteTypeOneOf10.


        :return: The host_update of this EppReadWriteTypeOneOf10.
        :rtype: HostUpdateType
        """
        return self._host_update

    @host_update.setter
    def host_update(self, host_update: HostUpdateType):
        """Sets the host_update of this EppReadWriteTypeOneOf10.


        :param host_update: The host_update of this EppReadWriteTypeOneOf10.
        :type host_update: HostUpdateType
        """
        if host_update is None:
            raise ValueError("Invalid value for `host_update`, must not be `None`")  # noqa: E501

        self._host_update = host_update
