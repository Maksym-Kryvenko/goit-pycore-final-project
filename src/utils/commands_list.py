from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED


def print_help():
    console = Console()
    
    commands={
        "Commands for contacts:": "",
        " ------------------ ": "",
        "hello": "Greet the user",
        "?/help": "Show all commands",
        "close/exit": "Exit the application",
        "add": "Add a contact with phone number",
        "change": "Modify a contact number",
        "phone": "Show the contsct's phones numbers",
        "all": "Show all contacts",
        "add-birthday": "Add/change contact's birthday",
        "show-birthday": "Show a contact's birthday",
        "birthdays": "Sow upcoming birthdays",
        "search": "Search for a contact",
        "del": "Delete a contact",
        "":"",
        "Commands for notes:": "",
        " ------------------": "",
        "add_note": "Add a note",
        "edit_note": "Edit a note",
        "search_notes": "Search for a note",
        "all_notes": "Show all notes",
        "del_note": "Delete a note",
        "add_tag": "Add a tag for a note",
        "remove_tag": "Remove a note's tag"
    }

    # Create table
    table = Table(title="[bold green]List of commands[/bold green]", box=ROUNDED, show_header=True)

    # Add columns
    table.add_column("Command", style="bold cyan")
    table.add_column("Description", style="green")

    # Add rows
    for command, description in commands.items():
        table.add_row(command, description)
    
    console.print("\nWelcome to yuor Personal Assistant!\n", style="green")
    console.print(table)
