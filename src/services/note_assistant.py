"""Assistant for Note and NoteBook operations."""

from typing import Optional
from src.models import Note, NoteBook, AddressBook
from src.services.storage import save_pkl_book
from src.config import DEFAULT_NOTEBOOK_FILENAME
from src.models.fields import NoteText
from datetime import datetime
from src.errors import NotFoundError


class NoteAssistant:
    """Assistant layer for Note and NoteBook management."""

    def __init__(self, notebook: NoteBook, address_book: AddressBook):
        self.notebook = notebook
        self.__address_book = address_book

    def add_note(
        self, content: str, contact: str = None, tags: Optional[tuple] = None
    ) -> Note:
        """Add a new note."""
        note = Note(content=content, contact=contact, tags=tags)
        self.notebook.add_note(note)
        return note

    def delete_note(self, note_id: str) -> bool:
        """Delete a note by ID."""
        self.notebook.delete_note(note_id)
        return True

    def edit_note(self, note_id: str, content: str) -> Note:
        """Edit a note's content by ID."""
        note = self.find_note(note_id)
        if not note:
            raise NotFoundError(f"Note with id '{note_id}' not found")
        note.content = NoteText(content)
        note.updated_at = datetime.now()
        return note

    def find_note(self, note_id: str) -> Optional[Note]:
        """Find a note by ID."""
        return self.notebook.find_note(note_id)

    def add_tags_to_note(self, note_id: str, *tags: str) -> bool:
        """Add tags to a note."""
        note = self.find_note(note_id)
        if not note:
            raise NotFoundError(f"Note with id '{note_id}' not found")
        note.add_tags(*tags)
        return True

    def remove_tag_from_note(self, note_id: str, tag: str) -> bool:
        """Remove a tag from a note."""
        note = self.find_note(note_id)
        if not note:
            raise NotFoundError(f"Note with id '{note_id}' not found")
        if tag not in note.tags:
            raise NotFoundError(f"Tag '{tag}' not found in note with id '{note_id}'")
        note.remove_tag(tag)
        return True

    def link_note_to_contact(self, note_id: str, contact: str) -> bool:
        """Link a note to a contact."""
        note = self.find_note(note_id)
        if not note:
            raise NotFoundError(f"Note with id '{note_id}' not found")
        note.link_to_contact(contact, self.__address_book)
        return True

    def unlink_note_from_contact(self, note_id: str) -> bool:
        """Unlink a note from a contact."""
        note = self.find_note(note_id)
        if not note:
            raise NotFoundError(f"Note with id '{note_id}' not found")
        note.unlink_contact()
        return True

    def search_notes(self, query: str) -> list:
        """Search notes by tags or contact name."""
        # Try to search by tags first
        results = self.search_by_tags(query)
        if results:
            return results
        # Then try to search by contact
        return self.search_by_contact(query)

    def search(self, query: str) -> list:
        self.search_by_tags(query.split()) or self.search_by_contact(query)

    def search_by_tags(self, *tags: str) -> list:
        """Search notes by tags."""
        return self.notebook.search_by_tags(*tags)

    def search_by_contact(self, contact_name: str) -> list:
        """Search notes by contact name."""
        return self.notebook.search_by_contact(contact_name)

    def get_all_notes(self) -> list:
        """Get all notes."""
        return list(self.notebook.values())

    def get_all_tags(self) -> list:
        """Get all unique tags."""
        return self.notebook.get_all_tags()

    def sort_by_created_date(self, reverse: bool = False) -> list:
        """Sort notes by creation date."""
        return self.notebook.sort_by_created_date(reverse=reverse)

    def sort_by_updated_date(self, reverse: bool = False) -> list:
        """Sort notes by update date."""
        return self.notebook.sort_by_updated_date(reverse=reverse)

    def save_data(self):
        save_pkl_book(self.notebook, DEFAULT_NOTEBOOK_FILENAME)
        return True
