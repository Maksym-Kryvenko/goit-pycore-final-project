from datetime import datetime
from typing import Optional
import re


class Field:
    """Base class for all fields."""
    
    def __init__(self, value):
        self._value = None
        self.value = value  # Use setter for validation
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value
    
    def __str__(self) -> str:
        return str(self._value) if self._value else ""
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._value})"
    
    def __eq__(self, other) -> bool:
        """Compare fields by value."""
        if isinstance(other, Field):
            return self._value == other._value
        return self._value == other


class Name(Field):
    """Name field with validation."""
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value: str):
        if not new_value or not new_value.strip():
            raise ValueError("Name cannot be empty")
        self._value = new_value.strip()


class Phone(Field):
    """Phone field with validation."""
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value: Optional[str]):
        if new_value:
            # Remove all non-digit characters
            cleaned = re.sub(r'\D', '', new_value)
            if len(cleaned) < 10:
                raise ValueError("Phone must have at least 10 digits")
            self._value = cleaned
        else:
            self._value = None


class Email(Field):
    """Email field with validation."""
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value: Optional[str]):
        if new_value:
            cleaned = new_value.strip()
            # Basic email validation
            if '@' not in cleaned or '.' not in cleaned.split('@')[-1]:
                raise ValueError("Invalid email format")
            self._value = cleaned.lower()
        else:
            self._value = None


class Address(Field):
    """Address field."""
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value: Optional[str]):
        if new_value:
            self._value = new_value.strip()
        else:
            self._value = None


class Birthday(Field):
    """Birthday field with string to datetime conversion."""
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value: Optional[str]):
        if new_value:
            if isinstance(new_value, str):
                try:
                    # Parse string to datetime (expected format: DD.MM.YYYY)
                    self._value = datetime.strptime(new_value, '%d.%m.%Y')
                except ValueError:
                    raise ValueError("Birthday must be in format DD.MM.YYYY")
            elif isinstance(new_value, datetime):
                self._value = new_value
            else:
                raise ValueError("Birthday must be a string or datetime object")
        else:
            self._value = None
    
    def __str__(self) -> str:
        return self._value.strftime('%d.%m.%Y') if self._value else ""
