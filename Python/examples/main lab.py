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

    #Walls
    RSMA.add_wall(1.297, 0, 5.023, 1.310, 0, 6.276, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(1.675, 0, 7.447, 2.363, 0, 8.520, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(3.317, 0, 9.331, 5.076, 0, 9.967, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(5.076, 0, 9.967, 6.941, 0, 9.814, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(6.941, 0, 9.814, 6.941, 0, 8.723, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(6.941, 0, 8.723, 8.401, 0, 7.440, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(8.401, 0, 7.440, 8.779, 0, 6.679, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(8.779, 0, 6.679, 8.951, 0, 5.824, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(8.951, 0, 5.824, 8.865, 0, 4.827, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(8.865, 0, 4.827, 8.531, 0, 3.987, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(8.531, 0, 3.982, 8.029, 0, 3.309, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(8.029, 0, 3.309, 7.490, 0, 2.860, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(7.490, 0, 2.860, 6.716, 0, 2.479, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(6.716, 0, 2.479, 5.793, 0, 2.308, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(5.793, 0, 2.308, 4.730, 0, 2.438, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(4.730, 0, 2.438, 3.608, 0, 4.808, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(3.608, 0, 4.808, 3.553, 0, 6.243, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(3.553, 0, 6.243, 4.053, 0, 7.110, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(4.053, 0, 7.110, 4.938, 0, 7.684, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(4.938, 0, 7.684, 6.001, 0, 7.778, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(6.001, 0, 7.778, 6.901, 0, 7.421, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(6.901, 0, 7.421, 7.615, 0, 6.611, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(7.615, 0, 6.611, 7.858, 0, 5.617, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(7.858, 0, 5.617, 7.698, 0, 4.781, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(7.698, 0, 4.781, 7.273, 0, 4.111, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(7.273, 0, 4.111, 6.717, 0, 3.677, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(6.717, 0, 3.677, 5.658, 0, 3.405, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(6.901, 0, 7.421, 4.578, 0, 8.723, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(4.578, 0, 8.723, 3.101, 0, 7.691, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(2.460, 0, 5.820, 2.582, 0, 4.426, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(1.638, 0, 3.818, 2.304, 0, 2.758, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(3.242, 0, 1.928, 4.376, 0, 1.396, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(5.614, 0, 1.205, 6.855, 0, 1.371, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(7.999, 0, 1.880, 8.954, 0, 2.690, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(9.642, 0, 3.737, 10.007, 0, 4.935, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(10.020, 0, 6.187, 9.679, 0, 7.392, 0.02, 0.075)
    time.sleep(0.01)
    RSMA.add_wall(9.013, 0, 8.453, 8.075, 0, 9.282, 0.02, 0.075)
    time.sleep(0.01)

    #Markers

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

    RSMA.add_drone(5, 6, 5)
    time.sleep(0.01)
    
    RSMA.set_drone_camera(1, 90, 0, 0, 0.01)
    time.sleep(0.01)
    
    RSMA.set_drone_control(1, True)
    time.sleep(0.01)

    RSMA.add_robot("DarkieBot_Petya", 0.375, 0.05, 0.332, 0, 0 ,0)
    time.sleep(0.01)

    move(1, 1, 0)

    RSMA.trails_start(0)
    time.sleep(0.01)

    RSMA.controller_position(0)
    time.sleep(0.01)


    print(RSMAClient.controllers)

    time.sleep(1)
    #disconnecting to RSMA
    RSMA.disconnect()

def move(vz, vx, wr):
    v1 = (2000 * wr - 2000 * vx - 34641*vz) / 6000
    v2 = (2000 * wr - 2000 * vx + 34641*vz) / 6000
    v3 = (wr + 2 * vx) / 3

    RSMA.gpio_write(0, "PA", "1", 1)
    time.sleep(0.01)
    RSMA.gpio_write(0, "PA", "3", v1)
    time.sleep(0.01)
    RSMA.gpio_write(0, "PA", "5", 1)
    time.sleep(0.01)
    RSMA.gpio_write(0, "PA", "6", v2)
    time.sleep(0.01)

if __name__ == '__main__':
    main()