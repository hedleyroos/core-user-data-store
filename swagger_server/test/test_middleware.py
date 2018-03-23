import random

from ge_core_shared import db_actions
from werkzeug.test import Client

from swagger_server.models.site_data_schema import SiteDataSchema
from swagger_server.test import BaseTestCase

from project.settings import API_KEY_HEADER


class TestAuthMiddleware(BaseTestCase):

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

    def test_unauthorized_request(self):
        response = self.client.open(
            '/api/v1/sitedataschemas/{site_id}'.format(
                site_id=self.sitedataschema_model.site_id
            ),
            method='GET')
        self.assert401(response)

    def test_incorrect_token(self):
        response = self.client.open(
            '/api/v1/sitedataschemas/{site_id}'.format(
                site_id=self.sitedataschema_model.site_id
            ),
            method='GET',
            headers={"X-API-KEY": "wrong-key"}
        )
        self.assert401(response)

    def test_authorized_request(self):
        response = self.client.open(
            '/api/v1/sitedataschemas/{site_id}'.format(
                site_id=self.sitedataschema_model.site_id
            ),
            method='GET',
            headers=self.headers
        )
        self.assert200(response)
