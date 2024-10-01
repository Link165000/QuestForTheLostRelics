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
            command = input("Enter command (move, quest, combat, quit): ")
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
        elif command.lower() == 'combat':
            self.handle_combat()
        elif command.lower() == 'quest':
            self.handle_quests()
        elif command.lower() == 'move':
            self.move_character()
        else:
            print(f"Unknown command: {command}")

    def handle_combat(self):
        # For demonstration, we'll simulate combat against a dummy enemy
        enemy = {'name': 'Goblin', 'health': 50, 'element': 'Earth'}
        combat = Combat(self.player_data, enemy)

        while enemy['health'] > 0:
            action = input("Choose action (attack, combo, run): ")
            if action.lower() == 'attack':
                combat.attack()
            elif action.lower() == 'combo':
                combat.combo_attack()
            elif action.lower() == 'run':
                print("You ran away!")
                break
            else:
                print("Invalid action. Try again.")

    def handle_quests(self):
        print("Available Quests:")
        # Display quests (Placeholder for quest logic)
        print("1. Slay 5 Goblins - Reward: 50 XP")
        print("2. Collect 10 Herbs - Reward: 30 XP")

    def move_character(self):
        direction = input("Enter direction to move (up, down, left, right): ")
        if direction.lower() in ['up', 'down', 'left', 'right']:
            print(f"You moved {direction}.")
            # Update current location logic here
        else:
            print("Invalid direction.")

if __name__ == "__main__":
    client = Client()
    client.run()
