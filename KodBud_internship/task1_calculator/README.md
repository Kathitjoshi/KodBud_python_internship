# Task 1 — Simple Calculator

A command-line calculator for addition, subtraction, multiplication, and division. Runs in a loop until you choose to exit. Built with the `rich` library for clean terminal output — bordered panels, colour-coded results, formatted menus.

## How to Run

```bash
# 1. Install dependency
pip install rich

# 2. Run
python calculator.py
```

## What It Does

- Pick an operation from a formatted menu
- Enter two numbers
- Result is displayed in a styled panel
- Division by zero is caught and reported cleanly
- Invalid input is rejected without crashing
- Loop continues until you select Exit
