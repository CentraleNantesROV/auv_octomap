cmake_minimum_required(VERSION 3.5)
project(auv_octomap)


# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

set(CMAKE_CXX_STANDARD 17)

  
install(DIRECTORY launch maps DESTINATION share/${PROJECT_NAME})
  
ament_package()
