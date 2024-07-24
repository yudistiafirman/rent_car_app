from rich.console import Console
from rich.panel import Panel

console = Console()

def display_success_message(message: str): 
    console.print(Panel.fit(f"[bold green]✅ {message}", border_style="green"))