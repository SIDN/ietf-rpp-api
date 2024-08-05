from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class ContactIntLocType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None):  # noqa: E501
        """ContactIntLocType - a model defined in OpenAPI

        :param type: The type of this ContactIntLocType.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'type': str
        }

        self.attribute_map = {
            'type': '@type'
        }

        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'ContactIntLocType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The contact_intLocType of this ContactIntLocType.  # noqa: E501
        :rtype: ContactIntLocType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ContactIntLocType.


        :return: The type of this ContactIntLocType.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ContactIntLocType.


        :param type: The type of this ContactIntLocType.
        :type type: str
        """
        allowed_values = ["loc", "int"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type