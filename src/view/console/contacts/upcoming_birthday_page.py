from rich.box import ROUNDED
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

def print_upcoming_birthdays(console: Console, data: list[dict]):
    title = Panel(
        "[bold cyan]Upcoming Birthdays[/bold cyan]",
        border_style="cyan",
        box=ROUNDED
    )
    table = Table(title=title, show_lines=True)

    table.add_column("Name", style="red", no_wrap=True)
    table.add_column("Email", style="blue")
    table.add_column("Phone", style="red", no_wrap=True)
    table.add_column("Address", style="blue")
    table.add_column("Birthday", style="red", no_wrap=True)
    table.add_column("Congratulation Date", style="red", no_wrap=True)

    if not data:
        table.add_row(
            "[dim]No contacts found[/dim]",
            "[dim]-[/dim]",
            "[dim]-[/dim]",
            "[dim]-[/dim]",
            "[dim]-[/dim]",
            "[dim]-[/dim]"
        )
    else:
        for item in data:
            contact = item.get('contact')
            emails = _emails(contact.emails)
            phones = _phones(contact.phones)
            addresse = str(contact.address)
            birthday = str(contact.birthday)
            congratulation_date = str(item.get('congratulation_date').strftime('%d.%m.%Y'))
            table.add_row(str(contact.name), emails, phones, addresse, birthday, congratulation_date)

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
