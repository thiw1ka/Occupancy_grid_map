#ifndef OCCUPANCY_GRID_MAP_HPP
#define OCCUPANCY_GRID_MAP_HPP

#include <rclcpp/rclcpp.hpp>
#include <nav_msgs/msg/occupancy_grid.hpp>

class OccupancyGridMap {
public:
  OccupancyGridMap();
  ~OccupancyGridMap();

  void initialize(int width, int height, float resolution);
  void updateCell(int x, int y, int8_t value);
  nav_msgs::msg::OccupancyGrid getGrid() const;

private:
  nav_msgs::msg::OccupancyGrid grid_;
};

#endif // OCCUPANCY_GRID_MAP_HPP
