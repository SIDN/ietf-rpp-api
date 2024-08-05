from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.domain_host_attr_type import DomainHostAttrType
from rpp_py_flask_server.models.domain_ns_type_one_of import DomainNsTypeOneOf
from rpp_py_flask_server.models.domain_ns_type_one_of1 import DomainNsTypeOneOf1
from rpp_py_flask_server import util

from rpp_py_flask_server.models.domain_host_attr_type import DomainHostAttrType  # noqa: E501
from rpp_py_flask_server.models.domain_ns_type_one_of import DomainNsTypeOneOf  # noqa: E501
from rpp_py_flask_server.models.domain_ns_type_one_of1 import DomainNsTypeOneOf1  # noqa: E501

class DomainNsType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host_obj=None, host_attr=None):  # noqa: E501
        """DomainNsType - a model defined in OpenAPI

        :param host_obj: The host_obj of this DomainNsType.  # noqa: E501
        :type host_obj: List[str]
        :param host_attr: The host_attr of this DomainNsType.  # noqa: E501
        :type host_attr: List[DomainHostAttrType]
        """
        self.openapi_types = {
            'host_obj': List[str],
            'host_attr': List[DomainHostAttrType]
        }

        self.attribute_map = {
            'host_obj': 'hostObj',
            'host_attr': 'hostAttr'
        }

        self._host_obj = host_obj
        self._host_attr = host_attr

    @classmethod
    def from_dict(cls, dikt) -> 'DomainNsType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_nsType of this DomainNsType.  # noqa: E501
        :rtype: DomainNsType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host_obj(self) -> List[str]:
        """Gets the host_obj of this DomainNsType.


        :return: The host_obj of this DomainNsType.
        :rtype: List[str]
        """
        return self._host_obj

    @host_obj.setter
    def host_obj(self, host_obj: List[str]):
        """Sets the host_obj of this DomainNsType.


        :param host_obj: The host_obj of this DomainNsType.
        :type host_obj: List[str]
        """
        if host_obj is None:
            raise ValueError("Invalid value for `host_obj`, must not be `None`")  # noqa: E501
        if host_obj is not None and len(host_obj) < 1:
            raise ValueError("Invalid value for `host_obj`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._host_obj = host_obj

    @property
    def host_attr(self) -> List[DomainHostAttrType]:
        """Gets the host_attr of this DomainNsType.


        :return: The host_attr of this DomainNsType.
        :rtype: List[DomainHostAttrType]
        """
        return self._host_attr

    @host_attr.setter
    def host_attr(self, host_attr: List[DomainHostAttrType]):
        """Sets the host_attr of this DomainNsType.


        :param host_attr: The host_attr of this DomainNsType.
        :type host_attr: List[DomainHostAttrType]
        """
        if host_attr is None:
            raise ValueError("Invalid value for `host_attr`, must not be `None`")  # noqa: E501
        if host_attr is not None and len(host_attr) < 1:
            raise ValueError("Invalid value for `host_attr`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._host_attr = host_attr
