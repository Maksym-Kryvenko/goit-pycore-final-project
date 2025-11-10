"""В utils додати функції валідації по регуляркам email + phone + date(має валідувати коректність дати + день народження був у минулому)"""

import re


def check_email(email: str) -> bool:
    """Validate email"""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


def check_phone(phone: str) -> bool:
    """
    Validate that the phone number consists of exactly 10 digits.
    """
    pattern = r'^\d{10}$'
    return re.fullmatch(pattern, phone) is not None


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

