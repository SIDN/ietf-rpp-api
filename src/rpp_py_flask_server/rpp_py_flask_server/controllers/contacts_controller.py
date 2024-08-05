import connexion
from typing import Dict
from typing import Tuple
from typing import Union
from flask import request

from rpp_py_flask_server import util



from rpp_py_flask_server.controllers_impl import contacts_impl

def contacts_id_delete(id, ):  # noqa: E501
    """Contact delete

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
        return contacts_impl.contacts_id_delete(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_delete in contacts_impl: {e}")


def contacts_id_get(id, filter=None, val=None, ):  # noqa: E501
    """Contact info

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
    :param rpp_auth_info: Object authorization details
    :type rpp_auth_info: str
    :param rpp_roid: Object linked to authorization
    :type rpp_roid: str
    :param filter: 
    :type filter: str
    :param val: 
    :type val: str
    :param body: Default request body
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    rpp_cltrid = request.headers.get('rpp_cltrid')
    rpp_svcs = request.headers.get('rpp_svcs')
    accept_language = request.headers.get('accept_language')
    rpp_svcs_ext = request.headers.get('rpp_svcs_ext')
    rpp_auth_info = request.headers.get('rpp_auth_info')
    rpp_roid = request.headers.get('rpp_roid')










    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_get(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, rpp_auth_info, rpp_roid, filter, val, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_get in contacts_impl: {e}")


def contacts_id_head(id, ):  # noqa: E501
    """Contact check

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
        return contacts_impl.contacts_id_head(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_head in contacts_impl: {e}")


def contacts_id_patch(id, ):  # noqa: E501
    """Contact update

     # noqa: E501

    :param id: Object identifier
    :type id: str
    :param rpp_cltrid: Client transaction identifier
    :type rpp_cltrid: str
    :param rpp_svcs: Namespace used
    :type rpp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param body: Default request body
    :type body: str
    :param rpp_svcs_ext: Extension namespace used
    :type rpp_svcs_ext: str

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
        return contacts_impl.contacts_id_patch(id, rpp_cltrid, rpp_svcs, accept_language, body, rpp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_patch in contacts_impl: {e}")


def contacts_id_transfers_latest_delete(id, ):  # noqa: E501
    """Contact transfer cancel

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
    :param rpp_auth_info: Object authorization details
    :type rpp_auth_info: str
    :param rpp_roid: Object linked to authorization
    :type rpp_roid: str
    :param body: Default request body
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    rpp_cltrid = request.headers.get('rpp_cltrid')
    rpp_svcs = request.headers.get('rpp_svcs')
    accept_language = request.headers.get('accept_language')
    rpp_svcs_ext = request.headers.get('rpp_svcs_ext')
    rpp_auth_info = request.headers.get('rpp_auth_info')
    rpp_roid = request.headers.get('rpp_roid')








    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_transfers_latest_delete(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, rpp_auth_info, rpp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_transfers_latest_delete in contacts_impl: {e}")


def contacts_id_transfers_latest_get(id, ):  # noqa: E501
    """Contact transfer query

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
    :param rpp_auth_info: Object authorization details
    :type rpp_auth_info: str
    :param rpp_roid: Object linked to authorization
    :type rpp_roid: str
    :param body: Default request body
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    rpp_cltrid = request.headers.get('rpp_cltrid')
    rpp_svcs = request.headers.get('rpp_svcs')
    accept_language = request.headers.get('accept_language')
    rpp_svcs_ext = request.headers.get('rpp_svcs_ext')
    rpp_auth_info = request.headers.get('rpp_auth_info')
    rpp_roid = request.headers.get('rpp_roid')








    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_transfers_latest_get(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, rpp_auth_info, rpp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_transfers_latest_get in contacts_impl: {e}")


def contacts_id_transfers_latest_put(id, ):  # noqa: E501
    """Contact transfer approve

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
    :param rpp_auth_info: Object authorization details
    :type rpp_auth_info: str
    :param rpp_roid: Object linked to authorization
    :type rpp_roid: str
    :param body: Default request body
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    rpp_cltrid = request.headers.get('rpp_cltrid')
    rpp_svcs = request.headers.get('rpp_svcs')
    accept_language = request.headers.get('accept_language')
    rpp_svcs_ext = request.headers.get('rpp_svcs_ext')
    rpp_auth_info = request.headers.get('rpp_auth_info')
    rpp_roid = request.headers.get('rpp_roid')








    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_transfers_latest_put(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, rpp_auth_info, rpp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_transfers_latest_put in contacts_impl: {e}")


def contacts_id_transfers_post(id, ):  # noqa: E501
    """Contact transfer request

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
    :param rpp_auth_info: Object authorization details
    :type rpp_auth_info: str
    :param rpp_roid: Object linked to authorization
    :type rpp_roid: str
    :param body: Default request body
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    rpp_cltrid = request.headers.get('rpp_cltrid')
    rpp_svcs = request.headers.get('rpp_svcs')
    accept_language = request.headers.get('accept_language')
    rpp_svcs_ext = request.headers.get('rpp_svcs_ext')
    rpp_auth_info = request.headers.get('rpp_auth_info')
    rpp_roid = request.headers.get('rpp_roid')








    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_transfers_post(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, rpp_auth_info, rpp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_transfers_post in contacts_impl: {e}")


def contacts_post():  # noqa: E501
    """Contact create

     # noqa: E501

    :param rpp_cltrid: Client transaction identifier
    :type rpp_cltrid: str
    :param rpp_svcs: Namespace used
    :type rpp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param body: Default request body
    :type body: str
    :param rpp_svcs_ext: Extension namespace used
    :type rpp_svcs_ext: str

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
        return contacts_impl.contacts_post(rpp_cltrid, rpp_svcs, accept_language, body, rpp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_post in contacts_impl: {e}")

