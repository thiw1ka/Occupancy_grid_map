#include "occupancy_grid_map/occupancy_grid_map.hpp"

OccupancyGridMap::OccupancyGridMap() {}

OccupancyGridMap::~OccupancyGridMap() {}

void OccupancyGridMap::initialize(int width, int height, float resolution) {
  grid_.info.width = width;
  grid_.info.height = height;
  grid_.info.resolution = resolution;
  grid_.data.resize(width * height, -1);  // Initialize with unknown
}

void OccupancyGridMap::updateCell(int x, int y, int8_t value) {
  if (x >= 0 && x < static_cast<int>(grid_.info.width) &&
      y >= 0 && y < static_cast<int>(grid_.info.height)) {
    int index = y * grid_.info.width + x;
    grid_.data[index] = value;
  }
}

nav_msgs::msg::OccupancyGrid OccupancyGridMap::getGrid() const {
  return grid_;
}
