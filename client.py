import socket
import pygame
from map_generation import generate_map
from quests import Quest
from combat import Combat
from save_system import load_player_data

class Client:
    def __init__(self, host='127.0.0.1', port=12345):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.player_data = load_player_data()

    def run(self):
        while True:
            command = input("Enter command: ")
            self.client.send(command.encode('utf-8'))

if __name__ == "__main__":
    client = Client()
    client.run()
