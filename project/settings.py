import logging
import os

DEFAULT_API_LIMIT = os.environ.get("DEFAULT_API_LIMIT", 50)
API_KEY_HEADER = "X-API-KEY"
ALLOWED_API_KEYS = set(os.environ["ALLOWED_API_KEYS"].split(","))
UNPROTECTED_API_ENDPOINTS = {
    "/api/v1/healthcheck"
}

# core shared settings
ACTION_MODELS = "user_data_store.models"
ACTION_MAPPINGS = "user_data_store.mappings"

# sentry settings
SENTRY_DSN = os.environ.get("SENTRY_DSN", None)
SENTRY_LOG_LEVEL = os.environ.get("SENTRY_LOG_LEVEL", logging.ERROR)

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DB_URI",
    "postgresql+psycopg2://user_data_store:password@127.0.0.1:5432/user_data_store"
)
SQLALCHEMY_TRACK_MODIFICATIONS = \
    os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", "false").lower() == "true"