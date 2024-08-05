from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.domain_m_name_type import DomainMNameType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.domain_m_name_type import DomainMNameType  # noqa: E501

class EppReadWriteTypeOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_check=None):  # noqa: E501
        """EppReadWriteTypeOneOf - a model defined in OpenAPI

        :param domain_check: The domain_check of this EppReadWriteTypeOneOf.  # noqa: E501
        :type domain_check: DomainMNameType
        """
        self.openapi_types = {
            'domain_check': DomainMNameType
        }

        self.attribute_map = {
            'domain_check': 'domain_check'
        }

        self._domain_check = domain_check

    @classmethod
    def from_dict(cls, dikt) -> 'EppReadWriteTypeOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_readWriteType_oneOf of this EppReadWriteTypeOneOf.  # noqa: E501
        :rtype: EppReadWriteTypeOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_check(self) -> DomainMNameType:
        """Gets the domain_check of this EppReadWriteTypeOneOf.


        :return: The domain_check of this EppReadWriteTypeOneOf.
        :rtype: DomainMNameType
        """
        return self._domain_check

    @domain_check.setter
    def domain_check(self, domain_check: DomainMNameType):
        """Sets the domain_check of this EppReadWriteTypeOneOf.


        :param domain_check: The domain_check of this EppReadWriteTypeOneOf.
        :type domain_check: DomainMNameType
        """
        if domain_check is None:
            raise ValueError("Invalid value for `domain_check`, must not be `None`")  # noqa: E501

        self._domain_check = domain_check