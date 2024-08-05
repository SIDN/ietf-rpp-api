import unittest

from flask import json

from rpp_py_flask_server.test import BaseTestCase


class TestHostsController(BaseTestCase):
    """HostsController integration test stubs"""

    def test_hosts_id_delete(self):
        """Test case for hosts_id_delete

        Host delete
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
            '/rpp/v1/hosts/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            data=json.dumps(body),
            content_type='application/rpp+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hosts_id_get(self):
        """Test case for hosts_id_get

        Host info
        """
        body = 'body_example'
        query_string = [('filter', 'filter_example'),
                        ('val', 'val_example')]
        headers = { 
            'Accept': 'application/rpp+json',
            'Content-Type': 'application/rpp+json',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/rpp/v1/hosts/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            data=json.dumps(body),
            content_type='application/rpp+json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hosts_id_head(self):
        """Test case for hosts_id_head

        Host check
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
            '/rpp/v1/hosts/{id}'.format(id='id_example'),
            method='HEAD',
            headers=headers,
            data=json.dumps(body),
            content_type='application/rpp+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hosts_id_patch(self):
        """Test case for hosts_id_patch

        Host update
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
            '/rpp/v1/hosts/{id}'.format(id='id_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(body),
            content_type='application/rpp+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hosts_post(self):
        """Test case for hosts_post

        Host create
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
            '/rpp/v1/hosts',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/rpp+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
