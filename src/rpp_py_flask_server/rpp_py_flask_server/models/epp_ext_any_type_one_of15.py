from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.sec_dnsds_or_key_type import SecDNSDsOrKeyType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.sec_dnsds_or_key_type import SecDNSDsOrKeyType  # noqa: E501

class EppExtAnyTypeOneOf15(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sec_dns_inf_data=None):  # noqa: E501
        """EppExtAnyTypeOneOf15 - a model defined in OpenAPI

        :param sec_dns_inf_data: The sec_dns_inf_data of this EppExtAnyTypeOneOf15.  # noqa: E501
        :type sec_dns_inf_data: SecDNSDsOrKeyType
        """
        self.openapi_types = {
            'sec_dns_inf_data': SecDNSDsOrKeyType
        }

        self.attribute_map = {
            'sec_dns_inf_data': 'secDNS_infData'
        }

        self._sec_dns_inf_data = sec_dns_inf_data

    @classmethod
    def from_dict(cls, dikt) -> 'EppExtAnyTypeOneOf15':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_extAnyType_oneOf_15 of this EppExtAnyTypeOneOf15.  # noqa: E501
        :rtype: EppExtAnyTypeOneOf15
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sec_dns_inf_data(self) -> SecDNSDsOrKeyType:
        """Gets the sec_dns_inf_data of this EppExtAnyTypeOneOf15.


        :return: The sec_dns_inf_data of this EppExtAnyTypeOneOf15.
        :rtype: SecDNSDsOrKeyType
        """
        return self._sec_dns_inf_data

    @sec_dns_inf_data.setter
    def sec_dns_inf_data(self, sec_dns_inf_data: SecDNSDsOrKeyType):
        """Sets the sec_dns_inf_data of this EppExtAnyTypeOneOf15.


        :param sec_dns_inf_data: The sec_dns_inf_data of this EppExtAnyTypeOneOf15.
        :type sec_dns_inf_data: SecDNSDsOrKeyType
        """
        if sec_dns_inf_data is None:
            raise ValueError("Invalid value for `sec_dns_inf_data`, must not be `None`")  # noqa: E501

        self._sec_dns_inf_data = sec_dns_inf_data