# Task 2 — Number Guessing Game

The program picks a secret random number between 1 and 100. Guess until you get it right. After each wrong guess you get a Too High or Too Low hint, and the display narrows the active range so you can see exactly where the number must be.

## How to Run

```bash
# 1. Install dependency
pip install rich

# 2. Run
python guessing_game.py
```

## What It Does

- Random number generated using the `random` module
- Hints narrow the visible range after every guess
- Attempt counter shown on win
- Best score tracked across multiple rounds in a session
- Replay option after each game
