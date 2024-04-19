# RSMA-API
[Switch to English](/README.md)\
API для передачи данных и команд в RMSA через Socket по протоколу TCP

## Поддерживаемые платформы:
- Python
- C#

## Запланирована поддержка:
- C++
- C
- Matlab
- JavaScript

## Начало работы
API поддерживает работу с RSMA в Unity и RSMA Edu

### Запуск RSMA в Unity или RSMA Edu
Используя терминал или скрипты, запустите встроенный RSMA-сервер

#### RSMA
Откройте терминал, используя сочетание клавиш **Ctrl+Alt+T** или нажав на значок терминала в левом верхнем углу.\
[Подробнее о командах терминала](https://github.com/GrimDarkTech/RSMADocs/blob/main/Manual/ru/Utilities/TerminalCommands.md)\
Чтобы запустить сервер, используйте команду:
```RSMA Terminal
server_start
```
После успешного запуска сервера в терминале появится сообщение *"Starting server on 127.0.0.1:7777"*

---

Используйте скрипт на C# для запуска RSMA-сервера

``` C#
    CommandHandler.server = new RSMAServer();

    CommandHandler.server.serverIP = "127.0.0.1";
    CommandHandler.server.serverPort = 7777;

    CommandHandler.server.Run();
```
#### RSMA Edu
Откройте терминал, используя сочетание клавиш **Ctrl+Alt+T** или нажав на значок терминала в левом верхнем углу.\
[Подробнее о командах терминала](https://github.com/GrimDarkTech/RSMADocs/blob/main/Manual/ru/Utilities/TerminalCommands.md)\
Чтобы запустить сервер, используйте команду:
```RSMA Terminal
server_start
```
После успешного запуска сервера в терминале появится сообщение *"Starting server on 127.0.0.1:7777"*

### Подключение к RSMA через RSMA-API
Импортируйте RSMA-API в свой проект.\
**Предупреждение: В проекте должен использоваться поддерживаемый RSMA-API язык программирования**
Для получения более подробных инструкций перейдите в раздел документации, соответствующий платформе:
#### Документация:
- [Python](Docs/ru/Python/Manual.md)
- [C#]()
- [C++]()
