from dronekit import connect, VehicleMode
import os






class DroneManager:
    def __init__(self):
      self.worldText = []

    def add_drone(self, drone_count):
        #drone_ip = f"{self.ip}:{self.port}"
        
        
        # Klasör yolu
        klasör_yolu = os.path.join(os.path.expanduser("~"), "ardupilot_gazebo", "worlds")

        # Dosya adı
        dosya_adı = "iris_multiuav_runway.world"

        # Dosya yolunu oluştur
        dosya_yolu = os.path.join(klasör_yolu, dosya_adı)
        
        
        end = "\n</world>\n</sdf>"
        pose = 0
        count = 0
       
        with open(dosya_yolu, "r") as file:
         
            for line in file:  
              if '</world>' in line:
                print("İstenilen metin bulundu:", line)
                break
              if '<model name="iris_demo_0">' in line:
                print("asdfasd")
                break
              
              self.worldText.append(line)
              
        for i in range(drone_count):
           add= f'\n<model name="iris_demo_{count}">\n<pose> {pose} 0 0 0 0 0 0 </pose>\n <include>\n<uri>model://iris_with_ardupilot_{count}</uri>\n</include>\n</model>\n'
           self.worldText.append(add)
      
           pose+=5
           count+=1
        
        self.worldText.append(end)
        
        with open(dosya_yolu, "w") as file:
            # worldText listesini dosyaya yaz
            for line in self.worldText:
                
                file.write(line)

        self.port += 10
        print("start_port", self.port)


    def update_start_ardupilot_sh(self, drone_count):
      # Dosya yolu
      dosya_yolu = "src/start_instructions_sh/start_ardupilot.sh"
      new_text = []
      print("DRONE_COUNT: ", drone_count)
      for i in range(drone_count):
         new_text.append("\ncd ~/ardupilot/Tools/autotest\n./sim_vehicle.py -v ArduCopter -f gazebo-iris --console I" + str(i) + "\n")
      

      print(new_text)
      
      with open(dosya_yolu, "w") as file:
        for line in new_text:      
          file.write(line)
        




