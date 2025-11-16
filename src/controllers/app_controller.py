from src.config import COMMANDS
from src.errors import DuplicationError, NotFoundError, ValidationError, CommandError
from src.view.view import View
from src.services.assistent import Assistent
from src.services.note_assistant import NoteAssistant


class AppController:
    def __init__(self, view: View, assistent: Assistent, note_assistent: NoteAssistant):
        self.assistent = assistent
        self.note_assistent = note_assistent
        self.view = view
        self.command_routes = self.build_command_routes()
        self._running = True

    def build_command_routes(self) -> None:
        command_routes = {}
        for command, settings in COMMANDS.items():
            method_name = f"cmd_{command.replace('-', '_').lower()}"
            custom_route = settings.get("controller_route")
            handler = getattr(self, custom_route or method_name)
            command_routes[command] = handler
        return command_routes


    def run(self) -> None:
        self.view.render_welcome()
        self.view.render_help_proposal()
        self._update_view_data()
        while self._running:
            raw = self.view.prompt(self.assistent.get_all_contacts(), self.note_assistent.get_all_notes())
            if not raw:
                continue
            cmd, *args = raw.split()
            handler = self.command_routes.get(cmd.lower())
            if handler:
                try:
                    handler(args)
                except CommandError as exc:
                    self.view.render_error(success=False, data={"error": str(exc)})
                except ValidationError as exc:
                    self.view.render_error(success=False, data={"error": str(exc)})
                except NotFoundError as exc:
                    self.view.render_error(success=False, data={"error": str(exc)})
                except DuplicationError as exc:
                    self.view.render_error(success=False, data={"error": str(exc)})
                except Exception as exc:
                    # For unexpected exceptions, provide a generic message.
                    self.view.render_error(success=False, data={"error": f"An unexpected error occurred: {exc}"})
            else:
                self.view.invalid_command()

    def cmd_hello(self, _):
        self.view.render_hello()

    def cmd_help(self, _args: list[str]) -> None:
        self.view.render_help()

    def cmd_add(self, args: list[str]) -> None:
        """Add a new contact to the contacts dictionary."""
        self.check_args(args, "add", 2)
        name, phone = args
        action, contact = self.assistent.add_contact(name, phone)
        self.view.render_add(success=True, data={"action": action, "contact": contact})
        self._update_view_data()

    def cmd_change(self, args: list[str]) -> None:
        self.check_args(args, "change", 3)
        name, old_value, new_value, *_ = args
        contact = self.assistent.change_contact(name, old_value, new_value)
        self.view.render_change(success=True, data={"contact": contact})

    def cmd_rename(self, args: list[str]) -> None:
        self.check_args(args, "rename", 2)
        name, new_name, *_ = args
        contact = self.assistent.rename_contact(name, new_name)
        self.view.render_rename(success=True, data={"contact": contact, "old_name": name, "new_name": new_name})

    def cmd_add_address(self, args: list[str]) -> None:
        self.check_args(args, "add-address", 2)
        name, *address = args
        contact = self.assistent.add_address(name, " ".join(address))
        self.view.render_add_address(success=True, data={"contact": contact})

    def cmd_delete(self, args: list[str]) -> None:
        self.check_args(args, "delete", 1)
        name, *_ = args
        self.assistent.delete_contact(name)
        self.view.render_delete(success=True, data={"name": name})
        self._update_view_data()

    def cmd_search(self, args: list[str]) -> None:
        self.check_args(args, "search", 1)
        query, *_ = args
        contacts = self.assistent.search_contacts(query)
        self.view.render_contacts(success=True, data={"contacts": contacts, "search": query})

    def cmd_show_phone(self, args: list[str]) -> None:
        self.check_args(args, "phone", 1)
        search, *_ = args
        contacts = self.assistent.search_contacts(search)

        self.view.render_show_phone(success=True, data={"contacts": contacts, "search": search})

    def cmd_show_all(self, _args: list[str]) -> None:
        records = self.assistent.get_all_contacts()
        self.view.render_all(success=True, data={"contacts": records})

    def cmd_add_birthday(self, args: list[str]) -> None:
        self.check_args(args, "add-birthday", 2)
        name, birthday, *_ = args
        record = self.assistent.add_birthday(name, birthday)
        self.view.render_add_birthday(
            success=True,
            data={"name": record.name, "birthday": record.birthday},
        )

    def cmd_show_birthday(self, args: list[str]) -> None:
        self.check_args(args, "show-birthday", 1)
        name, *_ = args
        contacts = self.assistent.show_birthday(name)

        self.view.render_show_birthday(
            success=True, data={"contacts": contacts, "search": name}
        )

    def cmd_birthdays(self, _args: list[str]) -> None:
        data = self.assistent.birthdays()
        self.view.render_birthdays(success=True, data=data)

    def cmd_add_note(self, args: list[str]) -> None:
        self.check_args(args, "add-note", 1)
        content = " ".join(args)
        note = self.note_assistent.add_note(content)
        self.view.render_add_note(success=True, data={"note": note})
        self._update_view_data()

    def cmd_edit_note(self, args: list[str]) -> None:
        self.check_args(args, "edit-note", 2)
        note_id, content, *_ = args
        note = self.note_assistent.edit_note(note_id, content)
        self.view.render_edit_note(success=True, data={"note": note})

    def cmd_delete_note(self, args: list[str]) -> None:
        self.check_args(args, "delete-note", 1)
        note_id, *_ = args
        self.note_assistent.delete_note(note_id)
        self.view.render_delete_note(success=True, data={"note_id": note_id})
        self._update_view_data()

    # TODO: add search by tags and contact, search by content is not implemented yet
    def cmd_search_notes(self, args: list[str]) -> None:
        self.check_args(args, "search-notes", 1)
        query, *_ = args
        notes = self.note_assistent.search_notes(query)
        self.view.render_search_notes(success=True, data={"notes": notes})

    def cmd_all_notes(self, _args: list[str]) -> None:
        self.view.render_all_notes(
            success=True, data={"notes": self.note_assistent.get_all_notes()}
        )

    def cmd_add_tag(self, args: list[str]) -> None:
        self.check_args(args, "add-tag", 2)
        note_id, tag, *_ = args
        self.note_assistent.add_tags_to_note(note_id, tag)
        self.view.render_add_tag(success=True, data={"note_id": note_id, "tag": tag})

    def cmd_remove_tag(self, args: list[str]) -> None:
        self.check_args(args, "remove-tag", 2)
        note_id, tag, *_ = args
        self.note_assistent.remove_tag_from_note(note_id, tag)
        self.view.render_remove_tag(success=True, data={"note_id": note_id, "tag": tag})

    def cmd_all_tags(self, _args: list[str]) -> None:
        tags = self.note_assistent.get_all_tags()
        self.view.render_all_tags(success=True, data={"tags": tags})

    # TODO: show all tags, not only for one note
    def cmd_get_tags(self, args: list[str]) -> None:
        self.check_args(args, "get-tags", 1)
        note_id, *_ = args
        tags = self.note_assistent.get_all_tags(note_id)
        self.view.render_get_tags(success=True, data={"note_id": note_id, "tags": tags})

    def cmd_link_contact(self, args: list[str]) -> None:
        self.check_args(args, "link-contact", 2)
        contact_id, note_id, *_ = args
        self.note_assistent.link_note_to_contact(note_id, contact_id)
        self.view.render_link_contact(
            success=True, data={"note_id": note_id, "contact_id": contact_id}
        )

    def cmd_unlink_contact(self, args: list[str]) -> None:
        self.check_args(args, "unlink-contact", 1)
        note_id, *_ = args
        self.note_assistent.unlink_note_from_contact(note_id)
        self.view.render_unlink_contact(success=True, data={"note_id": note_id})

    def cmd_sort_created(self, args: list[str]) -> None:
        self.check_args(args, "sort-created", 1)
        reverse, *_ = args
        result = self.note_assistent.sort_by_created_date(reverse)
        self.view.render_sort_created(success=True, data={"notes": result})

    def cmd_sort_updated(self, args: list[str]) -> None:
        self.check_args(args, "sort-updated", 1)
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


    def _update_view_data(self) -> None:
        contacts = list(self.assistent.get_all_contacts())
        notes = list(self.note_assistent.get_all_notes())
        self.view.update_data(contacts=contacts, notes=notes)

    def check_args(self, args: list[str], command: str, min_args: int = 1) -> bool:
        if len(args) < min_args:
            raise CommandError(f"Usage: {COMMANDS[command]['example']}. Expected {min_args} arguments, got {len(args)}. Please check the command and try again.")
        return True