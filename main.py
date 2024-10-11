#main code file, import any other function from file here
# e.g. from Town import blacksmith or something
#if tryna import from another folder do as i did down belolw
#                  || 
#                  \/


from authentication.auth import register_user, login_user
from game.movement_client import display_map, receive_map, client

def login():
    print("Welcome to Quest for the Lost Relics!")
    
    action = input("Do you want to (1) Register or (2) Login? ")
    try:
        if action == '1':
           username = input("Enter a new username: ")
           password = input("Enter a password: ")
           register_user(username, password)
        elif action == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login_user(username, password):
              print(f"Welcome back, {username}!")
            else:
               print("Login failed.")
    except ValueError:
        print("must be a number between 1 or 2") 

def start_game():
    print("Starting the game...")
    # Add game initialization logic here
    display_map()
    receive_map()
    client()

def main():
    login()
    start_game()



if __name__ == "__main__":
    main()

