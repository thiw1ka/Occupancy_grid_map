from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os


def generate_launch_description():
    """Launch occupancy grid map node and Gazebo."""
    
    # Gazebo world launch - empty world
    gazebo = ExecuteProcess(
        cmd=['gazebo', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )
    
    occupancy_grid_node = Node(
        package='occupancy_grid_map',
        executable='occupancy_grid_node',
        name='occupancy_grid_map_node',
        output='screen',
    )

        
    # visulizer = Node(
    #     package='rviz2',
    #     executable='rviz2',
    #     arguments=['-d', os.path.join(
    #         get_package_share_directory('slam_sim'),'rviz')+'/rviz1.rviz']
    # )

    #     simulation = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(
    #         get_package_share_directory('turtlebot3_gazebo'),'launch'),
    #         '/turtlebot3_house.launch.py']),launch_arguments={}.items()
    #     )

    return LaunchDescription([
        gazebo,
        occupancy_grid_node,
    ])
