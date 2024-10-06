from authentication.auth import register_user, login_user

# Example login flow
def main():
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

if __name__ == "__main__":
    main()
