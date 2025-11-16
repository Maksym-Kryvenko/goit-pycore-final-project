from datetime import datetime
import re
from src.errors import ValidationError
from src.utils.validators import check_name, check_email, check_phone, check_date


class Field:
    """Base class for all fields."""

    def __init__(self, value):
        self._value = None
        self.value = value

    def __str__(self) -> str:
        return str(self.value) if self.value else ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value})"

    def __eq__(self, other) -> bool:
        """Compare fields by value."""
        if isinstance(other, Field):
            return self.value == other.value
        return self.value == other


class Name(Field):
    """Name field with validation."""

    def __init__(self, value: str):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        if not check_name(new_value):
            raise ValidationError("Name cannot be empty and must not contain digits")
        self._value = new_value.strip()


class Phone(Field):
    """Phone field with validation."""

    def __init__(self, value: str):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        if new_value is None:
            self._value = None
        else:
            if not check_phone(new_value):
                raise ValidationError("Phone must be +380XX-XXX-XX-XX format")
            self._value = self.__normalize_phone(new_value)

    def __normalize_phone(self, phone_number: str) -> str:
        """
        Normalize a phone number to the format +380XX-XXX-XX-XX.
        :param phone_number: str The input phone number in various formats.

        Return: str The normalized phone number.
        """
        try:
            phone_number = phone_number.strip().replace(" ", "")
            phone_number = phone_number[phone_number.index("0") :]
            found_number = re.fullmatch(
                r"(\d{3})[\s\t()\n-]*(\d{3})[\s\t()\n-]*(\d{2})[\s\t()\n-]*(\d{2})",
                phone_number,
            )
            if not found_number:
                raise ValidationError("Phone must be +380XX-XXX-XX-XX format")
            found_number = f"+38{found_number[0]}"
            _ = found_number[12]  # Ensure if the string is long enough
            return found_number
        except (ValueError, IndexError) as e:
            raise ValidationError("Phone must be +380XX-XXX-XX-XX format") from e


class Email(Field):
    """Email field with validation."""

    def __init__(self, value: str):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        if new_value is None:
            self._value = None
        else:
            if not check_email(new_value):
                raise ValidationError("Invalid email format")
            self._value = new_value.strip().lower()


class Address(Field):
    """Address field."""

    def __init__(self, value: str):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        if new_value is None:
            self._value = None
        else:
            self._value = new_value.strip() if new_value.strip() else None


class Birthday(Field):
    """Birthday field with string to datetime conversion."""

    def __init__(self, value: str):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        if new_value is None:
            self._value = None
        else:
            if not check_date(new_value):
                raise ValidationError(
                    "Birthday must be in format DD.MM.YYYY and cannot be today or in the future"
                )
            self._value = datetime.strptime(new_value, "%d.%m.%Y").date()

    def __str__(self) -> str:
        return self._value.strftime("%d.%m.%Y") if self._value else ""


class NoteText(Field):
    """Note text field."""

    def __init__(self, value: str):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        # Allow empty strings, just strip whitespace
        if new_value is None:
            self._value = None
        else:
            self._value = new_value.strip()


class NoteTag(Field):
    """Note tag field."""

    def __init__(self, value: str):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        self._value = new_value.strip().lower() if new_value else None
