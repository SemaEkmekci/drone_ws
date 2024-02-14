import subprocess
import time
import os

def start_gazebo():
        # Gazebo'yu başlat
        #self.gazebo_process = subprocess.Popen(["gazebo", "--verbose", "worlds/iris_arducopter_runway.world"])
        #self.gazebo_process = subprocess.Popen(["gazebo", "--verbose", "/opt/ros/iron/share/gazebo_plugins/worlds/iris_arducopter_runway.world"])
        # Gazebo'nun başlaması için bekleyin
        komut = "gazebo --verbose worlds/iris_arducopter_runway.world"
        subprocess.run(komut, shell=True)
        time.sleep(10)


def start_ardupilot():
        # Ardupilot SITL'i başlat
        ardupilot_path = os.path.expanduser('~/ardupilot/ArduCopter')
        subprocess.Popen(['../Tools/autotest/sim_vehicle.py', '-f', 'gazebo-iris', '--console', '--map'], cwd=ardupilot_path)   