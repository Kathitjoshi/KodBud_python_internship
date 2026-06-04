import random
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich import box

console = Console()

def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    low, high = 1, 100

    console.print(Panel(
        "[bold white]I've picked a number between [cyan]1[/] and [cyan]100[/].\nCan you guess it?[/]",
        style="bold magenta", padding=(1,4),
        subtitle="[dim]Hint: watch the range narrow[/]"
    ))

    while True:
        console.print(f"\n  Range: [cyan]{low}[/] — [cyan]{high}[/]")
        raw = Prompt.ask("  [bold]Your guess[/]")
        try:
            guess = int(raw)
        except ValueError:
            console.print("  [red]Please enter a whole number.[/]")
            continue

        if guess < 1 or guess > 100:
            console.print("  [yellow]Out of range (1–100).[/]")
            continue

        attempts += 1

        if guess < secret:
            low = max(low, guess + 1)
            console.print(f"  [yellow]Too low![/]  Try higher.")
        elif guess > secret:
            high = min(high, guess - 1)
            console.print(f"  [yellow]Too high![/]  Try lower.")
        else:
            stars = "★" * min(attempts, 10)
            msg = (
                f"[bold green]Correct![/] The number was [bold cyan]{secret}[/].\n"
                f"You got it in [bold]{attempts}[/] attempt{'s' if attempts != 1 else ''}.\n"
                f"[yellow]{stars}[/]"
            )
            console.print(Panel(msg, border_style="green", padding=(1,4)))
            return attempts

def main():
    console.clear()
    console.print()
    console.print(Panel(
        Text("Number Guessing Game", justify="center", style="bold white"),
        style="bold magenta", padding=(1,4),
        subtitle="[dim]Python CLI · Task 2[/]"
    ))

    scores = []
    while True:
        console.print()
        a = play_game()
        scores.append(a)
        if len(scores) > 1:
            console.print(f"  [dim]Best so far: {min(scores)} attempts[/]")
        if not Confirm.ask("\n  Play again?"):
            console.print(Panel("[bold]Thanks for playing![/]", border_style="magenta", padding=(0,4)))
            break

if __name__ == "__main__":
    main()
