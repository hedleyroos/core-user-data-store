from user_data_store.transformation import Transformation, Mapping
from werkzeug.http import http_date


def datetime_to_string(date):
    return http_date(date.timetuple())

DB_TO_API_ADMINNOTE_TRANSFORMATION = Transformation(
    mappings=[
        Mapping(input_field="created_date", conversion=datetime_to_string),
        Mapping(input_field="updated_date", conversion=datetime_to_string)
    ],
    copy_fields=[
        "creator_id", "note", "user_id"
    ]
)