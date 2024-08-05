from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.contact_sid_type import ContactSIDType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.contact_sid_type import ContactSIDType  # noqa: E501

class EppReadWriteTypeOneOf13(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, contact_delete=None):  # noqa: E501
        """EppReadWriteTypeOneOf13 - a model defined in OpenAPI

        :param contact_delete: The contact_delete of this EppReadWriteTypeOneOf13.  # noqa: E501
        :type contact_delete: ContactSIDType
        """
        self.openapi_types = {
            'contact_delete': ContactSIDType
        }

        self.attribute_map = {
            'contact_delete': 'contact_delete'
        }

        self._contact_delete = contact_delete

    @classmethod
    def from_dict(cls, dikt) -> 'EppReadWriteTypeOneOf13':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_readWriteType_oneOf_13 of this EppReadWriteTypeOneOf13.  # noqa: E501
        :rtype: EppReadWriteTypeOneOf13
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contact_delete(self) -> ContactSIDType:
        """Gets the contact_delete of this EppReadWriteTypeOneOf13.


        :return: The contact_delete of this EppReadWriteTypeOneOf13.
        :rtype: ContactSIDType
        """
        return self._contact_delete

    @contact_delete.setter
    def contact_delete(self, contact_delete: ContactSIDType):
        """Sets the contact_delete of this EppReadWriteTypeOneOf13.


        :param contact_delete: The contact_delete of this EppReadWriteTypeOneOf13.
        :type contact_delete: ContactSIDType
        """
        if contact_delete is None:
            raise ValueError("Invalid value for `contact_delete`, must not be `None`")  # noqa: E501

        self._contact_delete = contact_delete