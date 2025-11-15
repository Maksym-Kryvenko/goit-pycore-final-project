from src.view.view import View
from src.view.console.commands_list import print_help
from src.view.console import contact as contact_renderer
from src.view.console import notes as notes_renderer
from src.view.console import tags as tags_renderer


class ConsoleView(View):
    def prompt(self, message: str) -> str:
        return input(message).strip()

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
            self._show(f"New {data.get('record')} was successful created")
        elif data.get("action") == "updated":
            self._show(
                f"{data.get('contact', data.get('record'))} was successful updated"
            )

    def render_change(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"{data.get('contact', data.get('record'))} was successful updated")

    def render_contacts(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Search results:\n{contact_renderer.render_contacts(data.get('contacts'))}")

    def render_show_phone(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Phones: {data.get('contacts_phones')}")

    def render_all(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"All contacts:\n{contact_renderer.render_contacts(data.get('contacts'))}")

    def render_add_birthday(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Updated brithday for {data.get('name')}, new values is {data.get('birthday')}")

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

        self._show(f"{data.get('record')} was successful renamed")

    def render_show_birthday(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Birthday: {data.get('birthday')}")

    def render_birthdays(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Birthdays:\n{contact_renderer.render_upcoming_birthdays(data)}")

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

        self._show(f"Search results:\n{notes_renderer.render_notes(data.get('notes'))}")

    def render_list_notes(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"All notes:\n{notes_renderer.render_notes(data.get('notes'))}")

    def render_add_tag(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(
            f"{data.get('note_id')} was successful tagged with {data.get('tag')}"
        )

    def render_remove_tag(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"{data.get('note_id')} was successful untagged with {tags_renderer.render_tags([data.get('tag')])}")

    def render_get_tags(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Tags:\n{tags_renderer.render_tags(data.get('tags'))}")

    def render_link_contact(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(
            f"{data.get('note_id')} was successful linked to {data.get('contact_id')}"
        )

    def render_unlink_contact(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(
            f"{data.get('note_id')} was successful unlinked from {data.get('contact_id')}"
        )

    def render_sort_created(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Notes sorted by created date:\n{notes_renderer.render_notes(data.get('notes'))}")

    def render_sort_updated(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Notes sorted by updated date:\n{notes_renderer.render_notes(data.get('notes'))}")

    def render_all_notes(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"All notes:\n{notes_renderer.render_notes(data.get('notes'))}")

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
