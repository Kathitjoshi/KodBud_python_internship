# KodBud Python Internship

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow?style=flat-square)
![Rich](https://img.shields.io/badge/CLI-Rich-blueviolet?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-2ea44f?style=flat-square)
![Tasks](https://img.shields.io/badge/Tasks-8%2F8-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

Eight Python projects completed as part of the KodBud Python Programming Internship. Every task is a standalone, runnable program. Tasks 1–6 are CLI tools styled with the `rich` library for clean terminal output. Tasks 7 and 8 are full desktop GUI applications built with Tkinter — the two showcase projects.

---

## Table of Contents

1. [Simple Calculator](#1-simple-calculator)
2. [Number Guessing Game](#2-number-guessing-game)
3. [Contact Book](#3-contact-book)
4. [Bulk File Renamer](#4-bulk-file-renamer)
5. [Password Strength Checker](#5-password-strength-checker)
6. [YouTube Video Downloader](#6-youtube-video-downloader)
7. [Weather App — GUI](#7-weather-app--gui)
8. [Arlo Chatbot — GUI](#8-arlo-chatbot--gui)
9. [Requirements Summary](#requirements-summary)
10. [Repository Structure](#repository-structure)

---

## 1. Simple Calculator

**Folder:** `task1_calculator/`

A command-line calculator for addition, subtraction, multiplication, and division. The program runs in a continuous loop — pick an operation, enter two numbers, get the result. Built with the `rich` library for formatted terminal output including bordered result panels and a clean operations table. Input validation rejects non-numeric entries without crashing, and division by zero is caught explicitly.

**Core concepts:** `if-elif-else`, functions, `try/except`, `float()` casting, `rich` panels and tables.

**Run:**
```bash
cd task1_calculator
pip install rich
python calculator.py
```

---

## 2. Number Guessing Game

**Folder:** `task2_number_guessing_game/`

The program picks a secret random integer between 1 and 100. The player guesses until correct, receiving "Too high" or "Too low" hints after each attempt. A key detail: the display narrows the active range after every guess, so the player can see exactly where the number must be. Attempts are counted and displayed on win. After each round the player can play again, with a running best-score tracker across multiple games.

**Core concepts:** `random` module, `while` loop, attempt counter, `rich` progress visual, conditional hints.

**Run:**
```bash
cd task2_number_guessing_game
pip install rich
python guessing_game.py
```

---

## 3. Contact Book

**Folder:** `task3_contact_book/`

A persistent CLI contact manager. Each contact stores a name, phone number, and email. Contacts are saved to `contacts.json` using Python's `json` module so they survive between sessions. The interface displays contacts in a formatted `rich` table with colour-coded columns. Search is case-insensitive and partial-match, so typing "kath" finds "Kathit". Deleting a contact removes it from the JSON file immediately.

**Core concepts:** lists of dictionaries, `json` module for file I/O, `os.path`, CRUD logic, `rich` Table.

**Run:**
```bash
cd task3_contact_book
pip install rich
python contact_book.py
```

---

## 4. Bulk File Renamer

**Folder:** `task4_file_renamer/`

Renames all files in a given folder to a sequential pattern — `file_1.txt`, `file_2.txt`, and so on. The user provides a folder path and an optional prefix. Before any renaming happens, the script shows a full preview table of old name → new name so the user can verify before confirming. A `rich` progress bar tracks the renaming as it happens. Files are sorted before numbering to ensure a deterministic ordering. Original extensions are preserved.

**Core concepts:** `os` module, `os.listdir()`, `os.rename()`, `os.path.splitext()`, automation scripting, `rich` progress bar.

**Run:**
```bash
cd task4_file_renamer
pip install rich
python file_renamer.py
```

---

## 5. Password Strength Checker

**Folder:** `task5_password_checker/`

Evaluates a password against four security criteria: minimum eight characters, at least one uppercase letter, at least one digit, and at least one special character. Results are displayed in a formatted table showing PASS or FAIL per criterion. A filled block bar visualises the overall score, and the password is rated Strong, Moderate, or Weak based on how many checks pass. The loop continues so multiple passwords can be tested in one session.

**Core concepts:** `re` (regular expressions) module, string validation, multi-criteria scoring, `rich` Table and styled output.

**Run:**
```bash
cd task5_password_checker
pip install rich
python password_checker.py
```

---

## 6. YouTube Video Downloader

**Folder:** `task6_youtube_downloader/`

Downloads a YouTube video at its highest available resolution. After the URL is entered, the script fetches and displays the video's title, author, duration, and view count before starting the download. A live progress bar shows download speed, bytes transferred, and estimated time remaining. The destination folder is created automatically if it does not exist. Invalid URLs and unavailable videos are caught with specific error messages rather than a generic crash.

**Core concepts:** `pytube` library, `os.makedirs()`, exception handling, `rich` progress bar with `DownloadColumn` and `TransferSpeedColumn`.

**Run:**
```bash
cd task6_youtube_downloader
pip install pytube rich
python downloader.py
```

---

## 7. Weather App — GUI

**Folder:** `task7_weather_app/`

A full desktop weather application built with Tkinter and the OpenWeatherMap API. This is one of the two showcase projects.

![OpenWeatherMap](https://img.shields.io/badge/API-OpenWeatherMap-orange?style=flat-square)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow?style=flat-square)
![Requests](https://img.shields.io/badge/Library-requests-blue?style=flat-square)

The application opens a dark-themed 520×720 window. The user enters their API key once (it can also be pre-set as an environment variable), then searches any city by name. Results load without freezing the UI because the API call runs on a background thread. The weather card displays the condition icon, temperature in both Celsius and Fahrenheit, feels-like temperature, and humidity. A six-cell stats grid below shows wind speed, visibility, atmospheric pressure, cloud cover, and sunrise/sunset times adjusted to the city's local timezone.

**What it shows:**

| Field | Detail |
|---|---|
| Temperature | °C and °F side by side |
| Feels Like | Apparent temperature in °C |
| Humidity | Relative humidity % |
| Wind Speed | m/s |
| Visibility | km |
| Pressure | hPa |
| Cloud Cover | % |
| Sunrise / Sunset | Local city time |

**Setup:**
```bash
# 1. Install dependency
pip install requests

# 2. Get a free API key at openweathermap.org/api
# 3. Optional: set it as an env variable
export OPENWEATHER_API_KEY=your_key_here

# 4. Run
cd task7_weather_app
python weather_app.py
```

On Ubuntu/Debian, Tkinter may need to be installed separately:
```bash
sudo apt-get install python3-tk
```

---

## 8. Arlo Chatbot — GUI

**Folder:** `task8_chatbot/`

A desktop chatbot named Arlo, built with Tkinter and Python's standard library only. No internet, no API, no ML model — just regex pattern matching and a clean chat interface. This is the second showcase project.

The window renders a scrollable chat canvas with user messages on the right (green bubbles) and Arlo's replies on the left (blue bubbles), each timestamped. Sending a message is as simple as pressing Enter. Arlo responds with a short delay to make the exchange feel natural. The pattern matching covers about a dozen intent categories with randomised responses per category to reduce repetition.

**Topics Arlo handles:**

| Intent | Example Input |
|---|---|
| Greetings | "Hello", "Hey", "Hi" |
| Farewells | "Bye", "Goodbye", "See you" |
| Time / Date | "What time is it?", "What day is today?" |
| Jokes | "Tell me a joke", "Make me laugh" |
| Identity | "What's your name?", "Who are you?" |
| Capabilities | "What can you do?", "Help" |
| Python | "Tell me about Python", "I like coding" |
| Mood check | "How are you?" |
| Emotional cues | "I'm sad", "I'm bored" |
| Compliments | "You're awesome" |
| Weather (redirect) | "What's the weather?" |

**Run:**
```bash
cd task8_chatbot
python chatbot.py
```

On Ubuntu/Debian:
```bash
sudo apt-get install python3-tk
python chatbot.py
```

No `pip install` needed — Tkinter is part of Python's standard library.

---

## Requirements Summary

| Task | External Packages |
|---|---|
| 1–5 | `rich` |
| 6 | `pytube`, `rich` |
| 7 | `requests` (+ system `python3-tk` on Linux) |
| 8 | None (`tkinter` is stdlib) |

Python 3.8 or higher recommended for all tasks.

---

## Repository Structure

```
KodBud_python_internship/
├── README.md
├── task1_calculator/
│   ├── calculator.py
│   ├── requirements.txt
│   └── README.md
├── task2_number_guessing_game/
│   ├── guessing_game.py
│   ├── requirements.txt
│   └── README.md
├── task3_contact_book/
│   ├── contact_book.py
│   ├── requirements.txt
│   └── README.md
├── task4_file_renamer/
│   ├── file_renamer.py
│   ├── requirements.txt
│   └── README.md
├── task5_password_checker/
│   ├── password_checker.py
│   ├── requirements.txt
│   └── README.md
├── task6_youtube_downloader/
│   ├── downloader.py
│   ├── requirements.txt
│   └── README.md
├── task7_weather_app/
│   ├── weather_app.py
│   ├── requirements.txt
│   └── README.md
└── task8_chatbot/
    ├── chatbot.py
    └── README.md
    ├── requirements.txt
```

---

## About

Completed as part of the KodBud Python Programming Internship. Each task is a working, runnable program — not a toy snippet. The goal was to apply core Python concepts to real problems and ship something that actually runs.
