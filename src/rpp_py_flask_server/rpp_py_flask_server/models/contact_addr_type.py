from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class ContactAddrType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cc=None, city=None, pc=None, sp=None, street=None):  # noqa: E501
        """ContactAddrType - a model defined in OpenAPI

        :param cc: The cc of this ContactAddrType.  # noqa: E501
        :type cc: str
        :param city: The city of this ContactAddrType.  # noqa: E501
        :type city: str
        :param pc: The pc of this ContactAddrType.  # noqa: E501
        :type pc: str
        :param sp: The sp of this ContactAddrType.  # noqa: E501
        :type sp: str
        :param street: The street of this ContactAddrType.  # noqa: E501
        :type street: List[str]
        """
        self.openapi_types = {
            'cc': str,
            'city': str,
            'pc': str,
            'sp': str,
            'street': List[str]
        }

        self.attribute_map = {
            'cc': 'cc',
            'city': 'city',
            'pc': 'pc',
            'sp': 'sp',
            'street': 'street'
        }

        self._cc = cc
        self._city = city
        self._pc = pc
        self._sp = sp
        self._street = street

    @classmethod
    def from_dict(cls, dikt) -> 'ContactAddrType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The contact_addrType of this ContactAddrType.  # noqa: E501
        :rtype: ContactAddrType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cc(self) -> str:
        """Gets the cc of this ContactAddrType.


        :return: The cc of this ContactAddrType.
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc: str):
        """Sets the cc of this ContactAddrType.


        :param cc: The cc of this ContactAddrType.
        :type cc: str
        """
        if cc is None:
            raise ValueError("Invalid value for `cc`, must not be `None`")  # noqa: E501
        if cc is not None and len(cc) > 2:
            raise ValueError("Invalid value for `cc`, length must be less than or equal to `2`")  # noqa: E501
        if cc is not None and len(cc) < 2:
            raise ValueError("Invalid value for `cc`, length must be greater than or equal to `2`")  # noqa: E501

        self._cc = cc

    @property
    def city(self) -> str:
        """Gets the city of this ContactAddrType.


        :return: The city of this ContactAddrType.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this ContactAddrType.


        :param city: The city of this ContactAddrType.
        :type city: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501
        if city is not None and len(city) > 255:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `255`")  # noqa: E501
        if city is not None and len(city) < 1:
            raise ValueError("Invalid value for `city`, length must be greater than or equal to `1`")  # noqa: E501

        self._city = city

    @property
    def pc(self) -> str:
        """Gets the pc of this ContactAddrType.


        :return: The pc of this ContactAddrType.
        :rtype: str
        """
        return self._pc

    @pc.setter
    def pc(self, pc: str):
        """Sets the pc of this ContactAddrType.


        :param pc: The pc of this ContactAddrType.
        :type pc: str
        """
        if pc is not None and len(pc) > 16:
            raise ValueError("Invalid value for `pc`, length must be less than or equal to `16`")  # noqa: E501

        self._pc = pc

    @property
    def sp(self) -> str:
        """Gets the sp of this ContactAddrType.


        :return: The sp of this ContactAddrType.
        :rtype: str
        """
        return self._sp

    @sp.setter
    def sp(self, sp: str):
        """Sets the sp of this ContactAddrType.


        :param sp: The sp of this ContactAddrType.
        :type sp: str
        """
        if sp is not None and len(sp) > 255:
            raise ValueError("Invalid value for `sp`, length must be less than or equal to `255`")  # noqa: E501

        self._sp = sp

    @property
    def street(self) -> List[str]:
        """Gets the street of this ContactAddrType.


        :return: The street of this ContactAddrType.
        :rtype: List[str]
        """
        return self._street

    @street.setter
    def street(self, street: List[str]):
        """Sets the street of this ContactAddrType.


        :param street: The street of this ContactAddrType.
        :type street: List[str]
        """
        if street is not None and len(street) > 3:
            raise ValueError("Invalid value for `street`, number of items must be less than or equal to `3`")  # noqa: E501
        if street is not None and len(street) < 0:
            raise ValueError("Invalid value for `street`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._street = street
