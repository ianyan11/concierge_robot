import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

#launch an empty gazebo world from the gazebo_ros package launch gazebo launch file directly
def generate_launch_description():
    print("Running  simulation/launch/world.launch.py")

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory("gazebo_ros"), '/launch/gzserver.launch.py']),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )
    
    gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory("gazebo_ros"), '/launch/gzclient.launch.py']),
    )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),
        gazebo_server,
        gazebo_client,
    ])

if __name__ == '__main__':
    generate_launch_description()