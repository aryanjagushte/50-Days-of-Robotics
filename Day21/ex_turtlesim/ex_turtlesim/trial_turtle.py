#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SquareCircleTurtle(Node):
    def __init__(self):
        super().__init__('square_circle_turtle')
        self.turtle1_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.get_logger().info("Node started. Turtle1 will draw a square.")

        # Turtle1: Draw Square
        self.get_logger().info("Turtle1: Moving forward")
        msg1 = Twist()
        msg1.linear.x = 2.0
        msg1.angular.z = 0.0
        self.turtle1_publisher.publish(msg1)
        time.sleep(1)

        self.get_logger().info("Turtle1: Turning 90 degrees")
        msg1.linear.x = 0.0
        msg1.angular.z = 1.57
        self.turtle1_publisher.publish(msg1)
        time.sleep(1)

        self.get_logger().info("Turtle1: Moving forward")
        msg1.linear.x = 2.0
        msg1.angular.z = 0.0
        self.turtle1_publisher.publish(msg1)
        time.sleep(1)

        self.get_logger().info("Turtle1: Turning 90 degrees")
        msg1.linear.x = 0.0
        msg1.angular.z = 1.57
        self.turtle1_publisher.publish(msg1)
        time.sleep(1)

        self.get_logger().info("Turtle1: Moving forward")
        msg1.linear.x = 2.0
        msg1.angular.z = 0.0
        self.turtle1_publisher.publish(msg1)
        time.sleep(1)

        self.get_logger().info("Turtle1: Turning 90 degrees")
        msg1.linear.x = 0.0
        msg1.angular.z = 1.57
        self.turtle1_publisher.publish(msg1)
        time.sleep(1)

        self.get_logger().info("Turtle1: Moving forward")
        msg1.linear.x = 2.0
        msg1.angular.z = 0.0
        self.turtle1_publisher.publish(msg1)
        time.sleep(1)

        self.get_logger().info("Turtle1: Turning 90 degrees")
        msg1.linear.x = 0.0
        msg1.angular.z = 1.57
        self.turtle1_publisher.publish(msg1)
        time.sleep(1)

        self.get_logger().info("Turtle1: Square completed. Stopping Turtle1.")
        msg1.linear.x = 0.0
        msg1.angular.z = 0.0
        self.turtle1_publisher.publish(msg1)

        # Turtle2: Draw Circle
        self.get_logger().info("Turtle2: Starting circle")
        msg2 = Twist()
        msg2.linear.x = 1.0
        msg2.angular.z = -1.0

        for _ in range(72):  # Simulate one circle by publishing for 36 steps
            self.turtle1_publisher.publish(msg2)
            time.sleep(0.1)

        self.get_logger().info("Turtle2: Circle completed. Stopping Turtle2.")
        msg2.linear.x = 0.0
        msg2.angular.z = 0.0
        self.turtle1_publisher.publish(msg2)

def main(args=None):
    rclpy.init(args=args)
    node = SquareCircleTurtle()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
