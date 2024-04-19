# Python RSMA-API
[Switch to English](../../../Docs/en/Python/Manual.md)

## Описание
API для обмена сообщениями и командами с RSMA через socket.

## Структура
Описание основных классов и файлов
### SocketClient
Оболочка для socket. Реализует основные функции подключения/отключения, получения и отправки сообщений, а также обрабатывает исключения.
### RSMAClient
Оболочка для сокетного клиента. Унаследована от **SocketClient**. Кроме того, он обрабатывает сообщения с данными о местоположении контроллеров и данными GPIO
### RSMA
Основной класс для взаимодействия с RSMA. Содержит методы для подключения, отключения и отправки сообщений. Дополнительно содержит методы-оболочки для всех команд терминала

## Начало работы

### Подключение модулей
Подключите следующие модули:

```Python
import time

from rsmapy import RSMA

from rsma_client import RSMAClient
```

### Подключение к серверу
Чтобы подключиться к RSMA, воспользуйтесь методом ```RSMA.connect(ip, name)```, укажите IP-адрес сервера и имя клиента

```Python
#connecting to RSMA
RSMA.connect("127.0.0.1","RSMApy")
#waiting 0.1 second
time.sleep(0.1)
```

### Отправка сообщений
Чтобы отправить сообщение на сервер, используйте метод ```SMS.message(text)```, передав текст сообщения в качестве аргумента.\
**Внимание!** Любой метод, описанный ниже, является оболочкой метода для сообщений. Чтобы получить подтверждение выполнения команды, подождите около 0,01 секунды, используя метод ```time.sleep(0.1)```

```Python
#sending message to RSMA
RSMA.message("Hello RSMA!")
time.sleep(0.1)
```

### Выполнение команд
Чтобы отправить текстовую команду из списка команд терминала, используйте метод ```RSMA.execute(команда)```, укажите текст команды в качестве аргумента

```Python
#executing command
RSMA.execute("marker Blue 0 0 0")
time.sleep(0.01)
```

### Отключение от сервера
Чтобы отключиться RSMA, воспользуйтесь методом ```RSMA.disconnect()```.
**Внимание!** Перед отключением дождитесь ответов на предыдущие запросы от сервера, используя метод `time.sleep(1)`.

```Python
time.sleep(1)
#disconnecting to RSMA
RSMA.disconnect()
```

### Методы-команды
Методы, указанные в списке, отправляют команды на сервер

#### load_scene(scene_name: str)
Загружает сцену по названию сцены

```Python
RSMA.load_scene("SupremeFlat")
time.sleep(0.02)
```

#### add_marker(color: str, x, y, z)
Создает маркер в указанной точке

```Python
RSMA.add_marker("Blue", 0.375, 0, 1.385)
time.sleep(0.01)
```

#### add_wall(start_x, start_y, start_z, end_x, end_y, end_z, height, width)
Создает стену с заданными параметрами

```Python
RSMA.add_wall(1.275, 0, 1.500, 2.025, 0, 1.500, 0.02, 0.075)
time.sleep(0.01)
```

#### add_robot(robot_name: str, x, y, z, r_x, r_y, r_z)
Добавляет робота на сцену

```Python
RSMA.add_robot("DarkieBot_Skuf", 0.375, 0.05, 0.332, 0, 0 ,0)
time.sleep(0.01)
```

#### gpio_write(id, port, pin, value)
Устанавливает значение вывода порта GPIO

```Python
RSMA.gpio_write(0, "PA", 1, 1)
time.sleep(0.01)
```

#### gpio_read(id, port, pin)
Считывает значение вывода  порта GPIO. Значение вывода порта перехватывается и сохраняется классом **RSMAClient** в списке **gpios**

```Python
RSMA.gpio_read(0, "PA", 1)
time.sleep(0.01)
```

#### add_drone(x, y, z)
Создает новый беспилотник/дрон

```Python
RSMA.add_drone(0.5, 2.5, 1)
time.sleep(0.01)
```

#### set_drone_acceleration(id, x, y, z)
Задает направление и величину ускорения дрона

```Python
set_drone_acceleration(0, 0, 0.1, 0.3)
time.sleep(0.01)
```

#### set_drone_camera(id, x, y, z, smooth)
Поворачивает камеру дрона под заданными углами с заданной плавностью

```Python
RSMA.set_drone_camera(1, 90, 0, 0, 0.01)
time.sleep(0.01)
```

#### set_drone_control(id, mode)
Включает/отключает ручное управление дроном

```Python
RSMA.set_drone_control(1, True)
time.sleep(0.01)
```

#### drone_move(id, x, y, z, kp, ki, kd)
Управляет дроном с помощью ПИД-регулятора для перемещения в указанную точку

```Python
RSMA.drone_move(0, 0, 5, 10, 3, 2.513, 4.565)
time.sleep(0.01)
```

#### drone_switch_camera(id)
Переключает камеру по id дрона

```Python
RSMA.drone_switch_camera(0)
time.sleep(0.01)
```

#### writer_start(id)
Запускает программу записи (Writer), которая записывает данные о местоположении робота в CSV-файл

```Python
RSMA.writer_start(0)
time.sleep(0.01)
```

#### writer_stop(id)
Останавливает запись (Writer) данных о местоположении робота в CSV-файл

```Python
RSMA.writer_stop(0)
time.sleep(0.01)
```

#### controller_position(id)
Считывает положение контроллера робота. Значение перехватывается и сохраняется классом **RSMAClient** в списке **controllers**

```Python
RSMA.controller_position(0)
time.sleep(0.01)
```