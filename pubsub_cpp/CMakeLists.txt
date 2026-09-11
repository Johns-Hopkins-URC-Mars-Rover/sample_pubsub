cmake_minimum_required(VERSION 3.8)
project(pubsub_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(basic_pub src/pub.cpp)
ament_target_dependencies(basic_pub rclcpp std_msgs)

add_executable(basic_sub src/sub.cpp)
ament_target_dependencies(basic_sub rclcpp std_msgs)

install(TARGETS
  basic_pub
  basic_sub
  DESTINATION lib/${PROJECT_NAME})

ament_package()
