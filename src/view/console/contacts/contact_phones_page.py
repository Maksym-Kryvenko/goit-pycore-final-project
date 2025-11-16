from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich.box import ROUNDED


def print_contacts_phones(console: Console, contacts, search: str = None):

    if not search:
        title = Panel("[bold cyan]Phones[/bold cyan]", border_style="cyan", box=ROUNDED)
    else:
        title = Panel(
            Align.left(f"[bold yellow]Phones for:[/bold yellow] {search}"),
            border_style="yellow",
            box=ROUNDED,
        )

    table = Table(title=title, show_lines=True)

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Phones", style="magenta")

    if not contacts:
        # Add a row indicating no data
        table.add_row(
            "[dim]No contacts found[/dim]",
            "[dim]-[/dim]",
        )
    else:
        for c in contacts:
            phones = _phones(c.phones)
            table.add_row(str(c.name), phones)

    console.print(table)


def _phones(phones: list) -> str:
    """Render a list of phone numbers."""
    if not phones:
        return ""
    return "\n".join([str(phone) for phone in phones])
