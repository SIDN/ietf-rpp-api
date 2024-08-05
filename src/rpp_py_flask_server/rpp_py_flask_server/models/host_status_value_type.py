from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class HostStatusValueType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CLIENTDELETEPROHIBITED = 'clientDeleteProhibited'
    CLIENTUPDATEPROHIBITED = 'clientUpdateProhibited'
    LINKED = 'linked'
    OK = 'ok'
    PENDINGCREATE = 'pendingCreate'
    PENDINGDELETE = 'pendingDelete'
    PENDINGTRANSFER = 'pendingTransfer'
    PENDINGUPDATE = 'pendingUpdate'
    SERVERDELETEPROHIBITED = 'serverDeleteProhibited'
    SERVERUPDATEPROHIBITED = 'serverUpdateProhibited'
    def __init__(self):  # noqa: E501
        """HostStatusValueType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'HostStatusValueType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The host_statusValueType of this HostStatusValueType.  # noqa: E501
        :rtype: HostStatusValueType
        """
        return util.deserialize_model(dikt, cls)
