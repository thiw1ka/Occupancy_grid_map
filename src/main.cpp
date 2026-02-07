#include <rclcpp/rclcpp.hpp>
#include "occupancy_grid_map/occupancy_grid_map.hpp"

class OccupancyGridMapNode : public rclcpp::Node {
public:
  OccupancyGridMapNode() : Node("occupancy_grid_map_node") {
    // Initialize the occupancy grid map
    map_.initialize(100, 100, 0.05);  // 100x100 grid with 0.05m resolution
    
    // Create publisher for occupancy grid
    grid_publisher_ =
        this->create_publisher<nav_msgs::msg::OccupancyGrid>("occupancy_grid", 10);
    
    // Create a timer to publish grid periodically
    timer_ = this->create_wall_timer(
        std::chrono::seconds(1),
        std::bind(&OccupancyGridMapNode::publishGrid, this));
    
    RCLCPP_INFO(this->get_logger(), "Occupancy Grid Map Node initialized");
  }

private:
  void publishGrid() {
    auto grid = map_.getGrid();
    grid.header.frame_id = "map";
    grid.header.stamp = this->now();
    grid_publisher_->publish(grid);
  }

  OccupancyGridMap map_;
  rclcpp::Publisher<nav_msgs::msg::OccupancyGrid>::SharedPtr grid_publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<OccupancyGridMapNode>());
  rclcpp::shutdown();
  return 0;
}
