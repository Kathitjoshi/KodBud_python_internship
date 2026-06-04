import os
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

try:
    from yt_dlp import YoutubeDL
except ImportError:
    console.print("[red]yt-dlp not installed. Run: pip install yt-dlp[/]")
    exit(1)

def download(url, dest):
    try:
        console.print(f"\n  Connecting to YouTube...")
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(dest, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            t = Table(box=box.ROUNDED, border_style="red", header_style="bold red", show_lines=True)
            t.add_column("Field",  style="dim white",  width=12)
            t.add_column("Value",  style="bold white",  width=42)
            t.add_row("Title",    info.get('title', 'Unknown'))
            t.add_row("Author",   info.get('uploader', 'Unknown'))
            t.add_row("Duration", f"{info.get('duration', 0) // 60}m {info.get('duration', 0) % 60}s")
            t.add_row("Views",    f"{info.get('view_count', 0):,}")
            console.print(t)

            filesize = info.get('filesize') or info.get('filesize_approx', 0)
            if filesize:
                console.print(f"\n  Format: [bold cyan]{info.get('format', 'Unknown')}[/]")
                console.print(f"  Size: [bold cyan]{filesize / (1024*1024):.1f} MB[/]\n")
            else:
                console.print(f"\n  Format: [bold cyan]{info.get('format', 'Unknown')}[/]\n")

            console.print("  [bold red]Downloading...[/]")
            ydl.download([url])

        console.print(Panel(
            f"[bold green]Download complete![/]\nSaved to: [cyan]{dest}[/]",
            border_style="green", padding=(1,4)
        ))

    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg or "unavailable" in error_msg.lower():
            console.print("  [red]This video is unavailable or age-restricted.[/]")
        elif "invalid" in error_msg.lower() or "http" in error_msg.lower():
            console.print("  [red]Invalid YouTube URL or connection error.[/]")
        else:
            console.print(f"  [red]Error: {error_msg}[/]")

def main():
    console.clear()
    console.print()
    console.print(Panel(
        Text("YouTube Video Downloader", justify="center", style="bold white"),
        style="bold red", padding=(1,4),
        subtitle="[dim]Powered by yt-dlp · Task 6[/]"
    ))

    url  = Prompt.ask("\n  YouTube URL").strip()
    dest = Prompt.ask("  Save to folder [dim](default: current dir)[/]").strip() or "."

    if not os.path.isdir(dest):
        os.makedirs(dest)
        console.print(f"  [dim]Created folder: {dest}[/]")

    download(url, dest)

if __name__ == "__main__":
    main()
