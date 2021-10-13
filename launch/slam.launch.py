import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            output='screen',

            parameters=[os.path.join(get_package_share_directory(
                "ros2_x_omni_slam"), 'params', 'mapper_params_offline.yaml')
            ],
        )
    ])

