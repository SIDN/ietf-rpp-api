from datetime import datetime
from rpp_py_flask_server.models.epp_response_type import EppResponseType, EppMsgQType, EppResultType, EppTrIDType
from rpp_py_flask_server.models.domain_cre_data_type import DomainCreDataType 

def domains_post(repp_cltrid, repp_svcs, accept_language, epp_read_write_type, repp_svcs_ext):

    print(epp_read_write_type.domain_create)
    print(f'Create domain {epp_read_write_type.domain_create.name}')

    r = EppResponseType()
    r.msg_q = EppMsgQType(1, 'ABC123')
    r.result = [EppResultType(code=1000, msg='Command completed successfully')]
    r.tr_id = EppTrIDType(repp_cltrid, 'SV-ID-12345')
    r.res_data = DomainCreDataType(name=epp_read_write_type.domain_create.name,  cr_date=datetime.now(),
                                   ex_date=datetime.now())


    return r

def domains_id_delete(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body):
    return 'TODO'

  
def domains_id_get(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, filter, val, body):
    return 'TODO'
