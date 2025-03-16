from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.contact_auth_id_type import ContactAuthIDType
from rpp_py_flask_server.models.contact_create_type import ContactCreateType
from rpp_py_flask_server.models.contact_mid_type import ContactMIDType
from rpp_py_flask_server.models.contact_sid_type import ContactSIDType
from rpp_py_flask_server.models.contact_update_type import ContactUpdateType
from rpp_py_flask_server.models.domain_create_type import DomainCreateType
from rpp_py_flask_server.models.domain_info_type import DomainInfoType
from rpp_py_flask_server.models.domain_m_name_type import DomainMNameType
from rpp_py_flask_server.models.domain_s_name_type import DomainSNameType
from rpp_py_flask_server.models.domain_transfer_type import DomainTransferType
from rpp_py_flask_server.models.domain_update_type import DomainUpdateType
from rpp_py_flask_server.models.epp_read_write_type_one_of import EppReadWriteTypeOneOf
from rpp_py_flask_server.models.epp_read_write_type_one_of1 import EppReadWriteTypeOneOf1
from rpp_py_flask_server.models.epp_read_write_type_one_of10 import EppReadWriteTypeOneOf10
from rpp_py_flask_server.models.epp_read_write_type_one_of11 import EppReadWriteTypeOneOf11
from rpp_py_flask_server.models.epp_read_write_type_one_of12 import EppReadWriteTypeOneOf12
from rpp_py_flask_server.models.epp_read_write_type_one_of13 import EppReadWriteTypeOneOf13
from rpp_py_flask_server.models.epp_read_write_type_one_of14 import EppReadWriteTypeOneOf14
from rpp_py_flask_server.models.epp_read_write_type_one_of15 import EppReadWriteTypeOneOf15
from rpp_py_flask_server.models.epp_read_write_type_one_of16 import EppReadWriteTypeOneOf16
from rpp_py_flask_server.models.epp_read_write_type_one_of17 import EppReadWriteTypeOneOf17
from rpp_py_flask_server.models.epp_read_write_type_one_of18 import EppReadWriteTypeOneOf18
from rpp_py_flask_server.models.epp_read_write_type_one_of2 import EppReadWriteTypeOneOf2
from rpp_py_flask_server.models.epp_read_write_type_one_of3 import EppReadWriteTypeOneOf3
from rpp_py_flask_server.models.epp_read_write_type_one_of4 import EppReadWriteTypeOneOf4
from rpp_py_flask_server.models.epp_read_write_type_one_of5 import EppReadWriteTypeOneOf5
from rpp_py_flask_server.models.epp_read_write_type_one_of6 import EppReadWriteTypeOneOf6
from rpp_py_flask_server.models.epp_read_write_type_one_of7 import EppReadWriteTypeOneOf7
from rpp_py_flask_server.models.epp_read_write_type_one_of8 import EppReadWriteTypeOneOf8
from rpp_py_flask_server.models.epp_read_write_type_one_of9 import EppReadWriteTypeOneOf9
from rpp_py_flask_server.models.host_create_type import HostCreateType
from rpp_py_flask_server.models.host_m_name_type import HostMNameType
from rpp_py_flask_server.models.host_s_name_type import HostSNameType
from rpp_py_flask_server.models.host_update_type import HostUpdateType
from rpp_py_flask_server.models.sec_dnsds_or_key_type import SecDNSDsOrKeyType
from rpp_py_flask_server.models.sec_dns_update_type import SecDNSUpdateType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.contact_auth_id_type import ContactAuthIDType  # noqa: E501
from rpp_py_flask_server.models.contact_create_type import ContactCreateType  # noqa: E501
from rpp_py_flask_server.models.contact_mid_type import ContactMIDType  # noqa: E501
from rpp_py_flask_server.models.contact_sid_type import ContactSIDType  # noqa: E501
from rpp_py_flask_server.models.contact_update_type import ContactUpdateType  # noqa: E501
from rpp_py_flask_server.models.domain_create_type import DomainCreateType  # noqa: E501
from rpp_py_flask_server.models.domain_info_type import DomainInfoType  # noqa: E501
from rpp_py_flask_server.models.domain_m_name_type import DomainMNameType  # noqa: E501
from rpp_py_flask_server.models.domain_s_name_type import DomainSNameType  # noqa: E501
from rpp_py_flask_server.models.domain_transfer_type import DomainTransferType  # noqa: E501
from rpp_py_flask_server.models.domain_update_type import DomainUpdateType  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of import EppReadWriteTypeOneOf  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of1 import EppReadWriteTypeOneOf1  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of10 import EppReadWriteTypeOneOf10  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of11 import EppReadWriteTypeOneOf11  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of12 import EppReadWriteTypeOneOf12  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of13 import EppReadWriteTypeOneOf13  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of14 import EppReadWriteTypeOneOf14  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of15 import EppReadWriteTypeOneOf15  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of16 import EppReadWriteTypeOneOf16  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of17 import EppReadWriteTypeOneOf17  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of18 import EppReadWriteTypeOneOf18  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of2 import EppReadWriteTypeOneOf2  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of3 import EppReadWriteTypeOneOf3  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of4 import EppReadWriteTypeOneOf4  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of5 import EppReadWriteTypeOneOf5  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of6 import EppReadWriteTypeOneOf6  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of7 import EppReadWriteTypeOneOf7  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of8 import EppReadWriteTypeOneOf8  # noqa: E501
from rpp_py_flask_server.models.epp_read_write_type_one_of9 import EppReadWriteTypeOneOf9  # noqa: E501
from rpp_py_flask_server.models.host_create_type import HostCreateType  # noqa: E501
from rpp_py_flask_server.models.host_m_name_type import HostMNameType  # noqa: E501
from rpp_py_flask_server.models.host_s_name_type import HostSNameType  # noqa: E501
from rpp_py_flask_server.models.host_update_type import HostUpdateType  # noqa: E501
from rpp_py_flask_server.models.sec_dns_update_type import SecDNSUpdateType  # noqa: E501
from rpp_py_flask_server.models.sec_dnsds_or_key_type import SecDNSDsOrKeyType  # noqa: E501

class EppReadWriteType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_check=None, domain_create=None, domain_delete=None, domain_info=None, domain_transfer=None, domain_update=None, host_check=None, host_create=None, host_delete=None, host_info=None, host_update=None, contact_check=None, contact_create=None, contact_delete=None, contact_info=None, contact_transfer=None, contact_update=None, sec_dns_create=None, sec_dns_update=None):  # noqa: E501
        """EppReadWriteType - a model defined in OpenAPI

        :param domain_check: The domain_check of this EppReadWriteType.  # noqa: E501
        :type domain_check: DomainMNameType
        :param domain_create: The domain_create of this EppReadWriteType.  # noqa: E501
        :type domain_create: DomainCreateType
        :param domain_delete: The domain_delete of this EppReadWriteType.  # noqa: E501
        :type domain_delete: DomainSNameType
        :param domain_info: The domain_info of this EppReadWriteType.  # noqa: E501
        :type domain_info: DomainInfoType
        :param domain_transfer: The domain_transfer of this EppReadWriteType.  # noqa: E501
        :type domain_transfer: DomainTransferType
        :param domain_update: The domain_update of this EppReadWriteType.  # noqa: E501
        :type domain_update: DomainUpdateType
        :param host_check: The host_check of this EppReadWriteType.  # noqa: E501
        :type host_check: HostMNameType
        :param host_create: The host_create of this EppReadWriteType.  # noqa: E501
        :type host_create: HostCreateType
        :param host_delete: The host_delete of this EppReadWriteType.  # noqa: E501
        :type host_delete: HostSNameType
        :param host_info: The host_info of this EppReadWriteType.  # noqa: E501
        :type host_info: HostSNameType
        :param host_update: The host_update of this EppReadWriteType.  # noqa: E501
        :type host_update: HostUpdateType
        :param contact_check: The contact_check of this EppReadWriteType.  # noqa: E501
        :type contact_check: ContactMIDType
        :param contact_create: The contact_create of this EppReadWriteType.  # noqa: E501
        :type contact_create: ContactCreateType
        :param contact_delete: The contact_delete of this EppReadWriteType.  # noqa: E501
        :type contact_delete: ContactSIDType
        :param contact_info: The contact_info of this EppReadWriteType.  # noqa: E501
        :type contact_info: ContactAuthIDType
        :param contact_transfer: The contact_transfer of this EppReadWriteType.  # noqa: E501
        :type contact_transfer: ContactAuthIDType
        :param contact_update: The contact_update of this EppReadWriteType.  # noqa: E501
        :type contact_update: ContactUpdateType
        :param sec_dns_create: The sec_dns_create of this EppReadWriteType.  # noqa: E501
        :type sec_dns_create: SecDNSDsOrKeyType
        :param sec_dns_update: The sec_dns_update of this EppReadWriteType.  # noqa: E501
        :type sec_dns_update: SecDNSUpdateType
        """
        self.openapi_types = {
            'domain_check': DomainMNameType,
            'domain_create': DomainCreateType,
            'domain_delete': DomainSNameType,
            'domain_info': DomainInfoType,
            'domain_transfer': DomainTransferType,
            'domain_update': DomainUpdateType,
            'host_check': HostMNameType,
            'host_create': HostCreateType,
            'host_delete': HostSNameType,
            'host_info': HostSNameType,
            'host_update': HostUpdateType,
            'contact_check': ContactMIDType,
            'contact_create': ContactCreateType,
            'contact_delete': ContactSIDType,
            'contact_info': ContactAuthIDType,
            'contact_transfer': ContactAuthIDType,
            'contact_update': ContactUpdateType,
            'sec_dns_create': SecDNSDsOrKeyType,
            'sec_dns_update': SecDNSUpdateType
        }

        self.attribute_map = {
            'domain_check': 'domain_check',
            'domain_create': 'domain_create',
            'domain_delete': 'domain_delete',
            'domain_info': 'domain_info',
            'domain_transfer': 'domain_transfer',
            'domain_update': 'domain_update',
            'host_check': 'host_check',
            'host_create': 'host_create',
            'host_delete': 'host_delete',
            'host_info': 'host_info',
            'host_update': 'host_update',
            'contact_check': 'contact_check',
            'contact_create': 'contact_create',
            'contact_delete': 'contact_delete',
            'contact_info': 'contact_info',
            'contact_transfer': 'contact_transfer',
            'contact_update': 'contact_update',
            'sec_dns_create': 'secDNS_create',
            'sec_dns_update': 'secDNS_update'
        }

        self._domain_check = domain_check
        self._domain_create = domain_create
        self._domain_delete = domain_delete
        self._domain_info = domain_info
        self._domain_transfer = domain_transfer
        self._domain_update = domain_update
        self._host_check = host_check
        self._host_create = host_create
        self._host_delete = host_delete
        self._host_info = host_info
        self._host_update = host_update
        self._contact_check = contact_check
        self._contact_create = contact_create
        self._contact_delete = contact_delete
        self._contact_info = contact_info
        self._contact_transfer = contact_transfer
        self._contact_update = contact_update
        self._sec_dns_create = sec_dns_create
        self._sec_dns_update = sec_dns_update

    @classmethod
    def from_dict(cls, dikt) -> 'EppReadWriteType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_readWriteType of this EppReadWriteType.  # noqa: E501
        :rtype: EppReadWriteType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_check(self) -> DomainMNameType:
        """Gets the domain_check of this EppReadWriteType.


        :return: The domain_check of this EppReadWriteType.
        :rtype: DomainMNameType
        """
        return self._domain_check

    @domain_check.setter
    def domain_check(self, domain_check: DomainMNameType):
        """Sets the domain_check of this EppReadWriteType.


        :param domain_check: The domain_check of this EppReadWriteType.
        :type domain_check: DomainMNameType
        """
        if domain_check is None:
            raise ValueError("Invalid value for `domain_check`, must not be `None`")  # noqa: E501

        self._domain_check = domain_check

    @property
    def domain_create(self) -> DomainCreateType:
        """Gets the domain_create of this EppReadWriteType.


        :return: The domain_create of this EppReadWriteType.
        :rtype: DomainCreateType
        """
        return self._domain_create

    @domain_create.setter
    def domain_create(self, domain_create: DomainCreateType):
        """Sets the domain_create of this EppReadWriteType.


        :param domain_create: The domain_create of this EppReadWriteType.
        :type domain_create: DomainCreateType
        """
        if domain_create is None:
            raise ValueError("Invalid value for `domain_create`, must not be `None`")  # noqa: E501

        self._domain_create = domain_create

    @property
    def domain_delete(self) -> DomainSNameType:
        """Gets the domain_delete of this EppReadWriteType.


        :return: The domain_delete of this EppReadWriteType.
        :rtype: DomainSNameType
        """
        return self._domain_delete

    @domain_delete.setter
    def domain_delete(self, domain_delete: DomainSNameType):
        """Sets the domain_delete of this EppReadWriteType.


        :param domain_delete: The domain_delete of this EppReadWriteType.
        :type domain_delete: DomainSNameType
        """
        if domain_delete is None:
            raise ValueError("Invalid value for `domain_delete`, must not be `None`")  # noqa: E501

        self._domain_delete = domain_delete

    @property
    def domain_info(self) -> DomainInfoType:
        """Gets the domain_info of this EppReadWriteType.


        :return: The domain_info of this EppReadWriteType.
        :rtype: DomainInfoType
        """
        return self._domain_info

    @domain_info.setter
    def domain_info(self, domain_info: DomainInfoType):
        """Sets the domain_info of this EppReadWriteType.


        :param domain_info: The domain_info of this EppReadWriteType.
        :type domain_info: DomainInfoType
        """
        if domain_info is None:
            raise ValueError("Invalid value for `domain_info`, must not be `None`")  # noqa: E501

        self._domain_info = domain_info

    @property
    def domain_transfer(self) -> DomainTransferType:
        """Gets the domain_transfer of this EppReadWriteType.


        :return: The domain_transfer of this EppReadWriteType.
        :rtype: DomainTransferType
        """
        return self._domain_transfer

    @domain_transfer.setter
    def domain_transfer(self, domain_transfer: DomainTransferType):
        """Sets the domain_transfer of this EppReadWriteType.


        :param domain_transfer: The domain_transfer of this EppReadWriteType.
        :type domain_transfer: DomainTransferType
        """
        if domain_transfer is None:
            raise ValueError("Invalid value for `domain_transfer`, must not be `None`")  # noqa: E501

        self._domain_transfer = domain_transfer

    @property
    def domain_update(self) -> DomainUpdateType:
        """Gets the domain_update of this EppReadWriteType.


        :return: The domain_update of this EppReadWriteType.
        :rtype: DomainUpdateType
        """
        return self._domain_update

    @domain_update.setter
    def domain_update(self, domain_update: DomainUpdateType):
        """Sets the domain_update of this EppReadWriteType.


        :param domain_update: The domain_update of this EppReadWriteType.
        :type domain_update: DomainUpdateType
        """
        if domain_update is None:
            raise ValueError("Invalid value for `domain_update`, must not be `None`")  # noqa: E501

        self._domain_update = domain_update

    @property
    def host_check(self) -> HostMNameType:
        """Gets the host_check of this EppReadWriteType.


        :return: The host_check of this EppReadWriteType.
        :rtype: HostMNameType
        """
        return self._host_check

    @host_check.setter
    def host_check(self, host_check: HostMNameType):
        """Sets the host_check of this EppReadWriteType.


        :param host_check: The host_check of this EppReadWriteType.
        :type host_check: HostMNameType
        """
        if host_check is None:
            raise ValueError("Invalid value for `host_check`, must not be `None`")  # noqa: E501

        self._host_check = host_check

    @property
    def host_create(self) -> HostCreateType:
        """Gets the host_create of this EppReadWriteType.


        :return: The host_create of this EppReadWriteType.
        :rtype: HostCreateType
        """
        return self._host_create

    @host_create.setter
    def host_create(self, host_create: HostCreateType):
        """Sets the host_create of this EppReadWriteType.


        :param host_create: The host_create of this EppReadWriteType.
        :type host_create: HostCreateType
        """
        if host_create is None:
            raise ValueError("Invalid value for `host_create`, must not be `None`")  # noqa: E501

        self._host_create = host_create

    @property
    def host_delete(self) -> HostSNameType:
        """Gets the host_delete of this EppReadWriteType.


        :return: The host_delete of this EppReadWriteType.
        :rtype: HostSNameType
        """
        return self._host_delete

    @host_delete.setter
    def host_delete(self, host_delete: HostSNameType):
        """Sets the host_delete of this EppReadWriteType.


        :param host_delete: The host_delete of this EppReadWriteType.
        :type host_delete: HostSNameType
        """
        if host_delete is None:
            raise ValueError("Invalid value for `host_delete`, must not be `None`")  # noqa: E501

        self._host_delete = host_delete

    @property
    def host_info(self) -> HostSNameType:
        """Gets the host_info of this EppReadWriteType.


        :return: The host_info of this EppReadWriteType.
        :rtype: HostSNameType
        """
        return self._host_info

    @host_info.setter
    def host_info(self, host_info: HostSNameType):
        """Sets the host_info of this EppReadWriteType.


        :param host_info: The host_info of this EppReadWriteType.
        :type host_info: HostSNameType
        """
        if host_info is None:
            raise ValueError("Invalid value for `host_info`, must not be `None`")  # noqa: E501

        self._host_info = host_info

    @property
    def host_update(self) -> HostUpdateType:
        """Gets the host_update of this EppReadWriteType.


        :return: The host_update of this EppReadWriteType.
        :rtype: HostUpdateType
        """
        return self._host_update

    @host_update.setter
    def host_update(self, host_update: HostUpdateType):
        """Sets the host_update of this EppReadWriteType.


        :param host_update: The host_update of this EppReadWriteType.
        :type host_update: HostUpdateType
        """
        if host_update is None:
            raise ValueError("Invalid value for `host_update`, must not be `None`")  # noqa: E501

        self._host_update = host_update

    @property
    def contact_check(self) -> ContactMIDType:
        """Gets the contact_check of this EppReadWriteType.


        :return: The contact_check of this EppReadWriteType.
        :rtype: ContactMIDType
        """
        return self._contact_check

    @contact_check.setter
    def contact_check(self, contact_check: ContactMIDType):
        """Sets the contact_check of this EppReadWriteType.


        :param contact_check: The contact_check of this EppReadWriteType.
        :type contact_check: ContactMIDType
        """
        if contact_check is None:
            raise ValueError("Invalid value for `contact_check`, must not be `None`")  # noqa: E501

        self._contact_check = contact_check

    @property
    def contact_create(self) -> ContactCreateType:
        """Gets the contact_create of this EppReadWriteType.


        :return: The contact_create of this EppReadWriteType.
        :rtype: ContactCreateType
        """
        return self._contact_create

    @contact_create.setter
    def contact_create(self, contact_create: ContactCreateType):
        """Sets the contact_create of this EppReadWriteType.


        :param contact_create: The contact_create of this EppReadWriteType.
        :type contact_create: ContactCreateType
        """
        if contact_create is None:
            raise ValueError("Invalid value for `contact_create`, must not be `None`")  # noqa: E501

        self._contact_create = contact_create

    @property
    def contact_delete(self) -> ContactSIDType:
        """Gets the contact_delete of this EppReadWriteType.


        :return: The contact_delete of this EppReadWriteType.
        :rtype: ContactSIDType
        """
        return self._contact_delete

    @contact_delete.setter
    def contact_delete(self, contact_delete: ContactSIDType):
        """Sets the contact_delete of this EppReadWriteType.


        :param contact_delete: The contact_delete of this EppReadWriteType.
        :type contact_delete: ContactSIDType
        """
        if contact_delete is None:
            raise ValueError("Invalid value for `contact_delete`, must not be `None`")  # noqa: E501

        self._contact_delete = contact_delete

    @property
    def contact_info(self) -> ContactAuthIDType:
        """Gets the contact_info of this EppReadWriteType.


        :return: The contact_info of this EppReadWriteType.
        :rtype: ContactAuthIDType
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info: ContactAuthIDType):
        """Sets the contact_info of this EppReadWriteType.


        :param contact_info: The contact_info of this EppReadWriteType.
        :type contact_info: ContactAuthIDType
        """
        if contact_info is None:
            raise ValueError("Invalid value for `contact_info`, must not be `None`")  # noqa: E501

        self._contact_info = contact_info

    @property
    def contact_transfer(self) -> ContactAuthIDType:
        """Gets the contact_transfer of this EppReadWriteType.


        :return: The contact_transfer of this EppReadWriteType.
        :rtype: ContactAuthIDType
        """
        return self._contact_transfer

    @contact_transfer.setter
    def contact_transfer(self, contact_transfer: ContactAuthIDType):
        """Sets the contact_transfer of this EppReadWriteType.


        :param contact_transfer: The contact_transfer of this EppReadWriteType.
        :type contact_transfer: ContactAuthIDType
        """
        if contact_transfer is None:
            raise ValueError("Invalid value for `contact_transfer`, must not be `None`")  # noqa: E501

        self._contact_transfer = contact_transfer

    @property
    def contact_update(self) -> ContactUpdateType:
        """Gets the contact_update of this EppReadWriteType.


        :return: The contact_update of this EppReadWriteType.
        :rtype: ContactUpdateType
        """
        return self._contact_update

    @contact_update.setter
    def contact_update(self, contact_update: ContactUpdateType):
        """Sets the contact_update of this EppReadWriteType.


        :param contact_update: The contact_update of this EppReadWriteType.
        :type contact_update: ContactUpdateType
        """
        if contact_update is None:
            raise ValueError("Invalid value for `contact_update`, must not be `None`")  # noqa: E501

        self._contact_update = contact_update

    @property
    def sec_dns_create(self) -> SecDNSDsOrKeyType:
        """Gets the sec_dns_create of this EppReadWriteType.


        :return: The sec_dns_create of this EppReadWriteType.
        :rtype: SecDNSDsOrKeyType
        """
        return self._sec_dns_create

    @sec_dns_create.setter
    def sec_dns_create(self, sec_dns_create: SecDNSDsOrKeyType):
        """Sets the sec_dns_create of this EppReadWriteType.


        :param sec_dns_create: The sec_dns_create of this EppReadWriteType.
        :type sec_dns_create: SecDNSDsOrKeyType
        """
        if sec_dns_create is None:
            raise ValueError("Invalid value for `sec_dns_create`, must not be `None`")  # noqa: E501

        self._sec_dns_create = sec_dns_create

    @property
    def sec_dns_update(self) -> SecDNSUpdateType:
        """Gets the sec_dns_update of this EppReadWriteType.


        :return: The sec_dns_update of this EppReadWriteType.
        :rtype: SecDNSUpdateType
        """
        return self._sec_dns_update

    @sec_dns_update.setter
    def sec_dns_update(self, sec_dns_update: SecDNSUpdateType):
        """Sets the sec_dns_update of this EppReadWriteType.


        :param sec_dns_update: The sec_dns_update of this EppReadWriteType.
        :type sec_dns_update: SecDNSUpdateType
        """
        if sec_dns_update is None:
            raise ValueError("Invalid value for `sec_dns_update`, must not be `None`")  # noqa: E501

        self._sec_dns_update = sec_dns_update
