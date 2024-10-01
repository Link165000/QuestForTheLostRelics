import socket
import threading
import random
import json
from quests import Quest
from map_generation import generate_map, get_terrain_type

# Server settings
HOST = '127.0.0.1'  # Localhost
PORT = 12345         # Port to listen on

clients = []
player_data = {}

# Simple map generation
map_size = 20
game_map = generate_map(map_size)
npcs = {}
quests = []

# Sample quest
quests.append(Quest("Defeat the Goblin", "Defeat 3 Goblins in the forest.", "Goblin", 3))

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)
    player_data[addr] = {
        'name': addr,
        'health': 100,
        'position': (0, 0),
        'quests': []
    }

    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if message:
                print(f"[{addr}] {message}")
                process_message(addr, message)
            else:
                break
        except:
            break

    conn.close()
    clients.remove(conn)
    del player_data[addr]
    print(f"[DISCONNECTED] {addr} disconnected.")

def process_message(addr, message):
    parts = message.split(',')
    command = parts[0]

    if command == "MOVE":
        direction = parts[1]
        move_player(addr, direction)
    elif command == "COMBAT":
        target = parts[1]
        combat(addr, target)
    elif command == "QUEST":
        accept_quest(addr, parts[1])
    elif command == "STATUS":
        check_status(addr)

    broadcast(f"Update: {player_data}")

def move_player(addr, direction):
    if direction == 'UP':
        player_data[addr]['position'] = (player_data[addr]['position'][0], player_data[addr]['position'][1] - 1)
    elif direction == 'DOWN':
        player_data[addr]['position'] = (player_data[addr]['position'][0], player_data[addr]['position'][1] + 1)
    elif direction == 'LEFT':
        player_data[addr]['position'] = (player_data[addr]['position'][0] - 1, player_data[addr]['position'][1])
    elif direction == 'RIGHT':
        player_data[addr]['position'] = (player_data[addr]['position'][0] + 1, player_data[addr]['position'][1])

def combat(addr, target):
    if target in player_data:
        damage = random.randint(10, 20)  # Random damage for combat
        player_data[target]['health'] -= damage
        if player_data[target]['health'] <= 0:
            print(f"[COMBAT] {target} has been defeated!")
            del player_data[target]

    broadcast(f"Combat Update: {player_data}")

def accept_quest(addr, quest_name):
    for quest in quests:
        if quest.name == quest_name:
            player_data[addr]['quests'].append(quest)
            print(f"[QUEST] {addr} accepted quest: {quest.name}")
            break

def check_status(addr):
    # Send the current status of quests to the player
    quests_status = player_data[addr]['quests']
    response = f"Quest Status: {[quest.name for quest in quests_status]}"
    clients[addr].send(response.encode('utf-8'))

def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("[SERVER STARTED]")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start()
