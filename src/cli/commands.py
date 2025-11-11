from colorama import Fore
from src.models.address_book import AddressBook
from src.models.contact import Contact

# @input_error
def add_contact(args, book: AddressBook):
    """Add a new contact to the contacts dictionary."""
    name, phone, *_ = args
    record = book.search_contacts(name)
    message = f"{Fore.GREEN}Contact updated.{Fore.RESET}"
    if record is None:
        record = Contact(name)
        book.add_contact(record)
        message = f"{Fore.GREEN}Contact added.{Fore.RESET}"
    # ToDo: create add_phone in Contact class
    # if phone:
    #     record.add_phone(phone)
    return message

