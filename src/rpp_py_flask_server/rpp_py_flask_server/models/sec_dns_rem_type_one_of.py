from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class SecDNSRemTypeOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, all=None):  # noqa: E501
        """SecDNSRemTypeOneOf - a model defined in OpenAPI

        :param all: The all of this SecDNSRemTypeOneOf.  # noqa: E501
        :type all: bool
        """
        self.openapi_types = {
            'all': bool
        }

        self.attribute_map = {
            'all': 'all'
        }

        self._all = all

    @classmethod
    def from_dict(cls, dikt) -> 'SecDNSRemTypeOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The secDNS_remType_oneOf of this SecDNSRemTypeOneOf.  # noqa: E501
        :rtype: SecDNSRemTypeOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def all(self) -> bool:
        """Gets the all of this SecDNSRemTypeOneOf.


        :return: The all of this SecDNSRemTypeOneOf.
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all: bool):
        """Sets the all of this SecDNSRemTypeOneOf.


        :param all: The all of this SecDNSRemTypeOneOf.
        :type all: bool
        """
        if all is None:
            raise ValueError("Invalid value for `all`, must not be `None`")  # noqa: E501

        self._all = all