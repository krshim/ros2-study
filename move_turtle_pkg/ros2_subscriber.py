import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

class HelloworldSubscriber(Node):
    def __init__(self):
        super().__init__('ros2_subscriber_node')
        qos_profile = QoSProfile(depth=10)
        self.helloworld_subscriber = self.create_subscription(
            String,
            'nearthlab',
            self.subscribe_topic_message,
            qos_profile)

    def subscribe_topic_message(self, msg):
        print(msg)
        self.get_logger().info(f'Received message: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = HelloworldSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
