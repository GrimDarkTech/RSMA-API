# RSMA-API
[Switch to Russian](/README-ru.md)\
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
Open the terminal using the keyboard shortcut **Ctrl+Alt+T** or by clicking on the terminal icon in the upper left corner.\
[Learn more about terminal commands](https://github.com/GrimDarkTech/RSMADocs/blob/main/Manual/en/Utilities/TerminalCommands.md)\
To start the server, use the command:
```RSMA Terminal
server_start
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
Open the terminal using the keyboard shortcut **Ctrl+Alt+T** or by clicking on the terminal icon in the upper left corner.\
[Learn more about terminal commands](https://github.com/GrimDarkTech/RSMADocs/blob/main/Manual/en/Utilities/TerminalCommands.md)\
To start the server, use the command:
```RSMA Terminal
server_start
```
Upon successful server startup, the message *"Starting server on 127.0.0.1:7777"* will appear in the terminal

### Connect to RSMA via RSMA-API
Import the RSMA-API into your project.\
**Warning The project must use a supported RSMA-API programming language**
For more detailed instructions, go to the documentation section corresponding to the required platform:
#### Platform documentation:
- [Python](Docs/en/Python/Manual.md)
- [C#]()
- [C++]()
