# Occupancy Grid Map

A ROS2 package for occupancy grid mapping.

## Overview

This package provides a ROS2 node that creates and publishes occupancy grid maps. The `occupancy_grid_map_node` initializes a 100x100 occupancy grid with 0.05m resolution and publishes grid data periodically.

## Dependencies

- ROS2 (Humble or newer)
- rclcpp
- std_msgs
- geometry_msgs
- nav_msgs

## Building the Package

From your workspace root directory:

```bash
colcon build
```

## Running the Package

### Option 1: Run directly using ros2 run

```bash
# Source the setup file
source install/setup.bash

# Run the node
ros2 run occupancy_grid_map occupancy_grid_node
```

### Option 2: Run using launch file

```bash
# Source the setup file
source install/setup.bash

# Run using launch file
ros2 launch occupancy_grid_map occupancy_grid_map.launch.py
```

## Node Details

### occupancy_grid_map_node

**Published Topics:**
- `/occupancy_grid` (nav_msgs/OccupancyGrid) - The occupancy grid map, published every 1 second

**Parameters:**
- None currently configured

## File Structure

```
.
├── CMakeLists.txt          # CMake build configuration
├── package.xml             # ROS2 package manifest
├── README.md              # This file
├── launch/
│   └── occupancy_grid_map.launch.py  # Launch file
├── include/
│   └── occupancy_grid_map/
│       └── occupancy_grid_map.hpp    # Header file
└── src/
    ├── main.cpp                      # Node entry point
    └── occupancy_grid_map.cpp        # Implementation
```

## License

Apache License 2.0
