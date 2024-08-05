from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.domain_inf_data_type import DomainInfDataType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.domain_inf_data_type import DomainInfDataType  # noqa: E501

class EppExtAnyTypeOneOf2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_inf_data=None):  # noqa: E501
        """EppExtAnyTypeOneOf2 - a model defined in OpenAPI

        :param domain_inf_data: The domain_inf_data of this EppExtAnyTypeOneOf2.  # noqa: E501
        :type domain_inf_data: DomainInfDataType
        """
        self.openapi_types = {
            'domain_inf_data': DomainInfDataType
        }

        self.attribute_map = {
            'domain_inf_data': 'domain_infData'
        }

        self._domain_inf_data = domain_inf_data

    @classmethod
    def from_dict(cls, dikt) -> 'EppExtAnyTypeOneOf2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_extAnyType_oneOf_2 of this EppExtAnyTypeOneOf2.  # noqa: E501
        :rtype: EppExtAnyTypeOneOf2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_inf_data(self) -> DomainInfDataType:
        """Gets the domain_inf_data of this EppExtAnyTypeOneOf2.


        :return: The domain_inf_data of this EppExtAnyTypeOneOf2.
        :rtype: DomainInfDataType
        """
        return self._domain_inf_data

    @domain_inf_data.setter
    def domain_inf_data(self, domain_inf_data: DomainInfDataType):
        """Sets the domain_inf_data of this EppExtAnyTypeOneOf2.


        :param domain_inf_data: The domain_inf_data of this EppExtAnyTypeOneOf2.
        :type domain_inf_data: DomainInfDataType
        """
        if domain_inf_data is None:
            raise ValueError("Invalid value for `domain_inf_data`, must not be `None`")  # noqa: E501

        self._domain_inf_data = domain_inf_data
