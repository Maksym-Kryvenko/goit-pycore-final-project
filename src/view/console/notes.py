import textwrap
from src.models import Note
from src.view.console.tags import render_tags


def render_note(note: Note) -> str:
    """Render a single note as a formatted string."""
    return textwrap.dedent(f"""
        note id: {note.id};
        note content: {note.content};
        note tags: {render_tags(note.tags)};
        contact: {note.contact.name if note.contact else 'No contact'}
    """).strip()


def render_notes(notes: list) -> str:
    """Render a list of notes."""
    if not notes:
        return "No notes"
    return "\n--------------------------------\n".join([render_note(note) for note in notes])

