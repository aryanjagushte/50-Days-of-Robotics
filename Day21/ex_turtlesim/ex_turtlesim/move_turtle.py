#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveTurtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)  # creating publisher
        self.timer = self.create_timer(0.5, self.move_turtle)
        self.get_logger().info('turtle node started!!')  # message will get printed on the terminal

    def move_turtle(self):
        msg = Twist()
        msg.linear.x = 1.0  # linear constant speed
        msg.angular.z = 1.0  # no rotation
        self.publisher_.publish(msg)
        self.get_logger().info('turtle is moving forward')

def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
