from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.domain_transfer_type import DomainTransferType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.domain_transfer_type import DomainTransferType  # noqa: E501

class EppReadWriteTypeOneOf4(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_transfer=None):  # noqa: E501
        """EppReadWriteTypeOneOf4 - a model defined in OpenAPI

        :param domain_transfer: The domain_transfer of this EppReadWriteTypeOneOf4.  # noqa: E501
        :type domain_transfer: DomainTransferType
        """
        self.openapi_types = {
            'domain_transfer': DomainTransferType
        }

        self.attribute_map = {
            'domain_transfer': 'domain_transfer'
        }

        self._domain_transfer = domain_transfer

    @classmethod
    def from_dict(cls, dikt) -> 'EppReadWriteTypeOneOf4':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_readWriteType_oneOf_4 of this EppReadWriteTypeOneOf4.  # noqa: E501
        :rtype: EppReadWriteTypeOneOf4
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_transfer(self) -> DomainTransferType:
        """Gets the domain_transfer of this EppReadWriteTypeOneOf4.


        :return: The domain_transfer of this EppReadWriteTypeOneOf4.
        :rtype: DomainTransferType
        """
        return self._domain_transfer

    @domain_transfer.setter
    def domain_transfer(self, domain_transfer: DomainTransferType):
        """Sets the domain_transfer of this EppReadWriteTypeOneOf4.


        :param domain_transfer: The domain_transfer of this EppReadWriteTypeOneOf4.
        :type domain_transfer: DomainTransferType
        """
        if domain_transfer is None:
            raise ValueError("Invalid value for `domain_transfer`, must not be `None`")  # noqa: E501

        self._domain_transfer = domain_transfer
