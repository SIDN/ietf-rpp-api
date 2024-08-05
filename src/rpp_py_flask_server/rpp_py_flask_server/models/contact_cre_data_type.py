from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class ContactCreDataType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cr_date=None, id=None):  # noqa: E501
        """ContactCreDataType - a model defined in OpenAPI

        :param cr_date: The cr_date of this ContactCreDataType.  # noqa: E501
        :type cr_date: datetime
        :param id: The id of this ContactCreDataType.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'cr_date': datetime,
            'id': str
        }

        self.attribute_map = {
            'cr_date': 'crDate',
            'id': 'id'
        }

        self._cr_date = cr_date
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'ContactCreDataType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The contact_creDataType of this ContactCreDataType.  # noqa: E501
        :rtype: ContactCreDataType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cr_date(self) -> datetime:
        """Gets the cr_date of this ContactCreDataType.


        :return: The cr_date of this ContactCreDataType.
        :rtype: datetime
        """
        return self._cr_date

    @cr_date.setter
    def cr_date(self, cr_date: datetime):
        """Sets the cr_date of this ContactCreDataType.


        :param cr_date: The cr_date of this ContactCreDataType.
        :type cr_date: datetime
        """
        if cr_date is None:
            raise ValueError("Invalid value for `cr_date`, must not be `None`")  # noqa: E501

        self._cr_date = cr_date

    @property
    def id(self) -> str:
        """Gets the id of this ContactCreDataType.


        :return: The id of this ContactCreDataType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ContactCreDataType.


        :param id: The id of this ContactCreDataType.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 16:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `16`")  # noqa: E501
        if id is not None and len(id) < 3:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `3`")  # noqa: E501

        self._id = id
