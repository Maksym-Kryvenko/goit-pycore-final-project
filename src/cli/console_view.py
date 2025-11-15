import textwrap
from src.cli.view import View
from src.cli.commands_list import print_help
from src.models import Contact, Note
from src.models.fields import NoteTag


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

    def render_show_phone(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Phones: {data.get('contacts_phones')}")

    def render_all(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"All contacts:\n{self._render_contacts(data.get('contacts'))}")

    def render_add_birthday(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"New {data} was successful created")

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

        self._show(f"Birthdays: {data.get('birthdays')}")

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

        self._show(f"Search results:\n{data.get('notes')}")

    def render_list_notes(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"All notes:\n{data.get('notes')}")

    def render_add_tag(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(
            f"{data.get('note_id')} was successful tagged with {data.get('tag')}"
        )

    def render_remove_tag(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(
            f"{data.get('note_id')} was successful untagged with {self._render_tags([data.get('tag')])}"
        )

    def render_get_tags(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"Tags:\n{self._render_tags(data.get('tags'))}")

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

        self._show(
            f"Notes sorted by created date:\n{self._render_notes(data.get('notes'))}"
        )

    def render_sort_updated(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(
            f"Notes sorted by updated date:\n{self._render_notes(data.get('notes'))}"
        )

    def render_all_notes(self, success: bool, data: dict) -> None:
        if not success:
            return self.render_error(data)

        self._show(f"All notes: {self._render_notes(data.get('notes'))}")

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

    def _render_contacts(self, contacts: list) -> str:
        return "\n".join([self._render_contact(contact) for contact in contacts])

    def _render_contact(self, contact: Contact) -> str:
        return textwrap.dedent(
            f"""
                name: {contact.name};
                phones: {self._render_phones(contact.phones)};
                email: {self._render_emails(contact.emails)};
                address: {contact.address or "No address"};
                birthday: {contact.birthday or "No birthday"};
            """
        ).strip()

    def _render_emails(self, emails: list) -> str:
        return ", ".join([email.value for email in emails]) or "No emails"

    def _render_phones(self, phones: list) -> str:
        return ", ".join([phone.value for phone in phones]) or "No phones"

    def _render_notes(self, notes: list) -> str:
        return "\n".join([self._render_note(note) for note in notes]) or "No notes"

    def _render_note(self, note: Note) -> str:
        return textwrap.dedent(
            f"""
            note id: {note.id};
            note content: {note.content};
            note tags: {self._render_tags(note.tags)};
            contact: {note.contact.name if note.contact else 'No contact'}
        """
        ).strip()

    def _render_tags(self, tags: list) -> str:
        return ", ".join([self._render_tag(tag) for tag in tags]) or "No tags"

    def _render_tag(self, tag: NoteTag) -> str:
        return f"#{tag.value}"
