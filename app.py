# app.py
from datetime import datetime
import platform
import os
from rich.panel import Panel
from rich.console import Console

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

    system_name = "AkiroOS"
    version = "0.2-beta"
    kernel = "Akiro Kernel (Simulated)"
    shell = "AkiroShell • Stable (Not Real yet...)"
    arch = platform.machine()
    host_os = platform.system()
    python_version = platform.python_version()
    pid = os.getpid()

    console.print(
        Panel(
            f"""
[bold cyan]{system_name}[/bold cyan]
Version: {version}

User: {user}
Process ID: {pid}

Time: {now}

Kernel: {kernel}
Shell: {shell}
Architecture: {arch}

Host OS: {host_os}
Python: {python_version}
""".strip(),
            title="System Information",
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
