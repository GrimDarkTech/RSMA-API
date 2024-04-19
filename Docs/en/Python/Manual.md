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

### Importing modules
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

### Disconnecting from server
To diconnect from RSMA, use the ```RSMA.disconnect()``` method.
** Attention!** Before disconnecting, wait for responses to previous requests from the server using the ```time.sleep(1)``` method

```Python
time.sleep(1)
#disconnecting to RSMA
RSMA.disconnect()
```

### Methods-commands
The methods shown in the table send commands to the server

#### load_scene(scene_name: str)
Loads a scene by the name of the scene

```Python
RSMA.load_scene("SupremeFlat")
time.sleep(0.02)
```

#### add_marker(color: str, x, y, z)
Creates a marker at the specified point

```Python
RSMA.add_marker("Blue", 0.375, 0, 1.385)
time.sleep(0.01)
```

#### add_wall(start_x, start_y, start_z, end_x, end_y, end_z, height, width)
Creates a wall with the specified parameters

```Python
RSMA.add_wall(1.275, 0, 1.500, 2.025, 0, 1.500, 0.02, 0.075)
time.sleep(0.01)
```

#### add_robot(robot_name: str, x, y, z, r_x, r_y, r_z)
Adds a robot to the scene

```Python
RSMA.add_robot("DarkieBot_Skuf", 0.375, 0.05, 0.332, 0, 0 ,0)
time.sleep(0.01)
```

#### gpio_write(id, port, pin, value)
Sets the value of the GPIO port pin

```Python
RSMA.gpio_write(0, "PA", 1, 1)
time.sleep(0.01)
```

#### gpio_read(id, port, pin)
Reads the value of the GPIO port pin. The port pin value is captured and saved by **RSMAClient** to the list **gpios**

```Python
RSMA.gpio_read(0, "PA", 1)
time.sleep(0.01)
```

#### add_drone(x, y, z)
Creates a new drone

```Python
RSMA.add_drone(0.5, 2.5, 1)
time.sleep(0.01)
```

#### set_drone_acceleration(id, x, y, z)
Sets the direction and magnitude of the drone acceleration

```Python
set_drone_acceleration(0, 0, 0.1, 0.3)
time.sleep(0.01)
```

#### set_drone_camera(id, x, y, z, smooth)
Rotates the drone's camera at preset angles with a preset smoothness

```Python
RSMA.set_drone_camera(1, 90, 0, 0, 0.01)
time.sleep(0.01)
```

#### set_drone_control(id, mode)
Enables/disables manual drone control

```Python
RSMA.set_drone_control(1, True)
time.sleep(0.01)
```

#### drone_move(id, x, y, z, kp, ki, kd)
Controls the drone using a PID controller to move to the specified point

```Python
RSMA.drone_move(0, 0, 5, 10, 3, 2.513, 4.565)
time.sleep(0.01)
```

#### drone_switch_camera(id)
Switches the camera by drone ID

```Python
RSMA.drone_switch_camera(0)
time.sleep(0.01)
```

#### writer_start(id)
Starts a Writer that writes data about the object's position to a CSV file

```Python
RSMA.writer_start(0)
time.sleep(0.01)
```

#### writer_stop(id)
Stops the writer writing data about the object's position to a CSV file

```Python
RSMA.writer_stop(0)
time.sleep(0.01)
```

#### controller_position(id)
Reads the robot's controller position. The value is captured and saved by **RSMAClient** to the list **controllers**

```Python
RSMA.controller_position(0)
time.sleep(0.01)
```