from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.contact_cre_data_type import ContactCreDataType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.contact_cre_data_type import ContactCreDataType  # noqa: E501

class EppExtAnyTypeOneOf11(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, contact_cre_data=None):  # noqa: E501
        """EppExtAnyTypeOneOf11 - a model defined in OpenAPI

        :param contact_cre_data: The contact_cre_data of this EppExtAnyTypeOneOf11.  # noqa: E501
        :type contact_cre_data: ContactCreDataType
        """
        self.openapi_types = {
            'contact_cre_data': ContactCreDataType
        }

        self.attribute_map = {
            'contact_cre_data': 'contact_creData'
        }

        self._contact_cre_data = contact_cre_data

    @classmethod
    def from_dict(cls, dikt) -> 'EppExtAnyTypeOneOf11':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_extAnyType_oneOf_11 of this EppExtAnyTypeOneOf11.  # noqa: E501
        :rtype: EppExtAnyTypeOneOf11
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contact_cre_data(self) -> ContactCreDataType:
        """Gets the contact_cre_data of this EppExtAnyTypeOneOf11.


        :return: The contact_cre_data of this EppExtAnyTypeOneOf11.
        :rtype: ContactCreDataType
        """
        return self._contact_cre_data

    @contact_cre_data.setter
    def contact_cre_data(self, contact_cre_data: ContactCreDataType):
        """Sets the contact_cre_data of this EppExtAnyTypeOneOf11.


        :param contact_cre_data: The contact_cre_data of this EppExtAnyTypeOneOf11.
        :type contact_cre_data: ContactCreDataType
        """
        if contact_cre_data is None:
            raise ValueError("Invalid value for `contact_cre_data`, must not be `None`")  # noqa: E501

        self._contact_cre_data = contact_cre_data
