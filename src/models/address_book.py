from typing import Dict, List, Optional
from .contact import Contact


class AddressBook:
    """AddressBook model to manage contacts."""
    
    def __init__(self):
        self._contacts: Dict[str, Contact] = {}
    
    # Contacts property
    @property
    def contacts(self) -> Dict[str, Contact]:
        return self._contacts
    
    def add_contact(self, contact: Contact) -> None:
        """Add a new contact to the address book."""
        if contact.name in self._contacts:
            raise ValueError(f"Contact with name '{contact.name}' already exists")
        self._contacts[contact.name] = contact
    
    def remove_contact(self, name: str) -> None:
        """Remove a contact from the address book."""
        if name not in self._contacts:
            raise ValueError(f"Contact with name '{name}' not found")
        del self._contacts[name]
    
    def get_contact(self, name: str) -> Optional[Contact]:
        """Get a contact by name."""
        return self._contacts.get(name)
    
    def update_contact(self, name: str, **kwargs) -> None:
        """Update contact fields."""
        contact = self.get_contact(name)
        if not contact:
            raise ValueError(f"Contact with name '{name}' not found")
        
        for key, value in kwargs.items():
            if hasattr(contact, key):
                setattr(contact, key, value)
    
    def search_contacts(self, query: str) -> List[Contact]:
        """Search contacts by name, phone, or email."""
        query = query.lower()
        results = []
        for contact in self._contacts.values():
            if (query in contact.name.lower() or
                (contact.phone and query in contact.phone.lower()) or
                (contact.email and query in contact.email.lower())):
                results.append(contact)
        return results
    
    def get_all_contacts(self) -> List[Contact]:
        """Get all contacts."""
        return list(self._contacts.values())
    
    def __len__(self) -> int:
        return len(self._contacts)
    
    def __str__(self) -> str:
        if not self._contacts:
            return "AddressBook is empty"
        return f"AddressBook with {len(self._contacts)} contact(s)"
    
    def __repr__(self) -> str:
        return f"AddressBook(contacts={len(self._contacts)})"
