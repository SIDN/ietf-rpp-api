from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rpp_py_flask_server.models.base_model import Model
from rpp_py_flask_server.models.epp_creds_options_type import EppCredsOptionsType
from rpp_py_flask_server.models.epp_login_svc_type import EppLoginSvcType
from rpp_py_flask_server import util

from rpp_py_flask_server.models.epp_creds_options_type import EppCredsOptionsType  # noqa: E501
from rpp_py_flask_server.models.epp_login_svc_type import EppLoginSvcType  # noqa: E501

class EppLoginType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cl_id=None, new_pw=None, options=None, pw=None, svcs=None):  # noqa: E501
        """EppLoginType - a model defined in OpenAPI

        :param cl_id: The cl_id of this EppLoginType.  # noqa: E501
        :type cl_id: str
        :param new_pw: The new_pw of this EppLoginType.  # noqa: E501
        :type new_pw: str
        :param options: The options of this EppLoginType.  # noqa: E501
        :type options: EppCredsOptionsType
        :param pw: The pw of this EppLoginType.  # noqa: E501
        :type pw: str
        :param svcs: The svcs of this EppLoginType.  # noqa: E501
        :type svcs: EppLoginSvcType
        """
        self.openapi_types = {
            'cl_id': str,
            'new_pw': str,
            'options': EppCredsOptionsType,
            'pw': str,
            'svcs': EppLoginSvcType
        }

        self.attribute_map = {
            'cl_id': 'clID',
            'new_pw': 'newPW',
            'options': 'options',
            'pw': 'pw',
            'svcs': 'svcs'
        }

        self._cl_id = cl_id
        self._new_pw = new_pw
        self._options = options
        self._pw = pw
        self._svcs = svcs

    @classmethod
    def from_dict(cls, dikt) -> 'EppLoginType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_loginType of this EppLoginType.  # noqa: E501
        :rtype: EppLoginType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cl_id(self) -> str:
        """Gets the cl_id of this EppLoginType.


        :return: The cl_id of this EppLoginType.
        :rtype: str
        """
        return self._cl_id

    @cl_id.setter
    def cl_id(self, cl_id: str):
        """Sets the cl_id of this EppLoginType.


        :param cl_id: The cl_id of this EppLoginType.
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
    def new_pw(self) -> str:
        """Gets the new_pw of this EppLoginType.


        :return: The new_pw of this EppLoginType.
        :rtype: str
        """
        return self._new_pw

    @new_pw.setter
    def new_pw(self, new_pw: str):
        """Sets the new_pw of this EppLoginType.


        :param new_pw: The new_pw of this EppLoginType.
        :type new_pw: str
        """
        if new_pw is not None and len(new_pw) > 16:
            raise ValueError("Invalid value for `new_pw`, length must be less than or equal to `16`")  # noqa: E501
        if new_pw is not None and len(new_pw) < 6:
            raise ValueError("Invalid value for `new_pw`, length must be greater than or equal to `6`")  # noqa: E501

        self._new_pw = new_pw

    @property
    def options(self) -> EppCredsOptionsType:
        """Gets the options of this EppLoginType.


        :return: The options of this EppLoginType.
        :rtype: EppCredsOptionsType
        """
        return self._options

    @options.setter
    def options(self, options: EppCredsOptionsType):
        """Sets the options of this EppLoginType.


        :param options: The options of this EppLoginType.
        :type options: EppCredsOptionsType
        """
        if options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def pw(self) -> str:
        """Gets the pw of this EppLoginType.


        :return: The pw of this EppLoginType.
        :rtype: str
        """
        return self._pw

    @pw.setter
    def pw(self, pw: str):
        """Sets the pw of this EppLoginType.


        :param pw: The pw of this EppLoginType.
        :type pw: str
        """
        if pw is None:
            raise ValueError("Invalid value for `pw`, must not be `None`")  # noqa: E501
        if pw is not None and len(pw) > 16:
            raise ValueError("Invalid value for `pw`, length must be less than or equal to `16`")  # noqa: E501
        if pw is not None and len(pw) < 6:
            raise ValueError("Invalid value for `pw`, length must be greater than or equal to `6`")  # noqa: E501

        self._pw = pw

    @property
    def svcs(self) -> EppLoginSvcType:
        """Gets the svcs of this EppLoginType.


        :return: The svcs of this EppLoginType.
        :rtype: EppLoginSvcType
        """
        return self._svcs

    @svcs.setter
    def svcs(self, svcs: EppLoginSvcType):
        """Sets the svcs of this EppLoginType.


        :param svcs: The svcs of this EppLoginType.
        :type svcs: EppLoginSvcType
        """
        if svcs is None:
            raise ValueError("Invalid value for `svcs`, must not be `None`")  # noqa: E501

        self._svcs = svcs
