# coding: utf-8

from __future__ import absolute_import

import uuid

from swagger_server.models.admin_note import AdminNote
from swagger_server.models.admin_note_create import AdminNoteCreate
from swagger_server.models.admin_note_update import AdminNoteUpdate
from swagger_server.models.site_data_schema import SiteDataSchema
from swagger_server.models.site_data_schema_update import SiteDataSchemaUpdate
from swagger_server.models.user_site_data import UserSiteData
from swagger_server.models.user_site_data_update import UserSiteDataUpdate
from . import BaseTestCase
from flask import json


class TestUserDataController(BaseTestCase):
    """ UserDataController integration test stubs """

    def test_adminnote_create(self):
        """
        Test case for adminnote_create

        """
        data = AdminNoteCreate(**{
            "creator_id": "%s" % uuid.uuid1(),
            "note": "This is text",
            "user_id": "%s" % uuid.uuid1(),
        })
        response = self.client.open(
            "/api/v1/adminnotes/",
            method="POST",
            data=json.dumps(data),
            content_type="application/json")

        response_data = json.loads(response.data)
        self.assertEqual(response_data["creator_id"], data.creator_id)
        self.assertEqual(response_data["note"], data.note)
        self.assertEqual(response_data["user_id"], data.user_id)



    def test_adminnote_delete(self):
        """
        Test case for adminnote_delete

        """
        response = self.client.open(
            '/api/v1/adminnotes/{user_id}/{creator_id}/{created_at}/'.format(
                user_id=self.user_id.hex,
                creator_id=self.creator_id.hex,
                created_at=self.created_at
            ), method='DELETE')

        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_adminnote_list(self):
        """
        Test case for adminnote_list


        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('user_id', 'user_id_example'),
                        ('creator_id', 'creator_id_example')]
        response = self.client.open('/api/v1/adminnotes/',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_adminnote_read(self):
        """
        Test case for adminnote_read


        """
        response = self.client.open('/api/v1/adminnotes/{user_id}/{creator_id}/{created_at}/'.format(user_id='user_id_example', creator_id='creator_id_example', created_at='2013-10-20T19:20:30+01:00'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_adminnote_update(self):
        """
        Test case for adminnote_update


        """
        data = AdminNoteUpdate()
        response = self.client.open('/api/v1/adminnotes/{user_id}/{creator_id}/{created_at}/'.format(user_id='user_id_example', creator_id='creator_id_example', created_at='2013-10-20T19:20:30+01:00'),
                                    method='PUT',
                                    data=json.dumps(data),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


    def test_sitedataschema_create(self):
        """
        Test case for sitedataschema_create


        """
        data = SiteDataSchema(**{
            "site_id": 1,
            "schema": object.__dict__
        })
        response = self.client.open(
            "/api/v1/sitedataschemas/",
            method="POST",
            data=json.dumps(data),
            content_type="application/json")

        response_data = json.loads(response.data)
        self.assertEqual(response_data["site_id"], data.site_id)
        self.assertEqual(response_data["schema"], data.schema)

    def test_sitedataschema_delete(self):
        """
        Test case for sitedataschema_delete


        """
        response = self.client.open('/api/v1/sitedataschemas/{site_id}/'.format(site_id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_sitedataschema_list(self):
        """
        Test case for sitedataschema_list


        """
        query_string = [('offset', 1),
                        ('limit', 100)]
        response = self.client.open('/api/v1/sitedataschemas/',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_sitedataschema_read(self):
        """
        Test case for sitedataschema_read


        """
        response = self.client.open('/api/v1/sitedataschemas/{site_id}/'.format(site_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_sitedataschema_update(self):
        """
        Test case for sitedataschema_update


        """
        data = SiteDataSchemaUpdate()
        response = self.client.open('/api/v1/sitedataschemas/{site_id}/'.format(site_id=56),
                                    method='PUT',
                                    data=json.dumps(data),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_usersitedata_create(self):
        """
        Test case for usersitedata_create


        """
        data = UserSiteData()
        response = self.client.open('/api/v1/usersitedata/',
                                    method='POST',
                                    data=json.dumps(data),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_usersitedata_delete(self):
        """
        Test case for usersitedata_delete


        """
        response = self.client.open('/api/v1/usersitedata/{user_id}/{site_id}/'.format(user_id='user_id_example', site_id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_usersitedata_list(self):
        """
        Test case for usersitedata_list


        """
        query_string = [('offset', 1),
                        ('limit', 100),
                        ('user_id', 'user_id_example'),
                        ('site_id', 56)]
        response = self.client.open('/api/v1/usersitedata/',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_usersitedata_read(self):
        """
        Test case for usersitedata_read


        """
        response = self.client.open('/api/v1/usersitedata/{user_id}/{site_id}/'.format(user_id='user_id_example', site_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_usersitedata_update(self):
        """
        Test case for usersitedata_update


        """
        data = UserSiteDataUpdate()
        response = self.client.open('/api/v1/usersitedata/{user_id}/{site_id}/'.format(user_id='user_id_example', site_id=56),
                                    method='PUT',
                                    data=json.dumps(data),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
