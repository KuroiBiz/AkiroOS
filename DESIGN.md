# AkiroOS — Design Overview

AkiroOS is a **simulated operating system** built in Python.  
It focuses on learning core OS concepts such as user sessions, system services, and modular apps — without interacting with real hardware.

This document explains **how the system is structured**, what each file does, and how components interact.

---

## 🧠 System Architecture (High-Level)

AkiroOS is composed of three main layers:

1. **Entry & Control Layer** — boot process and UI loop  
2. **Application Layer** — system apps (WiFi, info, help)  
3. **Authentication Layer** — user management and security  

All components communicate through **direct function calls**, keeping the system simple and readable.

---

## 📁 File Structure & Responsibilities

### `main.py` — System Entry Point
Responsible for:
- Displaying the boot screen
- Handling login/signup flow
- Starting the desktop environment
- Managing the main event loop

How it works:
- Initializes the system UI
- Authenticates the user via `auth.py`
- Launches the desktop menu
- Routes user input to system apps

This file acts as the **kernel-like controller** of AkiroOS. :contentReference[oaicite:0]{index=0}

---

### `auth.py` — Authentication & User Management
Responsible for:
- User signup and login
- Secure password hashing
- Storing user credentials locally

How it works:
- Uses `bcrypt` to hash passwords
- Stores users in a local JSON database (`users.json`)
- Prevents duplicate usernames
- Verifies credentials during login

This module simulates a **user authentication subsystem** found in real operating systems. :contentReference[oaicite:1]{index=1}

---

### `app.py` — System Applications
Responsible for:
- Core system utilities (apps)
- Displaying system information
- Simulating WiFi state
- Providing help documentation

Included apps:
- **WiFi App**: toggles simulated WiFi state
- **System Info App**: shows OS, host, architecture, and runtime data
- **Help App**: explains basic system usage

This file represents **userland system services**. :contentReference[oaicite:2]{index=2}

---

## 🔐 Data Storage

### `users.json`
- Stores user credentials locally
- Passwords are **hashed**, never stored in plain text
- File is created automatically if missing

This design avoids server dependency and keeps the system self-contained.

---

## ⚙️ Design Principles

- **Simulation-first**: No real hardware access
- **Modular**: Each file has a clear role
- **Readable**: Prioritizes clarity over complexity
- **Honest**: Clearly labeled simulated components
- **Educational**: Built for learning OS concepts

---

## 🚧 Current Limitations

- No real multitasking or process scheduling
- No persistent system state beyond users
- No real networking or hardware interaction

These limitations are intentional and align with AkiroOS’s learning-focused goals.

---

## 🚀 Future Directions

- Process & scheduler simulation
- Uptime tracking
- Virtual filesystem
- Configurable system services
- Plugin-based apps

---

*AkiroOS is an educational project designed to explore operating system concepts in a controlled and accessible way.*
