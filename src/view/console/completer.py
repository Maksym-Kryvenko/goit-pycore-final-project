from prompt_toolkit.completion import Completer, Completion
from src.view.console.commands_list import COMMANDS
from typing import List
from src.models import Contact, Note


class AddressBookCompleter(Completer):
    def __init__(self, contacts: List[Contact] = [], notes: List[Note] = []):
        self.contacts: List[Contact] = contacts
        self.notes: List[Note] = notes
        self.commands = {
            cmd: desc for cmd, desc in COMMANDS.items() 
            if cmd and not cmd.startswith(" ") and not cmd.endswith(":")
        }

    def update_data(self, contacts: List[Contact] = None, notes: List[Note] = None):
        if contacts is not None:
            self.contacts = contacts
        if notes is not None:
            self.notes = notes

    def get_completions(self, document, event):
        text = document.text_before_cursor
        parts = text.split()

        # Get the actual word at cursor position (handles spaces correctly)
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        current_word = word_before_cursor.lower() if word_before_cursor else ""
        
        # Check if we're after a space (no word at cursor)
        is_after_space = word_before_cursor is None or word_before_cursor == ""
        
        # Calculate start position correctly
        if word_before_cursor:
            start_position = -len(word_before_cursor)
        else:
            start_position = 0  # Insert at cursor if no word

        # No input yet - show all commands
        if len(parts) == 0:
            yield from self.empty_word_completions(document)
            return

        # First word - complete commands (only if we're still typing the command)
        if len(parts) == 1 and not is_after_space:
            yield from self.first_word_completions(document)
            return

        # Second word and beyond - context-aware completion
        command = parts[0].lower()

        # Commands that need contact names
        second_arg_contact_commands = {
            "phone", "show-birthday", "add-birthday", "add-address",
            "rename", "delete", "change", "link-contact", "add", "search"
        }

        # Commands that need note IDs
        second_arg_note_id_commands = {
            "edit-note", "delete-note", "add-tag", "remove-tag",
            "get-tags", "link-contact", "unlink-contact", "search-notes", "add-tag", "remove-tag"
        }

        # Second word completion (after command + space, or command + partial word)
        if len(parts) == 2 and not is_after_space or (len(parts) == 1 and is_after_space):
            if command in second_arg_contact_commands:
                yield from self.second_word_completions_contact(current_word, start_position)
            elif command in second_arg_note_id_commands:
                yield from self.second_word_completions_note_id(current_word, start_position)

        # Third word completion (for commands like add-tag note_id tag)
        if len(parts) == 3 and not is_after_space or (len(parts) == 2 and is_after_space):
            if command in {"link-contact", "unlink-contact"}:
                yield from self.third_word_completions_note_id(current_word, start_position)
        


    def empty_word_completions(self, document):
        """Show all commands when no input"""
        for cmd, meta in self.commands.items():
            yield Completion(
                cmd,
                start_position=0,
                display_meta=meta
            )

    def first_word_completions(self, document):
        """Complete commands"""
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        word = word_before_cursor.lower() if word_before_cursor else ""
        start_position = -len(word_before_cursor) if word_before_cursor else 0
        
        for cmd, meta in self.commands.items():
            if not word or cmd.lower().startswith(word):
                yield Completion(
                    cmd,
                    start_position=start_position,
                    display_meta=meta
                )

    def second_word_completions_contact(self, current_word: str, start_position: int):
        """Complete with contact names"""
        for contact in self.contacts:
            contact_name = str(contact.name).lower()
            if not current_word or contact_name.startswith(current_word):
                yield Completion(
                    str(contact.name),
                    start_position=start_position,
                    display_meta=f"Contact: {contact_name}"
                )
    
    def second_word_completions_note_id(self, current_word: str, start_position: int):
        """Complete with note IDs"""
        for note in self.notes:
            note_id_lower = note.id.lower()
            if not current_word or note_id_lower.startswith(current_word):
                yield Completion(
                    note.id,
                    start_position=start_position,
                    display_meta=f"Note ID: {note.id}"
                )
    
    def third_word_completions_note_id(self, current_word: str, start_position: int):
        """Complete third word with note IDs (for commands like add-tag note_id tag)"""
        for note in self.notes:
            note_id_lower = note.id.lower()
            if not current_word or note_id_lower.startswith(current_word):
                yield Completion(
                    note.id,
                    start_position=start_position,
                    display_meta=f"Note ID: {note.id}"
                )
