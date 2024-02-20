import socket

class SocketClient:

    def __init__(self, server_IP: str, server_port: int, client_name: str):
        self.server_IP = server_IP
        self.server_port = server_port
        self.client_name = client_name
        self.is_connected = False
    



HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 7777  # The port used by the server

client = socket.socket()

print("Starting")

client.connect((HOST, PORT))

print("Connecting to server")

message = "Aboba<|CR|><|EOM|>"
messageBytes = message.encode()

client.send(messageBytes)

print("Waiting for server response")

data = client.recv(1024)

print("Server sent: ", data.decode())

message = "Aboba<|M|>Hey server<|EOM|>"
messageBytes = message.encode()

client.send(messageBytes)

data = client.recv(1024)

print("Server sent: ", data.decode())

abo = input()

print(abo)

client.shutdown(2)
client.close()

