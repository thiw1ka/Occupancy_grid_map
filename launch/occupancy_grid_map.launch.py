from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    """Launch occupancy grid map node and Gazebo."""
    
    # Launch TurtleBot3 empty world (this will start Gazebo)
    turtlebot3_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(
            get_package_share_directory('turtlebot3_gazebo'), 'launch', 'empty_world.launch.py'
        ))
    )
    
    occupancy_grid_node = Node(
        package='occupancy_grid_map',
        executable='occupancy_grid_node',
        name='occupancy_grid_map_node',
        output='screen',
        # arguments=['--ros-args', '--log-level', 'DEBUG'],
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        # do not set a fixed node name to avoid name conflicts
        output='screen',
        # arguments=['--ros-args', '--log-level', 'DEBUG'],
    )

    return LaunchDescription([
        # export TurtleBot3 model for included launch
        SetEnvironmentVariable('TURTLEBOT3_MODEL', 'burger'),
        # ensure rviz has access to the X display from the current environment
        SetEnvironmentVariable('DISPLAY', os.environ.get('DISPLAY', ':0')),
        turtlebot3_launch,
        occupancy_grid_node,
        rviz_node,
    ])
