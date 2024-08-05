from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class EppTransferOpType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    APPROVE = 'approve'
    CANCEL = 'cancel'
    QUERY = 'query'
    REJECT = 'reject'
    REQUEST = 'request'
    def __init__(self):  # noqa: E501
        """EppTransferOpType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'EppTransferOpType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_transferOpType of this EppTransferOpType.  # noqa: E501
        :rtype: EppTransferOpType
        """
        return util.deserialize_model(dikt, cls)