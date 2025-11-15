from src.models import AddressBook
from src.models.contact import Contact
from src.services.storage import save_pkl_book
from src.config import DEFAULT_ADDRESSBOOK_FILENAME


class Assistent:
    def __init__(self, address_book: AddressBook):
        self.address_book = address_book

    def add_contact(self, name: str, phone: str = None) -> tuple[str, Contact]:
        record = self.address_book.find(name)
        if record and not phone:
            raise ValueError(
                "Contact already exists, please specify phone number if you want to update it"
            )
        elif record is None:
            if "@" in phone:
                record = Contact(name, email=phone)
            else:
                record = Contact(name, phone)
            self.address_book.add_contact(record)
            return ("created", record)
        else:
            if "@" in phone:
                record.add_email(phone)
            else:
                record.add_phone(phone)
            return ("updated", record)

    def change_contact(self, name: str, phone_old: str, phone_new: str) -> Contact:
        record = self.address_book.find(name)
        if record is None:
            raise ValueError("Contact not found, please check the name")

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

    def rename_contact(self, name: str, new_name: str):
        record = self.address_book.find(name)
        if not record:
            raise ValueError("Contact not found, please check the name")
        if self.address_book.find(new_name):
            raise ValueError(f"Contact with name {new_name} already exists.")
        self.address_book.update_contact(name, user_name=new_name)

        return record

    def add_address(self, name: str, address: str) -> Contact:
        record = self.address_book.find(name)
        if record is None:
            raise ValueError("Contact not found, please check the name")
        else:
            record.add_address(address)
        return record

    def add_birthday(self, name: str, birth: str) -> Contact:
        record = self.address_book.find(name)
        if record is None:
            raise ValueError("Contact not found, please check the name")
        else:
            record.add_birthday(birth)
        return record

    def delete_contact(self, name: str) -> Contact:
        record = self.address_book.find(name)
        if record is None:
            raise ValueError("Contact not found, please check the name")
        else:
            self.address_book.remove_contact(name)
        return record

    def get_phone(self, name: str) -> str:
        contacts = self.address_book.search_contacts(name)
        if contacts is None:
            raise ValueError("Contact not found, please check the name")

        return {
            contact.name.value: [phone.value for phone in contact.phones]
            for contact in contacts
        }

    def get_all_contacts(self) -> list[Contact]:
        return self.address_book.data.values()

    def show_birthday(self, name: str) -> str:
        record = self.address_book.find(name)

        if record is None:
            return ValueError("Contact not found, please check the name")

        return record.birthday

    def birthdays(self):
        return self.address_book.get_upcoming_birthdays()
        # TODO: Update function to use the new method
        # return list(filter(lambda contact: contact.is_birthday_next_week(), self.address_book.data.values()))

    def save_data(self):
        save_pkl_book(self.address_book, DEFAULT_ADDRESSBOOK_FILENAME)
        return True
