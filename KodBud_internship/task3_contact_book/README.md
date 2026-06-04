# Task 3 — Contact Book

A persistent CLI contact manager. Contacts (name, phone, email) are stored in a local `contacts.json` file so they survive between sessions. Displayed in a formatted `rich` table with colour-coded columns.

## How to Run

```bash
# 1. Install dependency
pip install rich

# 2. Run
python contact_book.py
```

## What It Does

- Add a contact with name, phone, and email
- View all contacts in a formatted table
- Search by name — case-insensitive, partial match
- Delete a contact by name
- All changes saved to `contacts.json` immediately
