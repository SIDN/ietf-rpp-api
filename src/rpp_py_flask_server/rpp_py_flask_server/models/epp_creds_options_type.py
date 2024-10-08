from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.epp_version_type import EppVersionType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.epp_version_type import EppVersionType  # noqa: E501

class EppCredsOptionsType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lang=None, version=None):  # noqa: E501
        """EppCredsOptionsType - a model defined in OpenAPI

        :param lang: The lang of this EppCredsOptionsType.  # noqa: E501
        :type lang: str
        :param version: The version of this EppCredsOptionsType.  # noqa: E501
        :type version: EppVersionType
        """
        self.openapi_types = {
            'lang': str,
            'version': EppVersionType
        }

        self.attribute_map = {
            'lang': 'lang',
            'version': 'version'
        }

        self._lang = lang
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'EppCredsOptionsType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_credsOptionsType of this EppCredsOptionsType.  # noqa: E501
        :rtype: EppCredsOptionsType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lang(self) -> str:
        """Gets the lang of this EppCredsOptionsType.


        :return: The lang of this EppCredsOptionsType.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang: str):
        """Sets the lang of this EppCredsOptionsType.


        :param lang: The lang of this EppCredsOptionsType.
        :type lang: str
        """
        if lang is None:
            raise ValueError("Invalid value for `lang`, must not be `None`")  # noqa: E501

        self._lang = lang

    @property
    def version(self) -> EppVersionType:
        """Gets the version of this EppCredsOptionsType.


        :return: The version of this EppCredsOptionsType.
        :rtype: EppVersionType
        """
        return self._version

    @version.setter
    def version(self, version: EppVersionType):
        """Sets the version of this EppCredsOptionsType.


        :param version: The version of this EppCredsOptionsType.
        :type version: EppVersionType
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version
