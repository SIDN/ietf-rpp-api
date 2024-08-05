from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.domain_create_type import DomainCreateType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.domain_create_type import DomainCreateType  # noqa: E501

class EppReadWriteTypeOneOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_create=None):  # noqa: E501
        """EppReadWriteTypeOneOf1 - a model defined in OpenAPI

        :param domain_create: The domain_create of this EppReadWriteTypeOneOf1.  # noqa: E501
        :type domain_create: DomainCreateType
        """
        self.openapi_types = {
            'domain_create': DomainCreateType
        }

        self.attribute_map = {
            'domain_create': 'domain_create'
        }

        self._domain_create = domain_create

    @classmethod
    def from_dict(cls, dikt) -> 'EppReadWriteTypeOneOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_readWriteType_oneOf_1 of this EppReadWriteTypeOneOf1.  # noqa: E501
        :rtype: EppReadWriteTypeOneOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_create(self) -> DomainCreateType:
        """Gets the domain_create of this EppReadWriteTypeOneOf1.


        :return: The domain_create of this EppReadWriteTypeOneOf1.
        :rtype: DomainCreateType
        """
        return self._domain_create

    @domain_create.setter
    def domain_create(self, domain_create: DomainCreateType):
        """Sets the domain_create of this EppReadWriteTypeOneOf1.


        :param domain_create: The domain_create of this EppReadWriteTypeOneOf1.
        :type domain_create: DomainCreateType
        """
        if domain_create is None:
            raise ValueError("Invalid value for `domain_create`, must not be `None`")  # noqa: E501

        self._domain_create = domain_create
