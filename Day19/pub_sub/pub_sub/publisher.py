#!/usr/bin/env python3

import rclpy            
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):        #inherits node
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher_ = self.create_publisher(String, 'simple_topic', 10)    #creates publisher 
        self.timer = self.create_timer(1.0, self.timer_callback)  #calls every sec. to publish a message
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello ROS2! Count: {self.count}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
