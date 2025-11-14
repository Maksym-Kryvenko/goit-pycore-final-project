from datetime import date
from typing import Optional


def is_birthday_within_next_days(
    dob: date, days: int = 7, today: Optional[date] = None
) -> bool:
    if today is None:
        today = date.today()

    try:
        next_bday = dob.replace(year=today.year)
    except ValueError:
        next_bday = date(today.year, 2, 28)

    if next_bday < today:
        try:
            next_bday = dob.replace(year=today.year + 1)
        except ValueError:
            next_bday = date(today.year + 1, 2, 28)

    return 0 <= (next_bday - today).days <= days
