from typing import Optional
from .field import Name, Phone, Email, Address, Birthday


class Contact:
    """Contact model with name, addresses, phone numbers, emails, and birthday."""
    
    def __init__(
        self,
        name: str,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        address: Optional[str] = None,
        birthday: Optional[str] = None
    ):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.email = Email(email)
        self.address = Address(address)
        self.birthday = Birthday(birthday)
    
    def __str__(self) -> str:
        parts = [f"Name: {self.name.value}"]
        if self.phone.value:
            parts.append(f"Phone: {self.phone.value}")
        if self.email.value:
            parts.append(f"Email: {self.email.value}")
        if self.address.value:
            parts.append(f"Address: {self.address.value}")
        if self.birthday.value:
            parts.append(f"Birthday: {self.birthday}")
        return ", ".join(parts)
    
    def __repr__(self) -> str:
        return f"Contact(name='{self.name.value}', phone='{self.phone.value}', email='{self.email.value}')"
