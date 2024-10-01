import socket
import json

# Client Configuration
HOST = '127.0.0.1'  # Server IP
PORT = 12345         # Server Port

# Connect to the server
def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        data = client.recv(1024)
        if not data:
            break
        game_state = json.loads(data.decode())
        print(f"Map: {game_state['map']}")
        print(f"Quests: {game_state['quests']}")
        print(f"NPCs available for trading: {game_state['npcs']}")

        # Sample interaction
        action = input("Enter action (trade, combat, quest, position): ")
        if action == "trade":
            npc = input("Enter NPC name: ")
            item = input("Enter item to trade: ")
            client.send(json.dumps({"type": "trade", "npc": npc, "item": item}).encode())
        elif action == "combat":
            enemy = input("Enter enemy name: ")
            client.send(json.dumps({"type": "combat", "enemy": enemy}).encode())
        elif action == "quest":
            quest_id = int(input("Enter quest ID: "))
            client.send(json.dumps({"type": "quest", "quest_id": quest_id}).encode())
        elif action == "position":
            position = input("Enter your position (x,y): ")
            client.send(json.dumps({"type": "position", "position": position}).encode())

    client.close()

if __name__ == "__main__":
    connect_to_server()
