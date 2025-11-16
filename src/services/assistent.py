from src.errors import DuplicationError, NotFoundError
from src.utils.is_birthday_within_next_days import congratulation_date
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

    def change_contact(self, name: str, old_value: str, new_value: str) -> Contact:
        record = self._find_contact(name)

        if "@" in old_value:
            record_email = record.find_email(old_value)
            if record_email is None:
                raise NotFoundError(f"Email {old_value} for contact {name} not found.")

            record.add_email(new_value)
            record.remove_email(old_value)

            return record
        else:
            record_phone = record.find_phone(old_value)
            if record_phone is None:
                raise NotFoundError(f"Phone {old_value} for contact {name} not found.")

            record.add_phone(new_value)
            record.remove_phone(old_value)

            return record

    def rename_contact(self, name: str, new_name: str) -> Contact:
        record = self._find_contact(name)

        if self.address_book.find(new_name):
            raise DuplicationError(f"Contact with name {new_name} already exists.")
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
        return sorted(
            self.address_book.search_contacts(query),
            key=lambda contact: str(contact.name),
        )

    def get_all_contacts(self) -> list[Contact]:
        return sorted(
            self.address_book.data.values(), key=lambda contact: str(contact.name)
        )

    def show_birthday(self, name: str) -> str:
        contacts = self.search_contacts(name)

        return contacts

    def birthdays(self) -> list[dict]:
        contacts = list(
            filter(
                lambda contact: contact.is_birthday_next_week(), self.get_all_contacts()
            )
        )
        return [
            {
                "contact": contact,
                "congratulation_date": congratulation_date(contact.birthday.value),
            }
            for contact in contacts
        ]

    def save_data(self) -> bool:
        save_pkl_book(self.address_book, DEFAULT_ADDRESSBOOK_FILENAME)
        return True

    def _find_contact(self, name: str) -> Contact:
        record = self.address_book.find(name)
        if record is None:
            raise NotFoundError("Contact not found, please check the name")
        return record
