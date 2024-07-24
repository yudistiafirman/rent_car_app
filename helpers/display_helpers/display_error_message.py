from rich.console import Console
from rich.panel import Panel

console = Console()

def display_error_message(message: str):
    console.print(Panel.fit(f"[bold red]❌ {message}", border_style="red"))