from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.host_pan_data_type import HostPanDataType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.host_pan_data_type import HostPanDataType  # noqa: E501

class EppExtAnyTypeOneOf9(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host_pan_data=None):  # noqa: E501
        """EppExtAnyTypeOneOf9 - a model defined in OpenAPI

        :param host_pan_data: The host_pan_data of this EppExtAnyTypeOneOf9.  # noqa: E501
        :type host_pan_data: HostPanDataType
        """
        self.openapi_types = {
            'host_pan_data': HostPanDataType
        }

        self.attribute_map = {
            'host_pan_data': 'host_panData'
        }

        self._host_pan_data = host_pan_data

    @classmethod
    def from_dict(cls, dikt) -> 'EppExtAnyTypeOneOf9':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_extAnyType_oneOf_9 of this EppExtAnyTypeOneOf9.  # noqa: E501
        :rtype: EppExtAnyTypeOneOf9
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host_pan_data(self) -> HostPanDataType:
        """Gets the host_pan_data of this EppExtAnyTypeOneOf9.


        :return: The host_pan_data of this EppExtAnyTypeOneOf9.
        :rtype: HostPanDataType
        """
        return self._host_pan_data

    @host_pan_data.setter
    def host_pan_data(self, host_pan_data: HostPanDataType):
        """Sets the host_pan_data of this EppExtAnyTypeOneOf9.


        :param host_pan_data: The host_pan_data of this EppExtAnyTypeOneOf9.
        :type host_pan_data: HostPanDataType
        """
        if host_pan_data is None:
            raise ValueError("Invalid value for `host_pan_data`, must not be `None`")  # noqa: E501

        self._host_pan_data = host_pan_data