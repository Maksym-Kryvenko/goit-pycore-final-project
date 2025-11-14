from src.cli.console_view import ConsoleView
from src.controllers.app_controller import AppController
from src.services.assistent import Assistent
from src.services.note_assistant import NoteAssistant
from src.services.storage import load_data

# from src.cli.parser import parse_input
# from src.cli.commands import add_contact, change_contact, get_phone, get_all_contacts, add_birthday, show_birthday, birthdays


def main():
    address_book, note_book = load_data()
    assistent = Assistent(address_book)
    note_assistent = NoteAssistant(note_book)
    view = ConsoleView()
    app_controller = AppController(view, assistent, note_assistent)
    app_controller.run()


if __name__ == "__main__":
    main()
