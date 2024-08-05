from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.contact_pa_clid_type import ContactPaCLIDType
from rpp_py_flask_server.models.epp_tr_id_type import EppTrIDType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.contact_pa_clid_type import ContactPaCLIDType  # noqa: E501
from rpp_py_flask_server.models.epp_tr_id_type import EppTrIDType  # noqa: E501

class ContactPanDataType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, pa_date=None, pa_trid=None):  # noqa: E501
        """ContactPanDataType - a model defined in OpenAPI

        :param id: The id of this ContactPanDataType.  # noqa: E501
        :type id: ContactPaCLIDType
        :param pa_date: The pa_date of this ContactPanDataType.  # noqa: E501
        :type pa_date: datetime
        :param pa_trid: The pa_trid of this ContactPanDataType.  # noqa: E501
        :type pa_trid: EppTrIDType
        """
        self.openapi_types = {
            'id': ContactPaCLIDType,
            'pa_date': datetime,
            'pa_trid': EppTrIDType
        }

        self.attribute_map = {
            'id': 'id',
            'pa_date': 'paDate',
            'pa_trid': 'paTRID'
        }

        self._id = id
        self._pa_date = pa_date
        self._pa_trid = pa_trid

    @classmethod
    def from_dict(cls, dikt) -> 'ContactPanDataType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The contact_panDataType of this ContactPanDataType.  # noqa: E501
        :rtype: ContactPanDataType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> ContactPaCLIDType:
        """Gets the id of this ContactPanDataType.


        :return: The id of this ContactPanDataType.
        :rtype: ContactPaCLIDType
        """
        return self._id

    @id.setter
    def id(self, id: ContactPaCLIDType):
        """Sets the id of this ContactPanDataType.


        :param id: The id of this ContactPanDataType.
        :type id: ContactPaCLIDType
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def pa_date(self) -> datetime:
        """Gets the pa_date of this ContactPanDataType.


        :return: The pa_date of this ContactPanDataType.
        :rtype: datetime
        """
        return self._pa_date

    @pa_date.setter
    def pa_date(self, pa_date: datetime):
        """Sets the pa_date of this ContactPanDataType.


        :param pa_date: The pa_date of this ContactPanDataType.
        :type pa_date: datetime
        """
        if pa_date is None:
            raise ValueError("Invalid value for `pa_date`, must not be `None`")  # noqa: E501

        self._pa_date = pa_date

    @property
    def pa_trid(self) -> EppTrIDType:
        """Gets the pa_trid of this ContactPanDataType.


        :return: The pa_trid of this ContactPanDataType.
        :rtype: EppTrIDType
        """
        return self._pa_trid

    @pa_trid.setter
    def pa_trid(self, pa_trid: EppTrIDType):
        """Sets the pa_trid of this ContactPanDataType.


        :param pa_trid: The pa_trid of this ContactPanDataType.
        :type pa_trid: EppTrIDType
        """
        if pa_trid is None:
            raise ValueError("Invalid value for `pa_trid`, must not be `None`")  # noqa: E501

        self._pa_trid = pa_trid
