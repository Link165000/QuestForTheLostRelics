import socket
import threading

# Display the received map from server
def display_map(map_data):
    print("\n" + "-" * 22)
    print(map_data)
    print("-" * 22)

# Function to receive map data from server
def receive_map(client_socket):
    while True:
        try:
            map_data = client_socket.recv(1024).decode()
            display_map(map_data)
        except ConnectionResetError:
            print("Connection to the server was lost.")
            break

# Main client function
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.100.2.113', 12345))

    # Get player name
    player_name = input("Enter your player name: ")
    client_socket.sendall(player_name.encode())

    # Start receiving map updates
    threading.Thread(target=receive_map, args=(client_socket,)).start()

    # Send movement commands
    while True:
        move = input("Move (W=up, A=left, S=down, D=right): ").upper()
        if move in ['W', 'A', 'S', 'D']:
            client_socket.sendall(move.encode())
        else:
            print("Invalid move. Please use W, A, S, or D.")

client()
