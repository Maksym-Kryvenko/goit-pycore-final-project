from rich.console import Console
from rich.panel import Panel
from src.models import Note

def print_note_card(console: Console, note: Note):
    lines = [
        f"[bold]Content:[/bold] {_content(note.content)}",
        f"[bold]Tags:[/bold] {_tags(note.tags)}",
    ]
    text = "\n".join(lines)

    console.print(Panel(text, title=f"Note: {note.id}", border_style="cyan"))



def _content(content: str) -> str:
    """Render the content of the note."""
    if not content:
        return ""
    return str(content)


def _tags(tags: list) -> str:
    """Render a list of tags."""
    if not tags:
        return ""
    return ", ".join([str(tag) for tag in tags])
