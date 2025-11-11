from typing import List
from collections import UserDict
from .contact import Contact
from .field import Name, Phone, Email, Address, Birthday
# from datetime import datetime, timedelta


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
            'name': Name,
            'phone': Phone,
            'email': Email,
            'address': Address,
            'birthday': Birthday
        }
        
        for key, value in kwargs.items():
            if key in field_map and hasattr(contact, key):
                setattr(contact, key, field_map[key](value))
            elif hasattr(contact, key):
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
    
    def __str__(self) -> str:
        if not self.data:
            return "AddressBook is empty"
        return f"AddressBook with {len(self.data)} contact(s)"
    
    def __repr__(self) -> str:
        return f"AddressBook(contacts={len(self.data)})"

    # def get_upcoming_birthdays(self):
    #     """Get a list of users with birthdays in the next 7 days."""
    #     today = datetime.today().date()

    #     upcoming_birthdays = []

    #     for key, user in self.data.items():
    #         selected_user = {} # Dictionary to hold user info for congratulations
    #         if user.birthday is not None:
    #             user_birthday = user.birthday.value
    #             birthday_this_year = user_birthday.replace(year=today.year) # Birthday date for the current year
    #             days_until_birthday = (birthday_this_year - today).days

    #             if 0 <= days_until_birthday <= 7: # Check if birthday is within the next 7 days
    #                 selected_user["name"] = key
    #                 if birthday_this_year.weekday() < 5:  # Check if birthday is on a weekday
    #                     selected_user["congratulation_date"] = birthday_this_year.strftime("%d.%m.%Y")
    #                 else:  # If birthday is on weekend, set congratulation date to next Monday
    #                     days_to_monday = 7 - birthday_this_year.weekday() # Days to next Monday
    #                     congratulation_date = birthday_this_year + timedelta(days=days_to_monday) # Calculate next Monday
    #                     selected_user["congratulation_date"] = congratulation_date.strftime("%d.%m.%Y")
    #                 upcoming_birthdays.append(selected_user)
    #     return upcoming_birthdays