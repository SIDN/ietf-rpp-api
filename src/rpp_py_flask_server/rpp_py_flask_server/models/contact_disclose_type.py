from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.contact_int_loc_type import ContactIntLocType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.contact_int_loc_type import ContactIntLocType  # noqa: E501

class ContactDiscloseType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, flag=None, addr=None, email=False, fax=False, name=None, org=None, voice=False):  # noqa: E501
        """ContactDiscloseType - a model defined in OpenAPI

        :param flag: The flag of this ContactDiscloseType.  # noqa: E501
        :type flag: bool
        :param addr: The addr of this ContactDiscloseType.  # noqa: E501
        :type addr: List[ContactIntLocType]
        :param email: The email of this ContactDiscloseType.  # noqa: E501
        :type email: bool
        :param fax: The fax of this ContactDiscloseType.  # noqa: E501
        :type fax: bool
        :param name: The name of this ContactDiscloseType.  # noqa: E501
        :type name: List[ContactIntLocType]
        :param org: The org of this ContactDiscloseType.  # noqa: E501
        :type org: List[ContactIntLocType]
        :param voice: The voice of this ContactDiscloseType.  # noqa: E501
        :type voice: bool
        """
        self.openapi_types = {
            'flag': bool,
            'addr': List[ContactIntLocType],
            'email': bool,
            'fax': bool,
            'name': List[ContactIntLocType],
            'org': List[ContactIntLocType],
            'voice': bool
        }

        self.attribute_map = {
            'flag': '@flag',
            'addr': 'addr',
            'email': 'email',
            'fax': 'fax',
            'name': 'name',
            'org': 'org',
            'voice': 'voice'
        }

        self._flag = flag
        self._addr = addr
        self._email = email
        self._fax = fax
        self._name = name
        self._org = org
        self._voice = voice

    @classmethod
    def from_dict(cls, dikt) -> 'ContactDiscloseType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The contact_discloseType of this ContactDiscloseType.  # noqa: E501
        :rtype: ContactDiscloseType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def flag(self) -> bool:
        """Gets the flag of this ContactDiscloseType.


        :return: The flag of this ContactDiscloseType.
        :rtype: bool
        """
        return self._flag

    @flag.setter
    def flag(self, flag: bool):
        """Sets the flag of this ContactDiscloseType.


        :param flag: The flag of this ContactDiscloseType.
        :type flag: bool
        """

        self._flag = flag

    @property
    def addr(self) -> List[ContactIntLocType]:
        """Gets the addr of this ContactDiscloseType.


        :return: The addr of this ContactDiscloseType.
        :rtype: List[ContactIntLocType]
        """
        return self._addr

    @addr.setter
    def addr(self, addr: List[ContactIntLocType]):
        """Sets the addr of this ContactDiscloseType.


        :param addr: The addr of this ContactDiscloseType.
        :type addr: List[ContactIntLocType]
        """
        if addr is not None and len(addr) > 2:
            raise ValueError("Invalid value for `addr`, number of items must be less than or equal to `2`")  # noqa: E501
        if addr is not None and len(addr) < 0:
            raise ValueError("Invalid value for `addr`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._addr = addr

    @property
    def email(self) -> bool:
        """Gets the email of this ContactDiscloseType.


        :return: The email of this ContactDiscloseType.
        :rtype: bool
        """
        return self._email

    @email.setter
    def email(self, email: bool):
        """Sets the email of this ContactDiscloseType.


        :param email: The email of this ContactDiscloseType.
        :type email: bool
        """

        self._email = email

    @property
    def fax(self) -> bool:
        """Gets the fax of this ContactDiscloseType.


        :return: The fax of this ContactDiscloseType.
        :rtype: bool
        """
        return self._fax

    @fax.setter
    def fax(self, fax: bool):
        """Sets the fax of this ContactDiscloseType.


        :param fax: The fax of this ContactDiscloseType.
        :type fax: bool
        """

        self._fax = fax

    @property
    def name(self) -> List[ContactIntLocType]:
        """Gets the name of this ContactDiscloseType.


        :return: The name of this ContactDiscloseType.
        :rtype: List[ContactIntLocType]
        """
        return self._name

    @name.setter
    def name(self, name: List[ContactIntLocType]):
        """Sets the name of this ContactDiscloseType.


        :param name: The name of this ContactDiscloseType.
        :type name: List[ContactIntLocType]
        """
        if name is not None and len(name) > 2:
            raise ValueError("Invalid value for `name`, number of items must be less than or equal to `2`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def org(self) -> List[ContactIntLocType]:
        """Gets the org of this ContactDiscloseType.


        :return: The org of this ContactDiscloseType.
        :rtype: List[ContactIntLocType]
        """
        return self._org

    @org.setter
    def org(self, org: List[ContactIntLocType]):
        """Sets the org of this ContactDiscloseType.


        :param org: The org of this ContactDiscloseType.
        :type org: List[ContactIntLocType]
        """
        if org is not None and len(org) > 2:
            raise ValueError("Invalid value for `org`, number of items must be less than or equal to `2`")  # noqa: E501
        if org is not None and len(org) < 0:
            raise ValueError("Invalid value for `org`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._org = org

    @property
    def voice(self) -> bool:
        """Gets the voice of this ContactDiscloseType.


        :return: The voice of this ContactDiscloseType.
        :rtype: bool
        """
        return self._voice

    @voice.setter
    def voice(self, voice: bool):
        """Sets the voice of this ContactDiscloseType.


        :param voice: The voice of this ContactDiscloseType.
        :type voice: bool
        """

        self._voice = voice