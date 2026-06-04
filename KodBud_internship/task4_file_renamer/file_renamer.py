import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import track
from rich.text import Text
from rich import box

console = Console()

def rename_files(folder, prefix):
    if not os.path.isdir(folder):
        console.print(f"  [red]'{folder}' is not a valid directory.[/]"); return

    files = sorted(f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)))
    if not files:
        console.print("  [yellow]No files found in that folder.[/]"); return

    console.print(f"\n  Found [bold cyan]{len(files)}[/] file(s). Previewing rename:\n")
    t = Table(box=box.ROUNDED, border_style="blue", header_style="bold cyan", show_lines=True)
    t.add_column("Original",    style="dim white",   width=30)
    t.add_column("→ New Name",  style="bold green",  width=30)
    renames = []
    for i, fname in enumerate(files, 1):
        ext = os.path.splitext(fname)[1]
        new = f"{prefix}_{i}{ext}"
        t.add_row(fname, new)
        renames.append((fname, new))
    console.print(t)

    confirm = Prompt.ask("\n  Proceed with rename? [bold](yes/no)[/]").strip().lower()
    if confirm not in ("yes", "y"):
        console.print("  [yellow]Cancelled.[/]"); return

    for fname, new in track(renames, description="  Renaming..."):
        old_path = os.path.join(folder, fname)
        new_path = os.path.join(folder, new)
        if old_path != new_path:
            os.rename(old_path, new_path)

    console.print(Panel(
        f"[bold green]Done![/] {len(renames)} file(s) renamed with prefix '[cyan]{prefix}[/]'.",
        border_style="green", padding=(0,4)
    ))

def main():
    console.clear()
    console.print()
    console.print(Panel(
        Text("Bulk File Renamer", justify="center", style="bold white"),
        style="bold blue", padding=(1,4),
        subtitle="[dim]Python CLI · Task 4[/]"
    ))
    folder = Prompt.ask("\n  Folder path").strip()
    prefix = Prompt.ask("  File prefix [dim](default: file)[/]").strip() or "file"
    rename_files(folder, prefix)

if __name__ == "__main__":
    main()
