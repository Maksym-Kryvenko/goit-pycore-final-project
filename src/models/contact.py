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
        self.phones = []
        self.emails = []
        self.address = Address(address) if address else Address(None)
        self.birthday = Birthday(birthday) if birthday else Birthday(None)

        # Add initial phone and email if provided
        if phone:
            self.add_phone(phone)
        if email:
            self.add_email(email)

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def add_email(self, email_address):
        self.emails.append(Email(email_address))

    def add_birthday(self, value: str):
        self.birthday = Birthday(value)

    def add_address(self, address: str):
        self.address = Address(address)

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def remove_email(self, email_address):
        self.emails = [email for email in self.emails if email.value != email_address]

    def find_phone(self, phone_number):
        """Find a phone number in the contact."""
        try:
            normalized_phone = Phone(phone_number)
            for phone in self.phones:
                if phone.value == normalized_phone.value:
                    return phone
        except ValueError:
            pass
        return None

    def find_email(self, email_address):
        """Find an email in the contact."""
        try:
            normalized_email = Email(email_address)
            for email in self.emails:
                if email.value == normalized_email.value:
                    return email
        except ValueError:
            pass
        return None

    def __str__(self) -> str:
        parts = [f"Name: {self.name.value}"]
        if self.phones:
            phones_str = ", ".join([phone.value for phone in self.phones])
            parts.append(f"Phones: {phones_str}")
        if self.emails:
            emails_str = ", ".join([email.value for email in self.emails])
            parts.append(f"Emails: {emails_str}")
        if self.address and self.address.value:
            parts.append(f"Address: {self.address.value}")
        if self.birthday and self.birthday.value:
            parts.append(f"Birthday: {self.birthday}")
        return ", ".join(parts)

    def __repr__(self) -> str:
        phones = [p.value for p in self.phones]
        emails = [e.value for e in self.emails]
        return f"Contact(name='{self.name.value}', phones={phones}, emails={emails})"

    def __eq__(self, other) -> bool:
        """Compare contacts by name."""
        if not isinstance(other, Contact):
            return False
        return self.name.value == other.name.value
