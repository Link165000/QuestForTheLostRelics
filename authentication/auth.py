import json
import hashlib
import os

#made this to safely encrypt passwords using hashlib and fopr user registry, it will save the passwrods and user detailks then the player can login and retrieve their passwords

user_data_file = os.path.join(os.path.dirname(__file__), 'user_data.json')


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    user_data = load_user_data()

    if username in user_data:
        print("Username already exists.")
        return False
    
    
    user_data[username] = {
        "password": hash_password(password),
        "stats": {},  
        "progress": {}  
    }

    save_user_data(user_data)
    print("User registered successfully.")
    return True


def login_user(username, password):
    user_data = load_user_data()

    if username not in user_data:
        print("User not found.")
        return False
    
    hashed_password = hash_password(password)
    if user_data[username]["password"] == hashed_password:
        print("Login successful!")
        return True
    else:
        print("Incorrect password.")
        return False


def load_user_data():
    if not os.path.exists(user_data_file):
        return {}

    with open(user_data_file, 'r') as file:
        return json.load(file)


def save_user_data(data):
    with open(user_data_file, 'w') as file:
        json.dump(data, file, indent=4)
