from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class HostCreDataType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cr_date=None, name=None):  # noqa: E501
        """HostCreDataType - a model defined in OpenAPI

        :param cr_date: The cr_date of this HostCreDataType.  # noqa: E501
        :type cr_date: datetime
        :param name: The name of this HostCreDataType.  # noqa: E501
        :type name: str
        """
        self.openapi_types = {
            'cr_date': datetime,
            'name': str
        }

        self.attribute_map = {
            'cr_date': 'crDate',
            'name': 'name'
        }

        self._cr_date = cr_date
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'HostCreDataType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The host_creDataType of this HostCreDataType.  # noqa: E501
        :rtype: HostCreDataType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cr_date(self) -> datetime:
        """Gets the cr_date of this HostCreDataType.


        :return: The cr_date of this HostCreDataType.
        :rtype: datetime
        """
        return self._cr_date

    @cr_date.setter
    def cr_date(self, cr_date: datetime):
        """Sets the cr_date of this HostCreDataType.


        :param cr_date: The cr_date of this HostCreDataType.
        :type cr_date: datetime
        """
        if cr_date is None:
            raise ValueError("Invalid value for `cr_date`, must not be `None`")  # noqa: E501

        self._cr_date = cr_date

    @property
    def name(self) -> str:
        """Gets the name of this HostCreDataType.


        :return: The name of this HostCreDataType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this HostCreDataType.


        :param name: The name of this HostCreDataType.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name
