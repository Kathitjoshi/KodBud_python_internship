# Task 5 — Password Strength Checker

Evaluates a password against four security criteria and rates it Strong, Moderate, or Weak. Results shown in a formatted table with PASS/FAIL per criterion and a visual score bar.

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run
python password_checker.py
```

## Criteria

| Check | Requirement |
|---|---|
| Length | Minimum 8 characters |
| Uppercase | At least one uppercase letter |
| Digit | At least one numeric digit |
| Special character | At least one symbol (`!@#$%^&*` etc.) |

## Ratings

- **Strong** — all 4 criteria met ✅
- **Moderate** — 2 or 3 criteria met ⚠️
- **Weak** — fewer than 2 criteria met ❌

Uses Python's `re` module for pattern matching. Loop continues so you can test multiple passwords in one session.

## Features

- Rich CLI with colored tables and progress bars
- Accurate criterion counting (only counts passing checks)
- Reliable password input using standard `input()`
- Type `quit`, `q`, or `exit` to exit the loop
