from src.helpers.is_birthday_within_next_days import congratulation_date
from src.models import AddressBook
from src.models.contact import Contact
from src.services.storage import save_pkl_book
from src.config import DEFAULT_ADDRESSBOOK_FILENAME


class Assistent:
    def __init__(self, address_book: AddressBook):
        self.address_book = address_book

    def add_contact(self, name: str, value: str) -> tuple[str, Contact]:
        record = self.address_book.find(name)
        
        if record is None:
            record = self._add_contact(name, value)
            return "created", record
        else:
            record = self._update_contact(record, value)
            return "updated", record

    def _add_contact(self, name: str, value: str) -> Contact:
        if "@" in value:
            record = Contact(name, email=value)
        else:
            record = Contact(name, phone=value)

        self.address_book.add_contact(record)
        return record

    def _update_contact(self, record: Contact, value: str) -> Contact:
        if "@" in value:
            record.add_email(value)
        else:
            record.add_phone(value)

        return record

    def change_contact(self, name: str, phone_old: str, phone_new: str) -> Contact:
        record = self._find_contact(name)

        if "@" in phone_old:
            record_email = record.find_email(phone_old)
            if record_email is None:
                raise ValueError(f"Email {phone_old} for contact {name} not found.")

            record.remove_email(phone_old)
            record.add_email(phone_new)

            return record
        else:
            record_phone = record.find_phone(phone_old)
            if record_phone is None:
                raise ValueError(f"Phone {phone_old} for contact {name} not found.")

            record.remove_phone(phone_old)
            record.add_phone(phone_new)

            return record

    def rename_contact(self, name: str, new_name: str) -> Contact:
        record = self._find_contact(name)

        if self.address_book.find(new_name):
            raise ValueError(f"Contact with name {new_name} already exists.")
        self.address_book.update_contact(name, user_name=new_name)

        return record

    def add_address(self, name: str, address: str) -> Contact:
        record = self._find_contact(name)

        record.add_address(address)
        return record

    def add_birthday(self, name: str, birth: str) -> Contact:
        record = self._find_contact(name)

        record.add_birthday(birth)
        return record

    def delete_contact(self, name: str) -> Contact:
        record = self._find_contact(name)

        self.address_book.remove_contact(name)
        return record


    def search_contacts(self, query: str) -> list[Contact]:
        return sorted(self.address_book.search_contacts(query), key=lambda contact: str(contact.name))

    def get_phone(self, name: str) -> dict[str, list[str]]:
        contacts = self.address_book.search_contacts(name)
        if not contacts:
            raise ValueError(f"Contacts with name: {name} not found")

        return { str(contact.name): [str(phone) for phone in contact.phones] for contact in contacts }

    def get_all_contacts(self) -> list[Contact]:
        return sorted(self.address_book.data.values(), key=lambda contact: str(contact.name))

    def show_birthday(self, name: str) -> str:
        record = self._find_contact(name)

        return record.birthday

    def birthdays(self) -> list[dict]:
        contacts = list(filter(lambda contact: contact.is_birthday_next_week(), self.get_all_contacts()))
        return [{ "contact": contact, "congratulation_date": congratulation_date(contact.birthday.value) } for contact in contacts]

    def save_data(self) -> bool:
        save_pkl_book(self.address_book, DEFAULT_ADDRESSBOOK_FILENAME)
        return True

    def _find_contact(self, name: str) -> Contact:
        record = self.address_book.find(name)
        if record is None:
            raise ValueError("Contact not found, please check the name")
        return record