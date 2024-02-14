import sys
import rclpy
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from kumanda import MinimalPublisher

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROS Kumanda")
        self.init_ui()
        self.minimal_publisher = MinimalPublisher() 

    def init_ui(self):
        self.button_forward = QPushButton("İleri Git")
        self.button_forward.clicked.connect(self.send_ros_forward_command)

        self.button_stop = QPushButton("Dur")
        self.button_stop.clicked.connect(self.send_ros_stop_command)

        self.button_status = QPushButton("Drone Bilgileri Al")
        self.button_status.clicked.connect(self.send_ros_drone_command)

        layout = QVBoxLayout()
        layout.addWidget(self.button_forward)
        layout.addWidget(self.button_stop)
        layout.addWidget(self.button_status)

        self.setLayout(layout)


    def send_ros_forward_command(self):
        self.minimal_publisher.send_message_once()  

    def send_ros_stop_command(self):
        self.minimal_publisher.send_stop_message()

    def send_ros_drone_command(self):
        self.minimal_publisher.send_drone_status_message()   



if __name__ == '__main__':
  
    rclpy.init()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

 
    sys.exit(app.exec_())
