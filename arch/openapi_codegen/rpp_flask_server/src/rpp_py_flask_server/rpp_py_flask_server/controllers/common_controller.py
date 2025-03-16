import connexion
from typing import Dict
from typing import Tuple
from typing import Union
from flask import request

from rpp_py_flask_server import util



from rpp_py_flask_server.controllers_impl import common_impl

def messages_get():  # noqa: E501
    """Poll request

     # noqa: E501

    :param rpp_cltrid: Client transaction identifier
    :type rpp_cltrid: str
    :param rpp_svcs: Namespace used
    :type rpp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param rpp_svcs_ext: Extension namespace used
    :type rpp_svcs_ext: str
    :param body: Default request body
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    rpp_cltrid = request.headers.get('rpp_cltrid')
    rpp_svcs = request.headers.get('rpp_svcs')
    accept_language = request.headers.get('accept_language')
    rpp_svcs_ext = request.headers.get('rpp_svcs_ext')





    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return common_impl.messages_get(rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module common_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function messages_get in common_impl: {e}")


def messages_id_head(id, ):  # noqa: E501
    """Poll ack

     # noqa: E501

    :param id: Object identifier
    :type id: str
    :param rpp_cltrid: Client transaction identifier
    :type rpp_cltrid: str
    :param rpp_svcs: Namespace used
    :type rpp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param rpp_svcs_ext: Extension namespace used
    :type rpp_svcs_ext: str
    :param body: Default request body
    :type body: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    rpp_cltrid = request.headers.get('rpp_cltrid')
    rpp_svcs = request.headers.get('rpp_svcs')
    accept_language = request.headers.get('accept_language')
    rpp_svcs_ext = request.headers.get('rpp_svcs_ext')






    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return common_impl.messages_id_head(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module common_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function messages_id_head in common_impl: {e}")


def root_get():  # noqa: E501
    """Hello

     # noqa: E501

    :param accept_language: Language used for response
    :type accept_language: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    accept_language = request.headers.get('accept_language')




    try:
        return common_impl.root_get(accept_language)
    except NameError as e:
        raise NotImplementedError(f"Missing module common_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function root_get in common_impl: {e}")

