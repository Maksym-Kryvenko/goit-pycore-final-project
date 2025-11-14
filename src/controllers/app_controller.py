from typing import Callable

from src.cli.view import View
from src.services.assistent import Assistent


class AppController:
    def __init__(self, assistent: Assistent, view: View):
        self.assistent = assistent
        self.view = view
        self.commands: dict[str, Callable[[list[str]], None]] = {
            "help": self.cmd_help,
            "hello": self.cmd_hello,
            "add": self.cmd_add,
            "change": self.cmd_change,
            "phone": self.cmd_show_phone,
            "all": self.cmd_show_all,
            "add-birthday": self.cmd_add_birthday,
            "show-birthday": self.cmd_show_birthday,
            "birthdays": self.cmd_birthdays,
            "exit": self.cmd_exit,
            "quit": self.cmd_exit,
        }
        self._running = True

    def run(self):
        self.view.render_welcome()
        self.view.render_help_proposal()

        while self._running:
            raw = self.view.prompt("> ")
            if not raw:
                continue
            cmd, *args = raw.split()
            handler = self.commands.get(cmd.lower())
            if handler:
                try:
                    handler(args)
                except Exception as exc:
                    self.view.render_error(success=False, data={"error": str(exc)})
            else:
                self.view.invalid_command()

    def cmd_hello(self):
        self.view.render_hello()

    def cmd_help(self, _):
        self.view.render_help()

    def cmd_add(self, args):
        """Add a new contact to the contacts dictionary."""
        
        if len(args) < 2:
            raise ValueError("Usage: add [name] [phone]")
        name, phone = args[0], args[1]
        action, record = self.assistent.add_contact(name, phone)

        self.view.render_add(success=True, data={"action": action, "record": record})

    def cmd_change(self, args):
        if len(args) < 3:
            raise ValueError("Usage: change [name] [old_phone] [new_phone]")
        name, old_phone, new_phone, *_ = args
        contact = self.assistent.change_contact(name, old_phone, new_phone)
        self.view.render_change(success=True, data={"contact": contact})

    def cmd_show_phone(self, args):
        if len(args) < 1:
            raise ValueError("Usage: phone [search]")
        search, *_ = args
        contacts_phones = self.assistent.get_phone(search)

        if contacts_phones:
            self.view.render_show_phone(success=True, data={"contacts_phones": contacts_phones})
        else:
            self.view.render_show_phone(success=False, data={"error": "Contact not found", "status_code": 404, "search": search})

    def cmd_show_all(self, _args):
        records = self.assistent.get_all_contacts()
        self.view.render_all(success=True, data={"contacts": records})

    def cmd_add_birthday(self, args):
        if len(args) < 2:
            raise ValueError("Usage: add-birthday [name] [birthday]")
        name, birthday, *_ = args
        record = self.assistent.add_birthday(name, birthday)
        self.view.render_add_birthday(success=True, data={"name": record.name.value, "birthday": record.birthday.value})

    def cmd_show_birthday(self, args):
        if len(args) < 1:
            raise ValueError("Usage: show-birthday [name]")
        name, *_ = args
        birthday = self.assistent.show_birthday(name)
        
        if birthday:
            self.view.render_show_birthday(success=True, data={"name": name, "birthday": birthday})
        else:
            self.view.render_show_birthday(success=False, data={"error": "Contact not found", "status_code": 404, "name": name})

    def cmd_birthdays(self, _args):
        records = self.assistent.birthdays()
        self.view.render_birthdays(success=True, data={"birthdays": records})

    def cmd_exit(self, _):
        data_saved = self.assistent.save_data()
        self._running = False
        if data_saved:
            self.view.render_exit(success=True, data={"message": "Data saved successfully"})
        else:
            self.view.render_exit(success=False, data={"error": "Failed to save data", "status_code": 500})

