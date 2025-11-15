from src.models.fields import NoteTag


def render_tag(tag: NoteTag) -> str:
    """Render a single tag."""
    return f"#{tag.value}"


def render_tags(tags: list) -> str:
    """Render a list of tags."""
    if not tags:
        return "No tags"
    return ", ".join([render_tag(tag) for tag in tags])
