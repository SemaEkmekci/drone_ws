from playsound import playsound
import time
import start as s

def main():
    playsound('ses.mp3')  
    #subprocess.run(["python3", "src/kontrol/kontrol/arayüz.py"])
    s.start_ardupilot()
    time.sleep(10)
    playsound('ses.mp3')  
    s.start_gazebo()
    time.sleep(10)
    playsound('ses.mp3')  

    


if __name__ == '__main__':
    main()
