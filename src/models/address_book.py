from typing import List, Optional
from collections import UserDict
from .contact import Contact


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
        """Update contact fields."""
        contact = self.data.get(name)
        if not contact:
            raise ValueError(f"Contact with name '{name}' not found")
        
        for key, value in kwargs.items():
            if hasattr(contact, key):
                setattr(contact, key, value)
    
    def search_contacts(self, query: str) -> List[Contact]:
        """Search contacts by name, phone, or email."""
        query = query.lower()
        results = []
        for contact in self.data.values():
            if (query in contact.name.value.lower() or
                (contact.phone.value and query in contact.phone.value.lower()) or
                (contact.email.value and query in contact.email.value.lower())):
                results.append(contact)
        return results
    
    def get_all_contacts(self) -> List[Contact]:
        """Get all contacts."""
        return list(self.data.values())
    
    def __str__(self) -> str:
        if not self.data:
            return "AddressBook is empty"
        return f"AddressBook with {len(self.data)} contact(s)"
    
    def __repr__(self) -> str:
        return f"AddressBook(contacts={len(self.data)})"
