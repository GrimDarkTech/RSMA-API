#from socket_client import RSMAClient
from rsma_client import RSMAClient

class RSMA:

    is_connected : bool = False 

    client: RSMAClient
    
    def connect(ip: str,client_name: str):
        if(not(RSMA.is_connected)):
            RSMA.client = RSMAClient(ip, 7777, client_name)
            RSMA.client.connect()
            RSMA.is_connected = True

    def disconnect():
        if(RSMA.is_connected):
            RSMA.client.disconnect()
            RSMA.is_connected = False
    
    def execute(command: str):
        if(RSMA.is_connected):
            RSMA.client.send_message("<|CMD|>" + command)

    def load_scene(scene_name: str):
        RSMA.execute(f"scene_load {scene_name}")

    def add_marker(color: str, x, y, z):
        RSMA.execute(f"marker {color} {x} {y} {z}")

    def add_wall(start_x, start_y, start_z, end_x, end_y, end_z, height, width):
        RSMA.execute(f"wall {start_x} {start_y} {start_z} {end_x} {end_y} {end_z} {height} {width}")

    def add_robot(robot_name: str, x, y, z, r_x, r_y, r_z):
        RSMA.execute(f"robot {robot_name} {x} {y} {z} {r_x} {r_y} {r_z}")
    
    def gpio_write(id, port, pin, value):
        RSMA.execute(f"gpio_write {id} {port} {pin} {value}")

    def gpio_read(id, port, pin):
        RSMA.execute(f"gpio_read {id} {port} {pin}")

    def add_drone(x, y, z):
        RSMA.execute(f"drone {x} {y} {z}")

    def set_drone_acceleration(id, x, y, z, yaw):
        RSMA.execute(f"drone_move {id} {x} {y} {z} {yaw}")

    def set_drone_camera(id, x, y, z, smooth):
        RSMA.execute(f"drone_camera {id} {x} {y} {z} {smooth}")

    def set_drone_control(id, mode):
        RSMA.execute(f"drone_manual_control {id} {mode}")

    def writer_start(id):
        RSMA.execute(f"writer_start {id}")
    
    def writer_stop(id):
        RSMA.execute(f"writer_stop {id}")

    def controller_position(id):
        RSMA.execute(f"controller_position {id}")

    def message(text: str):
        if(RSMA.is_connected):
            RSMA.client.send_message(text)