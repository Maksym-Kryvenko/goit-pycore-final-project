from src.models import AddressBook, NoteBook
from src.models.contact import Contact
from src.services.storage import save_data


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
            record = Contact(name, phone)
            self.address_book.add_contact(record)
            return ("created", record)
        else:
            record.add_phone(phone)
            return ("updated", record)

    def change_contact(self, name: str, phone_old: str, phone_new: str) -> Contact:
        record = self.address_book.find(name)
        if record is None:
            raise ValueError("Contact not found, please check the name")

        record_phone = record.find_phone(phone_old)
        if record_phone is None:
            raise ValueError(f"Phone {phone_old} for contact {name} not found.")

        record.remove_phone(phone_old)
        record.add_phone(phone_new)

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

    def add_birthday(self, name: str, birth: str) -> Contact:
        record = self.address_book.find(name)
        if record is None:
            raise ValueError("Contact not found, please check the name")
        else:
            record.add_birthday(birth)
        return record

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
        save_data(self.address_book, self.note_book)
        return True
