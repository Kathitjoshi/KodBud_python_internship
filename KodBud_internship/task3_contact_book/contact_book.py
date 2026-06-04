import json, os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich import box

console = Console()
FILE = "contacts.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def contacts_table(contacts, title="All Contacts"):
    t = Table(title=title, box=box.ROUNDED, border_style="cyan",
              header_style="bold cyan", show_lines=True)
    t.add_column("#",     style="dim",         width=4)
    t.add_column("Name",  style="bold white",  width=20)
    t.add_column("Phone", style="green",        width=16)
    t.add_column("Email", style="yellow",       width=28)
    for i, c in enumerate(contacts, 1):
        t.add_row(str(i), c["name"], c.get("phone","—"), c.get("email","—"))
    return t

def add_contact(contacts):
    console.print(Panel("[bold]Add New Contact[/]", border_style="cyan", padding=(0,2)))
    name  = Prompt.ask("  Name").strip()
    if not name:
        console.print("  [red]Name required.[/]"); return
    phone = Prompt.ask("  Phone").strip()
    email = Prompt.ask("  Email").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save(contacts)
    console.print(f"  [green]Contact '[bold]{name}[/]' saved.[/]")

def view_contacts(contacts):
    if not contacts:
        console.print("  [yellow]No contacts yet.[/]"); return
    console.print(contacts_table(contacts))

def search_contact(contacts):
    q = Prompt.ask("  Search name").strip().lower()
    results = [c for c in contacts if q in c["name"].lower()]
    if not results:
        console.print("  [yellow]No matches found.[/]")
    else:
        console.print(contacts_table(results, title=f"Results for '{q}'"))

def delete_contact(contacts):
    q = Prompt.ask("  Name to delete").strip().lower()
    before = len(contacts)
    updated = [c for c in contacts if c["name"].lower() != q]
    if len(updated) == before:
        console.print("  [yellow]No contact with that name.[/]"); return
    contacts.clear(); contacts.extend(updated)
    save(contacts)
    console.print(f"  [green]Deleted '[bold]{q}[/]'.[/]")

def main():
    contacts = load()
    console.clear()
    console.print()
    console.print(Panel(
        Text("Contact Book", justify="center", style="bold white"),
        style="bold cyan", padding=(1,4),
        subtitle=f"[dim]{len(contacts)} contact(s) stored · Task 3[/]"
    ))

    menu = {
        "1": ("Add contact",      add_contact),
        "2": ("View all",         view_contacts),
        "3": ("Search by name",   search_contact),
        "4": ("Delete contact",   delete_contact),
    }

    while True:
        console.print()
        t = Table(box=box.SIMPLE, show_header=False, padding=(0,2))
        t.add_column("k", style="bold cyan", width=4)
        t.add_column("v", style="white")
        for k, (label, _) in menu.items():
            t.add_row(f"[{k}]", label)
        t.add_row("[5]", "Exit")
        console.print(t)

        choice = Prompt.ask("\n  [bold]Select[/]").strip()
        if choice == "5":
            console.print(Panel("[bold green]Goodbye![/]", border_style="green", padding=(0,4)))
            break
        elif choice in menu:
            console.print()
            menu[choice][1](contacts)
        else:
            console.print("  [red]Invalid choice.[/]")

if __name__ == "__main__":
    main()
