import time

from rsmapy import RSMA

from rsma_client import RSMAClient

def main():
    #connecting to RSMA
    RSMA.connect("127.0.0.1","RSMApy")
    #waiting 1 second
    time.sleep(0.1)

    #sending message to RSMA
    RSMA.message("Hello RSMA!")
    time.sleep(0.1)

    #executing command
    RSMA.execute("marker Blue 0 0 0")
    time.sleep(0.01)

    #sending command to RSMA
    RSMA.load_scene("Agrobot")
    time.sleep(0.1)

    RSMA.add_robot("DarkieBot_Altushka", 535, 1.29, 523, 0, 0, 0)
    time.sleep(0.1)

    RSMA.add_robot("DarkieBot_Skuf", 535.5, 1.29, 523, 0, 0, 0)
    time.sleep(0.1)
    
    RSMA.add_robot("DarkieBot_Kitty", 534.5, 1.29, 523, 0, 0, 0)
    time.sleep(0.1)

    RSMA.gpio_write(0, "PA", "1", 0.5)
    time.sleep(0.1)
    RSMA.gpio_write(0, "PA", "3", 1)
    time.sleep(0.1)
    RSMA.gpio_write(0, "PB", "1", 1)
    time.sleep(0.1)
    RSMA.gpio_write(0, "PB", "3", 1)
    time.sleep(0.1)
    
    RSMA.gpio_write(1, "PA", "1", 1)
    time.sleep(0.1)
    RSMA.gpio_write(1, "PA", "3", 1)
    time.sleep(0.1)
    RSMA.gpio_write(1, "PA", "4", 1)
    time.sleep(0.1)
    
    #forward
    RSMA.gpio_write(2, "PA", "2", 1)
    time.sleep(0.05)
    RSMA.gpio_write(2, "PA", "3", 1)
    time.sleep(0.05)
    RSMA.gpio_write(2, "PA", "4", 1)
    time.sleep(0.05)
    RSMA.gpio_write(2, "PA", "6", 0.5)
    time.sleep(0.05)
    #rear
    RSMA.gpio_write(2, "PB", "2", 1)
    time.sleep(0.05)
    RSMA.gpio_write(2, "PB", "3", 0.6)
    time.sleep(0.05)
    RSMA.gpio_write(2, "PB", "5", 1)
    time.sleep(0.05)
    RSMA.gpio_write(2, "PB", "6", 1)
    time.sleep(0.05)
    
    for i in range (1, 10):
        RSMA.add_drone(434.5, 4, 423)
        time.sleep(0.01)
        RSMA.execute(f"drone_move {i} 534.5 {1.29 + i * 0.5} 523 3 2.113 3.065")
        time.sleep(0.01)
        
    RSMA.add_drone(534.5, 4, 523)
    time.sleep(0.01)
    
    RSMA.set_drone_camera(10, 90, 0, 0, 0.01)
    time.sleep(0.01)
    
    RSMA.set_drone_control(10, True)
    time.sleep(0.01)

    RSMA.controller_position(0)
    time.sleep(0.1)

    print(RSMAClient.controllers)

    time.sleep(1)
    #disconnecting to RSMA
    RSMA.disconnect()


if __name__ == '__main__':
    main()