# Task 7 — Weather App (GUI)

A desktop weather application built with Tkinter and the OpenWeatherMap API. Dark-themed GUI window — search any city and get a full real-time weather breakdown instantly.

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# On Ubuntu/Debian, also install Tkinter if not present:
# sudo apt-get install python3-tk
# (Tkinter ships with Python on Windows and macOS — no extra step needed)

# 2. Get a free API key at https://openweathermap.org/api
#    Sign up, go to API Keys section, copy your key.
#    ⚠️ NOTE: Newly generated API keys can take up to 2 hours to activate.

# 3. (Optional) Set your key as an environment variable to pre-fill it:
#    Linux / macOS:
export OPENWEATHER_API_KEY=your_key_here
#    Windows (PowerShell):
$env:OPENWEATHER_API_KEY="your_key_here"
#    Windows (CMD):
set OPENWEATHER_API_KEY=your_key_here

# 4. Run
python weather_app.py
```

If you skip step 3, just paste your API key into the key field inside the app.

## What It Shows

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

## Features

- Dark-themed Tkinter GUI — runs as a standalone desktop window
- API calls run on a background thread so the window never freezes
- API key field masked by default, visible on focus for security
- Condition icons (☀️ sun, ☁️ clouds, 🌧️ rain, ❄️ snow, ⛈️ storm, 🌫️ fog, etc.)
- Press Enter or click Search to fetch weather
- Helpful error messages for invalid cities, bad API keys, new keys still activating, and no internet
- Uses requests library for reliable HTTP calls

## Troubleshooting

**"Invalid API key" error?**
- New API keys take **up to 2 hours** to activate after creation — wait and retry
- Double-check you copied the key correctly (watch for extra spaces)
- Verify the key is marked "Active" on the OpenWeatherMap dashboard
