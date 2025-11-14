from src.cli.console_view import ConsoleView
from src.controllers.app_controller import AppController
from src.services.assistent import Assistent
from src.services.storage import load_data
# from src.cli.parser import parse_input
# from src.cli.commands import add_contact, change_contact, get_phone, get_all_contacts, add_birthday, show_birthday, birthdays


def main():
    address_book = load_data()
    assistent = Assistent(address_book)
    view = ConsoleView()
    app_controller = AppController(assistent, view)
    app_controller.run()

    # book = load_data()
    # print(f"{Fore.BLUE}Welcome to the assistant bot!{Fore.RESET}")
    # while True:
    #     user_input = input(f"{Fore.BLUE}Enter a command: {Fore.RESET}")
    #     command, *args = parse_input(user_input)

    #     if command in ["close", "exit"]:
    #         print(f"{Fore.BLUE}Good bye!{Fore.RESET}")
    #         save_data(book)
    #         break
    #     elif command == "hello":
    #         print(f"{Fore.BLUE}How can I help you?{Fore.RESET}")
    #     elif command == "add":
    #         print(add_contact(args, book))
    #     elif command == "change":
    #         print(change_contact(args, book))
    #     elif command == "phone":
    #         print(get_phone(args, book))
    #     elif command == "all":
    #         get_all_contacts(book)
    #     elif command == "add-birthday":
    #         print(add_birthday(args, book))
    #     elif command == "show-birthday":
    #          print(show_birthday(args, book))
    #     elif command == "birthdays":
    #        birthdays(book)
    #     else:
    #         print(f"{Fore.RED}Invalid command.{Fore.RESET}")


if __name__ == '__main__':
    main()