# RSMA-API
API for transferring data and commands to RMSA using Socket via TCP

## Supported:
- Python
- C#

## Planned supported:
- C++
- C
- Matlab
- JavaScript

## Getting started
The API supports working with RSMA in Unity and RSMA Edu

### Run RSMA in Unity or RSMA Edu
Using a terminal or scripts, run the built-in RSMA server

#### RSMA
Open the terminal using the keyboard shortcut **Ctrl+Alt+T** or by clicking on the terminal icon in the upper left corner, open the terminal.\
[Learn more about terminal commands](https://github.com/GrimDarkTech/RSMADocs/blob/main/Manual/en/TerminalCommands.md)\
To start the server, use the command:
```RSMA Terminal
server start
```
Upon successful server startup, the message *"Starting server on 127.0.0.1:7777"* will appear in the terminal

---

Use C# script tp start RSMA server

``` C#
    CommandHandler.server = new RSMAServer();

    CommandHandler.server.serverIP = "127.0.0.1";
    CommandHandler.server.serverPort = 7777;

    CommandHandler.server.Run();
```
#### RSMA Edu
Open the terminal using the keyboard shortcut **Ctrl+Alt+T** or by clicking on the terminal icon in the upper left corner, open the terminal.\
[Learn more about terminal commands](https://github.com/GrimDarkTech/RSMADocs/blob/main/Manual/en/TerminalCommands.md)\
To start the server, use the command:
```RSMA Terminal
server start
```
Upon successful server startup, the message *"Starting server on 127.0.0.1:7777"* will appear in the terminal