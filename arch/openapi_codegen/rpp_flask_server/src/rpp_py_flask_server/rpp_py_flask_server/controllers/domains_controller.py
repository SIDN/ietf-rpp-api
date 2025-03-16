import connexion
from typing import Dict
from typing import Tuple
from typing import Union
from flask import request

from rpp_py_flask_server.models.epp_read_write_type import EppReadWriteType  # noqa: E501
from rpp_py_flask_server import util



from rpp_py_flask_server.controllers_impl import domains_impl

def domains_id_delete(id, ):  # noqa: E501
    """Domain delete

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
        return domains_impl.domains_id_delete(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_delete in domains_impl: {e}")


def domains_id_get(id, filter=None, val=None, ):  # noqa: E501
    """Domain info

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
    :param filter: Name of attibute to filter on
    :type filter: str
    :param val: Value to use for filter
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
        return domains_impl.domains_id_get(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, rpp_auth_info, rpp_roid, filter, val, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_get in domains_impl: {e}")


def domains_id_head(id, ):  # noqa: E501
    """Domain check

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
        return domains_impl.domains_id_head(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_head in domains_impl: {e}")


def domains_id_patch(id, ):  # noqa: E501
    """Domain update

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
        return domains_impl.domains_id_patch(id, rpp_cltrid, rpp_svcs, accept_language, body, rpp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_patch in domains_impl: {e}")


def domains_id_renewals_post(id, unit=None, value=None, current_date=None, ):  # noqa: E501
    """Domain renew

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
    :param unit: Unit used for renewal value (e.g. y for year)
    :type unit: str
    :param value: Value for renewal
    :type value: int
    :param current_date: Date on which the current validity period ends
    :type current_date: str
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
        return domains_impl.domains_id_renewals_post(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, unit, value, current_date, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_renewals_post in domains_impl: {e}")


def domains_id_transfers_latest_delete(id, ):  # noqa: E501
    """Domain transfer cancel

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
        return domains_impl.domains_id_transfers_latest_delete(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_transfers_latest_delete in domains_impl: {e}")


def domains_id_transfers_latest_get(id, ):  # noqa: E501
    """Domain transfer query

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
        return domains_impl.domains_id_transfers_latest_get(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, rpp_auth_info, rpp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_transfers_latest_get in domains_impl: {e}")


def domains_id_transfers_latest_put(id, ):  # noqa: E501
    """Domain transfer approve

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
        return domains_impl.domains_id_transfers_latest_put(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_transfers_latest_put in domains_impl: {e}")


def domains_id_transfers_post(id, unit=None, value=None, ):  # noqa: E501
    """Domain transfer request

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
    :param unit: Unit used for renewal value (e.g. y for year)
    :type unit: str
    :param value: Value for renewal
    :type value: int
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
        return domains_impl.domains_id_transfers_post(id, rpp_cltrid, rpp_svcs, accept_language, rpp_svcs_ext, rpp_auth_info, rpp_roid, unit, value, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_transfers_post in domains_impl: {e}")


def domains_post():  # noqa: E501
    """Domain create

     # noqa: E501

    :param rpp_cltrid: Client transaction identifier
    :type rpp_cltrid: str
    :param rpp_svcs: Namespace used
    :type rpp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param epp_read_write_type: 
    :type epp_read_write_type: dict | bytes
    :param rpp_svcs_ext: Extension namespace used
    :type rpp_svcs_ext: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    rpp_cltrid = request.headers.get('rpp_cltrid')
    rpp_svcs = request.headers.get('rpp_svcs')
    accept_language = request.headers.get('accept_language')
    rpp_svcs_ext = request.headers.get('rpp_svcs_ext')




    if connexion.request.is_json:
        epp_read_write_type = EppReadWriteType.from_dict(connexion.request.get_json())  # noqa: E501




    try:
        return domains_impl.domains_post(rpp_cltrid, rpp_svcs, accept_language, epp_read_write_type, rpp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_post in domains_impl: {e}")

