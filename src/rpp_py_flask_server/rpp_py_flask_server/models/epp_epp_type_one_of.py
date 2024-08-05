from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.epp_greeting_type import EppGreetingType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.epp_greeting_type import EppGreetingType  # noqa: E501

class EppEppTypeOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, greeting=None):  # noqa: E501
        """EppEppTypeOneOf - a model defined in OpenAPI

        :param greeting: The greeting of this EppEppTypeOneOf.  # noqa: E501
        :type greeting: EppGreetingType
        """
        self.openapi_types = {
            'greeting': EppGreetingType
        }

        self.attribute_map = {
            'greeting': 'greeting'
        }

        self._greeting = greeting

    @classmethod
    def from_dict(cls, dikt) -> 'EppEppTypeOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_eppType_oneOf of this EppEppTypeOneOf.  # noqa: E501
        :rtype: EppEppTypeOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def greeting(self) -> EppGreetingType:
        """Gets the greeting of this EppEppTypeOneOf.


        :return: The greeting of this EppEppTypeOneOf.
        :rtype: EppGreetingType
        """
        return self._greeting

    @greeting.setter
    def greeting(self, greeting: EppGreetingType):
        """Sets the greeting of this EppEppTypeOneOf.


        :param greeting: The greeting of this EppEppTypeOneOf.
        :type greeting: EppGreetingType
        """
        if greeting is None:
            raise ValueError("Invalid value for `greeting`, must not be `None`")  # noqa: E501

        self._greeting = greeting