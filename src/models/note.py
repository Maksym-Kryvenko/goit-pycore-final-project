from datetime import datetime
import uuid
from .fields import NoteText, NoteTag


class Note:
    """Note model with id, content, tags, and timestamps."""

    def __init__(
        self,
        content: str,
        contact_name: str = None,
        tags: tuple = None,
    ):
        self.id = str(uuid.uuid4())
        self.content = NoteText(content) if content else NoteText("")
        self.contact_name = contact_name
        self.tags = [NoteTag(tag) for tag in tags] if tags else []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_tags(self, *tags: str) -> None:
        """Add one or more tags to the note."""
        for tag in tags:
            tag_clean = tag.strip().lower()
            if tag_clean and tag_clean not in self.tags:
                self.tags.append(tag_clean)
        self.updated_at = datetime.now()

    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the note."""
        tag_clean = tag.strip().lower()
        if tag_clean in self.tags:
            self.tags.remove(tag_clean)
            self.updated_at = datetime.now()

    # TODO: Implement relationship with Contact objects.
    def link_to_contact(self, contact_name: str) -> None:
        """Link note to a contact."""
        self.contact_name = contact_name
        self.updated_at = datetime.now()

    def unlink_contact(self) -> None:
        """Remove contact link from note."""
        self.contact_name = None
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        contact_str = f" [{self.contact_name}]" if self.contact_name else ""
        tags_str = f" #{' #'.join(self.tags)}" if self.tags else ""
        return f"Note{contact_str}: {self.content[:50]}...{tags_str}"

    def __repr__(self) -> str:
        return f"Note(id='{self.id[:8]}...', content='{self.content[:30]}...')"

    def __eq__(self, other) -> bool:
        """Compare notes by id."""
        if not isinstance(other, Note):
            return False
        return self.id == other.id
