import socket
import threading
import json

class Server:
    def __init__(self, host='127.0.0.1', port=12345):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(5)
        self.clients = []
        self.player_data = {}

        print(f"Server started on {host}:{port}")

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                self.broadcast(data, client_socket)
            except ConnectionResetError:
                break

        client_socket.close()

    def broadcast(self, message, client_socket):
        for client in self.clients:
            if client != client_socket:
                client.send(message.encode('utf-8'))

    def run(self):
        while True:
            client_socket, addr = self.server.accept()
            self.clients.append(client_socket)
            print(f"Connection from {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    server = Server()
    server.run()
