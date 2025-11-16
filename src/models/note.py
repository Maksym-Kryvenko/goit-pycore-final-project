from datetime import datetime
import uuid
from src.errors import NotFoundError
from src.models.fields import NoteText, NoteTag
from src.models.address_book import AddressBook


class Note:
    """Note model with id, content, tags, and timestamps."""

    def __init__(
        self,
        content: str,
        contact: str = None,
        tags: tuple = None,
    ):
        # Use shorter ID: first 8 hex characters of UUID
        self.id = uuid.uuid4().hex[:8]
        self.content = NoteText(content) if content else NoteText("")
        self.contact = contact
        self.tags = [NoteTag(tag) for tag in tags] if tags else []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_tags(self, *tags: str) -> None:
        """Add one or more tags to the note."""
        for tag in tags:
            tag_obj = NoteTag(tag)
            if tag_obj.value and tag_obj not in self.tags:
                self.tags.append(tag_obj)
        self.updated_at = datetime.now()

    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the note."""
        tag_obj = NoteTag(tag)
        if tag_obj in self.tags:
            self.tags.remove(tag_obj)
            self.updated_at = datetime.now()

    def link_to_contact(self, contact: str, address_book: AddressBook) -> None:
        """Link note to a contact."""
        _contact = address_book.find(contact)
        if _contact:
            self.contact = _contact
        else:
            raise NotFoundError("Contact not found")
        self.updated_at = datetime.now()

    def unlink_contact(self) -> None:
        """Remove contact link from note."""
        self.contact = None
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        contact_str = f" [{self.contact.name.value}]" if self.contact else ""
        tags_str = (
            f" #{' #'.join(str(tag.value) for tag in self.tags)}" if self.tags else ""
        )
        content_str = (
            str(self.content.value)[:50]
            if hasattr(self.content, "value")
            else str(self.content)[:50]
        )
        return f"Note{contact_str}: {content_str}...{tags_str}"

    def __repr__(self) -> str:
        content_str = (
            str(self.content.value)[:30]
            if hasattr(self.content, "value")
            else str(self.content)[:30]
        )
        return f"Note(id='{self.id}', content='{content_str}', contact='{self.contact}', tags='{self.tags}', created_at='{self.created_at}', updated_at='{self.updated_at}')"

    def __eq__(self, other) -> bool:
        """Compare notes by id."""
        if not isinstance(other, Note):
            return False
        return self.id == other.id
