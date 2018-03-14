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

from swagger_server.models.site_data_schema_update import SiteDataSchemaUpdate
from swagger_server.models.user_site_data import UserSiteData
from swagger_server.models.user_site_data_update import UserSiteDataUpdate
from user_data_store import db_actions
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

    def test_response(self):
        """
        Test case for adminnote_create

        """
        data = SiteDataSchemaCreate(**self.sitedataschema_data)
        response = self.client.open(
            "/api/v1/sitedataschemas",
            method="POST",
            data=json.dumps(data),
            content_type="application/json")
        r_data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(
            r_data["error"],
            "(psycopg2.IntegrityError) duplicate key value violates unique "\
            "constraint \"sitedataschema_pkey\" DETAIL:  Key (site_id)="\
            "(%s) already exists. " % self.sitedataschema_model.site_id
        )
