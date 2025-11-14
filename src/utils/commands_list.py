from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED


def print_help():
    console = Console()

    commands = {
        "Commands for contacts:": "",
        " ------------------ ": "",
        "hello": "Greet the user",  # COMPLETE
        "?/help": "Show all commands",  # COMPLETE
        "close/exit": "Exit the application",  # COMPLETE
        "add": "Add a contact with phone number or email",  # COMPLETE
        "change": "Modify a contact number or email",  # COMPLETE
        "phone": "Show the contact's phones numbers",  # COMPLETE
        "all": "Show all contacts",  # COMPLETE
        "add-birthday": "Add/change contact's birthday",  # COMPLETE
        "show-birthday": "Show a contact's birthday",  # COMPLETE
        "birthdays": "Sow upcoming birthdays",  # COMPLETE
        "search": "Search for a contact",  # COMPLETE
        "add-address": "Add or edit contact's address",  # COMPLETE
        "rename": "Rename existing contact",  # WIP
        "del": "Delete a contact",  # COMPLETE
        "": "",
        "Commands for notes:": "",
        " ------------------": "",
        "add_note": "Add a note",  # WIP
        "edit_note": "Edit a note",  # WIP
        "delete_note": "Delete a note",  # WIP
        "search_notes": "Search for a note",  # WIP
        "all_notes": "Show all notes",  # WIP
        "add_tag": "Add a tag for a note",  # WIP
        "remove_tag": "Remove a note's tag",  # WIP
        "get_tags": "Get all unique tags",  # WIP
        "link_contact": "Link note to a contact",  # WIP
        "unlink_contact": "Unlink note from a contact",  # WIP
        "sort_created": "Sort notes by created date",  # WIP
        "sort_updated": "Sort notes by updated date",  # WIP
    }

    # Create table
    table = Table(
        title="[bold green]List of commands[/bold green]", box=ROUNDED, show_header=True
    )

    # Add columns
    table.add_column("Command", style="bold cyan")
    table.add_column("Description", style="green")

    # Add rows
    for command, description in commands.items():
        table.add_row(command, description)

    console.print("\nWelcome to yuor Personal Assistant!\n", style="green")
    console.print(table)
