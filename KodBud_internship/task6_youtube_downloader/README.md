
## **Task 6: README.md**
```markdown
# Task 6 — YouTube Video Downloader

Downloads a YouTube video at its highest available resolution. Displays video info before downloading and shows real-time download status.

**Note:** Uses `yt-dlp` (actively maintained) instead of pytube — YouTube changed their API in 2024-2025, making pytube unreliable. yt-dlp works consistently with current YouTube.

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run
python downloader.py
```

When prompted:
- Paste the YouTube video URL
- Enter a destination folder path (or press Enter for the current directory)

## What It Does

- Fetches and displays title, author, duration, and view count before downloading
- Selects highest resolution stream automatically
- Shows download format and file size
- Creates destination folder if it does not exist
- Handles invalid URLs and unavailable videos with clear error messages
- Powered by yt-dlp — reliable and actively updated

## Requirements

- Python 3.7+
- yt-dlp (actively maintained YouTube downloader)
- rich (for formatting)
