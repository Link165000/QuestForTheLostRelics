import socket
import threading
import game_map
import combat
import quests

class GameClient:
    def __init__(self, host, port):
        self.server_address = (host, port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)

        self.player_data = {}
        self.map = game_map.GameMap()

        # Start listening to the server
        threading.Thread(target=self.listen_to_server, daemon=True).start()

    def listen_to_server(self):
        while True:
            data = self.client_socket.recv(1024).decode()
            self.handle_server_data(data)

    def handle_server_data(self, data):
        # Handle incoming data from the server
        pass

    def send_data(self, data):
        self.client_socket.sendall(data.encode())

    def move_player(self, direction):
        self.player_data['direction'] = direction
        self.send_data(f'MOVE {direction}')

    def combat_action(self, enemy):
        action = combat.choose_action()
        self.send_data(f'COMBAT {action} {enemy}')

    def quest_action(self, quest):
        quests.accept_quest(quest)

if __name__ == "__main__":
    client = GameClient("localhost", 12345)
