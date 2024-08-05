from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.domain_trn_data_type import DomainTrnDataType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.domain_trn_data_type import DomainTrnDataType  # noqa: E501

class EppExtAnyTypeOneOf5(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_trn_data=None):  # noqa: E501
        """EppExtAnyTypeOneOf5 - a model defined in OpenAPI

        :param domain_trn_data: The domain_trn_data of this EppExtAnyTypeOneOf5.  # noqa: E501
        :type domain_trn_data: DomainTrnDataType
        """
        self.openapi_types = {
            'domain_trn_data': DomainTrnDataType
        }

        self.attribute_map = {
            'domain_trn_data': 'domain_trnData'
        }

        self._domain_trn_data = domain_trn_data

    @classmethod
    def from_dict(cls, dikt) -> 'EppExtAnyTypeOneOf5':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_extAnyType_oneOf_5 of this EppExtAnyTypeOneOf5.  # noqa: E501
        :rtype: EppExtAnyTypeOneOf5
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_trn_data(self) -> DomainTrnDataType:
        """Gets the domain_trn_data of this EppExtAnyTypeOneOf5.


        :return: The domain_trn_data of this EppExtAnyTypeOneOf5.
        :rtype: DomainTrnDataType
        """
        return self._domain_trn_data

    @domain_trn_data.setter
    def domain_trn_data(self, domain_trn_data: DomainTrnDataType):
        """Sets the domain_trn_data of this EppExtAnyTypeOneOf5.


        :param domain_trn_data: The domain_trn_data of this EppExtAnyTypeOneOf5.
        :type domain_trn_data: DomainTrnDataType
        """
        if domain_trn_data is None:
            raise ValueError("Invalid value for `domain_trn_data`, must not be `None`")  # noqa: E501

        self._domain_trn_data = domain_trn_data