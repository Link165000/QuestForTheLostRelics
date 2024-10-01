from server import Server
from client import Client

if __name__ == "__main__":
    choice = input("Start server (s) or client (c)? ").lower()
    if choice == 's':
        server = Server()
        server.start()
    elif choice == 'c':
        client = Client()
        client.run()
