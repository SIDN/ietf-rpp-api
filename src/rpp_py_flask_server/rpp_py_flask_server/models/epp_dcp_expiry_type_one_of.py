from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class EppDcpExpiryTypeOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, absolute=None):  # noqa: E501
        """EppDcpExpiryTypeOneOf - a model defined in OpenAPI

        :param absolute: The absolute of this EppDcpExpiryTypeOneOf.  # noqa: E501
        :type absolute: datetime
        """
        self.openapi_types = {
            'absolute': datetime
        }

        self.attribute_map = {
            'absolute': 'absolute'
        }

        self._absolute = absolute

    @classmethod
    def from_dict(cls, dikt) -> 'EppDcpExpiryTypeOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_dcpExpiryType_oneOf of this EppDcpExpiryTypeOneOf.  # noqa: E501
        :rtype: EppDcpExpiryTypeOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def absolute(self) -> datetime:
        """Gets the absolute of this EppDcpExpiryTypeOneOf.


        :return: The absolute of this EppDcpExpiryTypeOneOf.
        :rtype: datetime
        """
        return self._absolute

    @absolute.setter
    def absolute(self, absolute: datetime):
        """Sets the absolute of this EppDcpExpiryTypeOneOf.


        :param absolute: The absolute of this EppDcpExpiryTypeOneOf.
        :type absolute: datetime
        """
        if absolute is None:
            raise ValueError("Invalid value for `absolute`, must not be `None`")  # noqa: E501

        self._absolute = absolute
