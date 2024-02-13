import rclpy
from rclpy.node import Node
import subprocess
import time

from geometry_msgs.msg import Twist
from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'ekmekci',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, '/demo/cmd_demo', 10)
        self.gazebo_process = None
        self.current_twist_msg = None

    def listener_callback(self, msg):
        if msg.data == "İleri Git":
            print("İleri Git Mesajı Alındı")
            self.start_gazebo_and_move_forward()
        elif msg.data == "Dur":
            print("Dur")
            self.stop_gazebo()

    def start_gazebo_and_move_forward(self):
        # Gazebo'yu başlat
        #self.gazebo_process = subprocess.Popen(["gazebo", "--verbose", "/opt/ros/iron/share/gazebo_plugins/worlds/gazebo_ros_diff_drive_demo.world"])
        self.gazebo_process = subprocess.Popen(["gazebo", "--verbose", "--master-uri", "http://127.0.0.1:11346", "/opt/ros/iron/share/gazebo_plugins/worlds/gazebo_ros_diff_drive_demo.world"])

        # Gazebo'nun başlaması için bekleyin
        time.sleep(5)

        # Twist mesajı oluştur
        self.current_twist_msg = Twist()
        self.current_twist_msg.linear.x = 1.0  # İleri doğrusal hız
        self.current_twist_msg.angular.z = 0.0  # Sıfır açısal hız

        # Twist mesajını yayınla
        self.publisher_.publish(self.current_twist_msg)
        self.get_logger().info('Twist mesajı yayınlandı.')

    def stop_gazebo(self):
        # Eğer mevcut bir Twist mesajı varsa, onu durdur
        if self.current_twist_msg:
            self.current_twist_msg.linear.x = 0.0  # Doğrusal hızı durdur
            self.current_twist_msg.angular.z = 0.0  # Açısal hızı durdur
            self.publisher_.publish(self.current_twist_msg)
            self.get_logger().info('Twist mesajı durduruldu.')

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)

    # Düğüm sonlandırıldığında Gazebo sürecini kapatın
    if minimal_subscriber.gazebo_process:
        minimal_subscriber.gazebo_process.terminate()

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
