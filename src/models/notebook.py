from collections import UserDict
from .note import Note


class NoteBook(UserDict):
    """NoteBook model to manage notes."""

    def __init__(self):
        super().__init__()

    def add_note(self, note: Note) -> None:
        """Add a new note to the notebook."""
        self.data[note.id] = note

    def delete_note(self, note_id: str) -> None:
        """Delete a note from the notebook."""
        if note_id not in self.data:
            raise ValueError(f"Note with id '{note_id}' not found")
        del self.data[note_id]

    def find_note(self, note_id: str) -> Note:
        """Find a note by id."""
        return self.data.get(note_id)

    def search_by_tags(self, *tags: str) -> list:
        """Search notes by one or multiple tags."""
        from .fields import NoteTag
        tags_objs = [NoteTag(tag) for tag in tags]
        results = []
        for note in self.data.values():
            if any(tag_obj in note.tags for tag_obj in tags_objs):
                results.append(note)
        return results

    def search_by_contact(self, contact_name: str) -> list:
        """Search notes by contact name."""
        results = []
        for note in self.data.values():
            if note.contact_name and contact_name.lower() in note.contact_name.lower():
                results.append(note)
        return results

    def get_all_tags(self) -> list:
        """Get all unique tags from all notes."""
        all_tags = set()
        for note in self.data.values():
            all_tags.update(tag.value for tag in note.tags)
        return sorted(list(all_tags))

    def sort_by_created_date(self, reverse: bool = False) -> list:
        """Sort notes by creation date."""
        return sorted(self.data.values(), key=lambda n: n.created_at, reverse=reverse)

    def sort_by_updated_date(self, reverse: bool = False) -> list:
        """Sort notes by update date."""
        return sorted(self.data.values(), key=lambda n: n.updated_at, reverse=reverse)

    def __str__(self) -> str:
        if not self.data:
            return "NoteBook is empty"
        return f"NoteBook with {len(self.data)} note(s)"

    def __repr__(self) -> str:
        return f"NoteBook(notes={len(self.data)})"