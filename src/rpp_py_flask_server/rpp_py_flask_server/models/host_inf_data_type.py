from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.host_addr_type import HostAddrType
from rpp_py_flask_server.models.host_status_type import HostStatusType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.host_addr_type import HostAddrType  # noqa: E501
from rpp_py_flask_server.models.host_status_type import HostStatusType  # noqa: E501

class HostInfDataType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, addr=None, cl_id=None, cr_date=None, cr_id=None, name=None, roid=None, status=None, tr_date=None, up_date=None, up_id=None):  # noqa: E501
        """HostInfDataType - a model defined in OpenAPI

        :param addr: The addr of this HostInfDataType.  # noqa: E501
        :type addr: List[HostAddrType]
        :param cl_id: The cl_id of this HostInfDataType.  # noqa: E501
        :type cl_id: str
        :param cr_date: The cr_date of this HostInfDataType.  # noqa: E501
        :type cr_date: datetime
        :param cr_id: The cr_id of this HostInfDataType.  # noqa: E501
        :type cr_id: str
        :param name: The name of this HostInfDataType.  # noqa: E501
        :type name: str
        :param roid: The roid of this HostInfDataType.  # noqa: E501
        :type roid: str
        :param status: The status of this HostInfDataType.  # noqa: E501
        :type status: List[HostStatusType]
        :param tr_date: The tr_date of this HostInfDataType.  # noqa: E501
        :type tr_date: datetime
        :param up_date: The up_date of this HostInfDataType.  # noqa: E501
        :type up_date: datetime
        :param up_id: The up_id of this HostInfDataType.  # noqa: E501
        :type up_id: str
        """
        self.openapi_types = {
            'addr': List[HostAddrType],
            'cl_id': str,
            'cr_date': datetime,
            'cr_id': str,
            'name': str,
            'roid': str,
            'status': List[HostStatusType],
            'tr_date': datetime,
            'up_date': datetime,
            'up_id': str
        }

        self.attribute_map = {
            'addr': 'addr',
            'cl_id': 'clID',
            'cr_date': 'crDate',
            'cr_id': 'crID',
            'name': 'name',
            'roid': 'roid',
            'status': 'status',
            'tr_date': 'trDate',
            'up_date': 'upDate',
            'up_id': 'upID'
        }

        self._addr = addr
        self._cl_id = cl_id
        self._cr_date = cr_date
        self._cr_id = cr_id
        self._name = name
        self._roid = roid
        self._status = status
        self._tr_date = tr_date
        self._up_date = up_date
        self._up_id = up_id

    @classmethod
    def from_dict(cls, dikt) -> 'HostInfDataType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The host_infDataType of this HostInfDataType.  # noqa: E501
        :rtype: HostInfDataType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def addr(self) -> List[HostAddrType]:
        """Gets the addr of this HostInfDataType.


        :return: The addr of this HostInfDataType.
        :rtype: List[HostAddrType]
        """
        return self._addr

    @addr.setter
    def addr(self, addr: List[HostAddrType]):
        """Sets the addr of this HostInfDataType.


        :param addr: The addr of this HostInfDataType.
        :type addr: List[HostAddrType]
        """
        if addr is not None and len(addr) < 0:
            raise ValueError("Invalid value for `addr`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._addr = addr

    @property
    def cl_id(self) -> str:
        """Gets the cl_id of this HostInfDataType.


        :return: The cl_id of this HostInfDataType.
        :rtype: str
        """
        return self._cl_id

    @cl_id.setter
    def cl_id(self, cl_id: str):
        """Sets the cl_id of this HostInfDataType.


        :param cl_id: The cl_id of this HostInfDataType.
        :type cl_id: str
        """
        if cl_id is None:
            raise ValueError("Invalid value for `cl_id`, must not be `None`")  # noqa: E501
        if cl_id is not None and len(cl_id) > 16:
            raise ValueError("Invalid value for `cl_id`, length must be less than or equal to `16`")  # noqa: E501
        if cl_id is not None and len(cl_id) < 3:
            raise ValueError("Invalid value for `cl_id`, length must be greater than or equal to `3`")  # noqa: E501

        self._cl_id = cl_id

    @property
    def cr_date(self) -> datetime:
        """Gets the cr_date of this HostInfDataType.


        :return: The cr_date of this HostInfDataType.
        :rtype: datetime
        """
        return self._cr_date

    @cr_date.setter
    def cr_date(self, cr_date: datetime):
        """Sets the cr_date of this HostInfDataType.


        :param cr_date: The cr_date of this HostInfDataType.
        :type cr_date: datetime
        """
        if cr_date is None:
            raise ValueError("Invalid value for `cr_date`, must not be `None`")  # noqa: E501

        self._cr_date = cr_date

    @property
    def cr_id(self) -> str:
        """Gets the cr_id of this HostInfDataType.


        :return: The cr_id of this HostInfDataType.
        :rtype: str
        """
        return self._cr_id

    @cr_id.setter
    def cr_id(self, cr_id: str):
        """Sets the cr_id of this HostInfDataType.


        :param cr_id: The cr_id of this HostInfDataType.
        :type cr_id: str
        """
        if cr_id is None:
            raise ValueError("Invalid value for `cr_id`, must not be `None`")  # noqa: E501
        if cr_id is not None and len(cr_id) > 16:
            raise ValueError("Invalid value for `cr_id`, length must be less than or equal to `16`")  # noqa: E501
        if cr_id is not None and len(cr_id) < 3:
            raise ValueError("Invalid value for `cr_id`, length must be greater than or equal to `3`")  # noqa: E501

        self._cr_id = cr_id

    @property
    def name(self) -> str:
        """Gets the name of this HostInfDataType.


        :return: The name of this HostInfDataType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this HostInfDataType.


        :param name: The name of this HostInfDataType.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def roid(self) -> str:
        """Gets the roid of this HostInfDataType.


        :return: The roid of this HostInfDataType.
        :rtype: str
        """
        return self._roid

    @roid.setter
    def roid(self, roid: str):
        """Sets the roid of this HostInfDataType.


        :param roid: The roid of this HostInfDataType.
        :type roid: str
        """
        if roid is None:
            raise ValueError("Invalid value for `roid`, must not be `None`")  # noqa: E501

        self._roid = roid

    @property
    def status(self) -> List[HostStatusType]:
        """Gets the status of this HostInfDataType.


        :return: The status of this HostInfDataType.
        :rtype: List[HostStatusType]
        """
        return self._status

    @status.setter
    def status(self, status: List[HostStatusType]):
        """Sets the status of this HostInfDataType.


        :param status: The status of this HostInfDataType.
        :type status: List[HostStatusType]
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if status is not None and len(status) > 7:
            raise ValueError("Invalid value for `status`, number of items must be less than or equal to `7`")  # noqa: E501
        if status is not None and len(status) < 1:
            raise ValueError("Invalid value for `status`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def tr_date(self) -> datetime:
        """Gets the tr_date of this HostInfDataType.


        :return: The tr_date of this HostInfDataType.
        :rtype: datetime
        """
        return self._tr_date

    @tr_date.setter
    def tr_date(self, tr_date: datetime):
        """Sets the tr_date of this HostInfDataType.


        :param tr_date: The tr_date of this HostInfDataType.
        :type tr_date: datetime
        """

        self._tr_date = tr_date

    @property
    def up_date(self) -> datetime:
        """Gets the up_date of this HostInfDataType.


        :return: The up_date of this HostInfDataType.
        :rtype: datetime
        """
        return self._up_date

    @up_date.setter
    def up_date(self, up_date: datetime):
        """Sets the up_date of this HostInfDataType.


        :param up_date: The up_date of this HostInfDataType.
        :type up_date: datetime
        """

        self._up_date = up_date

    @property
    def up_id(self) -> str:
        """Gets the up_id of this HostInfDataType.


        :return: The up_id of this HostInfDataType.
        :rtype: str
        """
        return self._up_id

    @up_id.setter
    def up_id(self, up_id: str):
        """Sets the up_id of this HostInfDataType.


        :param up_id: The up_id of this HostInfDataType.
        :type up_id: str
        """
        if up_id is not None and len(up_id) > 16:
            raise ValueError("Invalid value for `up_id`, length must be less than or equal to `16`")  # noqa: E501
        if up_id is not None and len(up_id) < 3:
            raise ValueError("Invalid value for `up_id`, length must be greater than or equal to `3`")  # noqa: E501

        self._up_id = up_id
