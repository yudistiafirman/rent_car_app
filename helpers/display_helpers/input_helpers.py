from rich.prompt import Prompt
from helpers.display_helpers.print_error_helpers import print_error
from typing import Callable

def get_valid_input(prompt_message: str, validation_function: Callable[[str], str]) -> str:
    while True:
        user_input = Prompt.ask(f"[bold yellow]{prompt_message}[/bold yellow]")
        error = validation_function(user_input)
        if error:
            print_error(error)
        else:
            return user_input