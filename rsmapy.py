from socket_client import SocketClient

class RSMA:

    is_connected : bool = False 

    client: SocketClient
    
    def connect(client_name: str):
        if(not(RSMA.is_connected)):
            RSMA.client = SocketClient("127.0.0.1", 7777, client_name)
            RSMA.client.connect()
            RSMA.is_connected = True

    def disconnect():
        if(RSMA.is_connected):
            RSMA.client.disconnect()
            RSMA.is_connected = False
    
    def execute(command: str):
        if(RSMA.is_connected):
            RSMA.client.send_message("<|CMD|>" + command)
    
    def message(text: str):
        if(RSMA.is_connected):
            RSMA.client.send_message(text)