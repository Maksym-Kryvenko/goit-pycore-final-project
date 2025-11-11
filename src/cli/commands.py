from colorama import Fore
from src.models.address_book import AddressBook
from src.models.contact import Contact


class InputPhoneError(Exception):
    """Exception for input phone error"""
    pass


class InputBirthdayError(Exception):
    """Exception for input birthday error"""
    pass


def input_error(func):
    """Decorator to handle input errors for contact functions."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{Fore.RED}Give correct command please{Fore.RESET}"
        except IndexError:
            return f"{Fore.RED}Enter the argument for the command{Fore.RESET}"
        except KeyError:
            return f"{Fore.RED}This contact does not exist{Fore.RESET}"
        except InputPhoneError:
            return f"{Fore.RED}Phone number must be 10 digits.{Fore.RESET}"
        except InputBirthdayError:
            return f"{Fore.RED}Invalid date format. Use DD.MM.YYYY{Fore.RESET}"
    return inner



@input_error
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

