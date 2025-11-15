from typing import List
from collections import UserDict
from .contact import Contact
from .fields import Name, Phone, Email, Address, Birthday


class AddressBook(UserDict):
    """AddressBook model to manage contacts."""

    def __init__(self):
        super().__init__()

    def add_contact(self, contact: Contact) -> None:
        """Add a new contact to the address book."""
        if contact.name.value in self.data:
            raise ValueError(f"Contact with name '{contact.name.value}' already exists")
        self.data[contact.name.value] = contact

    def remove_contact(self, name: str) -> None:
        """Remove a contact from the address book."""
        if name not in self.data:
            raise ValueError(f"Contact with name '{name}' not found")
        del self.data[name]

    def update_contact(self, name: str, **kwargs) -> None:
        """Update contact fields with proper Field validation."""
        contact = self.data.get(name)
        if not contact:
            raise ValueError(f"Contact with name '{name}' not found")

        field_map = {
            "user_name": Name,
            "phone": Phone,
            "email": Email,
            "address": Address,
            "birthday": Birthday,
        }

        for key, value in kwargs.items():
            key = "name" if key == "user_name" else key
            if key in field_map and hasattr(contact, key):
                setattr(contact, key, field_map[key](value))
            elif hasattr(contact, key):
                setattr(contact, key, value)

    def search_contacts(self, query: str) -> List[Contact]:
        """Search contacts by name, phone, or email."""
        query = query.lower()
        results = []
        for contact in self.data.values():
            # Search in name
            if query in contact.name.value.lower():
                results.append(contact)
                continue

            # Search in phones
            for phone in contact.phones:
                if query in phone.value.lower():
                    results.append(contact)
                    break
            else:
                # Search in emails (only if not found in phones)
                for email in contact.emails:
                    if query in email.value.lower():
                        results.append(contact)
                        break

        return results

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def __str__(self) -> str:
        if not self.data:
            return "AddressBook is empty"
        return f"AddressBook with {len(self.data)} contact(s)"

    def __repr__(self) -> str:
        return f"AddressBook(contacts={len(self.data)})"
