# Task 4 — Bulk File Renamer

Renames all files in a folder to a sequential pattern like `file_1.txt`, `file_2.txt`, etc. Shows a full preview table before doing anything so you can confirm before the rename happens.

## How to Run

```bash
# 1. Install dependency
pip install rich

# 2. Run
python file_renamer.py
```

When prompted:
- Enter the full path to the folder containing your files
- Enter a prefix (or press Enter to use the default: `file`)
- Review the preview table, then confirm to proceed

## What It Does

- Sorts files before numbering for deterministic order
- Preserves original file extensions
- Shows old name → new name preview before renaming
- Progress bar tracks the rename as it runs
- Skips files that already match the target name
