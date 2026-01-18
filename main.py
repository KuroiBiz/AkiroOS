# main.py
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import time
import auth, app

console = Console()

def boot(user):
    console.clear()
    console.print(
        Panel(
            Align.center("Starting AkiroOS…", vertical="middle"),
            style="green",
            height=5
        )
    )
    time.sleep(1)

    console.print("Loading services…", style="dim")
    time.sleep(1)

    desktop(user)

def desktop(user):
    while True:
        console.print()
        console.print(
            Panel(
                "1. WiFi\n2. System Info\n3. Help\n4. Shutdown",
                title=f"AkiroOS — {user}",
                subtitle="Select an option",
                style="blue"
            )
        )
        console.print("[bold cyan]>[/bold cyan] ", end="")
        choice = input()

        if choice == "1":
            app.wifi()
        elif choice == "2":
            app.info(user)
        elif choice == "3":
            app.help()
        elif choice == "4":
            console.print("System halted.", style="red")
            exit()
        else:
            console.print("Invalid option.", style="yellow")

# =====================
# ENTRY POINT
# =====================

console.clear()
console.print(
    Panel(
        Align.center("AkiroOS", vertical="middle"),
        subtitle="minimal • quiet • intentional",
        style="bold cyan",
        height=7
    )
)

console.print("1. Login")
console.print("2. Signup")
console.print("[bold cyan]>[/bold cyan] ", end="")
choice = input()

user = None
if choice == "1":
    user = auth.login()
elif choice == "2":
    user = auth.signup()

if user:
    boot(user)
else:
    console.print("Access denied. System halted.", style="red")
