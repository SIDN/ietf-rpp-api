from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.domain_chk_data_type import DomainChkDataType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.domain_chk_data_type import DomainChkDataType  # noqa: E501

class EppExtAnyTypeOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_chk_data=None):  # noqa: E501
        """EppExtAnyTypeOneOf - a model defined in OpenAPI

        :param domain_chk_data: The domain_chk_data of this EppExtAnyTypeOneOf.  # noqa: E501
        :type domain_chk_data: DomainChkDataType
        """
        self.openapi_types = {
            'domain_chk_data': DomainChkDataType
        }

        self.attribute_map = {
            'domain_chk_data': 'domain_chkData'
        }

        self._domain_chk_data = domain_chk_data

    @classmethod
    def from_dict(cls, dikt) -> 'EppExtAnyTypeOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_extAnyType_oneOf of this EppExtAnyTypeOneOf.  # noqa: E501
        :rtype: EppExtAnyTypeOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_chk_data(self) -> DomainChkDataType:
        """Gets the domain_chk_data of this EppExtAnyTypeOneOf.


        :return: The domain_chk_data of this EppExtAnyTypeOneOf.
        :rtype: DomainChkDataType
        """
        return self._domain_chk_data

    @domain_chk_data.setter
    def domain_chk_data(self, domain_chk_data: DomainChkDataType):
        """Sets the domain_chk_data of this EppExtAnyTypeOneOf.


        :param domain_chk_data: The domain_chk_data of this EppExtAnyTypeOneOf.
        :type domain_chk_data: DomainChkDataType
        """
        if domain_chk_data is None:
            raise ValueError("Invalid value for `domain_chk_data`, must not be `None`")  # noqa: E501

        self._domain_chk_data = domain_chk_data
