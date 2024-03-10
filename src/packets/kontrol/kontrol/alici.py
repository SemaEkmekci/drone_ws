import rclpy
import os
from rclpy.node import Node
import time
from dronekit import connect,VehicleMode
from geometry_msgs.msg import Twist
from std_msgs.msg import String


#drone = connect('127.0.0.1:14550', wait_ready=True, timeout=100)

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
            self.move_forward()
        elif msg.data == "Dur":
            print("Dur")
            self.stop_gazebo()
        elif msg.data == "Drone Bilgisi":
            print("Drone Bilgisi")
            self.drone_status()
        elif msg.data == "Takeoff":
            irtifa=int(input("Lütfen iha'yı yükseltmek istediğiniz irtifa bilgisini giriniz: "))
            self.takeoff(irtifa)
        else:
            print("Mesaj YOK")

    

    def move_forward(self):

    # Twist mesajı oluştur
        self.current_twist_msg = Twist()
        self.current_twist_msg.linear.x = 1.0  # İleri doğrusal hız
        self.current_twist_msg.angular.z = 0.0  # Sıfır açısal hız

    # Twist mesajını yayınla
        self.publisher_.publish(self.current_twist_msg)
        self.get_logger().info('Twist mesajı yayınlandı.')

    


    def drone_status(self):
        drone = connect('127.0.0.1:14550', wait_ready=True)
        print(f"Drone Arm Durumu: {drone.armed}")
        print(drone.location.global_frame)
        print(drone.location.global_relative_frame)
        print(drone.location.global_relative_frame.alt)

    
    def takeoff(self,irtifa):
    
        while drone.is_armable:
            print('\n\n\n--------------------------------------------\n\n')
            print('İha arm edilebilir!')
            drone.mode=VehicleMode("GUIDED")
            print('İha ' +str(drone.mode) +' geçti!')
            #  MOde geçişini yapıyorsun ama direk geçebilmesi ve senin console'da 
            # görebilmen için biraz zaman geçmesi gerekiyor.
            drone.armed=True
            
            # İha'yı aktif ettiğimiz gibi direk motorlar çalışmaz GPS de de görmüştük biraz süre geçmesi gerekiyor.
            
            while drone.armed is not True:

                print('İha arm ediliyor!')
                time.sleep(0.5)
            
            print('İha arm edildi!')

            drone.simple_takeoff(irtifa)
            
            break
        time.sleep(1)



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
