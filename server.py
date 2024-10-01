import socket
import threading
import json
from game_map import GameMap
from quests import QuestManager
from trading import NPC
from combat import Character

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345         # Port to listen on

# Global Variables
clients = {}
quest_manager = QuestManager()
game_map = GameMap(1000, 1000)  # Create a 1000x1000 map
npcs = [NPC("Merchant", ["Potion", "Sword", "Shield"]) for _ in range(5)]  # NPCs for trading

# Function to handle client connections
def handle_client(conn, addr):
    print(f'New connection: {addr}')
    clients[addr] = conn

    # Send initial game state
    conn.send(json.dumps({
        "map": game_map.map,
        "quests": quest_manager.quests,
        "npcs": [npc.name for npc in npcs]
    }).encode())

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            
            # Handle incoming data from clients
            message = json.loads(data.decode())
            handle_message(addr, message)
        except Exception as e:
            print(f"Error: {e}")
            break

    conn.close()
    del clients[addr]
    print(f'Connection closed: {addr}')

# Handle incoming messages from clients
def handle_message(addr, message):
    if message["type"] == "trade":
        handle_trade(addr, message["npc"], message["item"])
    elif message["type"] == "combat":
        handle_combat(addr, message["enemy"])

def handle_trade(addr, npc_name, item):
    npc = next((npc for npc in npcs if npc.name == npc_name), None)
    if npc:
        result = npc.trade(item)
        clients[addr].send(result.encode())

def handle_combat(addr, enemy_name):
    # Logic for combat can be expanded here
    pass

# Start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f'Server listening on {HOST}:{PORT}')
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
