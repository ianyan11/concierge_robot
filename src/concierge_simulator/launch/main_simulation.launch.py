from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_name = 'concierge_simulator'
    
    world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(package_name), 'launch', 'world.launch.py')
        ])
    )
    
    spawn_robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(package_name), 'launch', 'spawn_robot.launch.py')
        ])
    )

    return LaunchDescription([
        world_launch,
        spawn_robot_launch
    ])

if __name__ == '__main__':
    generate_launch_description()