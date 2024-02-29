import socket
import threading

class SocketClient:

    server_IP: str
    """Server IP address"""

    server_port: int
    """Port binded by the server"""

    client_name: str
    """Name of client"""

    is_connected: bool
    """True if client connected to server"""

    _client: socket
    """Socket client"""

    _message_reciver: threading.Thread
    """Uses to contain task for listening for messages"""

    def __init__(self, server_IP: str, server_port: int, client_name: str):
        self.server_IP = server_IP
        self.server_port = server_port
        self.client_name = client_name
        self.is_connected = False
        self._message_reciver = None
    
    def _listen_to_message_async(self):
        """Listening to messages"""
        while(True):
            buffer: bytes
            try:
                buffer = self._client.recv(1024)
            except:
                print(f"{self.client_name}: Connection error: The destination computer rejected the connection request. Try change client/user name")
                return
            
            response = buffer.decode()

            if(response.find("<|EOM|>") > -1):
                response = response.replace("<|EOM|>", "")

                message_text = ""
                client_name = ""
                if(response.find("<|M|>") > -1):
                    separetedValues = response.split("<|M|>")
                    client_name = separetedValues[0]
                    message_text = separetedValues[1]

                    ack_message = "<|M|><|ACK|>"
                    echo_buffer = ack_message.encode()
                    self._client.send(echo_buffer)

                    print(f"{self.client_name}: recived message from server")

            elif(response.find("<|ACK|>") > -1):
                if(response == "<|M|><|ACK|>"):
                    print(f"{self.client_name}: Message delivered")

                elif(response == "<|DR|><|ACK|>"):
                    try:
                        self._message_reciver.cancel()
                        self._client.shutdown(2)
                    except:
                        print("Error")
                        return
                    finally:
                        self._client.close()
                        self.is_connected = False
                        print(f"{self.client_name}: Disconnected")
                    return

    def connect(self):
        """Connects client to server"""
        if(self.is_connected):
            print(f"{self.client_name}: Сlient is already connected to server")
            return
        
        self._client = socket.socket()

        try:
            self._client.connect((self.server_IP, self.server_port))
        except:
            print(f"{self.client_name}: Connection error: The destination computer rejected the connection request. Make sure that the server is running and available for connection")
            return 
        print(f"{self.client_name}: Waiting for server responce")

        message = f"{self.client_name}<|CR|><|EOM|>"
        message_bytes = message.encode()

        try:
            self._client.send(message_bytes)
        except:
            print(f"{self.client_name}: Connection error: The destination computer rejected the connection request. Make sure that the server is running and available for connection")
            return
        
        buffer: bytes
        try:
            buffer = self._client.recv(1024)
        except:
            print(f"{self.client_name}: Connection error: The destination computer rejected the connection request. Try change client/user name")
            return
        
        response = buffer.decode()

        if(response == "<|CR|><|ACK|>"):
            print(f"{self.client_name}: successfully connect to server.")
            self.is_connected = True

        if(self._message_reciver == None):
            self._message_reciver = threading.Thread(target=self._listen_to_message_async)
            self._message_reciver.start()

    def send_message(self, message: str):
        """Sends message to server"""
        if(not self.is_connected):
            print(f"{self.client_name}: client is NOT connected to server")
            return
        
        message = f"{self.client_name}<|M|>" + message + "<|EOM|>"
        message_bytes = message.encode()

        try:
            self._client.send(message_bytes)
        except:
            print(f"{self.client_name}: Listener error: The remote computer has terminated an existing connection. Make sure that the server is running and available for connection")
            self.is_connected = False
            return
    
    def disconnect(self):
        """Disconnects cleint from server"""
        if(not self.is_connected):
            print(f"{self.client_name}: client is NOT connected to server")
            return
        
        message = f"{self.client_name}<|DR|><|EOM|>"
        message_bytes = message.encode()

        try:
            self._client.send(message_bytes)
        except:
            print(f"{self.client_name}: Listener error: The remote computer has terminated an existing connection. Make sure that the server is running and available for connection")
            self.is_connected = False
            return

        
