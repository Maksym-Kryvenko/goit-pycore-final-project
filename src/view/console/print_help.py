from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED
from src.config import GENERAL_COMMANDS, CONTACT_COMMANDS, NOTE_COMMANDS


def print_help(console: Console, title: str = "List of commands"):
    # Create table
    table = Table(
        title=f"[bold green]{title}[/bold green]", box=ROUNDED, show_header=True
    )

    # Add columns
    table.add_column("Command", style="bold cyan")
    table.add_column("Description", style="green")
    table.add_column("Example")

    for section_title, section_commands in [
        ("General Commands", GENERAL_COMMANDS),
        ("Contact Commands", CONTACT_COMMANDS),
        ("Note Commands", NOTE_COMMANDS),
    ]:
        table.add_section()
        table.add_row(f"[b yellow]{section_title}[/b yellow]", "", "")
        for command, settings in section_commands.items():
            table.add_row(
                f"  {command}",
                settings.get("description"),
                f"[bold][bash]{settings.get('example')}[/bash][/bold]",
            )
    console.print("\nWelcome to yuor Personal Assistant!\n", style="green")
    console.print(table)
