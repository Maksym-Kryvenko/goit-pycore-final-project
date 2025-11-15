
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich.box import ROUNDED

def print_contacts_birthdays(console: Console, contacts, search: str = None):

    if not search:
        title = Panel(
            "[bold cyan]Birthdays[/bold cyan]",
            border_style="cyan",
            box=ROUNDED
        )
    else:
        title = Panel(
            Align.left(f"[bold yellow]Birthdays for:[/bold yellow] {search}"),
            border_style="yellow",
            box=ROUNDED
        )

    table = Table(title=title, show_lines=True)

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Birthday", style="magenta")

    if not contacts:
        # Add a row indicating no data
        table.add_row(
            "[dim]No contacts found[/dim]",
            "[dim]-[/dim]",
        )
    else:
        for c in contacts:
            birthday = _birthday(c.birthday)
            table.add_row(str(c.name), birthday)

    console.print(table)



def _birthday(birthday: str) -> str:
    """Render a list of phone numbers."""
    if not birthday:
        return ""
    return str(birthday)

