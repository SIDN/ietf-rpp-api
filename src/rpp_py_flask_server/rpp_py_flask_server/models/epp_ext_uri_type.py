from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class EppExtURIType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ext_uri=None):  # noqa: E501
        """EppExtURIType - a model defined in OpenAPI

        :param ext_uri: The ext_uri of this EppExtURIType.  # noqa: E501
        :type ext_uri: List[str]
        """
        self.openapi_types = {
            'ext_uri': List[str]
        }

        self.attribute_map = {
            'ext_uri': 'extURI'
        }

        self._ext_uri = ext_uri

    @classmethod
    def from_dict(cls, dikt) -> 'EppExtURIType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_extURIType of this EppExtURIType.  # noqa: E501
        :rtype: EppExtURIType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ext_uri(self) -> List[str]:
        """Gets the ext_uri of this EppExtURIType.


        :return: The ext_uri of this EppExtURIType.
        :rtype: List[str]
        """
        return self._ext_uri

    @ext_uri.setter
    def ext_uri(self, ext_uri: List[str]):
        """Sets the ext_uri of this EppExtURIType.


        :param ext_uri: The ext_uri of this EppExtURIType.
        :type ext_uri: List[str]
        """
        if ext_uri is None:
            raise ValueError("Invalid value for `ext_uri`, must not be `None`")  # noqa: E501
        if ext_uri is not None and len(ext_uri) < 1:
            raise ValueError("Invalid value for `ext_uri`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ext_uri = ext_uri