from rich.console import Console
from rich.panel import Panel

console = Console()

def display_feature_panel(feature_title: str):
    console.print(Panel.fit(f"[bold green]{feature_title}", border_style="red"))

def display_expanded_feature_panel(feature_title: str):
    console.print(Panel(f"[bold green]{feature_title}", border_style="red", expand=True, title_align="center"))