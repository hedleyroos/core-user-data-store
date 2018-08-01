# coding: utf-8

from __future__ import absolute_import

import random
import uuid
from datetime import datetime
from dateutil.tz import tzutc

from flask import json
from ge_core_shared import db_actions
from sqlalchemy import text
import werkzeug

from swagger_server.models import AdminNoteCreate
from swagger_server.models.site_data_schema_create import SiteDataSchemaCreate
from swagger_server.models import UserSiteDataCreate
from swagger_server.models.admin_note import AdminNote
from swagger_server.models.deleted_user import DeletedUser
from swagger_server.models.deleted_user_create import DeletedUserCreate
from swagger_server.models.deleted_user_site import DeletedUserSite
from swagger_server.models.deleted_user_site_create import DeletedUserSiteCreate
from swagger_server.models.deleted_user_site_update import DeletedUserSiteUpdate
from swagger_server.models.deleted_user_update import DeletedUserUpdate
from swagger_server.models.site_data_schema import SiteDataSchema
from swagger_server.models.user_site_data import UserSiteData

from . import BaseTestCase
from project.settings import API_KEY_HEADER
from project.app import DB


class TestUserDataMiscController(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.headers = {API_KEY_HEADER: "test-api-key"}
        self.sitedataschema_data = {
            "site_id": random.randint(2, 2000000),
            "schema": {
                "type": "object",
                "properties": {
                    "item_1": {"type": "number"},
                    "item_2": {"type": "string"}
                },
                "additionalProperties": False
            }
        }
        self.sitedataschema_model = db_actions.crud(
            model="SiteDataSchema",
            api_model=SiteDataSchema,
            data=self.sitedataschema_data,
            action="create"
        )

    def test_delete_user_data_adminnote(self):
        user_id = "%s" % uuid.uuid1()
        for index in range(1, 30):
            adminnote_data = {
                "creator_id": "%s" % uuid.uuid1(),
                "note": "This is text %s" % index,
                "user_id": user_id,
            }
            db_actions.crud(
                model="AdminNote",
                api_model=AdminNoteCreate,
                data=adminnote_data,
                action="create"
            )

        response = self.client.open(
            '/api/v1/deleteuserdata/{user_id}'.format(
                user_id=user_id,
            ), method='GET',
            headers=self.headers)

        with self.assertRaises(werkzeug.exceptions.NotFound):
            note_list = db_actions.crud(
                model="AdminNote",
                api_model=AdminNote,
                action="read",
                query={
                    "user_id": user_id,
                }
            )
        response_data = json.loads(response.data)
        self.assertEqual(response_data["amount"], 29)

    def test_delete_user_data_site_data(self):
        user_id = "%s" % uuid.uuid1()
        for index in range(1, 24):
            sitedataschema_data = {
                "site_id": index,
                "schema": {
                    "type": "object",
                    "properties": {
                        "item_1": {"type": "number"},
                        "item_2": {"type": "string"}
                    },
                    "additionalProperties": False
                }
            }
            sitedataschema_model = db_actions.crud(
                model="SiteDataSchema",
                api_model=SiteDataSchemaCreate,
                data=sitedataschema_data,
                action="create"
            )
            data = {
                "site_id": sitedataschema_data["site_id"],
                "user_id": user_id,
                "data": {"item_1": 1, "item_2": "a string"},
            }
            db_actions.crud(
                model="UserSiteData",
                api_model=UserSiteDataCreate,
                data=data,
                action="create"
            )

        response = self.client.open(
            '/api/v1/deleteuserdata/{user_id}'.format(
                user_id=user_id,
            ), method='GET',
            headers=self.headers)

        with self.assertRaises(werkzeug.exceptions.NotFound):
            note_list = db_actions.crud(
                model="UserSiteData",
                api_model=UserSiteData,
                action="read",
                query={
                    "user_id": user_id,
                }
            )
        response_data = json.loads(response.data)
        self.assertEqual(response_data["amount"], 23)



class TestUserDataDeletedUserController(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.deleteduser_data = {
            "id": "%s" % uuid.uuid1(),
            "username": "SetupUseryName",
            "email": "asdasd@asd.com",
            "msisdn": "0865456321",
            "reason": "setupUserHere",
            "deleter_id": "%s" % uuid.uuid1()
        }
        self.deleteduser_model = db_actions.crud(
            model="DeletedUser",
            api_model=DeletedUserCreate,
            data=self.deleteduser_data,
            action="create"
        )
        self.headers = {API_KEY_HEADER: "test-api-key"}

    def test_deleted_user_create(self):
        data_dict = {
            "id": "%s" % uuid.uuid1(),
            "username": "UseryName",
            "email": "asdasd@asd.com",
            "msisdn": "0865456321",
            "reason": "Like I need one",
            "deleter_id": "%s" % uuid.uuid1(),
        }
        data = DeletedUserCreate(**data_dict)
        response = self.client.open(
            "/api/v1/deleteduser",
            method="POST",
            data=json.dumps(data),
            content_type="application/json",
            headers=self.headers)

        response_data = json.loads(response.data)
        for key, val in data_dict.items():
            self.assertEqual(response_data[key], getattr(data, key))

    def test_deleted_user_delete(self):
        data = {
            "id": "%s" % uuid.uuid1(),
            "username": "UseryName",
            "email": "asdasd@asd.com",
            "msisdn": "0865456321",
            "reason": "Like I need one",
            "deleter_id": "%s" % uuid.uuid1(),
        }
        model = db_actions.crud(
            model="DeletedUser",
            api_model=DeletedUserCreate,
            data=data,
            action="create"
        )

        response = self.client.open(
            '/api/v1/deleteduser/{user_id}'.format(
                user_id=model.id
            ), method='DELETE',
            headers=self.headers)

        with self.assertRaises(werkzeug.exceptions.NotFound):
            db_actions.crud(
                model="DeletedUser",
                api_model=DeletedUser,
                action="read",
                query={
                    "id": model.id
                }
            )

    def test_deleted_user_list(self):
        objects = []
        deleter_id = "%s" % uuid.uuid1()
        for index in range(1, random.randint(5, 20)):
            data = {
                "id": "%s" % uuid.uuid1(),
                "username": "UseryName",
                "email": "asdasd@asd.com",
                "msisdn": "0865456321",
                "reason": "Like I need %s" % index,
                "deleter_id": deleter_id
            }
            objects.append(db_actions.crud(
                model="DeletedUser",
                api_model=DeletedUserCreate,
                data=data,
                action="create"
            ))
        query_string = [
            ("deleter_id", deleter_id)
        ]
        response = self.client.open(
            '/api/v1/deleteduser',
            method='GET',
            query_string=query_string,
            headers=self.headers)
        response_data = json.loads(response.data)
        self.assertEqual(len(response_data), len(objects))
        self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))
        query_string = [
            ("deleter_id", deleter_id),
            ("limit", 2),
        ]
        response = self.client.open(
            '/api/v1/deleteduser',
            method='GET',
            query_string=query_string,
            headers=self.headers)
        response_data = json.loads(response.data)

        self.assertEqual(len(response_data), 2)
        self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))

    def test_deleted_user_read(self):
        response = self.client.open(
            '/api/v1/deleteduser/{user_id}'.format(
                user_id=self.deleteduser_model.id
            ),
            method='GET',
            headers=self.headers)
        response_data = json.loads(response.data)
        for key, val in self.deleteduser_data.items():
            self.assertEqual(response_data[key], getattr(self.deleteduser_model, key))

    def test_delete_user_update(self):
        original_data = {
            "id": "%s" % uuid.uuid1(),
            "username": "UseryName",
            "email": "asdasd@asd.com",
            "msisdn": "0865456321",
            "reason": "Like I need a reason",
            "deleter_id": "%s" % uuid.uuid1()
        }
        model = db_actions.crud(
            model="DeletedUser",
            api_model=DeletedUserCreate,
            data=original_data,
            action="create"
        )
        data = {
            "reason": "This is updated text",
            "username": "supersecretupdatedname%s" % uuid.uuid1()
        }

        updated_data = DeletedUserUpdate(**data)

        response = self.client.open(
            '/api/v1/deleteduser/{user_id}'.format(
                user_id=model.id),
            method='PUT',
            data=json.dumps(updated_data),
            content_type='application/json',
            headers=self.headers)
        response_data = json.loads(response.data)

        updated_entry = db_actions.crud(
            model="DeletedUser",
            api_model=DeletedUser,
            action="read",
            query={"id": model.id}
        )

        for key, val in data.items():
            self.assertEqual(response_data[key], getattr(updated_entry, key))


class TestUserDataDeletedUserSiteController(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.deletedusersite_data = {
            "deleted_user_id": "%s" % uuid.uuid1(),
            "site_id": 999999,
        }
        self.deletedusersite_model = db_actions.crud(
            model="DeletedUserSite",
            api_model=DeletedUserSiteCreate,
            data=self.deletedusersite_data,
            action="create"
        )
        self.headers = {API_KEY_HEADER: "test-api-key"}

    def test_deleted_user_site_create(self):
        data_dict = {
            "deleted_user_id": "%s" % uuid.uuid1(),
            "site_id": 1,
        }
        data = DeletedUserSiteCreate(**data_dict)
        response = self.client.open(
            "/api/v1/deletedusersite",
            method="POST",
            data=json.dumps(data),
            content_type="application/json",
            headers=self.headers)

        response_data = json.loads(response.data)
        for key, val in data_dict.items():
            self.assertEqual(response_data[key], getattr(data, key))

    def test_deleted_user_site_delete(self):
        data = {
            "deleted_user_id": "%s" % uuid.uuid1(),
            "site_id": 2,
        }
        model = db_actions.crud(
            model="DeletedUserSite",
            api_model=DeletedUserSiteCreate,
            data=data,
            action="create"
        )

        response = self.client.open(
            '/api/v1/deletedusersite/{user_id}/{site_id}'.format(
                user_id=model.deleted_user_id,
                site_id=model.site_id
            ), method='DELETE',
            headers=self.headers)

        with self.assertRaises(werkzeug.exceptions.NotFound):
            db_actions.crud(
                model="DeletedUserSite",
                api_model=DeletedUserSite,
                action="read",
                query={
                    "deleted_user_id": model.deleted_user_id,
                    "site_id": model.site_id
                }
            )

    def test_deleted_user_site_list(self):
        objects = []
        user_id = "%s" % uuid.uuid1()
        for index in range(1, random.randint(5, 20)):
            data = {
                "deleted_user_id": user_id,
                "site_id": index + 20,
            }
            objects.append(db_actions.crud(
                model="DeletedUserSite",
                api_model=DeletedUserSiteCreate,
                data=data,
                action="create"
            ))
        query_string = [
            ("user_id", user_id)
        ]
        response = self.client.open(
            '/api/v1/deletedusersite',
            method='GET',
            query_string=query_string,
            headers=self.headers)
        response_data = json.loads(response.data)
        self.assertEqual(len(response_data), len(objects))
        self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))
        query_string = [
            ("user_id", user_id),
            ("limit", 2),
        ]
        response = self.client.open(
            '/api/v1/deletedusersite',
            method='GET',
            query_string=query_string,
            headers=self.headers)
        response_data = json.loads(response.data)

        self.assertEqual(len(response_data), 2)
        self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))

    def test_deleted_user_site_read(self):
        response = self.client.open(
            '/api/v1/deletedusersite/{user_id}/{site_id}'.format(
                user_id=self.deletedusersite_model.deleted_user_id,
                site_id=self.deletedusersite_model.site_id,
            ),
            method='GET',
            headers=self.headers)
        response_data = json.loads(response.data)
        for key, val in self.deletedusersite_data.items():
            self.assertEqual(response_data[key], getattr(self.deletedusersite_model, key))

    def test_delete_user_update(self):
        original_data = {
            "deleted_user_id": "%s" % uuid.uuid1(),
            "site_id": 56431684,
        }
        model = db_actions.crud(
            model="DeletedUserSite",
            api_model=DeletedUserSiteCreate,
            data=original_data,
            action="create"
        )
        data = {
            "deletion_requested_via": "/shrug",
            "deletion_requested_at": datetime(2001, 1, 20, 0, 0, tzinfo=tzutc()),
            "deletion_confirmed_via": "who knows"
        }

        updated_data = DeletedUserSiteUpdate(**data)

        response = self.client.open(
            '/api/v1/deletedusersite/{user_id}/{site_id}'.format(
                user_id=model.deleted_user_id,
                site_id=model.site_id,
            ),
            method='PUT',
            data=json.dumps(updated_data),
            content_type='application/json',
            headers=self.headers)
        response_data = json.loads(response.data)

        updated_entry = db_actions.crud(
            model="DeletedUserSite",
            api_model=DeletedUserSite,
            action="read",
            query={
                "deleted_user_id": model.deleted_user_id,
                "site_id": model.site_id
            }
        )
        self.assertEqual(response_data["deletion_requested_via"], updated_entry.deletion_requested_via)
        self.assertEqual(response_data["deletion_requested_at"], updated_entry.deletion_requested_at.isoformat())
        self.assertEqual(response_data["deletion_confirmed_via"], updated_entry.deletion_confirmed_via)


if __name__ == '__main__':
    import unittest
    unittest.main()
