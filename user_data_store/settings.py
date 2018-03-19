import os

DEFAULT_API_LIMIT = os.environ.get("DEFAULT_API_LIMIT", 50)
DB_URI = os.environ.get(
        "DB_URI", "postgresql+psycopg2://user_data_store:password@127.0.0.1:5432/user_data_store")

API_KEY_HEADER = "X-API-KEY"
ALLOWED_API_KEYS = set(os.getenv("ALLOWED_API_KEYS").split(","))
