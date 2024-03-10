from dronekit import connect, VehicleMode
import os



class DroneConnect:
    def __init__(self, port, ip="127.0.0.1"):
        self.ip = ip
        self.port = str(port)

    def connect(self):
        #drone_ip = f"{self.ip}:{self.port}"
        drone_ip = f"{self.ip}:{self.port}"
        print("DRONE_CONNECT_IP: ", drone_ip)
        drone = connect(drone_ip, wait_ready=True, timeout=40)
        return drone


        

  
        




