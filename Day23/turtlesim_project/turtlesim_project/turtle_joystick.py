#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class TurtleJoystick(Node):
    def __init__(self):
        super().__init__('turtle_joystick')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.joy_subscriber_ = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        self.get_logger().info("Joystick node started successfully")

    def joy_callback(self, joy_msg):
        twist = Twist()

        # Use joystick axes to move        
        twist.linear.x = joy_msg.axes[1]  # Forward/Backward (left stick vertical)
        twist.angular.z = joy_msg.axes[0]  # Left/Right rotation (left stick horizontal)

        # Button Functioning
        if joy_msg.buttons[0] == 1:  # A Button
            self.get_logger().info("A Button : Turbo Mode ON")
            twist.linear.x = 2.0  # Double speed

        if joy_msg.buttons[1] == 1:  # B Button
            self.get_logger().info("B Button : Stop Turtle")
            twist.linear.x = 0.0
            twist.angular.z = 0.0

        if joy_msg.buttons[2] == 1:  # X Button
            self.get_logger().info("X Button : Reverse Mode ON")
            twist.linear.x = -1.0  # Move backward

        if joy_msg.buttons[3] == 1:  # Y Button
            self.get_logger().info("Y Button : Rotate Right")
            twist.angular.z = -1.0  # Rotate clockwise

        # Publish the velocity command
        self.publisher_.publish(twist)
        self.get_logger().info(f"Joystick input: linear={twist.linear.x}, angular={twist.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    node = TurtleJoystick()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
