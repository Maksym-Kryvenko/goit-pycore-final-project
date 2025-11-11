import re


def check_name(name: str) -> bool:
    """
    Validate that name is not empty and contains no digits.
    """
    name = name.strip()
    if not name or any(char.isdigit() for char in name):
        return False
    return True


def check_email(email: str) -> bool:
    """
    Validate email
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def check_phone(phone: str) -> bool:
    """
    Validate that the phone number is valid (Ukrainian format).
    """
    phone_number = phone.strip().replace(" ", "")
    phone_number = phone_number[phone_number.index("0") :]
    pattern = r"(\d{3})[\s\t()\n-]*(\d{3})[\s\t()\n-]*(\d{2})[\s\t()\n-]*(\d{2})"
    return re.fullmatch(pattern, phone_number) is not None


def check_date(date_str: str) -> bool:
    """
    Validate a date string in DD.MM.YYYY format, check if it's a real calendar date,
    and ensure the date is in the past (not today or in the future).

    Args:
        date_str (str): Date string to validate.

    Returns:
        bool: True if the date is valid, matches the format, and is only from the past, False otherwise.
    """
    pattern = r"^\d{2}\.\d{2}\.\d{4}$"
    if not re.match(pattern, date_str):
        return False
    try:
        from datetime import datetime

        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
        today = datetime.now()
        if date_obj < today:
            return True
        return False
    except ValueError:
        return False
