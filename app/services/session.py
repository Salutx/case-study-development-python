import os

SESSION_FILE = "user_session.txt"

def save_session(user):
    with open(SESSION_FILE, "w") as file:
        file.write(str(user.id)) 

def get_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as file:
            return file.read().strip()
    return None

def clear_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
