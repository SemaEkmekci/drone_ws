from playsound import playsound
import time
import start as s
import subprocess
import time


def main():
    playsound('ses.mp3')      
    start_instruction = s.start_ardupilot()
    subprocess.run(start_instruction, shell=True)
    time.sleep(10)
    playsound('ses.mp3')  
    s.start_gazebo()
    time.sleep(10)
    playsound('ses.mp3')  

    

if __name__ == '__main__':
    main()
