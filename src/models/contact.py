from datetime import datetime
from typing import Optional


class Contact:
    """Contact model with name, addresses, phone numbers, emails, and birthday."""
    
    def __init__(
        self,
        name: str,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        address: Optional[str] = None,
        birthday: Optional[datetime] = None
    ):
        self._name = name
        self._phone = phone
        self._email = email
        self._address = address
        self._birthday = birthday
    
    # Name property
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
    
    # Phone property
    @property
    def phone(self) -> Optional[str]:
        return self._phone
    
    @phone.setter
    def phone(self, value: Optional[str]):
        self._phone = value.strip() if value else None
    
    # Email property
    @property
    def email(self) -> Optional[str]:
        return self._email
    
    @email.setter
    def email(self, value: Optional[str]):
        self._email = value.strip() if value else None
    
    # Address property
    @property
    def address(self) -> Optional[str]:
        return self._address
    
    @address.setter
    def address(self, value: Optional[str]):
        self._address = value.strip() if value else None
    
    # Birthday property
    @property
    def birthday(self) -> Optional[datetime]:
        return self._birthday
    
    @birthday.setter
    def birthday(self, value: Optional[datetime]):
        self._birthday = value
    
    def __str__(self) -> str:
        parts = [f"Name: {self.name}"]
        if self.phone:
            parts.append(f"Phone: {self.phone}")
        if self.email:
            parts.append(f"Email: {self.email}")
        if self.address:
            parts.append(f"Address: {self.address}")
        if self.birthday:
            parts.append(f"Birthday: {self.birthday.strftime('%d.%m.%Y')}")
        return ", ".join(parts)
    
    def __repr__(self) -> str:
        return f"Contact(name='{self.name}', phone='{self.phone}', email='{self.email}')"
