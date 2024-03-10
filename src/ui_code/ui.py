import os
import sys
import time
# üst dizindeki dosyalara erişebilmek için
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
import rclpy
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from packets.kontrol.kontrol.kumanda import MinimalPublisher
import start_code.start_instructions as s
from start_code.start_manager import StartManager
from drone_add.drone import DroneManager
from drone_connect.droneConnect import DroneConnect


class MyMainWindow(QMainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        loadUi(os.path.join(current_dir, "ara.ui"), self)
        #self.minimal_publisher = MinimalPublisher()
        self.drone_count = 0
        self.start_port = 14550
        self.gazeboStartButton.clicked.connect(self.start_gazebo_run)#Gazebo butonu
        self.arduStartButton.clicked.connect(self.start_ardupilot_run)#Ardupilot Butonu
        self.rosStartButton.clicked.connect(self.start_receiver_run)#Ros butonu
        self.addButton.clicked.connect(self.send_ros_drone_command)#Denemelik buton bilgi alıyor!!Değişecek
        self.droneIdCombo.currentIndexChanged.connect(self.send_ros_drone_command)#Combo boxtan seçilen dorne ıdsini döndürüyor. ve o dronenin bilgilerini alacak ileride!!


        self.droneQuantitySpin.valueChanged.connect(self.onDroneCountChanged)

        baslangicIrtifa = self.formAltitudeEnter.text()#Başlangıç irtifasını verir
        formasyonIrtifa= self.formAltitudeEnter.text()#formasyon irtifasını verir
        
        formasyonIndex = self.formCombo.currentIndex()#Mevcut index
        formasyonId = self.droneIdCombo.itemText(formasyonIndex)#seçilen formasyonun indexini verir. Formasyon seçerken kullanılacak.
    
        self.droneManager = DroneManager()
        self.droneConnect = DroneConnect(self.start_port)

       
        
    def drone_connect(self):
        for i in range(self.drone_count):

            drone = self.droneConnect.connect()
        print("DRONE: " , drone)

    def start_gazebo_run(self):
        print("Gazebo Başlatılıyor.")
        #droneSayisi=self.droneQuantitySpin.value()

        self.droneManager.add_drone(self.drone_count)
       
        time.sleep(8)

        self.start_manager = StartManager([s.start_gazebo()])
        print("Dosya değişti: ")

    def start_ardupilot_run(self):
        print("Ardupilot Başlatılıyor")
        self.droneManager.update_start_ardupilot_sh(self.drone_count)
        #time.sleep(8)
        #self.start_manager = StartManager([s.start_ardupilot()])
        self.drone_connect()

    def send_ros_drone_command(self):
        secilen_index = self.droneIdCombo.currentIndex()#Mevcut index
        secilen_drone_id = self.droneIdCombo.itemText(secilen_index)#Mevcut indexteki yazı
        self.droneInfo.setText(secilen_drone_id)
        #self.minimal_publisher.send_drone_status_message()

    def start_receiver_run(self):
        print("ROS-alici Başlatılıyor")
        self.start_manager = StartManager([s.start_receiver()])
    
    def onDroneCountChanged(self, value):
        self.drone_count = value
        count = value
        print("value: ", count)
    

        


        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
