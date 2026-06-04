import re
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

CHECKS = [
    ("length",    "Minimum 8 characters",        lambda p: len(p) >= 8),
    ("uppercase", "At least one uppercase letter",lambda p: bool(re.search(r"[A-Z]", p))),
    ("digit",     "At least one digit",           lambda p: bool(re.search(r"[0-9]", p))),
    ("special",   "At least one special character",lambda p: bool(re.search(r"[!@#$%^&*()\-_=+\[\]{}|;:,.<>?/~`]", p))),
]

def evaluate(password):
    return [(label, desc, fn(password)) for label, desc, fn in CHECKS]

def strength_label(passed):
    if passed == 4: return "Strong",  "green"
    if passed >= 2: return "Moderate","yellow"
    return "Weak", "red"

def display_result(password):
    results = evaluate(password)
    passed  = sum(1 for _, _, ok in results if ok)
    label, color = strength_label(passed)

    t = Table(box=box.ROUNDED, border_style=color, header_style=f"bold {color}", show_lines=True)
    t.add_column("Check",       style="white",  width=30)
    t.add_column("Status",      style="bold",   width=8, justify="center")
    for _, desc, ok in results:
        t.add_row(desc, f"[green]PASS[/]" if ok else f"[red]FAIL[/]")

    bar_filled = "█" * passed
    bar_empty  = "░" * (4 - passed)
    bar = f"[{color}]{bar_filled}[/][dim]{bar_empty}[/]"

    console.print()
    console.print(t)
    console.print(Panel(
        f"Strength: [{color}][bold]{label}[/][/]   {bar}   {passed}/4 checks passed",
        border_style=color, padding=(0,4)
    ))

def main():
    console.clear()
    console.print()
    console.print(Panel(
        Text("Password Strength Checker", justify="center", style="bold white"),
        style="bold magenta", padding=(1,4),
        subtitle="[dim]Python CLI · Task 5[/]"
    ))

    while True:
        console.print()
        pw = input("  Enter password (or 'quit'): ")
        if pw.lower() in ("quit", "q", "exit"):
            console.print(Panel("[bold]Exiting.[/]", border_style="dim", padding=(0,4)))
            break
        display_result(pw)

if __name__ == "__main__":
    main()