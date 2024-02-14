import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'ekmekci', 10)
        
    

    def send_message_once(self):
        msg = String()
        msg.data = 'İleri Git'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
    
    def send_stop_message(self):
        msg = String()
        msg.data = 'Dur'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        
    def send_drone_status_message(self):
        msg = String()
        msg.data = 'Drone Bilgisi'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
    
    def send_drone_havalan_message(self):
        msg = String()
        msg.data = 'Havalan'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)   


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()