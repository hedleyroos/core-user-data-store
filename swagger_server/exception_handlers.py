import logging
import json

from project.app import DB

logger = logging.getLogger(__name__)


def db_exceptions(exception):
    logger.error(exception)
    DB.session.rollback()
    return json.dumps({"error": exception._message().replace("\n", " ")}), 500
