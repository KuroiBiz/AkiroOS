# app.py
from rich.console import Console
from rich.panel import Panel
from datetime import datetime

console = Console()
_wifi = False

def wifi():
    global _wifi
    console.print(Panel("WiFi Service", style="cyan"))
    console.print("1. Enable\n2. Disable\n3. Status")

    c = input("> ")
    if c == "1":
        _wifi = True
    elif c == "2":
        _wifi = False

    state = "CONNECTED" if _wifi else "DISCONNECTED"
    console.print(f"WiFi: {state}", style="green" if _wifi else "red")

def info(user):
    now = datetime.now().strftime("%H:%M • %d %b %Y")
    console.print(
        Panel(
            f"AkiroOS\nUser: {user}\nTime: {now}\nShell: Stable",
            title="System",
            style="magenta"
        )
    )

def help():
    console.print(
        Panel(
            "• Type numbers to navigate\n• No commands needed\n• System cleans itself",
            title="Help",
            style="yellow"
        )
    )
