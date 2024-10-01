import socket
from map_generation import generate_map
from quests import Quest
from combat import Combat
from save_system import load_player_data

class Client:
    def __init__(self, host='127.0.0.1', port=12345):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.player_data = load_player_data()
        self.game_map = generate_map(10)  # Example size
        self.current_location = (0, 0)  # Starting position

    def run(self):
        print("Welcome to the Multiplayer RPG!")
        while True:
            self.display_status()
            command = input("Enter command: ")
            self.client.send(command.encode('utf-8'))
            self.handle_command(command)

    def display_status(self):
        print(f"Player: {self.player_data.get('name', 'Unknown')}")
        print(f"Location: {self.current_location}")
        print("Current Map:")
        for row in self.game_map:
            print(' '.join(row))

    def handle_command(self, command):
        if command.lower() == 'quit':
            print("Exiting the game.")
            self.client.close()
            exit()
        else:
            print(f"Executed command: {command}")

if __name__ == "__main__":
    client = Client()
    client.run()
