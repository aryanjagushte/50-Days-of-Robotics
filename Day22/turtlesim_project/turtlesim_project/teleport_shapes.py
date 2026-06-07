#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TeleportShapes(Node):
    def __init__(self):
        super().__init__('teleport_shapes')
        self.turtle1_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        #self.turtle2_publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

        self.get_logger().info("Node started! turtle1 will draw a square & turtle2 will draw a circle.")

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

"""        # Turtle2: Draw Circle
        self.get_logger().info("Turtle2: Starting circle")
        msg2 = Twist()
        msg2.linear.x = 1.0
        msg2.angular.z = -1.0

        for _ in range(72):  # simulate and stop the turtle after completing, 7.2s
            self.turtle2_publisher.publish(msg2)
            time.sleep(0.1)

        self.get_logger().info("Turtle2: Circle completed. Stopping Turtle2.")
        msg2.linear.x = 0.0
        msg2.angular.z = 0.0
        self.turtle2_publisher.publish(msg2)"""

def main(args=None):
    rclpy.init(args=args)
    node = TeleportShapes()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
