from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    publisher = Node(
        package="pubsub_py",
        executable="basic_pub",
        output="screen",
        )
    
    subscriber = Node(
        package="pubsub_py",
        executable="basic_sub",
        output="screen",
        )

    return LaunchDescription([
        subscriber,
        publisher
        ])