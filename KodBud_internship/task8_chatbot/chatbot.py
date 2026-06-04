"""
Arlo Chatbot — Task 8
A modern GUI chatbot using Tkinter.
Run: python chatbot.py
No external dependencies.
"""

import tkinter as tk
from tkinter import scrolledtext
import random
import re
import threading
from datetime import datetime
import time

BOT_NAME = "Arlo"

BG       = "#0f0f13"
SIDE_BG  = "#16161e"
MSG_BG   = "#1e1e2a"
BOT_BG   = "#1a2a3a"
USER_BG  = "#1a3a2a"
ACCENT   = "#7dcfff"
ACCENT2  = "#9ece6a"
TEXT     = "#c0caf5"
TEXT_DIM = "#565f89"
BORDER   = "#2a2a3a"
GOLD     = "#e0af68"
PINK     = "#f7768e"

RESPONSES = {
    "greeting": [
        "Hey! Good to have you here.",
        "Hi there — what's on your mind?",
        "Hello! Ask me anything.",
    ],
    "farewell": [
        "Goodbye! Take care.",
        "See you later!",
        "Bye! Come back anytime.",
    ],
    "how_are_you": [
        "Running smoothly. How about you?",
        "All good! What can I help with?",
        "Great, thanks for asking.",
    ],
    "name": [
        f"I'm {BOT_NAME}, a rule-based chatbot built in Python.",
        f"My name is {BOT_NAME}. Nice to meet you!",
    ],
    "capabilities": [
        "I can tell jokes, share the time, answer general questions, and keep you company.",
        "Ask me for a joke, the current time, or anything else — I'll do my best.",
    ],
    "joke": [
        "Why do programmers prefer dark mode?\nBecause light attracts bugs. 🐛",
        "A SQL query walks into a bar, walks up to two tables and asks:\n'Can I join you?'",
        "Why do Java devs wear glasses?\nBecause they don't C#. 👓",
        "I told my computer I needed a break.\nNow it won't stop sending me Kit-Kat ads.",
        "Why was the developer unhappy at work?\nThey wanted arrays.",
    ],
    "thanks": ["You're welcome!", "Happy to help!", "Anytime! 😊"],
    "weather": ["I don't have live weather, but check out Task 7 in this repo — it does!"],
    "python": [
        "Python is great — readable, versatile, and perfect for everything from scripting to ML.",
        "Python was created by Guido van Rossum, first released in 1991. A timeless choice.",
    ],
    "bored": ["Want a joke? Just type 'joke'. 😄", "Tell me something! Or ask for a joke."],
    "sad":   ["Sorry to hear that. A joke might help — just say 'joke'.", "I'm here if you want to talk."],
    "compliment": ["Thank you! That's kind of you. 😊", "Aw, you're making me blush (virtually)."],
    "age":   ["I was born the moment this script ran — so pretty fresh!"],
    "default": [
        "Hmm, I'm not sure about that. Try asking for a joke or the time?",
        "I didn't quite catch that. Could you rephrase?",
        "That's a bit beyond me. Ask me something else!",
    ],
}

PATTERNS = [
    (r"\b(hi|hello|hey|howdy|hiya|greetings|sup|what'?s up)\b", "greeting"),
    (r"\b(how are you|how('?re| are) you doing|are you okay)\b", "how_are_you"),
    (r"\b(what('?s| is) your name|who are you|your name)\b",    "name"),
    (r"\b(help|what can you do|capabilities|options)\b",         "capabilities"),
    (r"\b(joke|tell me a joke|make me laugh|funny)\b",           "joke"),
    (r"\b(thanks|thank you|ty|thx|cheers|appreciate)\b",         "thanks"),
    (r"\b(weather|forecast|temperature|rain|sunny)\b",           "weather"),
    (r"\b(how old|your age|when were you born)\b",               "age"),
    (r"\b(python|coding|programming|code)\b",                    "python"),
    (r"\b(bored|boring|nothing to do)\b",                        "bored"),
    (r"\b(sad|upset|unhappy|down|not okay)\b",                   "sad"),
    (r"\b(you('?re| are) (great|amazing|cool|awesome|nice))\b",  "compliment"),
]

FAREWELL_WORDS = {"bye","goodbye","exit","quit","farewell","see you","cya","later"}

def get_response(text):
    lower = text.lower().strip()
    if re.search(r"\b(time|date|day|what time|what day)\b", lower):
        return f"It's {datetime.now().strftime('%A, %B %d at %I:%M %p')}."
    for pattern, key in PATTERNS:
        if re.search(pattern, lower):
            return random.choice(RESPONSES[key])
    return random.choice(RESPONSES["default"])


class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{BOT_NAME} — CLI Chatbot")
        self.geometry("560x760")
        self.resizable(False, False)
        self.configure(bg=BG)
        self._build()
        self._after_delay(600, lambda: self._add_bot("Hey! I'm Arlo, your Python-powered chatbot.\n\nAsk me anything — jokes, time, Python trivia, or just chat. 💬"))

    def _build(self):
        # ── Header bar ─────────────────────────────────────────
        hdr = tk.Frame(self, bg=SIDE_BG, height=64)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)

        dot = tk.Canvas(hdr, width=12, height=12, bg=SIDE_BG, highlightthickness=0)
        dot.pack(side="left", padx=(20,8), pady=26)
        dot.create_oval(1,1,11,11, fill=ACCENT2, outline="")

        tk.Label(hdr, text=f"{BOT_NAME}", font=("Georgia", 16, "bold"),
                 bg=SIDE_BG, fg=TEXT).pack(side="left")
        tk.Label(hdr, text=" · rule-based chatbot", font=("Georgia", 11),
                 bg=SIDE_BG, fg=TEXT_DIM).pack(side="left", pady=(4,0))

        tk.Label(hdr, text="Task 8 · Python Internship",
                 font=("Courier New", 9), bg=SIDE_BG, fg=TEXT_DIM).pack(side="right", padx=20)

        tk.Frame(self, bg=BORDER, height=1).pack(fill="x")

        # ── Chat scroll area ────────────────────────────────────
        self.chat_frame = tk.Frame(self, bg=BG)
        self.chat_frame.pack(fill="both", expand=True, padx=0, pady=0)

        self.canvas = tk.Canvas(self.chat_frame, bg=BG, highlightthickness=0, bd=0)
        self.scrollbar = tk.Scrollbar(self.chat_frame, orient="vertical",
                                       command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.inner = tk.Frame(self.canvas, bg=BG)
        self.canvas_window = self.canvas.create_window((0,0), window=self.inner, anchor="nw")

        self.inner.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(-1*(e.delta//120), "units"))

        # ── Input bar ───────────────────────────────────────────
        tk.Frame(self, bg=BORDER, height=1).pack(fill="x")
        input_row = tk.Frame(self, bg=SIDE_BG, height=70)
        input_row.pack(fill="x", side="bottom")
        input_row.pack_propagate(False)

        self.input_var = tk.StringVar()
        self.entry = tk.Entry(input_row, textvariable=self.input_var,
                              font=("Georgia", 13), bg=MSG_BG, fg=TEXT,
                              insertbackground=ACCENT, relief="flat", bd=0)
        self.entry.pack(side="left", fill="both", expand=True,
                        padx=(20,10), pady=18, ipady=4)
        self.entry.bind("<Return>", lambda e: self._send())
        self.entry.focus_set()

        send_btn = tk.Button(input_row, text="Send",
                             font=("Georgia", 12, "bold"),
                             bg=ACCENT, fg=BG,
                             activebackground="#a8d8ff", activeforeground=BG,
                             relief="flat", cursor="hand2", bd=0,
                             padx=18, pady=8,
                             command=self._send)
        send_btn.pack(side="right", padx=(0,20), pady=18)

    def _on_frame_configure(self, e):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, e):
        self.canvas.itemconfig(self.canvas_window, width=e.width)

    def _add_message(self, text, is_user):
        row = tk.Frame(self.inner, bg=BG)
        row.pack(fill="x", padx=16, pady=(6,2), anchor="e" if is_user else "w")

        if is_user:
            name_lbl = tk.Label(row, text="You", font=("Courier New", 9),
                                 bg=BG, fg=ACCENT2)
            name_lbl.pack(side="top", anchor="e", padx=4)
            bubble = tk.Frame(row, bg=USER_BG, bd=0)
            bubble.pack(side="right")
        else:
            name_lbl = tk.Label(row, text=BOT_NAME, font=("Courier New", 9),
                                 bg=BG, fg=ACCENT)
            name_lbl.pack(side="top", anchor="w", padx=4)
            bubble = tk.Frame(row, bg=BOT_BG, bd=0)
            bubble.pack(side="left")

        msg_lbl = tk.Label(bubble, text=text,
                           font=("Georgia", 12),
                           bg=USER_BG if is_user else BOT_BG,
                           fg=TEXT,
                           wraplength=360,
                           justify="left",
                           padx=14, pady=10)
        msg_lbl.pack()

        ts = tk.Label(row, text=datetime.now().strftime("%I:%M %p"),
                      font=("Courier New", 8), bg=BG, fg=TEXT_DIM)
        ts.pack(side="top", anchor="e" if is_user else "w", padx=4)

        self.after(50, self._scroll_bottom)

    def _add_bot(self, text):
        self._add_message(text, is_user=False)

    def _add_user(self, text):
        self._add_message(text, is_user=True)

    def _scroll_bottom(self):
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def _send(self):
        text = self.input_var.get().strip()
        if not text:
            return
        self.input_var.set("")
        self._add_user(text)

        if any(w in text.lower() for w in FAREWELL_WORDS):
            self.after(400, lambda: self._add_bot(random.choice(RESPONSES["farewell"])))
            return

        self.after(350, lambda t=text: self._respond(t))

    def _respond(self, text):
        response = get_response(text)
        self._add_bot(response)

    def _after_delay(self, ms, fn):
        self.after(ms, fn)


if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
