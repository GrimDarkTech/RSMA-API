import os
import time

from socket_client import SocketClient


client = SocketClient("127.0.0.1", 7777, "Tota")

client.client_name = input("Enter client name\n")

while(True):

    os.system('cls')
    print(client.client_name + " : " + str(client.is_connected))
    print("Enter \"connect\" to connect to the server")
    print("Enter \"disconnect\" to disconnect from the server")
    print("Enter \"message messageText\" to disconnect from the server")
    print("Enter \"exit\" to exit")

    input_str = input()
    
    time.sleep(0.1)

    if(input_str == "connect"):
        client.connect()
    elif(input_str == "disconnect"):
        client.disconnect()
    elif(input_str.find("message") > -1):
        client.send_message(input_str.replace("message ", ""))
    elif(input_str == "exit"):
        break

input("Press any key to Exit")
