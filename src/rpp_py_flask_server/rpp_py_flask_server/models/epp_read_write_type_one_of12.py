from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.contact_create_type import ContactCreateType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.contact_create_type import ContactCreateType  # noqa: E501

class EppReadWriteTypeOneOf12(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, contact_create=None):  # noqa: E501
        """EppReadWriteTypeOneOf12 - a model defined in OpenAPI

        :param contact_create: The contact_create of this EppReadWriteTypeOneOf12.  # noqa: E501
        :type contact_create: ContactCreateType
        """
        self.openapi_types = {
            'contact_create': ContactCreateType
        }

        self.attribute_map = {
            'contact_create': 'contact_create'
        }

        self._contact_create = contact_create

    @classmethod
    def from_dict(cls, dikt) -> 'EppReadWriteTypeOneOf12':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_readWriteType_oneOf_12 of this EppReadWriteTypeOneOf12.  # noqa: E501
        :rtype: EppReadWriteTypeOneOf12
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contact_create(self) -> ContactCreateType:
        """Gets the contact_create of this EppReadWriteTypeOneOf12.


        :return: The contact_create of this EppReadWriteTypeOneOf12.
        :rtype: ContactCreateType
        """
        return self._contact_create

    @contact_create.setter
    def contact_create(self, contact_create: ContactCreateType):
        """Sets the contact_create of this EppReadWriteTypeOneOf12.


        :param contact_create: The contact_create of this EppReadWriteTypeOneOf12.
        :type contact_create: ContactCreateType
        """
        if contact_create is None:
            raise ValueError("Invalid value for `contact_create`, must not be `None`")  # noqa: E501

        self._contact_create = contact_create
