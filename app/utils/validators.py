import re


def validate_email(email: str):

    pattern = r"^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$"

    return re.match(pattern, email) is not None


def validate_phone(phone: str):

    pattern = r"^[0-9]{10,15}$"

    return re.match(pattern, phone) is not None


def validate_age(age: int):

    return 0 < age < 120


def validate_required_fields(
    data: dict,
    required_fields: list
):

    missing_fields = []

    for field in required_fields:

        if field not in data:
            missing_fields.append(field)

    return missing_fields