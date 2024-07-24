from rich.console import Console

console = Console()

def print_error(error_message: str):
    console.print(f"[bold red]{error_message}[/bold red]")