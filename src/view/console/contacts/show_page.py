from rich.console import Console
from rich.panel import Panel
from src.models import Contact


def print_contact_card(console: Console, contact: Contact):
    lines = [
        f"[bold]Emails:[/bold] {_emails(contact.emails)}",
        f"[bold]Phones:[/bold] {_phones(contact.phones)}",
        f"[bold]Addresses:[/bold] {str(contact.address)}",
        f"[bold]Birthday:[/bold] {str(contact.birthday)}",
    ]
    text = "\n".join(lines)

    console.print(Panel(text, title=f"Contact: {contact.name}", border_style="cyan"))


def _phones(phones: list) -> str:
    """Render a list of phone numbers."""
    if not phones:
        return ""
    return ", ".join([str(phone) for phone in phones])


def _emails(emails: list) -> str:
    """Render a list of email addresses."""
    if not emails:
        return ""
    return ", ".join([str(email) for email in emails])
