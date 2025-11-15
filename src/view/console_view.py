from prompt_toolkit.history import InMemoryHistory
from rich.console import Console
from src.controllers.app_controller import AppController
from src.models import Contact, Note
from src.view.console.completer import AddressBookCompleter
from src.view.console.contacts import print_contacts, print_contact_card, print_upcoming_birthdays, print_contacts_birthdays, print_contacts_phones
from src.view.console.notes import print_notes, print_note_card
from src.view.console.tags import print_tags
from src.view.view import View
from src.view.console.commands_list import print_help
from typing import List
from prompt_toolkit import prompt

class ConsoleView(View):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.contacts = []
        self.notes = []
        self.console = Console()
        self.completer = AddressBookCompleter()
        self.history = InMemoryHistory()


    def set_controller(self, controller: AppController) -> None:
        self.controller = controller

    def update_data(self, contacts: List[Contact] = None, notes: List[Note] = None) -> None:
        if contacts is not None:
            self.contacts = contacts
        if notes is not None:
            self.notes = notes
        
        self.completer.update_data(contacts=self.contacts, notes=self.notes)

    def prompt(self, contacts: List[Contact], notes: List[Note]) -> str:
        user_input = prompt("> ", completer=self.completer, complete_while_typing=True, history=self.history)
        return user_input.strip()

    def render_welcome(self) -> None:
        print("Welcome to the assistant bot!")

    def render_error(self, data: dict) -> None:
        if data.get("error"):
            self._show_error(data.get("error"))
        else:
            self._show_error("Something went wrong")

    def render_help_proposal(self) -> None:
        self._show("Type 'help' to see the list of commands.")

    def invalid_command(self) -> None:
        self._show("Invalid command. Type 'help'.")

    def render_help(self) -> None:
        print_help()

    def render_hello(self) -> None:
        self._show("Welcome to the assistant bot!")

    def render_add(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        if data.get("action") == "created":
            self._show(f"New {data.get('contact').name} was successful created")
            print_contact_card(self.console, data.get('contact'))
        elif data.get("action") == "updated":
            self._show(f"{data.get('contact').name} was successful updated")
            print_contact_card(self.console, data.get('contact'))

    def render_change(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"{data.get('contact').name} was successful updated")
        print_contact_card(self.console, data.get('contact'))

    def render_contacts(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_contacts(self.console, data.get('contacts'), data.get('search')))

    def render_show_phone(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_contacts_phones(self.console, data.get('contacts'), data.get('search')))

    def render_all(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_contacts(self.console, data.get('contacts')))

    def render_add_birthday(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Updated brithday for {data.get('name')}, new values is {data.get('birthday')}")
        self._show(print_contact_card(self.console, data.get('contact')))

    def render_add_address(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"New {data.get('contact')} was successful created")

    def render_delete(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"{data.get('name')} was successful deleted")

    def render_rename(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Contact was successful renamed from {data.get('old_name')} to {data.get('new_name')}")
        self._show(print_contact_card(self.console, data.get('contact')))

    def render_show_birthday(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_contacts_birthdays(self.console, data.get('contacts'), data.get('search')))

    def render_birthdays(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_upcoming_birthdays(self.console, data))

    def render_add_note(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"New {data.get('note')} was successful created")

    def render_edit_note(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"{data.get('note')} was successful edited")

    def render_delete_note(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"{data.get('note_id')} was successful deleted")

    def render_search_notes(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_notes(self.console, data.get('notes'), data.get('search')))

    def render_list_notes(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_notes(self.console, data.get('notes')))

    def render_add_tag(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(
            f"{data.get('note_id')} was successful tagged with {data.get('tag')}"
        )

    def render_remove_tag(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"{data.get('note_id')} was successful untagged with {data.get('tag')}")

    def render_get_tags(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_tags(self.console, data.get('tags')))

    def render_link_contact(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(
            f"{data.get('note_id')} was successful linked to {data.get('contact_id')}"
        )
        self._show(print_note_card(self.console, data.get('note')))

    def render_unlink_contact(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(
            f"{data.get('note_id')} was successful unlinked from {data.get('contact_id')}"
        )

    def render_sort_created(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_notes(self.console, data.get('notes'), data.get('search')))

    def render_sort_updated(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_notes(self.console, data.get('notes'), data.get('search')))

    def render_all_notes(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(print_notes(self.console, data.get('notes')))

    def render_exit(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show("Data saved successfully")
        self._show("Good bye!")

    def _show(self, message: str = ""):
        if message:
            print(message)

    def _show_error(self, message: str) -> None:
        self._show(f"Error: {message}")
