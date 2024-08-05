from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class EppDcpRetentionTypeOneOf3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, stated=False):  # noqa: E501
        """EppDcpRetentionTypeOneOf3 - a model defined in OpenAPI

        :param stated: The stated of this EppDcpRetentionTypeOneOf3.  # noqa: E501
        :type stated: bool
        """
        self.openapi_types = {
            'stated': bool
        }

        self.attribute_map = {
            'stated': 'stated'
        }

        self._stated = stated

    @classmethod
    def from_dict(cls, dikt) -> 'EppDcpRetentionTypeOneOf3':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_dcpRetentionType_oneOf_3 of this EppDcpRetentionTypeOneOf3.  # noqa: E501
        :rtype: EppDcpRetentionTypeOneOf3
        """
        return util.deserialize_model(dikt, cls)

    @property
    def stated(self) -> bool:
        """Gets the stated of this EppDcpRetentionTypeOneOf3.


        :return: The stated of this EppDcpRetentionTypeOneOf3.
        :rtype: bool
        """
        return self._stated

    @stated.setter
    def stated(self, stated: bool):
        """Sets the stated of this EppDcpRetentionTypeOneOf3.


        :param stated: The stated of this EppDcpRetentionTypeOneOf3.
        :type stated: bool
        """
        if stated is None:
            raise ValueError("Invalid value for `stated`, must not be `None`")  # noqa: E501

        self._stated = stated
