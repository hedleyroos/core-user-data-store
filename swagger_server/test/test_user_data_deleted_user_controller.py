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
from swagger_server.models.deleted_user_update import DeletedUserUpdate

from . import BaseTestCase
from project.settings import API_KEY_HEADER


class TestUserDataDeletedUserController(BaseTestCase):

    def setUp(self):
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


if __name__ == '__main__':
    import unittest
    unittest.main()
