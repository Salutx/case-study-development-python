import os
from app.models.user import User
from playhouse.shortcuts import model_to_dict

SESSION_FILE = "user_session.txt"

def save_session(user):
    with open(SESSION_FILE, "w") as file:
        file.write(str(user.id)) 

def get_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as file:
            return file.read().strip()
    return None

def get_user_details():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as file:
            user_id = file.read().strip()
            user = User.get_by_id(user_id)

            return model_to_dict(user)
    return None

def clear_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
