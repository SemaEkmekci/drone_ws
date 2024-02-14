import sys
from playsound import playsound
import subprocess
import rclpy
from PyQt5.QtWidgets import QApplication

import time
import start as s

def main():
    playsound('ses.mp3')  
    #subprocess.run(["python3", "src/kontrol/kontrol/arayüz.py"])
    playsound('ses.mp3')  
    s.start_ardupilot()
    time.sleep(10)
    playsound('ses.mp3')  
    s.start_gazebo()
    time.sleep(10)
    

    

if __name__ == '__main__':
    main()
