import uuid
import datetime


def generate_uuid():

    return str(uuid.uuid4())


def current_timestamp():

    return datetime.datetime.utcnow().isoformat()


def format_response(
    success: bool,
    message: str,
    data=None
):

    return {
        "success": success,
        "message": message,
        "data": data
    }


def safe_get(
    dictionary: dict,
    key: str,
    default=None
):

    return dictionary.get(key, default)