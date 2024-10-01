import socket
import threading
import json
from quests import Quest
from combat import Combat
from save_system import save_player_data, load_player_data, save_game_state, load_game_state

class Server:
    def __init__(self, host='127.0.0.1', port=12345):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.clients = []
        self.player_data = load_player_data()
        self.game_state = load_game_state()

    def start(self):
        self.server.listen()
        print("Server started. Waiting for connections...")
        while True:
            client_socket, addr = self.server.accept()
            self.clients.append(client_socket)
            print(f"Connection from {addr} established.")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    self.handle_message(message, client_socket)
            except ConnectionResetError:
                break

    def handle_message(self, message, client_socket):
        print(f"Message from client: {message}")

        # Handle specific commands (e.g., combat, quests)

    def save_game(self):
        save_player_data(self.player_data)
        save_game_state(self.game_state)

if __name__ == "__main__":
    server = Server()
    server.start()
