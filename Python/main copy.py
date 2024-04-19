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

    #sending command to RSMA
    RSMA.load_scene("SupremeFlat")
    time.sleep(0.05)

    RSMA.add_wall(0, 0, 0, 0, 0, 3, 0.02, 0.075)
    time.sleep(0.01)

    RSMA.add_wall(0, 0, 3, 1.575, 0, 3, 0.02, 0.075)
    time.sleep(0.01)

    RSMA.add_wall(1.575, 0, 3, 1.575, 0, 2.250, 0.02, 0.075)
    time.sleep(0.01)

    RSMA.add_wall(1.575, 0, 2.250, 2.850, 0, 2.250, 0.02, 0.075)
    time.sleep(0.01)

    RSMA.add_wall(2.850, 0, 2.250, 2.850, 0, 0, 0.02, 0.075)
    time.sleep(0.01)

    RSMA.add_wall(2.850, 0, 0, 0, 0, 0, 0.02, 0.075)
    time.sleep(0.01)

    RSMA.add_wall(0.750, 0, 0, 0.750, 0, 2.250, 0.02, 0.075)
    time.sleep(0.01)

    RSMA.add_wall(1.275, 0, 1.500, 2.025, 0, 1.500, 0.02, 0.075)
    time.sleep(0.01)

    RSMA.add_marker("Green", 0.375, 0, 0.332)
    time.sleep(0.01)

    RSMA.add_marker("Blue", 0.375, 0, 1.385)
    time.sleep(0.01)

    RSMA.add_marker("Blue", 0.787, 0, 2.625)
    time.sleep(0.01)

    RSMA.add_marker("Blue", 1.192, 0, 2.250)
    time.sleep(0.01)
        
    RSMA.add_marker("Blue", 1.050, 0, 1.500)
    time.sleep(0.01)

    RSMA.add_marker("Blue", 1.650, 0, 1.875)
    time.sleep(0.01)

    RSMA.add_marker("Blue", 2.455, 0, 1.500)
    time.sleep(0.01)

    RSMA.add_marker("Blue", 1.650, 0, 0.750)
    time.sleep(0.01)

    RSMA.add_marker("Red", 1.650, 0, 0.332)
    time.sleep(0.01)

    RSMA.add_drone(0.5, 2.5, 1)
    time.sleep(0.01)
    
    RSMA.set_drone_camera(1, 90, 0, 0, 0.01)
    time.sleep(0.01)
    
    RSMA.set_drone_control(1, True)
    time.sleep(0.01)

    RSMA.add_robot("DarkieBot_Skuf", 0.375, 0.05, 0.332, 0, 0 ,0)
    time.sleep(0.01)

    print(RSMAClient.controllers)

    time.sleep(1)
    #disconnecting to RSMA
    RSMA.disconnect()


if __name__ == '__main__':
    main()