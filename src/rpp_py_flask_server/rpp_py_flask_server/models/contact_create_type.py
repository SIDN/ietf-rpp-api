from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.contact_auth_info_type import ContactAuthInfoType
from rpp_py_flask_server.models.contact_disclose_type import ContactDiscloseType
from rpp_py_flask_server.models.contact_e164_type import ContactE164Type
from rpp_py_flask_server.models.contact_postal_info_type import ContactPostalInfoType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.contact_auth_info_type import ContactAuthInfoType  # noqa: E501
from rpp_py_flask_server.models.contact_disclose_type import ContactDiscloseType  # noqa: E501
from rpp_py_flask_server.models.contact_e164_type import ContactE164Type  # noqa: E501
from rpp_py_flask_server.models.contact_postal_info_type import ContactPostalInfoType  # noqa: E501

class ContactCreateType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, auth_info=None, disclose=None, email=None, fax=None, id=None, postal_info=None, voice=None):  # noqa: E501
        """ContactCreateType - a model defined in OpenAPI

        :param auth_info: The auth_info of this ContactCreateType.  # noqa: E501
        :type auth_info: ContactAuthInfoType
        :param disclose: The disclose of this ContactCreateType.  # noqa: E501
        :type disclose: ContactDiscloseType
        :param email: The email of this ContactCreateType.  # noqa: E501
        :type email: str
        :param fax: The fax of this ContactCreateType.  # noqa: E501
        :type fax: ContactE164Type
        :param id: The id of this ContactCreateType.  # noqa: E501
        :type id: str
        :param postal_info: The postal_info of this ContactCreateType.  # noqa: E501
        :type postal_info: List[ContactPostalInfoType]
        :param voice: The voice of this ContactCreateType.  # noqa: E501
        :type voice: ContactE164Type
        """
        self.openapi_types = {
            'auth_info': ContactAuthInfoType,
            'disclose': ContactDiscloseType,
            'email': str,
            'fax': ContactE164Type,
            'id': str,
            'postal_info': List[ContactPostalInfoType],
            'voice': ContactE164Type
        }

        self.attribute_map = {
            'auth_info': 'authInfo',
            'disclose': 'disclose',
            'email': 'email',
            'fax': 'fax',
            'id': 'id',
            'postal_info': 'postalInfo',
            'voice': 'voice'
        }

        self._auth_info = auth_info
        self._disclose = disclose
        self._email = email
        self._fax = fax
        self._id = id
        self._postal_info = postal_info
        self._voice = voice

    @classmethod
    def from_dict(cls, dikt) -> 'ContactCreateType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The contact_createType of this ContactCreateType.  # noqa: E501
        :rtype: ContactCreateType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def auth_info(self) -> ContactAuthInfoType:
        """Gets the auth_info of this ContactCreateType.


        :return: The auth_info of this ContactCreateType.
        :rtype: ContactAuthInfoType
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info: ContactAuthInfoType):
        """Sets the auth_info of this ContactCreateType.


        :param auth_info: The auth_info of this ContactCreateType.
        :type auth_info: ContactAuthInfoType
        """
        if auth_info is None:
            raise ValueError("Invalid value for `auth_info`, must not be `None`")  # noqa: E501

        self._auth_info = auth_info

    @property
    def disclose(self) -> ContactDiscloseType:
        """Gets the disclose of this ContactCreateType.


        :return: The disclose of this ContactCreateType.
        :rtype: ContactDiscloseType
        """
        return self._disclose

    @disclose.setter
    def disclose(self, disclose: ContactDiscloseType):
        """Sets the disclose of this ContactCreateType.


        :param disclose: The disclose of this ContactCreateType.
        :type disclose: ContactDiscloseType
        """

        self._disclose = disclose

    @property
    def email(self) -> str:
        """Gets the email of this ContactCreateType.


        :return: The email of this ContactCreateType.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this ContactCreateType.


        :param email: The email of this ContactCreateType.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) < 1:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def fax(self) -> ContactE164Type:
        """Gets the fax of this ContactCreateType.


        :return: The fax of this ContactCreateType.
        :rtype: ContactE164Type
        """
        return self._fax

    @fax.setter
    def fax(self, fax: ContactE164Type):
        """Sets the fax of this ContactCreateType.


        :param fax: The fax of this ContactCreateType.
        :type fax: ContactE164Type
        """

        self._fax = fax

    @property
    def id(self) -> str:
        """Gets the id of this ContactCreateType.


        :return: The id of this ContactCreateType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ContactCreateType.


        :param id: The id of this ContactCreateType.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 16:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `16`")  # noqa: E501
        if id is not None and len(id) < 3:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `3`")  # noqa: E501

        self._id = id

    @property
    def postal_info(self) -> List[ContactPostalInfoType]:
        """Gets the postal_info of this ContactCreateType.


        :return: The postal_info of this ContactCreateType.
        :rtype: List[ContactPostalInfoType]
        """
        return self._postal_info

    @postal_info.setter
    def postal_info(self, postal_info: List[ContactPostalInfoType]):
        """Sets the postal_info of this ContactCreateType.


        :param postal_info: The postal_info of this ContactCreateType.
        :type postal_info: List[ContactPostalInfoType]
        """
        if postal_info is None:
            raise ValueError("Invalid value for `postal_info`, must not be `None`")  # noqa: E501
        if postal_info is not None and len(postal_info) > 2:
            raise ValueError("Invalid value for `postal_info`, number of items must be less than or equal to `2`")  # noqa: E501
        if postal_info is not None and len(postal_info) < 1:
            raise ValueError("Invalid value for `postal_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._postal_info = postal_info

    @property
    def voice(self) -> ContactE164Type:
        """Gets the voice of this ContactCreateType.


        :return: The voice of this ContactCreateType.
        :rtype: ContactE164Type
        """
        return self._voice

    @voice.setter
    def voice(self, voice: ContactE164Type):
        """Sets the voice of this ContactCreateType.


        :param voice: The voice of this ContactCreateType.
        :type voice: ContactE164Type
        """

        self._voice = voice
