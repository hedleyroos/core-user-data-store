# coding: utf-8

from __future__ import absolute_import

import random
import uuid
from datetime import datetime

import werkzeug

from swagger_server.models import AdminNoteCreate
from swagger_server.models import SiteDataSchemaCreate
from swagger_server.models import UserSiteDataCreate
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

        self.sitedataschema_data = {
            "site_id": random.randint(2, 2000000),
            "schema": {"test": "data"}
        }
        self.sitedataschema_model = db_actions.crud(
            model="SiteDataSchema",
            api_model=SiteDataSchema,
            data=self.sitedataschema_data,
            action="create"
        )

        self.usersitedata_data = {
            # TODO: not what I did here
            "site_id": random.randint(2, 2000000),
            "user_id": "%s" % uuid.uuid1(),
            "data": {"test": "data"},
            "consented_at": datetime.utcnow(),
            "blocked": False
        }
        self.usersitedata_model = db_actions.crud(
            model="UserSiteData",
            api_model=UserSiteData,
            data=self.usersitedata_data,
            action="create"
        )

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
        data = {
            "creator_id": "%s" % uuid.uuid1(),
            "note": "This is text",
            "user_id": "%s" % uuid.uuid1(),
        }
        model = db_actions.crud(
            model="AdminNote",
            api_model=AdminNote,
            data=data,
            action="create"
        )

        response = self.client.open(
            '/api/v1/adminnotes/{id}/'.format(
                id=model.id
            ), method='DELETE')

        with self.assertRaises(werkzeug.exceptions.NotFound):
            db_actions.crud(
                model="AdminNote",
                api_model=AdminNote,
                action="read",
                query={
                    "id": model.id
                }
            )

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
            ("limit", 2),
            ("admin_note_ids", ",".join(map(str, [adminnote.id for adminnote in objects])))
        ]
        response = self.client.open(
            '/api/v1/adminnotes/',
            method='GET',
            query_string=query_string)
        response_data = json.loads(response.data)

        self.assertEqual(len(response_data), 2)

    def test_adminnote_read(self):
        """
        Test case for adminnote_read

        """
        response = self.client.open(
            '/api/v1/adminnotes/{admin_note_id}/'.format(
                admin_note_id=self.adminnote_model.id
            ),
            method='GET')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["user_id"], self.adminnote_model.user_id)
        self.assertEqual(
            response_data["creator_id"], self.adminnote_model.creator_id)
        self.assertEqual(response_data["note"], self.adminnote_model.note)

    def test_adminnote_update(self):
        """
        Test case for adminnote_update

        """
        data = {
            "creator_id": "%s" % uuid.uuid1(),
            "note": "This is text",
            "user_id": "%s" % uuid.uuid1(),
        }
        model = db_actions.crud(
            model="AdminNote",
            api_model=AdminNote,
            data=data,
            action="create"
        )
        data = {
            "note": "This is updated text",
        }

        data = AdminNoteUpdate(**data)

        response = self.client.open(
            '/api/v1/adminnotes/{admin_note_id}/'.format(
                admin_note_id=model.id),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        response_data = json.loads(response.data)

        updated_entry = db_actions.crud(
            model="AdminNote",
            api_model=AdminNote,
            action="read",
            query={"id": model.id}
        )

        self.assertEqual(response_data["user_id"], updated_entry.user_id)
        self.assertEqual(
            response_data["creator_id"], updated_entry.creator_id)
        self.assertEqual(response_data["note"], updated_entry.note)

    def test_sitedataschema_create(self):
        """
        Test case for sitedataschema_create

        """
        data = SiteDataSchemaCreate(**{
            # TODO: not what I did here
            "site_id": random.randint(2, 2000000),
            "schema": {"test": "data"}
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
        data = {
            "site_id": random.randint(2, 2000000),
            "schema": {"test": "data"}
        }
        model = db_actions.crud(
            model="SiteDataSchema",
            api_model=SiteDataSchema,
            data=data,
            action="create"
        )

        response = self.client.open(
            '/api/v1/sitedataschemas/{site_id}/'.format(
                site_id=model.site_id
            ), method='DELETE')

        with self.assertRaises(werkzeug.exceptions.NotFound):
            db_actions.crud(
                model="SiteDataSchema",
                api_model=SiteDataSchema,
                action="read",
                query={
                    "site_id": model.site_id
                }
            )

    def test_sitedataschema_list(self):
        """
        Test case for sitedataschema_list


        """
        query_string = [
            ("limit", 5)
        ]
        response = self.client.open(
            '/api/v1/sitedataschemas/',
            method='GET',
            query_string=query_string)
        response_data = json.loads(response.data)

        self.assertEqual(len(response_data), 5)

    def test_sitedataschema_read(self):
        """
        Test case for sitedataschema_read

        """
        response = self.client.open(
            '/api/v1/sitedataschemas/{site_id}/'.format(
                site_id=self.sitedataschema_model.site_id
            ),
            method='GET')
        response_data = json.loads(response.data)
        self.assertEqual(
            response_data["site_id"], self.sitedataschema_model.site_id)
        self.assertEqual(
            response_data["schema"], self.sitedataschema_model.schema)

    def test_sitedataschema_update(self):
        """
        Test case for sitedataschema_update


        """
        data = {
            "site_id": random.randint(2, 2000000),
            "schema": {"test": "data"}
        }
        model = db_actions.crud(
            model="SiteDataSchema",
            api_model=SiteDataSchema,
            data=data,
            action="create"
        )
        data = {
            "schema": {"test": "updated_data"},
        }

        data = SiteDataSchemaUpdate(**data)

        response = self.client.open(
            '/api/v1/sitedataschemas/{site_id}/'.format(
                site_id=model.site_id),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        response_data = json.loads(response.data)

        updated_entry = db_actions.crud(
            model="SiteDataSchema",
            api_model=SiteDataSchema,
            action="read",
            query={"site_id": model.site_id}
        )

        self.assertEqual(updated_entry.site_id, model.site_id)
        self.assertEqual(
            response_data["site_id"], updated_entry.site_id)
        self.assertEqual(
            response_data["schema"], updated_entry.schema)

    def test_usersitedata_create(self):
        """
        Test case for usersitedata_create


        """
        data = UserSiteDataCreate(**{
            # TODO: not what I did here
            "site_id": random.randint(2, 2000000),
            "user_id": "%s" % uuid.uuid1(),
            "data": {"test": "data"},
            "consented_at": datetime.utcnow(),
            "blocked": False
        })
        response = self.client.open(
            "/api/v1/usersitedata/",
            method="POST",
            data=json.dumps(data),
            content_type="application/json")

        response_data = json.loads(response.data)

        self.assertEqual(response_data["site_id"], data.site_id)
        self.assertEqual(response_data["user_id"], data.user_id)
        self.assertEqual(response_data["data"], data.data)
        self.assertEqual(response_data["blocked"], data.blocked)

    def test_usersitedata_delete(self):
        """
        Test case for usersitedata_delete

        """
        data = {
            # TODO: not what I did here
            "site_id": random.randint(2, 2000000),
            "user_id": "%s" % uuid.uuid1(),
            "data": {"test": "delete this data"},
            "consented_at": datetime.utcnow(),
            "blocked": False
        }
        model = db_actions.crud(
            model="UserSiteData",
            api_model=UserSiteData,
            data=data,
            action="create"
        )

        response = self.client.open(
            '/api/v1/usersitedata/{user_id}/{site_id}/'.format(
                user_id=model.user_id,
                site_id=model.site_id
            ), method='DELETE')

        with self.assertRaises(werkzeug.exceptions.NotFound):
            db_actions.crud(
                model="UserSiteData",
                api_model=UserSiteData,
                action="read",
                query={
                    "user_id": model.user_id,
                    "site_id": model.site_id
                }
            )

    def test_usersitedata_list(self):
        """
        Test case for usersitedata_list


        """
        query_string = [
            ("limit", 5)
        ]
        response = self.client.open(
            '/api/v1/usersitedata/',
            method='GET',
            query_string=query_string)
        response_data = json.loads(response.data)

        self.assertEqual(len(response_data), 5)

    def test_usersitedata_read(self):
        """
        Test case for usersitedata_read

        """
        response = self.client.open(
            '/api/v1/usersitedata/{user_id}/{site_id}/'.format(
                user_id=self.usersitedata_model.user_id,
                site_id=self.usersitedata_model.site_id
            ),
            method='GET')

        response_data = json.loads(response.data)
        self.assertEquals(
            response_data["user_id"], self.usersitedata_model.user_id)
        self.assertEquals(
            response_data["site_id"], self.usersitedata_model.site_id)

    def test_usersitedata_update(self):
        """
        Test case for usersitedata_update

        """
        data = {
            # TODO: not what I did here
            "site_id": random.randint(2, 2000000),
            "user_id": "%s" % uuid.uuid1(),
            "data": {"test": "data"},
            "consented_at": datetime.utcnow(),
            "blocked": False
        }
        model = db_actions.crud(
            model="UserSiteData",
            api_model=UserSiteData,
            data=data,
            action="create"
        )
        data = {
            "data": {"test": "updated_data"},
        }

        data = UserSiteDataUpdate(**data)

        response = self.client.open(
            '/api/v1/usersitedata/{user_id}/{site_id}/'.format(
                user_id=model.user_id,
                site_id=model.site_id),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json')
        response_data = json.loads(response.data)

        updated_entry = db_actions.crud(
            model="UserSiteData",
            api_model=UserSiteData,
            action="read",
            query={
                "user_id": model.user_id,
                "site_id": model.site_id
            }
        )

        self.assertEqual(updated_entry.site_id, model.site_id)
        self.assertEqual(
            response_data["site_id"], updated_entry.site_id)
        self.assertEqual(
            response_data["data"], updated_entry.data)


if __name__ == '__main__':
    import unittest
    unittest.main()
