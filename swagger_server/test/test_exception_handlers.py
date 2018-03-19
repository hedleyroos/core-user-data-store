# coding: utf-8

from __future__ import absolute_import

import random

from swagger_server.models import SiteDataSchema
from swagger_server.models import SiteDataSchemaCreate
from user_data_store import db_actions
from user_data_store.settings import API_KEY_HEADER
from . import BaseTestCase
from flask import json


class TestExceptions(BaseTestCase):

    def setUp(self):
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
        self.assertEqual(response.status_code, 500)
        self.assertEqual(
            r_data["error"],
            "(psycopg2.IntegrityError) duplicate key value violates unique "\
            "constraint \"sitedataschema_pkey\" DETAIL:  Key (site_id)="\
            "(%s) already exists. " % self.sitedataschema_model.site_id
        )
