from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class ContactMIDType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None):  # noqa: E501
        """ContactMIDType - a model defined in OpenAPI

        :param id: The id of this ContactMIDType.  # noqa: E501
        :type id: List[str]
        """
        self.openapi_types = {
            'id': List[str]
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'ContactMIDType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The contact_mIDType of this ContactMIDType.  # noqa: E501
        :rtype: ContactMIDType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> List[str]:
        """Gets the id of this ContactMIDType.


        :return: The id of this ContactMIDType.
        :rtype: List[str]
        """
        return self._id

    @id.setter
    def id(self, id: List[str]):
        """Sets the id of this ContactMIDType.


        :param id: The id of this ContactMIDType.
        :type id: List[str]
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._id = id
