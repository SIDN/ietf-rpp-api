from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server import util


class EppTrIDType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cl_trid=None, sv_trid=None):  # noqa: E501
        """EppTrIDType - a model defined in OpenAPI

        :param cl_trid: The cl_trid of this EppTrIDType.  # noqa: E501
        :type cl_trid: str
        :param sv_trid: The sv_trid of this EppTrIDType.  # noqa: E501
        :type sv_trid: str
        """
        self.openapi_types = {
            'cl_trid': str,
            'sv_trid': str
        }

        self.attribute_map = {
            'cl_trid': 'clTRID',
            'sv_trid': 'svTRID'
        }

        self._cl_trid = cl_trid
        self._sv_trid = sv_trid

    @classmethod
    def from_dict(cls, dikt) -> 'EppTrIDType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_trIDType of this EppTrIDType.  # noqa: E501
        :rtype: EppTrIDType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cl_trid(self) -> str:
        """Gets the cl_trid of this EppTrIDType.


        :return: The cl_trid of this EppTrIDType.
        :rtype: str
        """
        return self._cl_trid

    @cl_trid.setter
    def cl_trid(self, cl_trid: str):
        """Sets the cl_trid of this EppTrIDType.


        :param cl_trid: The cl_trid of this EppTrIDType.
        :type cl_trid: str
        """
        if cl_trid is not None and len(cl_trid) > 64:
            raise ValueError("Invalid value for `cl_trid`, length must be less than or equal to `64`")  # noqa: E501
        if cl_trid is not None and len(cl_trid) < 3:
            raise ValueError("Invalid value for `cl_trid`, length must be greater than or equal to `3`")  # noqa: E501

        self._cl_trid = cl_trid

    @property
    def sv_trid(self) -> str:
        """Gets the sv_trid of this EppTrIDType.


        :return: The sv_trid of this EppTrIDType.
        :rtype: str
        """
        return self._sv_trid

    @sv_trid.setter
    def sv_trid(self, sv_trid: str):
        """Sets the sv_trid of this EppTrIDType.


        :param sv_trid: The sv_trid of this EppTrIDType.
        :type sv_trid: str
        """
        if sv_trid is None:
            raise ValueError("Invalid value for `sv_trid`, must not be `None`")  # noqa: E501
        if sv_trid is not None and len(sv_trid) > 64:
            raise ValueError("Invalid value for `sv_trid`, length must be less than or equal to `64`")  # noqa: E501
        if sv_trid is not None and len(sv_trid) < 3:
            raise ValueError("Invalid value for `sv_trid`, length must be greater than or equal to `3`")  # noqa: E501

        self._sv_trid = sv_trid
