import datetime
import textwrap
from src.models import Contact


def render_contacts(contacts: list,) -> str:
    """Render a list of contacts."""
    if not contacts:
        return "No contacts"
    return "\n--------------------------------\n".join([render_contact(contact) for contact in contacts])


def render_contact(contact: Contact) -> str:
    """Render a single contact as a formatted string."""
    return textwrap.dedent(
        f"""
        name: {str(contact.name)};
        phones: {render_phones(contact.phones)};
        email: {render_emails(contact.emails)};
        address: {str(contact.address) or "No address"};
        birthday: {str(contact.birthday) or "No birthday"};
    """).strip()


def render_contacts_phones(contacts: list) -> str:
    """Render a list of contacts with phones."""
    if not contacts:
        return "No contacts"
    return "\n--------------------------------\n".join([render_contact_phones(contact) for contact in contacts])

def render_contact_phones(contact: Contact) -> str:
    """Render a single contact with phones."""
    return f"{contact.name}'s phones: {render_phones(contact.phones)}"

def render_phones(phones: list) -> str:
    """Render a list of phone numbers."""
    if not phones:
        return "No phones"
    return ", ".join([str(phone) for phone in phones])


def render_emails(emails: list) -> str:
    """Render a list of email addresses."""
    if not emails:
        return "No emails"
    return ", ".join([str(email) for email in emails])

def render_upcoming_birthdays(data: list) -> str:
    """Render a list of upcoming birthdays."""
    if not data:
        return "No upcoming birthdays"
    result = [render_upcoming_birthday(item["contact"], item["congratulation_date"]) for item in data ]
    return "\n".join(result)

def render_upcoming_birthday(contact: Contact, congratulation_date: datetime.date) -> str:
        return f"{contact.name} - has birthday on {contact.birthday}, don't forget to congratulate on {congratulation_date}"
