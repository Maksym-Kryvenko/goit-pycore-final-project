from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich.box import ROUNDED


def print_contacts(console: Console, contacts, search: str = None):

    # title = "Address Book" if not search else Align.left("Search results for: " + search)
    if not search:
        title = Panel(
            "[bold cyan]Address Book[/bold cyan]", border_style="cyan", box=ROUNDED
        )
    else:
        title = Panel(
            Align.left(f"[bold yellow]Search results for:[/bold yellow] {search}"),
            border_style="yellow",
            box=ROUNDED,
        )

    table = Table(title=title, show_lines=True)

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Emails", style="green")
    table.add_column("Phones", style="magenta")
    table.add_column("Address", style="yellow")
    table.add_column("Birthday", style="purple")

    if not contacts:
        # Add a row indicating no data
        table.add_row(
            "[dim]No contacts found[/dim]",
            "[dim]-[/dim]",
            "[dim]-[/dim]",
            "[dim]-[/dim]",
            "[dim]-[/dim]",
        )
    else:
        for c in contacts:
            emails = _emails(c.emails)
            phones = _phones(c.phones)
            addresse = str(c.address)
            birthday = str(c.birthday)
            table.add_row(str(c.name), emails, phones, addresse, birthday)

    console.print(table)


def _phones(phones: list) -> str:
    """Render a list of phone numbers."""
    if not phones:
        return ""
    return "\n".join([str(phone) for phone in phones])


def _emails(emails: list) -> str:
    """Render a list of email addresses."""
    if not emails:
        return ""
    return "\n".join([str(email) for email in emails])
