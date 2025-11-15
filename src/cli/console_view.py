from src.cli.view import View


class ConsoleView(View):
    HELP = """
Commands:
    - add [name] [phone]: Add a new contact with a name and phone number, or add a phone number to an existing contact.
    - change [name] [old phone] [new phone]: Change the phone number for the specified contact.
    - phone [name]: Show the phone numbers for the specified contact.
    - all: Show all contacts in the address book.
    - add-birthday [name] [birthday]: Add a birthday for the specified contact, format: DD.MM.YYYY
    - show-birthday [name]: Show the birthday of the specified contact.
    - birthdays: Show birthdays that will occur within the next week.
    - hello: Receive a greeting from the bot.
    - close or exit: Close the program.
    """

    def prompt(self, message: str) -> str:
        return input(message).strip()

    def render_welcome(self) -> None:
        print("Welcome to the assistant bot!")

    def render_error(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")

    def render_help_proposal(self) -> None:
        self._show("Type 'help' to see the list of commands.")

    def invalid_command(self) -> None:
        self._show("Invalid command. Type 'help'.")

    def render_help(self) -> None:
        self._show(self.HELP)

    def render_hello(self) -> None:
        self._show("Welcome to the assistant bot!")

    def render_add(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            if data.get("action") == "created":
                self._show(f"New {data.get('record')} was successful created")
            elif data.get("action") == "updated":
                self._show(
                    f"{data.get('contact', data.get('record'))} was successful updated"
                )

    def render_change(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show(
                f"{data.get('contact', data.get('record'))} was successful updated"
            )

    def render_show_phone(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show(f"Phones: {data.get('contacts_phones')}")

    def render_all(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show(f"All contacts: {data.get('contacts')}")

    def render_add_birthday(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show(f"New {data.get('record')} was successful created")

        pass

    def render_add_address(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show(f"New {data.get('record')} was successful created")

    def render_delete(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show(f"New {data.get('record')} was successful deleted")

    def render_rename(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show(f"New {data.get('record')} was successful renamed")

    def render_show_birthday(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show(f"Birthday: {data.get('birthday')}")

    def render_birthdays(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show(f"Birthdays: {data.get('birthdays')}")

    def render_add_note(self, success: bool, data: dict) -> None:
        pass

    def render_edit_note(self, success: bool, data: dict) -> None:
        pass

    def render_delete_note(self, success: bool, data: dict) -> None:
        pass

    def render_search_notes(self, success: bool, data: dict) -> None:
        pass

    def render_list_notes(self, success: bool, data: dict) -> None:
        pass

    def render_add_tag(self, success: bool, data: dict) -> None:
        pass

    def render_remove_tag(self, success: bool, data: dict) -> None:
        pass

    def render_list_tags(self, success: bool, data: dict) -> None:
        pass

    def render_link(self, success: bool, data: dict) -> None:
        pass

    def render_unlink(self, success: bool, data: dict) -> None:
        pass

    def render_exit(self, success: bool, data: dict) -> None:
        if not success:
            if data.get("error"):
                self._show_error(data.get("error"))
            else:
                self._show_error("Something went wrong")
        else:
            self._show("Data saved successfully")
            self._show("Good bye!")

    def _show(self, message: str = ""):
        if message:
            print(message)

    def _show_error(self, message: str) -> None:
        print(f"Error: {message}")
