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
    else:
        print("Invalid option. Exiting.")


def main():
    login()
    # display_map()
    # receive_map()
    # client()



if __name__ == "__main__":
    main()

