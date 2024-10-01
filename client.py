import pygame
import socket
import threading
import random

# Client settings
HOST = '127.0.0.1'  # Server address
PORT = 12345         # Server port

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quest for the Lost Relics")

# Networking
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

threading.Thread(target=receive_messages).start()

# Player attributes
player_position = [400, 300]
player_health = 100

# Simple map generation
map_size = 20
game_map = [['.' for _ in range(map_size)] for _ in range(map_size)]
game_map[random.randint(0, map_size-1)][random.randint(0, map_size-1)] = 'E'  # Example Enemy

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        client.send("MOVE,LEFT".encode('utf-8'))
    if keys[pygame.K_RIGHT]:
        client.send("MOVE,RIGHT".encode('utf-8'))
    if keys[pygame.K_UP]:
        client.send("MOVE,UP".encode('utf-8'))
    if keys[pygame.K_DOWN]:
        client.send("MOVE,DOWN".encode('utf-8'))
    if keys[pygame.K_SPACE]:  # Press space to attack
        client.send(f"COMBAT,{addr}".encode('utf-8'))

    # Draw the game state
    screen.fill((0, 0, 0))  # Clear the screen
    for y in range(map_size):
        for x in range(map_size):
            if game_map[y][x] == '.':
                color = (0, 0, 255)  # Water
            elif game_map[y][x] == 'E':
                color = (255, 0, 0)  # Enemy
            else:
                color = (0, 255, 0)  # Default
            
            pygame.draw.rect(screen, color, (x * 40, y * 40, 40, 40))

    # Draw player
    pygame.draw.circle(screen, (0, 255, 0), (int(player_position[0]), int(player_position[1])), 20)
    pygame.display.flip()

client.close()
pygame.quit()

