"""
Weather App — Task 7
A modern GUI weather application using Tkinter + OpenWeatherMap API.
Run: python weather_app.py
Requires: pip install requests
"""

import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import os
import threading
from datetime import datetime

API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

CONDITION_ICONS = {
    "Clear": "☀",  "Clouds": "☁", "Rain": "🌧",
    "Drizzle": "🌦","Thunderstorm": "⛈","Snow": "❄",
    "Mist": "🌫",  "Fog": "🌫",   "Haze": "🌫",
    "Smoke": "🌫", "Dust": "🌫",  "Tornado": "🌪",
}

BG         = "#0d1117"
CARD_BG    = "#161b22"
ACCENT     = "#58a6ff"
ACCENT2    = "#3fb950"
TEXT       = "#e6edf3"
TEXT_DIM   = "#8b949e"
BORDER     = "#30363d"
WARN       = "#f85149"
GOLD       = "#d29922"

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("520x720")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.api_key = API_KEY
        self._build_ui()

    def _build_ui(self):
        # ── Header ──────────────────────────────────────────────
        hdr = tk.Frame(self, bg=BG)
        hdr.pack(fill="x", padx=28, pady=(28,0))

        tk.Label(hdr, text="Weather", font=("Georgia", 26, "bold"),
                 bg=BG, fg=TEXT).pack(side="left")
        tk.Label(hdr, text=" · Live Forecast", font=("Georgia", 14),
                 bg=BG, fg=TEXT_DIM).pack(side="left", pady=(8,0))

        # ── API key row ─────────────────────────────────────────
        key_row = tk.Frame(self, bg=BG)
        key_row.pack(fill="x", padx=28, pady=(14,0))
        tk.Label(key_row, text="API Key", font=("Courier New", 10),
                 bg=BG, fg=TEXT_DIM).pack(side="left")
        self.key_var = tk.StringVar(value=self.api_key)
        key_entry = tk.Entry(key_row, textvariable=self.key_var,
                             font=("Courier New", 10), bg=CARD_BG, fg=TEXT,
                             insertbackground=TEXT, relief="flat",
                             show="●", width=32, bd=0)
        key_entry.pack(side="left", padx=(8,0), ipady=4)
        key_entry.bind("<FocusIn>",  lambda e: key_entry.config(show=""))
        key_entry.bind("<FocusOut>", lambda e: key_entry.config(show="●"))
        self._border_line(key_row, BORDER)

        # ── Search row ──────────────────────────────────────────
        search_row = tk.Frame(self, bg=BG)
        search_row.pack(fill="x", padx=28, pady=(18,0))

        self.city_var = tk.StringVar()
        entry = tk.Entry(search_row, textvariable=self.city_var,
                         font=("Georgia", 15), bg=CARD_BG, fg=TEXT,
                         insertbackground=ACCENT, relief="flat",
                         width=24, bd=0)
        entry.pack(side="left", ipady=10, padx=(0,0))
        entry.bind("<Return>", lambda e: self._fetch())
        entry.focus_set()

        btn = tk.Button(search_row, text="Search →",
                        font=("Georgia", 12, "bold"),
                        bg=ACCENT, fg="#0d1117",
                        activebackground="#79c0ff", activeforeground="#0d1117",
                        relief="flat", cursor="hand2", bd=0,
                        padx=14, pady=8,
                        command=self._fetch)
        btn.pack(side="left", padx=(10,0))

        self._divider(28)

        # ── Status / Loading ────────────────────────────────────
        self.status_var = tk.StringVar(value="Enter a city name and press Search.")
        tk.Label(self, textvariable=self.status_var,
                 font=("Courier New", 10), bg=BG, fg=TEXT_DIM).pack(padx=28, anchor="w")

        # ── Main weather card ───────────────────────────────────
        self.card = tk.Frame(self, bg=CARD_BG, bd=0, relief="flat")
        self.card.pack(fill="x", padx=28, pady=(10,0))
        self._build_card()

        # ── Stats grid ─────────────────────────────────────────
        self.grid_frame = tk.Frame(self, bg=BG)
        self.grid_frame.pack(fill="x", padx=28, pady=(14,0))
        self._build_stats_grid()

        # ── Footer ─────────────────────────────────────────────
        tk.Label(self, text="Powered by OpenWeatherMap  ·  Task 7",
                 font=("Courier New", 9), bg=BG, fg=BORDER).pack(side="bottom", pady=14)

    def _build_card(self):
        for w in self.card.winfo_children():
            w.destroy()

        top = tk.Frame(self.card, bg=CARD_BG)
        top.pack(fill="x", padx=20, pady=(20,0))

        self.icon_lbl  = tk.Label(top, text="—", font=("Segoe UI Emoji", 52),
                                   bg=CARD_BG, fg=TEXT)
        self.icon_lbl.pack(side="left")

        right = tk.Frame(top, bg=CARD_BG)
        right.pack(side="left", padx=(18,0))

        self.temp_lbl = tk.Label(right, text="—°C", font=("Georgia", 42, "bold"),
                                  bg=CARD_BG, fg=TEXT)
        self.temp_lbl.pack(anchor="w")

        self.city_lbl = tk.Label(right, text="—", font=("Georgia", 16),
                                  bg=CARD_BG, fg=ACCENT)
        self.city_lbl.pack(anchor="w")

        self.desc_lbl = tk.Label(right, text="—", font=("Georgia", 12),
                                  bg=CARD_BG, fg=TEXT_DIM)
        self.desc_lbl.pack(anchor="w")

        tk.Frame(self.card, bg=BORDER, height=1).pack(fill="x", padx=20, pady=(18,0))

        bot = tk.Frame(self.card, bg=CARD_BG)
        bot.pack(fill="x", padx=20, pady=(12,20))

        self.feels_lbl   = self._mini_label(bot, "Feels like", "—°C")
        self.alt_temp_lbl= self._mini_label(bot, "°F",         "—°F")
        self.humid_lbl   = self._mini_label(bot, "Humidity",   "—%")

    def _mini_label(self, parent, title, val):
        f = tk.Frame(parent, bg=CARD_BG)
        f.pack(side="left", padx=(0,24))
        tk.Label(f, text=title, font=("Courier New", 9), bg=CARD_BG, fg=TEXT_DIM).pack(anchor="w")
        lbl = tk.Label(f, text=val, font=("Georgia", 13, "bold"), bg=CARD_BG, fg=TEXT)
        lbl.pack(anchor="w")
        return lbl

    def _build_stats_grid(self):
        for w in self.grid_frame.winfo_children():
            w.destroy()

        self.stat_labels = {}
        stats = [
            ("🌬", "Wind",       "wind",       "— m/s"),
            ("👁", "Visibility", "visibility", "— km"),
            ("📊", "Pressure",   "pressure",   "— hPa"),
            ("🌅", "Sunrise",    "sunrise",    "—"),
            ("🌇", "Sunset",     "sunset",     "—"),
            ("☁",  "Cloud Cover","clouds",     "—%"),
        ]
        for col in range(3):
            self.grid_frame.columnconfigure(col, weight=1)

        for i, (ico, title, key, default) in enumerate(stats):
            row, col = divmod(i, 3)
            cell = tk.Frame(self.grid_frame, bg=CARD_BG, bd=0)
            cell.grid(row=row, column=col, padx=(0 if col==0 else 6), pady=(0,6), sticky="nsew")
            tk.Label(cell, text=f"{ico} {title}", font=("Courier New", 9),
                     bg=CARD_BG, fg=TEXT_DIM).pack(anchor="w", padx=12, pady=(10,0))
            lbl = tk.Label(cell, text=default, font=("Georgia", 13, "bold"),
                           bg=CARD_BG, fg=TEXT)
            lbl.pack(anchor="w", padx=12, pady=(2,10))
            self.stat_labels[key] = lbl

    def _border_line(self, parent, color):
        tk.Frame(parent, bg=color, height=1).pack(side="bottom", fill="x")

    def _divider(self, padx=0):
        tk.Frame(self, bg=BORDER, height=1).pack(fill="x", padx=padx, pady=(16,0))

    def _fetch(self):
        city = self.city_var.get().strip()
        if not city:
            self.status_var.set("Please enter a city name.")
            return
        key = self.key_var.get().strip()
        if not key:
            messagebox.showwarning("API Key Missing",
                                   "Enter your OpenWeatherMap API key above.")
            return
        self.status_var.set(f"Fetching weather for {city}...")
        threading.Thread(target=self._do_fetch, args=(city, key), daemon=True).start()

    def _do_fetch(self, city, key):
        try:
            r = requests.get(BASE_URL, params={"q": city, "appid": key}, timeout=10)
            if r.status_code == 401:
                self.after(0, self.status_var.set, 
                    "Invalid API key. Newly generated keys may take up to 2 hours to activate.")
                return
            if r.status_code == 404:
                self.after(0, self.status_var.set, f"City '{city}' not found.")
                return
            if r.status_code != 200:
                self.after(0, self.status_var.set, f"API error ({r.status_code}).")
                return
            data = r.json()
            self.after(0, self._update_ui, data)
        except requests.exceptions.ConnectionError:
            self.after(0, self.status_var.set, "No internet connection.")
        except Exception as ex:
            self.after(0, self.status_var.set, f"Error: {ex}")

    def _fmt_time(self, unix_ts, tz_offset):
        return datetime.utcfromtimestamp(unix_ts + tz_offset).strftime("%I:%M %p")

    def _k2c(self, k): return k - 273.15
    def _k2f(self, k): return (k - 273.15)*9/5 + 32

    def _update_ui(self, d):
        cond       = d["weather"][0]["main"]
        desc       = d["weather"][0]["description"].title()
        temp_c     = self._k2c(d["main"]["temp"])
        temp_f     = self._k2f(d["main"]["temp"])
        feels_c    = self._k2c(d["main"]["feels_like"])
        humidity   = d["main"]["humidity"]
        wind       = d["wind"]["speed"]
        pressure   = d["main"]["pressure"]
        visibility = d.get("visibility", 0) / 1000
        clouds     = d["clouds"]["all"]
        sunrise    = self._fmt_time(d["sys"]["sunrise"], d["timezone"])
        sunset     = self._fmt_time(d["sys"]["sunset"],  d["timezone"])
        icon       = CONDITION_ICONS.get(cond, "🌡")
        name       = f"{d['name']}, {d['sys']['country']}"

        self.icon_lbl.config(text=icon)
        self.temp_lbl.config(text=f"{temp_c:.1f}°C")
        self.city_lbl.config(text=name)
        self.desc_lbl.config(text=desc)
        self.feels_lbl.config(text=f"{feels_c:.1f}°C")
        self.alt_temp_lbl.config(text=f"{temp_f:.1f}°F")
        self.humid_lbl.config(text=f"{humidity}%")

        self.stat_labels["wind"].config(text=f"{wind} m/s")
        self.stat_labels["visibility"].config(text=f"{visibility:.1f} km")
        self.stat_labels["pressure"].config(text=f"{pressure} hPa")
        self.stat_labels["sunrise"].config(text=sunrise)
        self.stat_labels["sunset"].config(text=sunset)
        self.stat_labels["clouds"].config(text=f"{clouds}%")

        self.status_var.set(f"Last updated · {datetime.now().strftime('%I:%M %p')}")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()