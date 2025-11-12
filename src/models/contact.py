from .fields import Name, Phone, Email, Address, Birthday


class Contact:
    """Contact model with name, addresses, phone numbers, emails, and birthday."""

    def __init__(
        self,
        name: str,
        phone: str = None,
        email: str = None,
        address: str = None,
        birthday: str = None,
    ):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.email = Email(email)
        self.address = Address(address)
        self.birthday = Birthday(birthday)

    # TODO: Implement methods for adding, removing, updating and searching contact attributes.

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

    def __eq__(self, other) -> bool:
        """Compare contacts by name."""
        if not isinstance(other, Contact):
            return False
        return self.name.value == other.name.value
    
    def add_phone(self, phone_number):
        self.phone = Phone(phone_number)
