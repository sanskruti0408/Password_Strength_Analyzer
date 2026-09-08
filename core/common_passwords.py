from pathlib import Path
PASSWORD_FILE = Path(__file__).resolve().parent.parent / "data" / "common_passwords.txt"

def load_common_passwords():
    with open(PASSWORD_FILE, "r", encoding="utf-8", errors="ignore") as file:
        passwords = {line.strip() for line in file if line.strip()}

    return passwords

COMMON_PASSWORDS = load_common_passwords()

def is_common_password(password):
    return password in COMMON_PASSWORDS

