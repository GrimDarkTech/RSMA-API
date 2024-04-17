from socket_client import SocketClient

class RSMAClient(SocketClient):

    controllers: list = []

    gpios: list = []

    def on_message_recived(self, text: str):
        """Called when recived message from server"""
        if(text.find("<|Position|>") > -1):
            text = text.replace("<|Position|>", "")
            text = text.replace(",", ".")
            splited = text.split("<|s|>")
            if(len(RSMAClient.controllers) == int(splited[0])):
                RSMAClient.controllers.append(splited)
            else:
                RSMAClient.controllers[int(splited[0])] = splited.copy()
        elif(text.find("<|GPIO|>") > -1):
            text = text.replace("<|GPIO|>", "")
            text = text.replace(",", ".")
            splited = text.split("<|s|>")
            if(len(RSMAClient.gpios) == int(splited[0])):
                RSMAClient.gpios.append(splited)
            else:
                RSMAClient.gpios[int(splited[0])] = splited.copy()
        else:
            print(text)



            

    def on_message_delivered(self):
        """Called when message delivered to server"""
        

    def on_connected(self):
        """Called when client connected to server"""
        
    
    def on_disconnected(self):
        """Called when client disconnected to server"""
        
