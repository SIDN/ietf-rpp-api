
def domains_post(repp_cltrid, repp_svcs, accept_language, epp_read_write_type, repp_svcs_ext):
    print('test123')
    print(type(epp_read_write_type))
    print(epp_read_write_type.domain_create)
    print(f'Create domain {epp_read_write_type.domain_create.name}')

    return f'created domain: {epp_read_write_type.domain_create.name}'

def domains_id_delete(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body):
    return 'hello'

  
def domains_id_get(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, filter, val, body):
    return id
