# coding: utf-8

from __future__ import absolute_import

import random
from unittest.mock import patch

from flask import json
from ge_core_shared import db_actions, decorators
from sqlalchemy.orm.exc import StaleDataError

from swagger_server.models import SiteDataSchema
from swagger_server.models import SiteDataSchemaCreate

from . import BaseTestCase
from project.settings import API_KEY_HEADER


class TestExceptions(BaseTestCase):

    @decorators.db_exception
    def setUp(self):
        super().setUp()
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

        self.headers = {API_KEY_HEADER: "test-api-key"}

    def test_response(self):
        """
        Test case for adminnote_create

        """
        data = SiteDataSchemaCreate(**self.sitedataschema_data)
        response = self.client.open(
            "/api/v1/sitedataschemas",
            method="POST",
            data=json.dumps(data),
            content_type="application/json",
            headers=self.headers
        )
        r_data = json.loads(response.data)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(
            r_data["error"],
            "ERROR:  duplicate key value violates unique constraint"
            " \"sitedataschema_pkey\" DETAIL:  Key (site_id)="
            "(%s) already exists." % self.sitedataschema_model.site_id
        )

    @patch("ge_core_shared.db_actions.db.session.commit")
    def test_staledataerror_response(self, mocked_crud):

        error = StaleDataError("Some reason")
        mocked_crud.side_effect = error
        data = SiteDataSchemaCreate(**self.sitedataschema_data)
        response = self.client.open(
            "/api/v1/sitedataschemas",
            method="POST",
            data=json.dumps(data),
            content_type="application/json",
            headers=self.headers
        )
        r_data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(
            "StaleDataError(Some reason)",
            r_data["error"]
        )
