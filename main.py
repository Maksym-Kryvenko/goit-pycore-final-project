from src.view.console_view import ConsoleView
from src.controllers.app_controller import AppController
from src.services.assistent import Assistent
from src.services.note_assistant import NoteAssistant
from src.services.storage import load_data


def main():
    address_book, note_book = load_data()
    assistent = Assistent(address_book)
    note_assistent = NoteAssistant(note_book, address_book)
    view = ConsoleView()
    app_controller = AppController(view, assistent, note_assistent)
    app_controller.run()


if __name__ == "__main__":
    main()
