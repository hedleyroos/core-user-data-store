# coding: utf-8

from __future__ import absolute_import

import random
import uuid
import werkzeug

from swagger_server.models.admin_note import AdminNote
from swagger_server.models.admin_note_update import AdminNoteUpdate
from swagger_server.models.site_data_schema import SiteDataSchema
from swagger_server.models.site_data_schema_update import SiteDataSchemaUpdate
from swagger_server.models.user_site_data import UserSiteData
from swagger_server.models.user_site_data_update import UserSiteDataUpdate
from user_data_store import db_actions
from . import BaseTestCase
from flask import json


class TestUserDataController(BaseTestCase):
    """ UserDataController integration test stubs """

    def setUp(self):
        self.adminnote_data = {
            "creator_id": "%s" % uuid.uuid1(),
            "note": "This is text",
            "user_id": "%s" % uuid.uuid1(),
        }
        self.adminnote_model = db_actions.crud(
            model="AdminNote",
            api_model=AdminNote,
            data=self.adminnote_data,
            action="create"
        )

    def test_adminnote_create(self):
        """
        Test case for adminnote_create

        """
        data = AdminNote(**{
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
        data = {
            "creator_id": "%s" % uuid.uuid1(),
            "note": "This is text",
            "user_id": "%s" % uuid.uuid1(),
        }
        create_response = self.client.open(
            "/api/v1/adminnotes/",
            method="POST",
            data=json.dumps(data),
            content_type="application/json")

        create_response_data = json.loads(create_response.data)
        import pdb; pdb.set_trace()

        response = self.client.open(
            '/api/v1/adminnotes/{user_id}/{creator_id}/{created_at}/'.format(
                user_id=create_response_data["user_id"],
                creator_id=create_response_data["creator_id"],
                created_at=create_response_data["created_at"]
            ), method='DELETE')

        try:
            db_actions.crud(
                model="AdminNote",
                api_model=AdminNote,
                action="read",
                query={
                    "user_id": create_response_data["user_id"],
                    "creator_id": create_response_data["creator_id"],
                    "created_at": create_response_data["created_at"]
                }
            )
            raise Exception
        except werkzeug.exceptions.NotFound:
            pass

    def test_adminnote_list(self):
        """
        Test case for adminnote_list


        """
        objects = []
        for index in range(1, random.randint(2, 20)):
            data = {
                "user_id": "%s" % uuid.uuid1(),
                "creator_id": "%s" % uuid.uuid1(),
                "note": "List notes"
            }
            objects.append(db_actions.crud(
                model="AdminNote",
                api_model=AdminNote,
                data=data,
                action="create"
            ))
        query_string = [
            (
                'adminnote_user_ids',
                ",".join(map(str, [adminnote.user_id for adminnote in objects]))
            ),
            (
                'adminnote_creator_ids',
                ",".join(map(
                    str, [adminnote.creator_id for adminnote in objects]))
            ),
            (
                "adminnote_created_ats",
                ",".join(map(
                    str, [adminnote.created_at for adminnote in objects]))
            )
        ]
        response = self.client.open(
            '/api/v1/adminnotes/',
            method='GET',
            query_string=query_string)
        response_data = json.loads(response.data)

        self.assertEqual(len(response_data), len(objects))

    def test_adminnote_read(self):
        """
        Test case for adminnote_read

        """
        response = self.client.open(
            '/api/v1/adminnotes/{user_id}/{creator_id}/{created_at}/'.format(
                user_id=self.adminnote_model.user_id,
                creator_id=self.adminnote_model.creator_id,
                created_at=self.adminnote_model.created_at
            ),
            method='GET')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["user_id"], self.adminnote_model.user_id)
        self.assertEqual(
            response_data["creator_id"], self.adminnote_model.creator_id)
        self.assertEqual(
            response_data["created_at"], self.adminnote_model.created_at)

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
