from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.contact_chk_data_type import ContactChkDataType
from rpp_py_flask_server.models.contact_cre_data_type import ContactCreDataType
from rpp_py_flask_server.models.contact_inf_data_type import ContactInfDataType
from rpp_py_flask_server.models.contact_pan_data_type import ContactPanDataType
from rpp_py_flask_server.models.contact_trn_data_type import ContactTrnDataType
from rpp_py_flask_server.models.domain_chk_data_type import DomainChkDataType
from rpp_py_flask_server.models.domain_cre_data_type import DomainCreDataType
from rpp_py_flask_server.models.domain_inf_data_type import DomainInfDataType
from rpp_py_flask_server.models.domain_pan_data_type import DomainPanDataType
from rpp_py_flask_server.models.domain_ren_data_type import DomainRenDataType
from rpp_py_flask_server.models.domain_trn_data_type import DomainTrnDataType
from rpp_py_flask_server.models.epp_ext_any_type_one_of import EppExtAnyTypeOneOf
from rpp_py_flask_server.models.epp_ext_any_type_one_of1 import EppExtAnyTypeOneOf1
from rpp_py_flask_server.models.epp_ext_any_type_one_of10 import EppExtAnyTypeOneOf10
from rpp_py_flask_server.models.epp_ext_any_type_one_of11 import EppExtAnyTypeOneOf11
from rpp_py_flask_server.models.epp_ext_any_type_one_of12 import EppExtAnyTypeOneOf12
from rpp_py_flask_server.models.epp_ext_any_type_one_of13 import EppExtAnyTypeOneOf13
from rpp_py_flask_server.models.epp_ext_any_type_one_of14 import EppExtAnyTypeOneOf14
from rpp_py_flask_server.models.epp_ext_any_type_one_of15 import EppExtAnyTypeOneOf15
from rpp_py_flask_server.models.epp_ext_any_type_one_of2 import EppExtAnyTypeOneOf2
from rpp_py_flask_server.models.epp_ext_any_type_one_of3 import EppExtAnyTypeOneOf3
from rpp_py_flask_server.models.epp_ext_any_type_one_of4 import EppExtAnyTypeOneOf4
from rpp_py_flask_server.models.epp_ext_any_type_one_of5 import EppExtAnyTypeOneOf5
from rpp_py_flask_server.models.epp_ext_any_type_one_of6 import EppExtAnyTypeOneOf6
from rpp_py_flask_server.models.epp_ext_any_type_one_of7 import EppExtAnyTypeOneOf7
from rpp_py_flask_server.models.epp_ext_any_type_one_of8 import EppExtAnyTypeOneOf8
from rpp_py_flask_server.models.epp_ext_any_type_one_of9 import EppExtAnyTypeOneOf9
from rpp_py_flask_server.models.host_chk_data_type import HostChkDataType
from rpp_py_flask_server.models.host_cre_data_type import HostCreDataType
from rpp_py_flask_server.models.host_inf_data_type import HostInfDataType
from rpp_py_flask_server.models.host_pan_data_type import HostPanDataType
from rpp_py_flask_server.models.sec_dnsds_or_key_type import SecDNSDsOrKeyType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.contact_chk_data_type import ContactChkDataType  # noqa: E501
from rpp_py_flask_server.models.contact_cre_data_type import ContactCreDataType  # noqa: E501
from rpp_py_flask_server.models.contact_inf_data_type import ContactInfDataType  # noqa: E501
from rpp_py_flask_server.models.contact_pan_data_type import ContactPanDataType  # noqa: E501
from rpp_py_flask_server.models.contact_trn_data_type import ContactTrnDataType  # noqa: E501
from rpp_py_flask_server.models.domain_chk_data_type import DomainChkDataType  # noqa: E501
from rpp_py_flask_server.models.domain_cre_data_type import DomainCreDataType  # noqa: E501
from rpp_py_flask_server.models.domain_inf_data_type import DomainInfDataType  # noqa: E501
from rpp_py_flask_server.models.domain_pan_data_type import DomainPanDataType  # noqa: E501
from rpp_py_flask_server.models.domain_ren_data_type import DomainRenDataType  # noqa: E501
from rpp_py_flask_server.models.domain_trn_data_type import DomainTrnDataType  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of import EppExtAnyTypeOneOf  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of1 import EppExtAnyTypeOneOf1  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of10 import EppExtAnyTypeOneOf10  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of11 import EppExtAnyTypeOneOf11  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of12 import EppExtAnyTypeOneOf12  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of13 import EppExtAnyTypeOneOf13  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of14 import EppExtAnyTypeOneOf14  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of15 import EppExtAnyTypeOneOf15  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of2 import EppExtAnyTypeOneOf2  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of3 import EppExtAnyTypeOneOf3  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of4 import EppExtAnyTypeOneOf4  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of5 import EppExtAnyTypeOneOf5  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of6 import EppExtAnyTypeOneOf6  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of7 import EppExtAnyTypeOneOf7  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of8 import EppExtAnyTypeOneOf8  # noqa: E501
from rpp_py_flask_server.models.epp_ext_any_type_one_of9 import EppExtAnyTypeOneOf9  # noqa: E501
from rpp_py_flask_server.models.host_chk_data_type import HostChkDataType  # noqa: E501
from rpp_py_flask_server.models.host_cre_data_type import HostCreDataType  # noqa: E501
from rpp_py_flask_server.models.host_inf_data_type import HostInfDataType  # noqa: E501
from rpp_py_flask_server.models.host_pan_data_type import HostPanDataType  # noqa: E501
from rpp_py_flask_server.models.sec_dnsds_or_key_type import SecDNSDsOrKeyType  # noqa: E501

class EppExtAnyType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_chk_data=None, domain_cre_data=None, domain_inf_data=None, domain_pan_data=None, domain_ren_data=None, domain_trn_data=None, host_chk_data=None, host_cre_data=None, host_inf_data=None, host_pan_data=None, contact_chk_data=None, contact_cre_data=None, contact_inf_data=None, contact_pan_data=None, contact_trn_data=None, sec_dns_inf_data=None):  # noqa: E501
        """EppExtAnyType - a model defined in OpenAPI

        :param domain_chk_data: The domain_chk_data of this EppExtAnyType.  # noqa: E501
        :type domain_chk_data: DomainChkDataType
        :param domain_cre_data: The domain_cre_data of this EppExtAnyType.  # noqa: E501
        :type domain_cre_data: DomainCreDataType
        :param domain_inf_data: The domain_inf_data of this EppExtAnyType.  # noqa: E501
        :type domain_inf_data: DomainInfDataType
        :param domain_pan_data: The domain_pan_data of this EppExtAnyType.  # noqa: E501
        :type domain_pan_data: DomainPanDataType
        :param domain_ren_data: The domain_ren_data of this EppExtAnyType.  # noqa: E501
        :type domain_ren_data: DomainRenDataType
        :param domain_trn_data: The domain_trn_data of this EppExtAnyType.  # noqa: E501
        :type domain_trn_data: DomainTrnDataType
        :param host_chk_data: The host_chk_data of this EppExtAnyType.  # noqa: E501
        :type host_chk_data: HostChkDataType
        :param host_cre_data: The host_cre_data of this EppExtAnyType.  # noqa: E501
        :type host_cre_data: HostCreDataType
        :param host_inf_data: The host_inf_data of this EppExtAnyType.  # noqa: E501
        :type host_inf_data: HostInfDataType
        :param host_pan_data: The host_pan_data of this EppExtAnyType.  # noqa: E501
        :type host_pan_data: HostPanDataType
        :param contact_chk_data: The contact_chk_data of this EppExtAnyType.  # noqa: E501
        :type contact_chk_data: ContactChkDataType
        :param contact_cre_data: The contact_cre_data of this EppExtAnyType.  # noqa: E501
        :type contact_cre_data: ContactCreDataType
        :param contact_inf_data: The contact_inf_data of this EppExtAnyType.  # noqa: E501
        :type contact_inf_data: ContactInfDataType
        :param contact_pan_data: The contact_pan_data of this EppExtAnyType.  # noqa: E501
        :type contact_pan_data: ContactPanDataType
        :param contact_trn_data: The contact_trn_data of this EppExtAnyType.  # noqa: E501
        :type contact_trn_data: ContactTrnDataType
        :param sec_dns_inf_data: The sec_dns_inf_data of this EppExtAnyType.  # noqa: E501
        :type sec_dns_inf_data: SecDNSDsOrKeyType
        """
        self.openapi_types = {
            'domain_chk_data': DomainChkDataType,
            'domain_cre_data': DomainCreDataType,
            'domain_inf_data': DomainInfDataType,
            'domain_pan_data': DomainPanDataType,
            'domain_ren_data': DomainRenDataType,
            'domain_trn_data': DomainTrnDataType,
            'host_chk_data': HostChkDataType,
            'host_cre_data': HostCreDataType,
            'host_inf_data': HostInfDataType,
            'host_pan_data': HostPanDataType,
            'contact_chk_data': ContactChkDataType,
            'contact_cre_data': ContactCreDataType,
            'contact_inf_data': ContactInfDataType,
            'contact_pan_data': ContactPanDataType,
            'contact_trn_data': ContactTrnDataType,
            'sec_dns_inf_data': SecDNSDsOrKeyType
        }

        self.attribute_map = {
            'domain_chk_data': 'domain_chkData',
            'domain_cre_data': 'domain_creData',
            'domain_inf_data': 'domain_infData',
            'domain_pan_data': 'domain_panData',
            'domain_ren_data': 'domain_renData',
            'domain_trn_data': 'domain_trnData',
            'host_chk_data': 'host_chkData',
            'host_cre_data': 'host_creData',
            'host_inf_data': 'host_infData',
            'host_pan_data': 'host_panData',
            'contact_chk_data': 'contact_chkData',
            'contact_cre_data': 'contact_creData',
            'contact_inf_data': 'contact_infData',
            'contact_pan_data': 'contact_panData',
            'contact_trn_data': 'contact_trnData',
            'sec_dns_inf_data': 'secDNS_infData'
        }

        self._domain_chk_data = domain_chk_data
        self._domain_cre_data = domain_cre_data
        self._domain_inf_data = domain_inf_data
        self._domain_pan_data = domain_pan_data
        self._domain_ren_data = domain_ren_data
        self._domain_trn_data = domain_trn_data
        self._host_chk_data = host_chk_data
        self._host_cre_data = host_cre_data
        self._host_inf_data = host_inf_data
        self._host_pan_data = host_pan_data
        self._contact_chk_data = contact_chk_data
        self._contact_cre_data = contact_cre_data
        self._contact_inf_data = contact_inf_data
        self._contact_pan_data = contact_pan_data
        self._contact_trn_data = contact_trn_data
        self._sec_dns_inf_data = sec_dns_inf_data

    @classmethod
    def from_dict(cls, dikt) -> 'EppExtAnyType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_extAnyType of this EppExtAnyType.  # noqa: E501
        :rtype: EppExtAnyType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_chk_data(self) -> DomainChkDataType:
        """Gets the domain_chk_data of this EppExtAnyType.


        :return: The domain_chk_data of this EppExtAnyType.
        :rtype: DomainChkDataType
        """
        return self._domain_chk_data

    @domain_chk_data.setter
    def domain_chk_data(self, domain_chk_data: DomainChkDataType):
        """Sets the domain_chk_data of this EppExtAnyType.


        :param domain_chk_data: The domain_chk_data of this EppExtAnyType.
        :type domain_chk_data: DomainChkDataType
        """
        if domain_chk_data is None:
            raise ValueError("Invalid value for `domain_chk_data`, must not be `None`")  # noqa: E501

        self._domain_chk_data = domain_chk_data

    @property
    def domain_cre_data(self) -> DomainCreDataType:
        """Gets the domain_cre_data of this EppExtAnyType.


        :return: The domain_cre_data of this EppExtAnyType.
        :rtype: DomainCreDataType
        """
        return self._domain_cre_data

    @domain_cre_data.setter
    def domain_cre_data(self, domain_cre_data: DomainCreDataType):
        """Sets the domain_cre_data of this EppExtAnyType.


        :param domain_cre_data: The domain_cre_data of this EppExtAnyType.
        :type domain_cre_data: DomainCreDataType
        """
        if domain_cre_data is None:
            raise ValueError("Invalid value for `domain_cre_data`, must not be `None`")  # noqa: E501

        self._domain_cre_data = domain_cre_data

    @property
    def domain_inf_data(self) -> DomainInfDataType:
        """Gets the domain_inf_data of this EppExtAnyType.


        :return: The domain_inf_data of this EppExtAnyType.
        :rtype: DomainInfDataType
        """
        return self._domain_inf_data

    @domain_inf_data.setter
    def domain_inf_data(self, domain_inf_data: DomainInfDataType):
        """Sets the domain_inf_data of this EppExtAnyType.


        :param domain_inf_data: The domain_inf_data of this EppExtAnyType.
        :type domain_inf_data: DomainInfDataType
        """
        if domain_inf_data is None:
            raise ValueError("Invalid value for `domain_inf_data`, must not be `None`")  # noqa: E501

        self._domain_inf_data = domain_inf_data

    @property
    def domain_pan_data(self) -> DomainPanDataType:
        """Gets the domain_pan_data of this EppExtAnyType.


        :return: The domain_pan_data of this EppExtAnyType.
        :rtype: DomainPanDataType
        """
        return self._domain_pan_data

    @domain_pan_data.setter
    def domain_pan_data(self, domain_pan_data: DomainPanDataType):
        """Sets the domain_pan_data of this EppExtAnyType.


        :param domain_pan_data: The domain_pan_data of this EppExtAnyType.
        :type domain_pan_data: DomainPanDataType
        """
        if domain_pan_data is None:
            raise ValueError("Invalid value for `domain_pan_data`, must not be `None`")  # noqa: E501

        self._domain_pan_data = domain_pan_data

    @property
    def domain_ren_data(self) -> DomainRenDataType:
        """Gets the domain_ren_data of this EppExtAnyType.


        :return: The domain_ren_data of this EppExtAnyType.
        :rtype: DomainRenDataType
        """
        return self._domain_ren_data

    @domain_ren_data.setter
    def domain_ren_data(self, domain_ren_data: DomainRenDataType):
        """Sets the domain_ren_data of this EppExtAnyType.


        :param domain_ren_data: The domain_ren_data of this EppExtAnyType.
        :type domain_ren_data: DomainRenDataType
        """
        if domain_ren_data is None:
            raise ValueError("Invalid value for `domain_ren_data`, must not be `None`")  # noqa: E501

        self._domain_ren_data = domain_ren_data

    @property
    def domain_trn_data(self) -> DomainTrnDataType:
        """Gets the domain_trn_data of this EppExtAnyType.


        :return: The domain_trn_data of this EppExtAnyType.
        :rtype: DomainTrnDataType
        """
        return self._domain_trn_data

    @domain_trn_data.setter
    def domain_trn_data(self, domain_trn_data: DomainTrnDataType):
        """Sets the domain_trn_data of this EppExtAnyType.


        :param domain_trn_data: The domain_trn_data of this EppExtAnyType.
        :type domain_trn_data: DomainTrnDataType
        """
        if domain_trn_data is None:
            raise ValueError("Invalid value for `domain_trn_data`, must not be `None`")  # noqa: E501

        self._domain_trn_data = domain_trn_data

    @property
    def host_chk_data(self) -> HostChkDataType:
        """Gets the host_chk_data of this EppExtAnyType.


        :return: The host_chk_data of this EppExtAnyType.
        :rtype: HostChkDataType
        """
        return self._host_chk_data

    @host_chk_data.setter
    def host_chk_data(self, host_chk_data: HostChkDataType):
        """Sets the host_chk_data of this EppExtAnyType.


        :param host_chk_data: The host_chk_data of this EppExtAnyType.
        :type host_chk_data: HostChkDataType
        """
        if host_chk_data is None:
            raise ValueError("Invalid value for `host_chk_data`, must not be `None`")  # noqa: E501

        self._host_chk_data = host_chk_data

    @property
    def host_cre_data(self) -> HostCreDataType:
        """Gets the host_cre_data of this EppExtAnyType.


        :return: The host_cre_data of this EppExtAnyType.
        :rtype: HostCreDataType
        """
        return self._host_cre_data

    @host_cre_data.setter
    def host_cre_data(self, host_cre_data: HostCreDataType):
        """Sets the host_cre_data of this EppExtAnyType.


        :param host_cre_data: The host_cre_data of this EppExtAnyType.
        :type host_cre_data: HostCreDataType
        """
        if host_cre_data is None:
            raise ValueError("Invalid value for `host_cre_data`, must not be `None`")  # noqa: E501

        self._host_cre_data = host_cre_data

    @property
    def host_inf_data(self) -> HostInfDataType:
        """Gets the host_inf_data of this EppExtAnyType.


        :return: The host_inf_data of this EppExtAnyType.
        :rtype: HostInfDataType
        """
        return self._host_inf_data

    @host_inf_data.setter
    def host_inf_data(self, host_inf_data: HostInfDataType):
        """Sets the host_inf_data of this EppExtAnyType.


        :param host_inf_data: The host_inf_data of this EppExtAnyType.
        :type host_inf_data: HostInfDataType
        """
        if host_inf_data is None:
            raise ValueError("Invalid value for `host_inf_data`, must not be `None`")  # noqa: E501

        self._host_inf_data = host_inf_data

    @property
    def host_pan_data(self) -> HostPanDataType:
        """Gets the host_pan_data of this EppExtAnyType.


        :return: The host_pan_data of this EppExtAnyType.
        :rtype: HostPanDataType
        """
        return self._host_pan_data

    @host_pan_data.setter
    def host_pan_data(self, host_pan_data: HostPanDataType):
        """Sets the host_pan_data of this EppExtAnyType.


        :param host_pan_data: The host_pan_data of this EppExtAnyType.
        :type host_pan_data: HostPanDataType
        """
        if host_pan_data is None:
            raise ValueError("Invalid value for `host_pan_data`, must not be `None`")  # noqa: E501

        self._host_pan_data = host_pan_data

    @property
    def contact_chk_data(self) -> ContactChkDataType:
        """Gets the contact_chk_data of this EppExtAnyType.


        :return: The contact_chk_data of this EppExtAnyType.
        :rtype: ContactChkDataType
        """
        return self._contact_chk_data

    @contact_chk_data.setter
    def contact_chk_data(self, contact_chk_data: ContactChkDataType):
        """Sets the contact_chk_data of this EppExtAnyType.


        :param contact_chk_data: The contact_chk_data of this EppExtAnyType.
        :type contact_chk_data: ContactChkDataType
        """
        if contact_chk_data is None:
            raise ValueError("Invalid value for `contact_chk_data`, must not be `None`")  # noqa: E501

        self._contact_chk_data = contact_chk_data

    @property
    def contact_cre_data(self) -> ContactCreDataType:
        """Gets the contact_cre_data of this EppExtAnyType.


        :return: The contact_cre_data of this EppExtAnyType.
        :rtype: ContactCreDataType
        """
        return self._contact_cre_data

    @contact_cre_data.setter
    def contact_cre_data(self, contact_cre_data: ContactCreDataType):
        """Sets the contact_cre_data of this EppExtAnyType.


        :param contact_cre_data: The contact_cre_data of this EppExtAnyType.
        :type contact_cre_data: ContactCreDataType
        """
        if contact_cre_data is None:
            raise ValueError("Invalid value for `contact_cre_data`, must not be `None`")  # noqa: E501

        self._contact_cre_data = contact_cre_data

    @property
    def contact_inf_data(self) -> ContactInfDataType:
        """Gets the contact_inf_data of this EppExtAnyType.


        :return: The contact_inf_data of this EppExtAnyType.
        :rtype: ContactInfDataType
        """
        return self._contact_inf_data

    @contact_inf_data.setter
    def contact_inf_data(self, contact_inf_data: ContactInfDataType):
        """Sets the contact_inf_data of this EppExtAnyType.


        :param contact_inf_data: The contact_inf_data of this EppExtAnyType.
        :type contact_inf_data: ContactInfDataType
        """
        if contact_inf_data is None:
            raise ValueError("Invalid value for `contact_inf_data`, must not be `None`")  # noqa: E501

        self._contact_inf_data = contact_inf_data

    @property
    def contact_pan_data(self) -> ContactPanDataType:
        """Gets the contact_pan_data of this EppExtAnyType.


        :return: The contact_pan_data of this EppExtAnyType.
        :rtype: ContactPanDataType
        """
        return self._contact_pan_data

    @contact_pan_data.setter
    def contact_pan_data(self, contact_pan_data: ContactPanDataType):
        """Sets the contact_pan_data of this EppExtAnyType.


        :param contact_pan_data: The contact_pan_data of this EppExtAnyType.
        :type contact_pan_data: ContactPanDataType
        """
        if contact_pan_data is None:
            raise ValueError("Invalid value for `contact_pan_data`, must not be `None`")  # noqa: E501

        self._contact_pan_data = contact_pan_data

    @property
    def contact_trn_data(self) -> ContactTrnDataType:
        """Gets the contact_trn_data of this EppExtAnyType.


        :return: The contact_trn_data of this EppExtAnyType.
        :rtype: ContactTrnDataType
        """
        return self._contact_trn_data

    @contact_trn_data.setter
    def contact_trn_data(self, contact_trn_data: ContactTrnDataType):
        """Sets the contact_trn_data of this EppExtAnyType.


        :param contact_trn_data: The contact_trn_data of this EppExtAnyType.
        :type contact_trn_data: ContactTrnDataType
        """
        if contact_trn_data is None:
            raise ValueError("Invalid value for `contact_trn_data`, must not be `None`")  # noqa: E501

        self._contact_trn_data = contact_trn_data

    @property
    def sec_dns_inf_data(self) -> SecDNSDsOrKeyType:
        """Gets the sec_dns_inf_data of this EppExtAnyType.


        :return: The sec_dns_inf_data of this EppExtAnyType.
        :rtype: SecDNSDsOrKeyType
        """
        return self._sec_dns_inf_data

    @sec_dns_inf_data.setter
    def sec_dns_inf_data(self, sec_dns_inf_data: SecDNSDsOrKeyType):
        """Sets the sec_dns_inf_data of this EppExtAnyType.


        :param sec_dns_inf_data: The sec_dns_inf_data of this EppExtAnyType.
        :type sec_dns_inf_data: SecDNSDsOrKeyType
        """
        if sec_dns_inf_data is None:
            raise ValueError("Invalid value for `sec_dns_inf_data`, must not be `None`")  # noqa: E501

        self._sec_dns_inf_data = sec_dns_inf_data
