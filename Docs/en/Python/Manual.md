# Python RSMA-API
[Switch to Russian](../../../Docs/ru/Python/Manual.md)

## Description
API for exchanging messages and commands with RSMA via socket.

## Structure
Description of the main classes and files
### SocketClient
Wrapper over socket. Implements the basic functions of connecting/disconnecting, receiving and sending messages, and handles exceptions. 
### RSMAClient
Wrapper over the Socket Client. Inherited from **SocketClient**. Additionally, it processes messages with data on the position of controllers and GPIO data
### RSMA
The main class for interacting with RSMA. Contains methods for connecting, disconnecting, and sending messages. Additionally contains wrapper methods for all terminal commands

## Getting started

### Connecting libraries
Connect the following libraries:

```Python
import time

from rsmapy import RSMA

from rsma_client import RSMAClient
```

### Connecting to server
To connect to RSMA, use the ```RSMA.connect(ip, name)``` method, specify the IP address of the server and the name of the client

```Python
#connecting to RSMA
RSMA.connect("127.0.0.1","RSMApy")
#waiting 0.1 second
time.sleep(0.1)
```

### Sending messages
To send a message to the server, use the ```RSMA.message(text)``` method, pass the message text as an argument.\
**Attention!** Any method described below is a wrapper over the methods for messages. To receive confirmation of the command execution, wait about 0.01 seconds using the ```time.sleep(0.1)``` method

```Python
#sending message to RSMA
RSMA.message("Hello RSMA!")
time.sleep(0.1)
```

### Executing commands
To send a text command from the list of terminal commands, use the method ```RSMA.execute(command)```, specify the command text as an argument

```Python
#executing command
RSMA.execute("marker Blue 0 0 0")
time.sleep(0.01)
```

### Connecting to server
To connect to RSMA, use the ```RSMA.disconnect()``` method.
** Attention!** Before disconnecting, wait for responses to previous requests from the server using the ```time.sleep(1)``` method

```Python
time.sleep(1)
#disconnecting to RSMA
RSMA.disconnect()
```

