from rpp_py_flask_server.models.epp_greeting_type import EppGreetingType, EppSvcMenuType, EppDcpType
from rpp_py_flask_server.models.epp_dcp_access_type import EppDcpAccessType
from rpp_py_flask_server.models.epp_dcp_expiry_type import EppDcpExpiryType
from rpp_py_flask_server.models.epp_dcp_statement_type import EppDcpStatementType
from rpp_py_flask_server.models.epp_dcp_purpose_type import EppDcpPurposeType
from rpp_py_flask_server.models.epp_dcp_recipient_type import EppDcpRecipientType
from rpp_py_flask_server.models.epp_dcp_retention_type import EppDcpRetentionType
from datetime import datetime

def root_get(accept_language):
    menu = EppSvcMenuType(lang=accept_language, version='1.0')
    stmt = EppDcpStatementType(purpose=EppDcpPurposeType(admin=True), recipient=EppDcpRecipientType(ours=True), retention=EppDcpRetentionType(stated=True))
    dcp = EppDcpType(access='all', statement=stmt)
    greeting = EppGreetingType(sv_id='rpp.ietf.org', sv_date=datetime.now(), svc_menu=menu, dcp=dcp)
    return greeting