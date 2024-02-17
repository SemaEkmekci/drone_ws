import os
import sys
# üst dizindeki dosyalara erişebilmek için
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
import rclpy
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from packets.kontrol.kontrol.kumanda import MinimalPublisher
import start_code.start_instructions as s
from start_code.start_manager import StartManager

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROS Kumanda")
        self.init_ui()
        self.minimal_publisher = MinimalPublisher()
        

    def init_ui(self):

        self.button_gazebo_run = QPushButton("Gazebo Başlat")
        self.button_gazebo_run.clicked.connect(self.start_gazebo_run)

        self.button_ardupilot_run = QPushButton("Ardupilot Başlat")
        self.button_ardupilot_run.clicked.connect(self.start_ardupilot_run)

        self.button_receiver_run = QPushButton("ROS-alici Başlat")
        self.button_receiver_run.clicked.connect(self.start_receiver_run)

        self.button_forward = QPushButton("İleri Git")
        self.button_forward.clicked.connect(self.send_ros_forward_command)

        self.button_stop = QPushButton("Dur")
        self.button_stop.clicked.connect(self.send_ros_stop_command)

        self.button_status = QPushButton("Drone Bilgileri Al")
        self.button_status.clicked.connect(self.send_ros_drone_command)

        self.button_havalan = QPushButton("Havalan")
        self.button_havalan.clicked.connect(self.send_ros_havalan_command)

        layout = QVBoxLayout()
        layout.addWidget(self.button_gazebo_run)
        layout.addWidget(self.button_ardupilot_run)
        layout.addWidget(self.button_receiver_run)
        layout.addWidget(self.button_forward)
        layout.addWidget(self.button_stop)
        layout.addWidget(self.button_status)
        layout.addWidget(self.button_havalan)

        self.setLayout(layout)


    def start_gazebo_run(self):
        print("Gazebo Başlatılıyor.")
        self.start_manager = StartManager([s.start_gazebo()])
    
    def start_ardupilot_run(self):
        print("Ardupilot Başlatılıyor")
        self.start_manager = StartManager([s.start_ardupilot()])
    
    def start_receiver_run(self):
        print("ROS-alici Başlatılıyor")
        self.start_manager = StartManager([s.start_receiver()])
    
    def send_ros_forward_command(self):
        self.minimal_publisher.send_message_once()  

    def send_ros_stop_command(self):
        self.minimal_publisher.send_stop_message()

    def send_ros_drone_command(self):
        self.minimal_publisher.send_drone_status_message()
    
    def send_ros_havalan_command(self):
        self.minimal_publisher.send_drone_havalan_message()


if __name__ == '__main__':
  
    rclpy.init()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

 
    sys.exit(app.exec_())
