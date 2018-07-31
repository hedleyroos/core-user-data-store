from ge_core_shared.transformation import Transformation, Mapping
from werkzeug.http import http_date


def datetime_to_string(date):
    return http_date(date.timetuple()) if date else None


def object_to_json(object):
    return object.__dict__


DB_TO_API_ADMINNOTE_TRANSFORMATION = Transformation(
    mappings=[
        Mapping(input_field="created_at", conversion=datetime_to_string),
        Mapping(input_field="updated_at", conversion=datetime_to_string)
    ],
    copy_fields=[
        "id", "creator_id", "note", "user_id",
    ]
)

DB_TO_API_SITEDATASCHEMA_TRANSFORMATION = Transformation(
    mappings=[
        Mapping(input_field="created_at", conversion=datetime_to_string),
        Mapping(input_field="updated_at", conversion=datetime_to_string)
    ],
    copy_fields=[
        "site_id", "schema"
    ]
)

DB_TO_API_USERSITEDATA_TRANSFORMATION = Transformation(
    mappings=[
        Mapping(input_field="created_at", conversion=datetime_to_string),
        Mapping(input_field="updated_at", conversion=datetime_to_string),
    ],
    copy_fields=[
        "site_id", "data", "user_id"
    ]
)

DB_TO_API_DELETEDUSER_TRANSFORMATION = Transformation(
    mappings=[
        Mapping(input_field="deleted_at", conversion=datetime_to_string),
        Mapping(input_field="created_at", conversion=datetime_to_string),
        Mapping(input_field="updated_at", conversion=datetime_to_string),
    ],
    copy_fields=[
        "id", "username", "email", "msisdn", "reason", "deleter_id"
    ]
)

DB_TO_API_DELETEDUSERSITE_TRANSFORMATION = Transformation(
    mappings=[
        Mapping(input_field="deletion_requested_at", conversion=datetime_to_string),
        Mapping(input_field="deletion_confirmed_at", conversion=datetime_to_string),
        Mapping(input_field="created_at", conversion=datetime_to_string),
        Mapping(input_field="updated_at", conversion=datetime_to_string),
    ],
    copy_fields=[
        "deleted_user_id", "site_id", "deletion_requested_via", "deletion_confirmed_via"
    ]
)
