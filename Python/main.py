import time
import math

from rsmapy import RSMA

def main():
    #connecting to RSMA
    RSMA.connect("127.0.0.1","RSMApy")

    #waiting 1 second
    time.sleep(1)

    #sending message to RSMA
    RSMA.message("Hello RSMA!")

    time.sleep(1)

    #sending command to RSMA
    #RSMA.load_scene("SupremeFlat")
    RSMA.load_scene("Agrobot")

    time.sleep(1)
    
    RSMA.execute("drone_manual_control 0 True")
    time.sleep(0.1)
    
    RSMA.execute("robot DarkieBot_Altushka 5 0,1 5 0 0 0")
    time.sleep(0.2)
    
    RSMA.execute("robot DarkieBot_Skuf 5.15 0,1 4.90 0 0 0")
    time.sleep(0.2)
    
    RSMA.execute("gpio_write 1 PA 1 1")
    time.sleep(0.1)

    RSMA.execute("gpio_write 1 PA 3 1")
    time.sleep(0.1)
    
    RSMA.execute("gpio_write 1 PA 4 0.7")
    time.sleep(0.1)
    
    RSMA.execute("gpio_write 0 PA 2 1")
    time.sleep(0.1)
    
    RSMA.execute("gpio_write 0 PA 3 1")
    time.sleep(0.1)
    
    RSMA.execute("gpio_write 0 PB 2 1")
    time.sleep(0.1)
    
    RSMA.execute("gpio_write 0 PA 3 0.4")
    time.sleep(0.1)
    
    RSMA.execute("drone_move 0 5 0.2 5 3 2.513 4.565")
    time.sleep(0.1)

    RSMA.execute("drone_manual_control 0 True")
    time.sleep(0.1)
    
    for i in range(1, 20):
    
        RSMA.execute(f"drone 0 1 {-5 + i * 0.1}")
        time.sleep(0.05)
        
        RSMA.execute(f"drone_move {i} {5 + 0.3 * i} {0.2 + 0.05 * i} {5 + i * 0.3} 0.5 0 0")
        time.sleep(0.05)
        
        RSMA.execute(f"drone_manual_control {i} True")
        time.sleep(0.05)
        
    time.sleep(0.2)
    
    RSMA.execute("drone 5 2 5")
    time.sleep(0.1)
    
    RSMA.execute(f"drone_camera {i + 1} 90 0 0 0,01")
    time.sleep(10)
    
    for i in range(1, 20):
        
        RSMA.execute(f"drone_move {i} {10 + 0.3 * i} {0.2 + 0.5 * i} {5 + i * 0.8} 0.5 0 0")
        time.sleep(0.05)
        
        RSMA.execute(f"drone_manual_control {i} True")
        time.sleep(0.05)
        
    time.sleep(0.2)

    #disconnecting to RSMA
    RSMA.disconnect()

    input("Press any key to Exit")

if __name__ == '__main__':
    main()