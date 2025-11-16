from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich.box import ROUNDED


def print_notes(console: Console, notes, search: str = None):

    if not search:
        title = Panel("[bold cyan]Notes[/bold cyan]", border_style="cyan", box=ROUNDED)
    else:
        title = Panel(
            Align.left(f"[bold yellow]Search results for:[/bold yellow] {search}"),
            border_style="yellow",
            box=ROUNDED,
        )

    table = Table(title=title, show_lines=True)

    table.add_column("Id", style="cyan", no_wrap=True)
    table.add_column("Content", style="green")
    table.add_column("Tags", style="magenta")
    table.add_column("Created At", style="blue")
    table.add_column("Updated At", style="blue")

    if not notes:
        # Add a row indicating no data
        table.add_row("[dim]No notes found[/dim]", "[dim]-[/dim]", "[dim]-[/dim]")
    else:
        for n in notes:
            tags = _tags(n.tags)
            table.add_row(
                str(n.id), str(n.content), tags, str(n.created_at), str(n.updated_at)
            )

    console.print(table)


def _tags(tags: list) -> str:
    """Render a list of tags."""
    if not tags:
        return ""
    return "\n".join([str(tag) for tag in tags])
