from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.contact_check_id_type import ContactCheckIDType
from rpp_py_flask_server.models.eppcom_reason_type import EppcomReasonType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.contact_check_id_type import ContactCheckIDType  # noqa: E501
from rpp_py_flask_server.models.eppcom_reason_type import EppcomReasonType  # noqa: E501

class ContactCheckType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, reason=None):  # noqa: E501
        """ContactCheckType - a model defined in OpenAPI

        :param id: The id of this ContactCheckType.  # noqa: E501
        :type id: ContactCheckIDType
        :param reason: The reason of this ContactCheckType.  # noqa: E501
        :type reason: EppcomReasonType
        """
        self.openapi_types = {
            'id': ContactCheckIDType,
            'reason': EppcomReasonType
        }

        self.attribute_map = {
            'id': 'id',
            'reason': 'reason'
        }

        self._id = id
        self._reason = reason

    @classmethod
    def from_dict(cls, dikt) -> 'ContactCheckType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The contact_checkType of this ContactCheckType.  # noqa: E501
        :rtype: ContactCheckType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> ContactCheckIDType:
        """Gets the id of this ContactCheckType.


        :return: The id of this ContactCheckType.
        :rtype: ContactCheckIDType
        """
        return self._id

    @id.setter
    def id(self, id: ContactCheckIDType):
        """Sets the id of this ContactCheckType.


        :param id: The id of this ContactCheckType.
        :type id: ContactCheckIDType
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def reason(self) -> EppcomReasonType:
        """Gets the reason of this ContactCheckType.


        :return: The reason of this ContactCheckType.
        :rtype: EppcomReasonType
        """
        return self._reason

    @reason.setter
    def reason(self, reason: EppcomReasonType):
        """Sets the reason of this ContactCheckType.


        :param reason: The reason of this ContactCheckType.
        :type reason: EppcomReasonType
        """

        self._reason = reason
