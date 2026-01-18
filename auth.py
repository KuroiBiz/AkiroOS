# auth.py
import json
import os

try:
    import bcrypt
except ImportError:
    print("bcrypt is not installed.")
    print("Run: python -m pip install bcrypt")
    exit()

DB = "users.json"


def _load():
    if not os.path.exists(DB):
        return {"users": []}
    with open(DB, "r") as f:
        return json.load(f)


def _save(data):
    with open(DB, "w") as f:
        json.dump(data, f, indent=2)


def signup():
    db = _load()
    username = input("Create username: ")
    password = input("Create password: ").encode()

    for u in db["users"]:
        if u["username"] == username:
            print("Username already exists.")
            return None

    hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode()
    db["users"].append({
        "username": username,
        "password": hashed
    })
    _save(db)
    return username


def login():
    db = _load()
    username = input("Username: ")
    password = input("Password: ").encode()

    for u in db["users"]:
        if u["username"] == username:
            if bcrypt.checkpw(password, u["password"].encode()):
                return username

    return None
