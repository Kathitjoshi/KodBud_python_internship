# Task 8 — Arlo Chatbot (GUI)

A rule-based desktop chatbot named Arlo, built with Tkinter and Python's standard library only. No API, no ML, no internet required. The whole thing runs offline.

## How to Run

```bash
# No pip installs needed — only standard library used.

# On Ubuntu/Debian, install Tkinter if not present:
# sudo apt-get install python3-tk
# Tkinter ships with Python on Windows and macOS — no extra step needed.

# Run
python chatbot.py
```

## What Arlo Can Do

| Topic | Example Input |
|---|---|
| Greetings | "Hello", "Hey", "Hi there" |
| Farewells | "Bye", "See you", "Quit" |
| Time & Date | "What time is it?", "What day is today?" |
| Jokes | "Tell me a joke", "Make me laugh" |
| Identity | "What's your name?", "Who are you?" |
| Capabilities | "What can you do?", "Help" |
| Python | "Tell me about Python" |
| Mood | "How are you?" |
| Emotional | "I'm sad", "I'm bored" |
| Compliments | "You're awesome" |
| Weather redirect | "What's the weather?" |

## How It Works

User input is matched against a set of regular expressions, each mapped to a response category. Responses within each category are randomised so repeated inputs don't give the same reply. Time and date queries are handled separately using `datetime` for a live response. Farewell words exit cleanly.

The GUI is a scrollable canvas with colour-coded message bubbles — green for the user, blue for Arlo — each with a timestamp. Press Enter to send.
