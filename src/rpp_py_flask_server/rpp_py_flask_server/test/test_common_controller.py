import unittest

from flask import json

from rpp_py_flask_server.test import BaseTestCase


class TestCommonController(BaseTestCase):
    """CommonController integration test stubs"""

    def test_messages_get(self):
        """Test case for messages_get

        Poll request
        """
        body = 'body_example'
        headers = { 
            'Accept': 'application/rpp+json',
            'Content-Type': 'application/rpp+json',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/rpp/v1/messages',
            method='GET',
            headers=headers,
            data=json.dumps(body),
            content_type='application/rpp+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_messages_id_head(self):
        """Test case for messages_id_head

        Poll ack
        """
        body = 'body_example'
        headers = { 
            'Content-Type': 'application/rpp+json',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/rpp/v1/messages/{id}'.format(id='id_example'),
            method='HEAD',
            headers=headers,
            data=json.dumps(body),
            content_type='application/rpp+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_get(self):
        """Test case for root_get

        Hello
        """
        headers = { 
            'Accept': 'application/rpp+json',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/rpp/v1/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
