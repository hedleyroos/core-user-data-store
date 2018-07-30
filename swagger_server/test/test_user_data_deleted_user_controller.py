# coding: utf-8

from __future__ import absolute_import

import random
import uuid
from datetime import datetime

from flask import json
from ge_core_shared import db_actions
import werkzeug

from swagger_server.models.deleted_user import DeletedUser
from swagger_server.models.deleted_user_create import DeletedUserCreate

from . import BaseTestCase
from project.settings import API_KEY_HEADER


class TestUserDataDeletedUserController(BaseTestCase):

    def setUp(self):
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

    #def test_adminnote_list(self):
    #    """
    #    Test case for adminnote_list


    #    """
    #    objects = []
    #    for index in range(2, 2+random.randint(2, 20)):
    #        data = {
    #            "user_id": "%s" % uuid.uuid1(),
    #            "creator_id": "%s" % uuid.uuid1(),
    #            "note": "List notes %s" % index
    #        }
    #        objects.append(db_actions.crud(
    #            model="AdminNote",
    #            api_model=AdminNote,
    #            data=data,
    #            action="create"
    #        ))
    #    query_string = [
    #        ("admin_note_ids", ",".join(map(str, [adminnote.id for adminnote in objects])))
    #    ]
    #    response = self.client.open(
    #        '/api/v1/adminnotes',
    #        method='GET',
    #        query_string=query_string,
    #        headers=self.headers)
    #    response_data = json.loads(response.data)

    #    self.assertEqual(len(response_data), len(objects))
    #    self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))
    #    query_string = [
    #        ("limit", 2),
    #        ("admin_note_ids", ",".join(map(str, [adminnote.id for adminnote in objects])))
    #    ]
    #    response = self.client.open(
    #        '/api/v1/adminnotes',
    #        method='GET',
    #        query_string=query_string,
    #        headers=self.headers)
    #    response_data = json.loads(response.data)

    #    self.assertEqual(len(response_data), 2)
    #    self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))

    #def test_adminnote_read(self):
    #    """
    #    Test case for adminnote_read

    #    """
    #    response = self.client.open(
    #        '/api/v1/adminnotes/{admin_note_id}'.format(
    #            admin_note_id=self.adminnote_model.id
    #        ),
    #        method='GET',
    #        headers=self.headers)
    #    response_data = json.loads(response.data)
    #    self.assertEqual(response_data["user_id"], self.adminnote_model.user_id)
    #    self.assertEqual(
    #        response_data["creator_id"], self.adminnote_model.creator_id)
    #    self.assertEqual(response_data["note"], self.adminnote_model.note)

    #def test_adminnote_update(self):
    #    """
    #    Test case for adminnote_update

    #    """
    #    data = {
    #        "creator_id": "%s" % uuid.uuid1(),
    #        "note": "This is text",
    #        "user_id": "%s" % uuid.uuid1(),
    #    }
    #    model = db_actions.crud(
    #        model="AdminNote",
    #        api_model=AdminNote,
    #        data=data,
    #        action="create"
    #    )
    #    data = {
    #        "note": "This is updated text",
    #    }

    #    data = AdminNoteUpdate(**data)

    #    response = self.client.open(
    #        '/api/v1/adminnotes/{admin_note_id}'.format(
    #            admin_note_id=model.id),
    #        method='PUT',
    #        data=json.dumps(data),
    #        content_type='application/json',
    #        headers=self.headers)
    #    response_data = json.loads(response.data)

    #    updated_entry = db_actions.crud(
    #        model="AdminNote",
    #        api_model=AdminNote,
    #        action="read",
    #        query={"id": model.id}
    #    )

    #    self.assertEqual(response_data["user_id"], updated_entry.user_id)
    #    self.assertEqual(
    #        response_data["creator_id"], updated_entry.creator_id)
    #    self.assertEqual(response_data["note"], updated_entry.note)

    #def test_sitedataschema_create(self):
    #    """
    #    Test case for sitedataschema_create

    #    """
    #    data = SiteDataSchemaCreate(**{
    #        "site_id": random.randint(2, 2000000),
    #        "schema": {"test": "data"}
    #    })
    #    response = self.client.open(
    #        "/api/v1/sitedataschemas",
    #        method="POST",
    #        data=json.dumps(data),
    #        content_type="application/json",
    #        headers=self.headers)

    #    response_data = json.loads(response.data)

    #    self.assertEqual(response_data["site_id"], data.site_id)
    #    self.assertEqual(response_data["schema"], data.schema)

    #def test_sitedataschema_delete(self):
    #    """
    #    Test case for sitedataschema_delete

    #    """
    #    data = {
    #        "site_id": random.randint(2, 2000000),
    #        "schema": {"test": "data"}
    #    }
    #    model = db_actions.crud(
    #        model="SiteDataSchema",
    #        api_model=SiteDataSchema,
    #        data=data,
    #        action="create"
    #    )

    #    response = self.client.open(
    #        '/api/v1/sitedataschemas/{site_id}'.format(
    #            site_id=model.site_id
    #        ), method='DELETE',
    #        headers=self.headers)

    #    with self.assertRaises(werkzeug.exceptions.NotFound):
    #        db_actions.crud(
    #            model="SiteDataSchema",
    #            api_model=SiteDataSchema,
    #            action="read",
    #            query={
    #                "site_id": model.site_id
    #            }
    #        )

    #def test_sitedataschema_list(self):
    #    """
    #    Test case for sitedataschema_list


    #    """
    #    query_string = [
    #        ("limit", 5)
    #    ]
    #    response = self.client.open(
    #        '/api/v1/sitedataschemas',
    #        method='GET',
    #        query_string=query_string,
    #        headers=self.headers)
    #    response_data = json.loads(response.data)

    #    self.assertEqual(len(response_data), 5)
    #    self.assertIn("X-Total-Count", response.headers)

    #def test_sitedataschema_read(self):
    #    """
    #    Test case for sitedataschema_read

    #    """
    #    response = self.client.open(
    #        '/api/v1/sitedataschemas/{site_id}'.format(
    #            site_id=self.sitedataschema_model.site_id
    #        ),
    #        method='GET',
    #        headers=self.headers)
    #    response_data = json.loads(response.data)
    #    self.assertEqual(
    #        response_data["site_id"], self.sitedataschema_model.site_id)
    #    self.assertEqual(
    #        response_data["schema"], self.sitedataschema_model.schema)

    #def test_sitedataschema_update(self):
    #    """
    #    Test case for sitedataschema_update


    #    """
    #    data = {
    #        "site_id": random.randint(2, 2000000),
    #        "schema": {"test": "data"}
    #    }
    #    model = db_actions.crud(
    #        model="SiteDataSchema",
    #        api_model=SiteDataSchema,
    #        data=data,
    #        action="create"
    #    )
    #    data = {
    #        "schema": {"test": "updated_data"},
    #    }

    #    data = SiteDataSchemaUpdate(**data)

    #    response = self.client.open(
    #        '/api/v1/sitedataschemas/{site_id}'.format(
    #            site_id=model.site_id),
    #        method='PUT',
    #        data=json.dumps(data),
    #        content_type='application/json',
    #        headers=self.headers)
    #    response_data = json.loads(response.data)

    #    updated_entry = db_actions.crud(
    #        model="SiteDataSchema",
    #        api_model=SiteDataSchema,
    #        action="read",
    #        query={"site_id": model.site_id}
    #    )

    #    self.assertEqual(updated_entry.site_id, model.site_id)
    #    self.assertEqual(
    #        response_data["site_id"], updated_entry.site_id)
    #    self.assertEqual(
    #        response_data["schema"], updated_entry.schema)

    #def test_usersitedata_create(self):
    #    """
    #    Test case for usersitedata_create


    #    """
    #    data = UserSiteDataCreate(**{
    #        "site_id": self.sitedataschema_data["site_id"],
    #        "user_id": "%s" % uuid.uuid1(),
    #        "data": {"item_1": 1, "item_2": 2},
    #    })
    #    response = self.client.open(
    #        "/api/v1/usersitedata",
    #        method="POST",
    #        data=json.dumps(data),
    #        content_type="application/json",
    #        headers=self.headers)

    #    # Response should contain bad request
    #    self.assertEquals(response.status_code, 400)
    #    json_data = json.loads(response.data)
    #    self.assertIn(
    #        "Data does not match expected schema:2 is not of type 'string'",
    #        json_data["detail"])

    #    data = UserSiteDataCreate(**{
    #        "site_id": self.sitedataschema_data["site_id"],
    #        "user_id": "%s" % uuid.uuid1(),
    #        "data": {"item_1": 1, "item_2": "a string"},
    #    })
    #    response = self.client.open(
    #        "/api/v1/usersitedata",
    #        method="POST",
    #        data=json.dumps(data),
    #        content_type="application/json",
    #        headers=self.headers)

    #    response_data = json.loads(response.data)

    #    self.assertEqual(response_data["site_id"], data.site_id)
    #    self.assertEqual(response_data["user_id"], data.user_id)
    #    self.assertEqual(response_data["data"], data.data)

    #def test_usersitedata_delete(self):
    #    """
    #    Test case for usersitedata_delete

    #    """
    #    data = {
    #        "site_id": random.randint(2, 2000000),
    #        "user_id": "%s" % uuid.uuid1(),
    #        "data": {"test": "delete this data"},
    #    }
    #    model = db_actions.crud(
    #        model="UserSiteData",
    #        api_model=UserSiteData,
    #        data=data,
    #        action="create"
    #    )

    #    response = self.client.open(
    #        '/api/v1/usersitedata/{user_id}/{site_id}'.format(
    #            user_id=model.user_id,
    #            site_id=model.site_id
    #        ), method='DELETE',
    #        headers=self.headers)

    #    with self.assertRaises(werkzeug.exceptions.NotFound):
    #        db_actions.crud(
    #            model="UserSiteData",
    #            api_model=UserSiteData,
    #            action="read",
    #            query={
    #                "user_id": model.user_id,
    #                "site_id": model.site_id
    #            }
    #        )

    #def test_usersitedata_list(self):
    #    """
    #    Test case for usersitedata_list


    #    """
    #    query_string = [
    #        ("limit", 5)
    #    ]
    #    response = self.client.open(
    #        '/api/v1/usersitedata',
    #        method='GET',
    #        query_string=query_string,
    #        headers=self.headers)
    #    response_data = json.loads(response.data)

    #    self.assertEqual(len(response_data), 5)
    #    self.assertIn("X-Total-Count", response.headers)

    #def test_usersitedata_read(self):
    #    """
    #    Test case for usersitedata_read

    #    """
    #    response = self.client.open(
    #        '/api/v1/usersitedata/{user_id}/{site_id}'.format(
    #            user_id=self.usersitedata_model.user_id,
    #            site_id=self.usersitedata_model.site_id
    #        ),
    #        method='GET',
    #        headers=self.headers)

    #    response_data = json.loads(response.data)
    #    self.assertEquals(
    #        response_data["user_id"], self.usersitedata_model.user_id)
    #    self.assertEquals(
    #        response_data["site_id"], self.usersitedata_model.site_id)

    #def test_usersitedata_update(self):
    #    """
    #    Test case for usersitedata_update

    #    """
    #    data = {
    #        "site_id": self.sitedataschema_data["site_id"],
    #        "user_id": "%s" % uuid.uuid1(),
    #        "data": {"test": "data"},
    #    }
    #    model = db_actions.crud(
    #        model="UserSiteData",
    #        api_model=UserSiteData,
    #        data=data,
    #        action="create"
    #    )
    #    data = {
    #        "data": {"test": "updated_data"},
    #    }

    #    data = UserSiteDataUpdate(**data)

    #    response = self.client.open(
    #        '/api/v1/usersitedata/{user_id}/{site_id}'.format(
    #            user_id=model.user_id,
    #            site_id=model.site_id),
    #        method='PUT',
    #        data=json.dumps(data),
    #        content_type='application/json',
    #        headers=self.headers)

    #    # Check for bad request
    #    self.assertEqual(response.status_code, 400)
    #    json_data = json.loads(response.data)
    #    self.assertIn(
    #        "Data does not match expected schema:Additional properties are not "
    #        "allowed ('test' was unexpected)", json_data["detail"])

    #    # Retry with correct data
    #    data = {"data": {"item_1": 1, "item_2": "another string"}}

    #    data = UserSiteDataUpdate(**data)

    #    response = self.client.open(
    #        '/api/v1/usersitedata/{user_id}/{site_id}'.format(
    #            user_id=model.user_id,
    #            site_id=model.site_id),
    #        method='PUT',
    #        data=json.dumps(data),
    #        content_type='application/json',
    #        headers=self.headers)

    #    response_data = json.loads(response.data)

    #    updated_entry = db_actions.crud(
    #        model="UserSiteData",
    #        api_model=UserSiteData,
    #        action="read",
    #        query={
    #            "user_id": model.user_id,
    #            "site_id": model.site_id
    #        }
    #    )

    #    self.assertEqual(updated_entry.site_id, model.site_id)
    #    self.assertEqual(
    #        response_data["site_id"], updated_entry.site_id)
    #    self.assertEqual(
    #        response_data["data"], updated_entry.data)


if __name__ == '__main__':
    import unittest
    unittest.main()
