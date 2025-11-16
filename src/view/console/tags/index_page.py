from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich.box import ROUNDED


def print_tags(console: Console, tags, search: str = None):

    if not search:
        title = Panel("[bold cyan]Tags[/bold cyan]", border_style="cyan", box=ROUNDED)
    else:
        title = Panel(
            Align.left(f"[bold yellow]Search results for:[/bold yellow] {search}"),
            border_style="yellow",
            box=ROUNDED,
        )

    table = Table(title=title, show_lines=True)

    table.add_column("Name", style="cyan", no_wrap=True)

    if not tags:
        # Add a row indicating no data
        table.add_row(
            "[dim]No tags found[/dim]",
        )
    else:
        for t in tags:
            table.add_row(str(t.value))
    console.print(table)
