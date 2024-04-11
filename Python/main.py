import time
import math

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

    #sending command to RSMA
    RSMA.load_scene("SupremeFlat")
    time.sleep(0.1)
    
    RSMA.set_drone_control(0, True)
    time.sleep(0.1)

    RSMA.add_robot("DarkieBot_Altushka", 1, 0.1, 1, 0, 0, 0)
    time.sleep(0.1)

    RSMA.gpio_write(0, "PA", "1", 1)
    time.sleep(0.1)
    
    RSMA.gpio_read(0, "PA", "1")
    time.sleep(0.1)

    RSMA.controller_position(0)
    time.sleep(0.1)

    print(RSMAClient.controllers)

    time.sleep(1)
    #disconnecting to RSMA
    RSMA.disconnect()


if __name__ == '__main__':
    main()