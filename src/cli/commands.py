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
    if record == []:
        record = Contact(name, phone)
        book.add_contact(record)
        message = f"{Fore.GREEN}Contact added.{Fore.RESET}"
    return message


@input_error
def change_contact(args, book: AddressBook):
    """Change the phone number of an existing contact."""
    return f'{Fore.RED}Needed to do change the phone number function!!!!!!!!!!!{Fore.RESET}'
    # name, phone_old, phone_new = args[0], args[1], args[2]
    # record = book.search_contacts(name)
    # if record is None:
    #     raise KeyError
    # else:
        # record_phone = record.find_phone(phone_old)
        # if record_phone is None:
            # return f"{Fore.RED}Phone {phone_old} for contact {name} not found.{Fore.RESET}"
        # else:
            # record.remove_phone(phone_old)
            # record.add_phone(phone_new)
            # return f"{Fore.GREEN}Phone {phone_old} for contact {name} was updated to {phone_new}.{Fore.RESET}"


@input_error
def get_phone(args, book: AddressBook):
    """Get phone numbers of a contact."""
    return f'{Fore.RED}Needed to do get phone function!!!!!!!!!!!{Fore.RESET}'
    # name, *_ = args
    # record = book.search_contacts(name)
    # if record is None:
    #     raise KeyError
    # else:
    #     return f"{Fore.GREEN}{record}{Fore.RESET}"


@input_error    
def get_all_contacts(book: AddressBook):
    """ Return all contacts"""
    print(f'{Fore.RED}Needed to do get all contact function!!!!!!!!!!!{Fore.RESET}')
    # for record in book.data.values():
    #     print(f"{Fore.GREEN}{record}{Fore.RESET}")


@input_error
def add_birthday(args, book):
    """Add a birthday to contact."""
    return f'{Fore.RED}Needed to do add birthday function!!!!!!!!!!!{Fore.RESET}'
    # name, birth, *_ = args
    # record = book.find(name)
    # if record is None:
    #     raise KeyError  
    # else:
    #     record.add_birthday(birth)
    # return f"{Fore.GREEN}Birthday was added to contact {name}.{Fore.RESET}"


@input_error
def show_birthday(args, book: AddressBook):
    """Show contact birthday"""
    return f'{Fore.RED}Needed to do show birthday function!!!!!!!!!!!{Fore.RESET}'
    # name, *_ = args
    # record = book.search_contacts(name)
    # if record is None:
    #     return f"{Fore.RED}Contact {name} not found.{Fore.RESET}"
    # else:
    #     birth = record.birthday
    #     if birth is None:
    #         return f"{Fore.RED}No information on birthday of contact {name}.{Fore.RESET}"
    #     else:
    #         return f"{Fore.GREEN}Contact {name} have birthday {birth}{Fore.RESET}"


@input_error
def birthdays(book: AddressBook):
    """Show upcoming birthdays"""
    print(f'{Fore.RED}Needed to do birthdays function!!!!!!!!!!!{Fore.RESET}')
    # upcoming_birthdays = book.get_upcoming_birthdays()
    # if len(upcoming_birthdays) < 1:
    #     print(f"{Fore.RED}No contacts with birthday in future 7 days.{Fore.RESET}")
    # else:
    #     for contact in upcoming_birthdays:
    #         print(f"{Fore.GREEN}{contact['name']}. Congratulation date: {contact['congratulation_date']}{Fore.RESET}")  


