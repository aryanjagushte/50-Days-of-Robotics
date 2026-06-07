import launch 
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pub_sub',   
            executable='publisher.py', 
            name='publisher',
            output='screen'
        ),
        Node(
            package='pub_sub',
            executable='subscriber.py',
            name='subscriber',
            output='screen'
        ),
    ])
