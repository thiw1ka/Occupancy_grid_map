cmake_minimum_required(VERSION 3.8)
project(occupancy_grid_map)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)

# Add library
add_library(occupancy_grid_map_lib
  src/occupancy_grid_map.cpp
)
target_include_directories(occupancy_grid_map_lib PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
ament_target_dependencies(occupancy_grid_map_lib
  rclcpp
  std_msgs
  geometry_msgs
  nav_msgs
)

# Add executable
add_executable(occupancy_grid_node src/main.cpp)
target_include_directories(occupancy_grid_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
ament_target_dependencies(occupancy_grid_node
  rclcpp
  std_msgs
  geometry_msgs
  nav_msgs
)
target_link_libraries(occupancy_grid_node occupancy_grid_map_lib)

# Install
install(TARGETS occupancy_grid_node
  DESTINATION lib/${PROJECT_NAME}
)
install(DIRECTORY include/
  DESTINATION include
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # ament_lint_auto_find_test_files()
endif()

ament_package()
