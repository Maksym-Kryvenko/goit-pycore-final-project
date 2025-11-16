from prompt_toolkit.application import get_app
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.styles import Style
from src.config import COMMANDS

style = Style.from_dict(
    {
        "prompt": "fg:#00ffcc bold",
        "bottom-toolbar": "fg:#666666 italic",
    }
)


def dynamic_bottom_toolbar() -> AnyFormattedText:
    app = get_app()
    buf = app.current_buffer
    text = buf.document.text_before_cursor.strip()
    parts = text.split()

    # Default hint
    hint = "Type a command, e.g. 'help' or 'add <name> <phone>'"

    if parts:
        cmd = parts[0].lower()
        if cmd in COMMANDS.keys():
            hint = f"Type '{COMMANDS[cmd]['example']}'"

    return f" {hint}"
