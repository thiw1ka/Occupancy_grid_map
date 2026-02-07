from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Launch occupancy grid map node."""
    
    occupancy_grid_node = Node(
        package='occupancy_grid_map',
        executable='occupancy_grid_node',
        name='occupancy_grid_map_node',
        output='screen',
    )

    return LaunchDescription([
        occupancy_grid_node,
    ])
