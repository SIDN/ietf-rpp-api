from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class EppDcpPurposeType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, admin=False, contact=False, other=False, prov=False):  # noqa: E501
        """EppDcpPurposeType - a model defined in OpenAPI

        :param admin: The admin of this EppDcpPurposeType.  # noqa: E501
        :type admin: bool
        :param contact: The contact of this EppDcpPurposeType.  # noqa: E501
        :type contact: bool
        :param other: The other of this EppDcpPurposeType.  # noqa: E501
        :type other: bool
        :param prov: The prov of this EppDcpPurposeType.  # noqa: E501
        :type prov: bool
        """
        self.openapi_types = {
            'admin': bool,
            'contact': bool,
            'other': bool,
            'prov': bool
        }

        self.attribute_map = {
            'admin': 'admin',
            'contact': 'contact',
            'other': 'other',
            'prov': 'prov'
        }

        self._admin = admin
        self._contact = contact
        self._other = other
        self._prov = prov

    @classmethod
    def from_dict(cls, dikt) -> 'EppDcpPurposeType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_dcpPurposeType of this EppDcpPurposeType.  # noqa: E501
        :rtype: EppDcpPurposeType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def admin(self) -> bool:
        """Gets the admin of this EppDcpPurposeType.


        :return: The admin of this EppDcpPurposeType.
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin: bool):
        """Sets the admin of this EppDcpPurposeType.


        :param admin: The admin of this EppDcpPurposeType.
        :type admin: bool
        """

        self._admin = admin

    @property
    def contact(self) -> bool:
        """Gets the contact of this EppDcpPurposeType.


        :return: The contact of this EppDcpPurposeType.
        :rtype: bool
        """
        return self._contact

    @contact.setter
    def contact(self, contact: bool):
        """Sets the contact of this EppDcpPurposeType.


        :param contact: The contact of this EppDcpPurposeType.
        :type contact: bool
        """

        self._contact = contact

    @property
    def other(self) -> bool:
        """Gets the other of this EppDcpPurposeType.


        :return: The other of this EppDcpPurposeType.
        :rtype: bool
        """
        return self._other

    @other.setter
    def other(self, other: bool):
        """Sets the other of this EppDcpPurposeType.


        :param other: The other of this EppDcpPurposeType.
        :type other: bool
        """

        self._other = other

    @property
    def prov(self) -> bool:
        """Gets the prov of this EppDcpPurposeType.


        :return: The prov of this EppDcpPurposeType.
        :rtype: bool
        """
        return self._prov

    @prov.setter
    def prov(self, prov: bool):
        """Sets the prov of this EppDcpPurposeType.


        :param prov: The prov of this EppDcpPurposeType.
        :type prov: bool
        """

        self._prov = prov
