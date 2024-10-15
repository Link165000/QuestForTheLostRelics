#main code file, import any other function from file here
# e.g. from Town import blacksmith or something
#if tryna import from another folder do as i did down belolw
#                  || 
#                  \/
import time
import sys
from authentication.auth import register_user, login_user
from game.movement_client import display_map, receive_map, client, map_data


# def loading_animation():
#     print("Starting game", end="", flush=True)  # Print without newline
#     # Loop for the animation
#     for _ in range(3):  # Repeat the dot animation 3 times
#         for dots in range(1, 4):  # Show 1 to 3 dots
#             print("." * dots, end="", flush=True)  # Print dots without newline
#             time.sleep(0.5)  # Pause for half a second
#             print("\rStarting game", end="", flush=True)  # Clear dots and print "Starting game" again
#     print("Starting game...") 

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
    # loading_animation()
    # Add game initialization logic here
    display_map(map_data)
    receive_map()
    client()

def main():
    login()
    start_game()



if __name__ == "__main__":
    main()

