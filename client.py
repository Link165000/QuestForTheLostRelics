import socket
import threading
import json

class Client:
    def __init__(self, host='127.0.0.1', port=12345):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.current_location = (0, 0)
        self.game_map = [[{"type": "forest", "enemies": ["wolf", "goblin"]} for _ in range(10)] for _ in range(10)]
        self.quests = []
        self.inventory = {}

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                print(message)
            except ConnectionResetError:
                print("Disconnected from the server.")
                break

    def send_message(self, message):
        self.client.send(message.encode('utf-8'))

    def run(self):
        threading.Thread(target=self.receive_messages).start()
        while True:
            command = input("Enter a command (move, trade, quest, exit): ")
            if command == "move":
                self.move()
            elif command == "trade":
                self.trade()
            elif command == "quest":
                self.show_quests()
            elif command == "exit":
                self.client.close()
                break

    def move(self):
        direction = input("Enter direction (up, down, left, right): ")
        if direction == "up":
            self.current_location = (self.current_location[0] - 1, self.current_location[1])
        elif direction == "down":
            self.current_location = (self.current_location[0] + 1, self.current_location[1])
        elif direction == "left":
            self.current_location = (self.current_location[0], self.current_location[1] - 1)
        elif direction == "right":
            self.current_location = (self.current_location[0], self.current_location[1] + 1)

        print(f"Moved to: {self.current_location} - Terrain: {self.get_terrain_type(self.current_location)}")
        self.send_message(f"{self.current_location}")

    def trade(self):
        item = input("Enter item to trade: ")
        if item in self.inventory:
            print(f"Traded {item}.")
            del self.inventory[item]
        else:
            print("Item not found in inventory.")

    def show_quests(self):
        if self.quests:
            print("Your Quests:")
            for quest in self.quests:
                print(quest)
        else:
            print("You have no active quests.")

    def get_terrain_type(self, location):
        # Simulated terrain type for the sake of example
        if location[0] % 2 == 0:
            return "Mountain"
        else:
            return "Forest"

if __name__ == "__main__":
    client = Client()
    client.run()
