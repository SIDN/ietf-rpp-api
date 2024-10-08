from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.sec_dns_key_data_type import SecDNSKeyDataType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.sec_dns_key_data_type import SecDNSKeyDataType  # noqa: E501

class SecDNSRemTypeOneOf2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key_data=None):  # noqa: E501
        """SecDNSRemTypeOneOf2 - a model defined in OpenAPI

        :param key_data: The key_data of this SecDNSRemTypeOneOf2.  # noqa: E501
        :type key_data: List[SecDNSKeyDataType]
        """
        self.openapi_types = {
            'key_data': List[SecDNSKeyDataType]
        }

        self.attribute_map = {
            'key_data': 'keyData'
        }

        self._key_data = key_data

    @classmethod
    def from_dict(cls, dikt) -> 'SecDNSRemTypeOneOf2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The secDNS_remType_oneOf_2 of this SecDNSRemTypeOneOf2.  # noqa: E501
        :rtype: SecDNSRemTypeOneOf2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key_data(self) -> List[SecDNSKeyDataType]:
        """Gets the key_data of this SecDNSRemTypeOneOf2.


        :return: The key_data of this SecDNSRemTypeOneOf2.
        :rtype: List[SecDNSKeyDataType]
        """
        return self._key_data

    @key_data.setter
    def key_data(self, key_data: List[SecDNSKeyDataType]):
        """Sets the key_data of this SecDNSRemTypeOneOf2.


        :param key_data: The key_data of this SecDNSRemTypeOneOf2.
        :type key_data: List[SecDNSKeyDataType]
        """
        if key_data is None:
            raise ValueError("Invalid value for `key_data`, must not be `None`")  # noqa: E501
        if key_data is not None and len(key_data) < 1:
            raise ValueError("Invalid value for `key_data`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._key_data = key_data
