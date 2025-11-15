from typing import Callable

from src.view.view import View
from src.services.assistent import Assistent
from src.services.note_assistant import NoteAssistant


class AppController:
    def __init__(self, view: View, assistent: Assistent, note_assistent: NoteAssistant):
        self.assistent = assistent
        self.note_assistent = note_assistent
        self.view = view
        self.commands: dict[str, Callable[[list[str]], None]] = {
            # General commands
            "help": self.cmd_help,
            "hello": self.cmd_hello,
            "exit": self.cmd_exit,
            "quit": self.cmd_exit,
            # Contact commands
            "add": self.cmd_add,
            "change": self.cmd_change,
            "search": self.cmd_search,
            "phone": self.cmd_show_phone,
            "rename": self.cmd_rename,
            "add-address": self.cmd_add_address,
            "delete": self.cmd_delete,
            "all": self.cmd_show_all,
            "add-birthday": self.cmd_add_birthday,
            "show-birthday": self.cmd_show_birthday,
            "birthdays": self.cmd_birthdays,
            # Note commands
            "add-note": self.cmd_add_note,
            "edit-note": self.cmd_edit_note,
            "delete-note": self.cmd_delete_note,
            "search-notes": self.cmd_search_notes,
            "all-notes": self.cmd_all_notes,
            "add-tag": self.cmd_add_tag,
            "remove-tag": self.cmd_remove_tag,
            "get-tags": self.cmd_get_tags,
            "link-contact": self.cmd_link_contact,
            "unlink-contact": self.cmd_unlink_contact,
            "sort-created": self.cmd_sort_created,
            "sort-updated": self.cmd_sort_updated,
        }
        self._running = True

    def run(self) -> None:
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
                    self.view.render_error(data={"error": str(exc)})
            else:
                self.view.invalid_command()

    def cmd_hello(self, _):
        self.view.render_hello()

    def cmd_help(self, _args: list[str]) -> None:
        self.view.render_help()

    def cmd_add(self, args: list[str]) -> None:
        """Add a new contact to the contacts dictionary."""

        if len(args) < 2:
            raise ValueError("Usage: add [name] [phone]")
        name, phone = args[0], args[1]
        action, record = self.assistent.add_contact(name, phone)

        self.view.render_add(success=True, data={"action": action, "record": record})

    def cmd_change(self, args: list[str]) -> None:
        if len(args) < 3:
            raise ValueError("Usage: change [name] [old_phone] [new_phone]")
        name, old_phone, new_phone, *_ = args
        contact = self.assistent.change_contact(name, old_phone, new_phone)
        self.view.render_change(success=True, data={"contact": contact})

    def cmd_rename(self, args: list[str]) -> None:
        if len(args) < 2:
            raise ValueError("Usage: rename [name] [new_name]")
        name, new_name, *_ = args
        contact = self.assistent.rename_contact(name, new_name)
        self.view.render_rename(success=True, data={"contact": contact})

    def cmd_add_address(self, args: list[str]) -> None:
        if len(args) < 2:
            raise ValueError("Usage: add-address [name] [address]")
        name, *address = args
        contact = self.assistent.add_address(name, " ".join(address))
        self.view.render_add_address(success=True, data={"contact": contact})

    def cmd_delete(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: delete [name]")
        name, *_ = args
        self.assistent.delete_contact(name)
        self.view.render_delete(success=True, data={"name": name})

    def cmd_search(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: search [query]")
        query, *_ = args
        contacts = self.assistent.search_contacts(query)
        self.view.render_contacts(success=True, data={"contacts": contacts})

    def cmd_show_phone(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: phone [search]")
        search, *_ = args
        contacts = self.assistent.search_contacts(search)

        self.view.render_show_phone(success=True, data={"contacts": contacts})

    def cmd_show_all(self, _args: list[str]) -> None:
        records = self.assistent.get_all_contacts()
        self.view.render_all(success=True, data={"contacts": records})

    def cmd_add_birthday(self, args: list[str]) -> None:
        if len(args) < 2:
            raise ValueError("Usage: add-birthday [name] [birthday]")
        name, birthday, *_ = args
        record = self.assistent.add_birthday(name, birthday)
        self.view.render_add_birthday(
            success=True,
            data={"name": record.name, "birthday": record.birthday},
        )

    def cmd_show_birthday(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: show-birthday [name]")
        name, *_ = args
        birthday = self.assistent.show_birthday(name)

        if birthday:
            self.view.render_show_birthday(
                success=True, data={"name": name, "birthday": birthday}
            )
        else:
            self.view.render_show_birthday(
                success=False,
                data={"error": "Contact not found", "status_code": 404, "name": name},
            )

    def cmd_birthdays(self, _args: list[str]) -> None:
        data = self.assistent.birthdays()
        self.view.render_birthdays(success=True, data=data)

    def cmd_add_note(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: add-note [content]")
        content = " ".join(args)
        note = self.note_assistent.add_note(content)
        self.view.render_add_note(success=True, data={"note": note})

    def cmd_edit_note(self, args: list[str]) -> None:
        if len(args) < 2:
            raise ValueError("Usage: edit-note [note_id] [content]")
        note_id, content, *_ = args
        note = self.note_assistent.edit_note(note_id, content)
        self.view.render_edit_note(success=True, data={"note": note})

    def cmd_delete_note(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: delete-note [note_id]")
        note_id, *_ = args
        self.note_assistent.delete_note(note_id)
        self.view.render_delete_note(success=True, data={"note_id": note_id})

    # TODO: add search by tags and contact, search by content is not implemented yet
    def cmd_search_notes(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: search-notes [query]")
        query, *_ = args
        notes = self.note_assistent.search_notes(query)
        self.view.render_search_notes(success=True, data={"notes": notes})

    def cmd_all_notes(self, _args: list[str]) -> None:
        self.view.render_all_notes(
            success=True, data={"notes": self.note_assistent.get_all_notes()}
        )

    def cmd_add_tag(self, args: list[str]) -> None:
        if len(args) < 2:
            raise ValueError("Usage: add-tag [note_id] [tag]")
        note_id, tag, *_ = args
        self.note_assistent.add_tags_to_note(note_id, tag)
        self.view.render_add_tag(success=True, data={"note_id": note_id, "tag": tag})

    def cmd_remove_tag(self, args: list[str]) -> None:
        if len(args) < 2:
            raise ValueError("Usage: remove-tag [note_id] [tag]")
        note_id, tag, *_ = args
        self.note_assistent.remove_tag_from_note(note_id, tag)
        self.view.render_remove_tag(success=True, data={"note_id": note_id, "tag": tag})

    def cmd_get_tags(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: get-tags [note_id]")
        note_id, *_ = args
        tags = self.note_assistent.get_all_tags(note_id)
        self.view.render_get_tags(success=True, data={"note_id": note_id, "tags": tags})

    def cmd_link_contact(self, args: list[str]) -> None:
        if len(args) < 2:
            raise ValueError("Usage: link-contact [note_id] [contact_id]")
        note_id, contact_id, *_ = args
        self.note_assistent.link_note_to_contact(note_id, contact_id)
        self.view.render_link_contact(
            success=True, data={"note_id": note_id, "contact_id": contact_id}
        )

    def cmd_unlink_contact(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: unlink-contact [note_id]")
        note_id, *_ = args
        self.note_assistent.unlink_note_from_contact(note_id)
        self.view.render_unlink_contact(success=True, data={"note_id": note_id})

    def cmd_sort_created(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: sort-created [reverse]")
        reverse, *_ = args
        result = self.note_assistent.sort_by_created_date(reverse)
        self.view.render_sort_created(success=True, data={"notes": result})

    def cmd_sort_updated(self, args: list[str]) -> None:
        if len(args) < 1:
            raise ValueError("Usage: sort-updated [reverse]")
        reverse, *_ = args
        result = self.note_assistent.sort_by_updated_date(reverse)
        self.view.render_sort_updated(success=True, data={"notes": result})

    def cmd_exit(self, _args: list[str]) -> None:
        data_saved = self.assistent.save_data() and self.note_assistent.save_data()

        self._running = False
        if data_saved:
            self.view.render_exit(
                success=True, data={"message": "Data saved successfully"}
            )
        else:
            self.view.render_exit(
                success=False, data={"error": "Failed to save data", "status_code": 500}
            )
