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
        "quit/exit": "Exit the application",  # COMPLETE
        "add": "Add a contact with phone number or email",  # COMPLETE
        "change": "Modify a contact number or email",  # COMPLETE
        "phone": "Show the contact's phones numbers",  # COMPLETE
        "all": "Show all contacts",  # COMPLETE
        "add-birthday": "Add/change contact's birthday",  # COMPLETE
        "show-birthday": "Show a contact's birthday",  # COMPLETE
        "birthdays": "Sow upcoming birthdays",  # COMPLETE
        "search": "Search for a contact",  # DO WE NEED THIS?
        "add-address": "Add or edit contact's address",  # COMPLETE
        "rename": "Rename existing contact",  # WIP
        "delete": "Delete a contact",  # COMPLETE
        "": "",
        "Commands for notes:": "",
        " ------------------": "",
        "add-note": "Add a note",  # WIP
        "edit-note": "Edit a note",  # WIP
        "delete-note": "Delete a note",  # WIP
        "search-notes": "Search for a note",  # WIP
        "all-notes": "Show all notes",  # WIP
        "add-tag": "Add a tag for a note",  # WIP
        "remove-tag": "Remove a note's tag",  # WIP
        "get-tags": "Get all unique tags",  # WIP
        "link-contact": "Link note to a contact",  # WIP
        "unlink-contact": "Unlink note from a contact",  # WIP
        "sort-created": "Sort notes by created date",  # WIP
        "sort-updated": "Sort notes by updated date",  # WIP
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
