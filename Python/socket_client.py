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

    logger: bool
    """If true, logging client messages"""

    def __init__(self, server_IP: str, server_port: int, client_name: str):
        self.server_IP = server_IP
        self.server_port = server_port
        self.client_name = client_name
        self.is_connected = False
        self._message_reciver = None
        self.logger = False
    
    def _listen_to_message_async(self):
        """Listening to messages"""
        while(True):
            buffer: bytes
            try:
                buffer = self._client.recv(1024)
            except:
                print(f"{self.client_name}: Connection error: The destination computer rejected the connection request. Try change client/user name")
                return
            
            received_text = buffer.decode()

            if(received_text.find("<|EOM|>") > -1 or received_text.find("<|ACK|>") > -1):
                messages = received_text.split("<|EOM|>")
                acks = received_text.split("<|ACK|>")

                if(len(messages) > 1):
                    for message in messages:
                        if(message.find("<|M|>") > -1):
                            text = message.split("<|M|>")[1]

                            ack_message = "<|M|><|ACK|>"
                            echo_buffer = ack_message.encode()
                            self._client.send(echo_buffer)

                            if(self.logger):
                                print(f"{self.client_name}: recived message from server")

                            self.on_message_recived(text)

                if(len(acks) > 1):
                    for ack in acks:
                        if(ack == "<|M|>"):
                            if(self.logger):
                                print(f"{self.client_name}: Message delivered")
                            self.on_message_delivered()
                        elif(ack == "<|DR|>"):
                            try:
                                self._message_reciver.join()
                                self._client.close()
                            except Exception as e:
                                print(e)
                                return
                            finally:
                                self._client.close()
                                self.is_connected = False
                                print(f"{self.client_name}: Disconnected")
                                self.on_disconnected
                            return

    def connect(self):
        """Connects client to server"""
        if(self.is_connected):
            print(f"{self.client_name}: Сlient is already connected to server")
            return
        
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self._client.connect((self.server_IP, self.server_port))
        except:
            print(f"{self.client_name}: Connection error: The destination computer rejected the connection request. Make sure that the server is running and available for connection")
            return 
        if(self.logger):
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
        else:
            self._client.close

        if(self._message_reciver == None):
            _message_reciver = threading.Thread(target=self._listen_to_message_async, daemon=True)
            _message_reciver.start()

        self.on_connected()

    def send_message(self, message_text: str):
        """Sends message to server"""
        if(not self.is_connected):
            print(f"{self.client_name}: client is NOT connected to server")
            return
        
        message = f"{self.client_name}<|M|>" + message_text + "<|EOM|>"
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

    def on_message_recived(self, text: str):
        """Called when recived message from server"""

    def on_message_delivered(self):
        """Called when message delivered to server"""

    def on_connected(self):
        """Called when client connected to server"""
    
    def on_disconnected(self):
        """Called when client disconnected to server"""

