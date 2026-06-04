from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from rich import box
import sys

console = Console()

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return None, "Division by zero"
    return a / b, None

def get_number(label):
    while True:
        raw = Prompt.ask(f"  [bold cyan]{label}[/]")
        try:
            return float(raw)
        except ValueError:
            console.print("  [red]Invalid number. Try again.[/]")

def main():
    console.clear()
    console.print()
    console.print(Panel(
        Text("Simple Calculator", justify="center", style="bold white"),
        style="bold blue",
        padding=(1, 4),
        subtitle="[dim]Python CLI · Task 1[/]"
    ))

    ops = {
        "1": ("Addition",       "+", add),
        "2": ("Subtraction",    "−", subtract),
        "3": ("Multiplication", "×", multiply),
        "4": ("Division",       "÷", divide),
    }

    while True:
        console.print()
        table = Table(box=box.ROUNDED, show_header=False, border_style="blue", padding=(0,2))
        table.add_column("Key",  style="bold cyan",  width=4)
        table.add_column("Op",   style="white",       width=18)
        for k, (name, sym, _) in ops.items():
            table.add_row(f"[{k}]", f"{name}  {sym}")
        table.add_row("[5]", "Exit")
        console.print(table)

        choice = Prompt.ask("\n  [bold]Select[/]").strip()

        if choice == "5":
            console.print(Panel("[bold green]Goodbye![/]", border_style="green", padding=(0,4)))
            break

        if choice not in ops:
            console.print("  [red]Invalid choice.[/]")
            continue

        name, sym, func = ops[choice]
        a = get_number("First number")
        b = get_number("Second number")
        result, err = func(a, b) if choice == "4" else (func(a, b), None)

        if err:
            console.print(Panel(f"[bold red]Error:[/] {err}", border_style="red", padding=(0,2)))
        else:
            expr = f"{a:g}  {sym}  {b:g}  =  [bold green]{result:g}[/]"
            console.print(Panel(expr, title=f"[dim]{name}[/]", border_style="green", padding=(0,4)))

if __name__ == "__main__":
    main()
