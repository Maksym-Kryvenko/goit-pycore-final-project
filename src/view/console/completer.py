from prompt_toolkit.completion import Completer, Completion
from src.config import COMMANDS
from typing import List
from src.models import Contact, Note


class ConsoleCompleter(Completer):
    def __init__(self, contacts: List[Contact] = [], notes: List[Note] = []):
        self.contacts: List[Contact] = contacts
        self.notes: List[Note] = notes
        self.commands = {
            cmd: meta['description'] for cmd, meta in COMMANDS.items()  
        }
        self.command_settings = COMMANDS

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
        if command in self.command_settings:
            if len(parts) == 2 and not is_after_space or (len(parts) == 1 and is_after_space):
                if self.command_settings[command].get("second_arg_contact_name"):
                    yield from self.search_in_contacts_by_name(current_word, start_position)
                elif self.command_settings[command].get("second_arg_note_id"):
                    yield from self.search_in_notes_by_id(current_word, start_position)
            if len(parts) == 3 and not is_after_space or (len(parts) == 2 and is_after_space):
                if self.command_settings[command].get("third_arg_note_id"):
                    yield from self.search_in_notes_by_id(current_word, start_position)
                elif self.command_settings[command].get("third_arg_tag_name"):
                    note_id = parts[1]
                    yield from self.search_in_tags_by_name(current_word, start_position, note_id)


    def empty_word_completions(self, _document):
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

    def search_in_contacts_by_name(self, current_word: str, start_position: int):
        """Complete with contact names"""
        for contact in self.contacts:
            contact_name = str(contact.name).lower()
            if not current_word or contact_name.startswith(current_word):
                yield Completion(
                    str(contact.name),
                    start_position=start_position,
                    display_meta=f"Contact: {contact_name}"
                )

    def search_in_notes_by_id(self, current_word: str, start_position: int):
        """Complete third word with note IDs (for commands like add-tag note_id tag)"""
        for note in self.notes:
            note_id_lower = note.id.lower()
            if not current_word or note_id_lower.startswith(current_word):
                yield Completion(
                    note.id,
                    start_position=start_position,
                    display_meta=f"Note ID: {note.id}"
                )


    def search_in_tags_by_name(self, current_word: str, start_position: int, note_id: str):
        """Complete third word with tag names"""
        note = next((note for note in self.notes if note.id == note_id), None)
        tags = note.tags if note else []
        for tag in tags:
            tag_name_lower = str(tag).lower()
            if not current_word or tag_name_lower.startswith(current_word):
                yield Completion(
                    str(tag),
                    start_position=start_position,
                    display_meta=f"Tag: {str(tag)}"
                )